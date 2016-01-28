from rest_framework import serializers
from models import email, full_name, time_stamp, post

class email_serializer(serializers.ModelSerializer):
    class Meta:
        model = email
        field = ('id', 'name')

class full_name_serializer(serializers.ModelSerializer):
    class meta:
        model = full_name
        field = ('id', 'name')

class time_stamp_serializer(serializers.ModelSerializer):
    class meta:
        model = time_stamp
        field = ('id','name')

class post_serializer(serializers.ModelSerializer):
    email = email serializer()
    full_name = full_name_serializer()
    time_stamp = time_stamp_serializer()

    class Meta:
        model = post
        field = ('id', 'post', 'email', 'full_name', 'time_stamp')
