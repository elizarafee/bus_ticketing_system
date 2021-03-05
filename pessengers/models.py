from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Pessenger(models.Model):
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email = models.EmailField(max_length=254)

# python3 manage.py shell 
# from pessengers.models import Pessenger
# p = Pessenger(name = "Eliza", phone_number = +447311256256, email = "elizarafee@gmail.com")
# p.save()
# p
# Pessenger.objects.all() == select * from Pessenger

    def __str__(self):
        return f"Name : {self.name}, Phone Number: {self.phone_number}, email: {self.email}"

# python3 manage.py shell
# from pessengers.models import Pessenger
# pessengers = Pessenger.objects.all()
# pessengers
# p = pessengers.first()    
# p                          -- returns the first value
# p.name, p.phone_number, p.email
# p.delete()                -- delete the particular pessenger