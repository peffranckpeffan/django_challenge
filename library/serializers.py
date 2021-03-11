from rest_framework import serializers

from . models import Book, Loan

class BookSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['name', 'status']

    def get_status(self, obj):
        return obj.status.description

class LoanSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Loan
        fields = ['mulct', 'name', 'status']

    def get_name(self, obj):
        return obj.id_book.name
    
    def get_status(self, obj):
        return obj.id_book.status.description