from rest_framework import serializers
from users.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users     # it will convert the object's data into a JSON representation, 
                          # including the specified fields: id, email, and password. 
        fields = ('id',
                'email',
                'password')
        