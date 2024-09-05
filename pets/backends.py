# backends.py
from django.contrib.auth.models import AnonymousUser

from django.contrib.auth.backends import BaseBackend
from .models import Supplier

class SupplierBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        print('call here',username,password)
        
        try:
            supplier = Supplier.objects.get(username=username)
            if supplier.password == password:  # Direct comparison without hashing
                return supplier
        except Supplier.DoesNotExist:
            # No user found with this username
            return None

    # def get_user(self, request,username):
    #     print('this is worling')
    #     try:
    #         return Supplier.objects.get()
    #     except Supplier.DoesNotExist:
    #         return 'no user found'