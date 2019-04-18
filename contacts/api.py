from tokenize import Token
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_401_UNAUTHORIZED,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from contacts.serializers import UserSerializer, ContactSerializer, UserDetailSerializer
from contacts.models import User, Contact
from django.contrib.auth import authenticate
from contacts.permissions import IsUserLogin


def validate_token(request):
    try:
        if 'token' in request.COOKIES:
            token = Token.objects.get(key=request.COOKIES['token'])
            return token
        else:
            return None
    except Token.DoesNotExist:
        return None


class UserProfile(APIView):
    permission_classes = (IsUserLogin,)

    def get(self, request):
        if validate_token(request) is not None:
            pk = request.COOKIES.get('user_id')
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response("Your token expire Login again", status=HTTP_400_BAD_REQUEST)

    def put(self, request):
        if validate_token(request) is not None:
            pk = request.COOKIES.get('user_id')
            user = User.objects.get(id=pk)
            payload = request.data
            serializer = UserSerializer(user, data=payload, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response("UNAUTHORIZED", status=HTTP_401_UNAUTHORIZED)

    def get_serialized(self, pk, user):

        queryset = Contact.objects.filter(user_id=pk)
        serializer = ContactSerializer(queryset, many=True)
        return serializer.data


class UserContacts(APIView):
    permission_classes = (IsUserLogin,)

    def get(self, request):
        if validate_token(request) is not None:
            pk = request.COOKIES.get('user_id')
            _id = int(pk)
            user = User.objects.get(id=_id)
            contact = Contact.objects.filter(user_id=user.id)
            serializer = ContactSerializer(contact, many=True)
            return Response(serializer.data)
        else:
            return Response("UNAUTHORIZED", status=HTTP_401_UNAUTHORIZED)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def put(self, request):
        if validate_token(request) is not None:
            contact = Contact.objects.get(id=request.data['id'])
            payload = request.data
            serializer = ContactSerializer(contact, data=payload, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response("UNAUTHORIZED", status=HTTP_401_UNAUTHORIZED)


class ContactDetails(APIView):

    def get(self, request, pk):
        book = Contact.objects.get(id=pk)
        serializer = ContactSerializer(book)
        return Response(serializer.data)


class UserDetails(APIView):


    def get(self, request, pk):
        user = User.objects.get(id=pk)
        self.get_serialized(pk, user)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def get_serialized(self, pk, user):
        queryset = Contact.objects.filter(user_id=pk)
        serializer = ContactSerializer(queryset, many=True)
        return serializer.data


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    response = HttpResponse()
    response.set_cookie('token', token.key)
    response.set_cookie('user_id', user.id)
    return response


class Logout(APIView):
    permission_classes = (IsUserLogin,)

    @csrf_exempt
    def get(self, request, format=None):
        response = HttpResponse()
        try:
            Token.objects.get(key=request.COOKIES['token']).delete()
        except Token.DoesNotExist:
            return Response("UNAUTHORIZED", status=HTTP_401_UNAUTHORIZED)
        response.delete_cookie('token')
        response.delete_cookie('user_id')
        return response