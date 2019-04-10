from tokenize import Token
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
from rest_framework import generics
from contacts.serializers import UserSerializer, ContactSerializer, EmailSerializer, UserDetailSerializer
from contacts.models import User, Contact, Email
from django.contrib.auth import authenticate


class UserAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response([UserSerializer(user).data for user in User.objects.all()])

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response([ContactSerializer(contact).data for contact in Contact.objects.all()])

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        # user = User.objects.get(id=request.data["user_id"])
        # if user.first_name:
        #     contact = Contact()
        #     contact.first_name = request.data["first_name"]
        #     contact.last_name = request.data["last_name"]
        #     contact.dob = request.data["dob"]
        #     contact.user_id = user
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.errors)


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
    return Response({'token': token.key,
                     'user_id': user.id},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)
