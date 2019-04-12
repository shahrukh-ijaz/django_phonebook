from tokenize import Token

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime
from contacts.serializers import UserSerializer, ContactSerializer, EmailSerializer, UserDetailSerializer, \
    ContactDetailSerializer
from contacts.models import User, Contact, Email
from django.contrib.auth import authenticate


class UserProfile(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        if 'token' in request.COOKIES:
            pk = request.COOKIES.get('user_id')
            user = User.objects.get(id=pk)
            contacts = self.get_serialized(pk, user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response("Your token expire Login again", status=HTTP_400_BAD_REQUEST)

    def put(self, request):
        if 'token' in request.COOKIES:
            pk = request.COOKIES.get('user_id')
            user = User.objects.get(id=pk)
            payload = request.data
            serializer = UserSerializer(user, data=payload, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response("PUT REQUEST FAILED", status=HTTP_400_BAD_REQUEST)

    def get_serialized(self, pk, user):

        queryset = Contact.objects.filter(user_id=pk)

        serializer = ContactSerializer(queryset, many=True)
        data = serializer.data
        return data


class UserContacts(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        pk = request.COOKIES.get('user_id')
        _id = int(pk)
        user = User.objects.get(id=_id)
        contact = Contact.objects.filter(user_id=user.id)
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def put(self, request):
        if 'token' in request.COOKIES:
            contact = Contact.objects.get(id=request.data['id'])
            payload = request.data
            serializer = ContactSerializer(contact, data=payload, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response("PUT REQUEST FAILED", status=HTTP_400_BAD_REQUEST)


class ContactDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk):
        book = Contact.objects.get(id=pk)
        serializer = ContactSerializer(book)
        return Response(serializer.data)


class UserDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        contacts = self.get_serialized(pk, user)

        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def get_serialized(self, pk, user):

        queryset = Contact.objects.filter(user_id=pk)

        serializer = ContactSerializer(queryset, many=True)
        data = serializer.data
        return data


@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
def login(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
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


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    if 'token' in request.COOKIES:
        token = request.COOKIES['token']
        user_id = request.COOKIES['user_id']
        data = {'sample_data': 123, 'token': token, 'user_id': user_id}
    else:
        data = {'sample_data': 'got nothing'}
    return Response(data, status=HTTP_200_OK)


class Logout(APIView):
    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    def get(self, request, format=None):
        response = HttpResponse()
        response.delete_cookie('token')
        response.delete_cookie('user_id')
        return response
