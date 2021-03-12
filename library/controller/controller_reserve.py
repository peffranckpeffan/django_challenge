from ..models import Reserve

from .controller_client import getClient
from .controller_book import getBook, getBookStatus

from datetime import *

#For a given book id and a given client id, make the reservation if the book is available
#and return a success messsage, in the case of the book is reserved or borrowed
#return a error message
def reserveBook(id_book, id_client):
    
    book = getBook({'id':id_book})

    if book.status.description !=  'Available':
        message = {'error' : 'The book is currently unavailable.'}
    else:
        bookstatus = getBookStatus({"description":'Reserved'})
        
        #Update the status of the book
        book.status = bookstatus
        book.save()

        #Create the reservation
        client = getClient({'id':id_client})
        reserve = Reserve(id_book=book, id_client=client)
        reserve.save()

        message = {'sucess' : 'Book successfully reserved.'}
    
    return message