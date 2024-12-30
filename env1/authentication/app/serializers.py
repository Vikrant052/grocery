from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name','last_name', 'email', 'phone'] 


class RegisterSerialzers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ( 'first_name','last_name', 'email', 'phone') 
        


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'password', 'confirm_password']

    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return email

    def validate_phone(self, phone):
        if CustomUser.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("A user with this phone number already exists.")
        return phone

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  
        return CustomUser.objects.create_user(
            email=validated_data['email'],
            name=f"{validated_data['first_name']} {validated_data['last_name']}",
            phone=validated_data['phone'],
            password=validated_data['password']
        )
        