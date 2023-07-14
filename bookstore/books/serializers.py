from rest_framework import serializers
from .models import Book
from books.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# class UserSerializer(serializers.ModelSerializer):
#     token = serializers.SerializerMethodField()

#     def get_token(self, obj):
#         refresh = RefreshToken.for_user(obj)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password','token']
#         extra_kwargs = {'password': {'write_only': True}}


#         def save(self):
#             reg = User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email'],
#             first_name=self.validated_data['first_name'],
#             last_name=self.validated_data['last_name'],
#             )
#             password = self.validated_data['password']
#             reg.set_password(password)


        
#             reg.save()


#             return reg


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

    def save(self):
        reg = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        
        
        reg.set_password(password)
        reg.save()
        return reg


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


