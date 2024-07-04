from rest_framework import serializers
from .models import StudentModel, LoginModel
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken


class StudentSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = StudentModel
        fields = ['id', 'name', 'email', 'age', 'password']

    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])
        return super().create(validate_data)

    def validate(self, attrs):
        if not attrs:
            raise serializers.ValidationError("Request data cannot be empty.")
        return super().validate(attrs)
        

class LoginStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = ['id', 'email', 'password']
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = StudentModel.objects.get(email=email)
        except StudentModel.DoesNotExist:
            raise serializers.ValidationError('Invalid email or password!')

        if not check_password(password, user.password):
            raise serializers.ValidationError('Invalid email or password!')

        token = RefreshToken.for_user(user)

        return {
            'message': 'Login successful!',
            'data': {
                'refresh': str(token),
                'access': str(token.access_token)
            },
            'isError': False
        }