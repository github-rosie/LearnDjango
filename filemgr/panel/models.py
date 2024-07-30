from django.db import models



class ModelWithImageField(models.Model):
    """ 
    models.Model class represents a database table in Django's ORM (Object-Relational Mapping), it defines the structure of the data (fields) and the behaviors of the data (methods) stored in the database.
    Pillow package has be be installed for ImageField to work
    """
    name = models.CharField(max_length=500)
    # images will be uploaded to directory: root/project/media/image/, when MEDIA_ROOT is setup in the project settings
    image = models.ImageField(upload_to='image/') 


class ModelWithFileField(models.Model):
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to='files/')  



""" 
class Invoice(models.Model):
    invoice_id = models.CharField(max_length=50)
    date = models.DateField()
    file = models.FileField()  # It is usually a pdf file

class PmtBatch(models.Model):
    batch_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=2)
    file = models.FileField() # It is usually an excel file 

class Transaction(models.Model):
    external_id = models.CharField(max_length=20)
    line_type = models.CharField(max_length=20)  # invoice, payment, credit note, refund, etc
    vendor_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False) # date must <= timezone.now()
    description = models.TextField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
"""
