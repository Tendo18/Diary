from rest_framework import serializers
from .models import Diary
from .models import Profile
from django.contrib.auth.models import User

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiarySerializer
        fields = ['fullname', 'gender', 'phone', 'image']

class RegisterSerializers(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only= True)
    password2 = serializers.CharField(write_only = True)
    username = serializers.CharField(write_only = True)
    email = serializers.EmailField(write_only = True)

    class Meta:
        model = Diary
        fields = ['fullname', 'username', 'email', 'password', 'gender', 'image', 'password1', 'password2']

        def validate(self, data):
            if data['password1'] != data['password2']:
                raise serializers.ValidationError("Password doesn't match")
            if data['username'].exists():
                raise serializers.ValidationError('Username exists')
            return data
        
        def create(self, validated_data):
            username = validated_data.pop('username')
            email = validated_data.pop('email')
            password = validated_data.pop('password')

            user = User.objects.create_user(username=username, email=email, password=password)
 
            profile = Profile.object.create(
            user = user,
            fullname = validated_data['fullname'],
            phone = validated_data['phone'],
            gender = validated_data['gender'],
            image = validated_data['image'],
            )
            
            return profile
        


