from rest_framework import serializers

from . models import Book, Loan

class BookSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title', 'status']

    def get_status(self, obj):
        return obj.status.description

class LoanSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Loan
        fields = ['mulct', 'title', 'status']

    def get_title(self, obj):
        return obj.id_book.title
    
    def get_status(self, obj):
        return obj.id_book.status.description