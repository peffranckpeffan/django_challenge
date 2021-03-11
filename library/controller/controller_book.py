from ..models import Book, BookStatus

from datetime import *

#Get all books from the database
def getBooks():
    books = Book.objects.all()
    return books

#Get the book for a given filter
def getBook(filter):
    book = Book.objects.get(**filter)
    return book

#Get the book status for a given filter
def getBookStatus(filter):
    bookstatus = BookStatus.objects.get(**filter)
    return bookstatus
