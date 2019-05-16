from rest_framework import serializers
from contacts.models import User, Contact, Email, Number


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'email')


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ('number', 'id')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'note', 'dob', 'user_id')


class ContactDetailSerializer(serializers.ModelSerializer):
    emails = EmailSerializer(many=True, required=False)
    numbers = NumberSerializer(many=True, required=False)

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'note', 'dob', 'emails', 'numbers')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
