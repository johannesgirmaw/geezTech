from rest_framework import serializers
from difflib import SequenceMatcher
from django.contrib.auth.password_validation import validate_password


def validate_password2(obj,value):
    if value != obj.context.get('request').data.get('password1'):
        raise serializers.ValidationError("password fields didn't match.")
    return value
def validate_password1(obj, value):
    user_attributes = ("username", "first_name", "last_name", "email")
    data = obj.context.get('request').data
    password  = value.lower()
    for attribute in user_attributes:
        if SequenceMatcher(a=data.get(attribute,"").lower(), b=password).ratio()>0.5:
            raise serializers.ValidationError(f"The password is too similar to the {attribute}.")
    validate_password(password)
    return value