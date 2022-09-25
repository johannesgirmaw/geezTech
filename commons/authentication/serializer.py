# from rest_framework import serializers
# from dj_rest_auth.registration.serializers import RegisterSerializer
# from django.db import transaction
# from .models import CustomUser

# class CustomRegisterSerializer(RegisterSerializer):
#     first_name=serializers.CharField(max_length=200)
#     last_name=serializers.CharField(max_length=200)
#     # age=serializers.IntegerField()
#     @transaction.atomic
#     def save(self,request):
#         user=super().save(request)
#         user.first_name=self.data.get('first_name' )
#         user.last_name=self.data.get('last_name' )
#         # user.age=self.data.get('age')
#         user.save()
#         return user
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=CustomUser
#         fields='__all__'