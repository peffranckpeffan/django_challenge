from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer, LoanSerializer

from .controller.controller_loan import updateLoanMulct, filterLoans
from .controller.controller_book import getBooks
from .controller.controller_reserve import reserveBook

#Returns a json with all books registered in the database
@api_view(['GET'])
def getAllBooks(request):

    books = getBooks()

    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)

#Returns a json with all books loaned to a given client
@api_view(['GET'])
def getLoanedBooks(request, pk_client):
    
    updateLoanMulct(filter = {'id_client':pk_client, 'date_return__isnull': True, 'status': True})
    
    loans = filterLoans({'id_client':pk_client, 'date_return__isnull': True, 'status': True})

    serializer = LoanSerializer(loans, many=True)

    return Response(serializer.data)

#Reserves the book to a given client
@api_view(['GET'])
def makeBookReservation(request, pk_book, pk_client):

    message = reserveBook(pk_book, pk_client)

    return Response(message)