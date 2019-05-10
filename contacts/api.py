from tokenize import Token
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
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

from contacts.decorators import validate_token
from contacts.serializers import UserSerializer, ContactSerializer, UserCreateSerializer
from contacts.models import User, Contact
from django.contrib.auth import authenticate
from contacts.permissions import IsUserLogin


class UserProfile(APIView):
    """This APIView os for the content of UserProfile."""
    permission_classes = (IsUserLogin,)

    @staticmethod
    @validate_token
    def get(request):
        pk = request.COOKIES.get('user_id')
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    @validate_token
    def put(request):
        pk = request.COOKIES.get('user_id')
        user = User.objects.get(id=pk)
        payload = request.data
        serializer = UserSerializer(user, data=payload, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response("UNAUTHORIZED", status=HTTP_401_UNAUTHORIZED)

    @staticmethod
    def get_serialized(pk):
        queryset = Contact.objects.filter(user_id=pk)
        serializer = ContactSerializer(queryset, many=True)
        return serializer.data


class UserContacts(APIView):
    """This APIView is for the all contacts of user."""
    permission_classes = (IsUserLogin,)

    @staticmethod
    @validate_token
    def get(request):
        pk = request.COOKIES.get('user_id')
        _id = int(pk)
        user = User.objects.get(id=_id)
        contact = Contact.objects.filter(user_id=user.id)
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    @staticmethod
    @validate_token
    def post(request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    @staticmethod
    @validate_token
    def put(request):
        contact = Contact.objects.get(id=request.data['id'])
        payload = request.data
        serializer = ContactSerializer(contact, data=payload, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
def login(request):
    """This view is for login of user."""
    username = request.data["username"]
    password = request.data["password"]
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


class Logout(APIView):
    """This APIView is for the logout of current login user."""
    permission_classes = (IsUserLogin,)

    @csrf_exempt
    def get(self, request):
        response = HttpResponse()
        try:
            Token.objects.get(key=request.COOKIES['token']).delete()
        except Token.DoesNotExist:
            return Response("UNAUTHORIZED", status=HTTP_401_UNAUTHORIZED)
        response.delete_cookie('token')
        response.delete_cookie('user_id')
        return response


class Signup(APIView):
    """This APIView is for the signup of user."""
    permission_classes = (AllowAny,)

    @csrf_exempt
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
