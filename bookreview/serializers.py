from rest_framework import serializers
from .models import Author
from .models import Book

 
 
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    class Meta:
        model = Author
        fields = ('id'