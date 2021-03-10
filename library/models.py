from django.db import models


class Status(models.Model):
    description = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300, null=True)
    author = models.CharField(max_length=300, null=True)
    publisher = models.CharField(max_length=300,null=True)
    year = models.IntegerField(null=True)
    pages = models.IntegerField(null=True)
    language = models.CharField(max_length=100,null=True)
    isbn = models.CharField(max_length=50, unique=True, default='')
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    id_book = models.ForeignKey(Book,null=True, on_delete=models.SET_NULL)
    id_client = models.ForeignKey(Client,null=True, on_delete=models.SET_NULL)
    date_loan = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    date_expected_return = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    date_return = models.DateTimeField(null=True, editable=False)
    fees = models.FloatField(null=True, editable=False)

class Reserve(models.Model):
    id_book = models.ForeignKey(Book,null=True, on_delete=models.SET_NULL)
    id_client = models.ForeignKey(Client,null=True, on_delete=models.SET_NULL)
    date_reserve = models.DateTimeField(auto_now_add=True, null=True, editable=False)





