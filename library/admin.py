from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(BookStatus)
admin.site.register(Client)
admin.site.register(Loan)
admin.site.register(Reserve)