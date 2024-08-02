from django.db import models

from .choices import TransactionType

class Transaction(models.Model):
    tran_type = models.CharField(max_length=20, choices=TransactionType)
    doc_id = models.CharField(max_length=30, blank=True, null=True)   
    doc_date = models.DateField(null=False, blank=False)
    vendor_name = models.TextField(max_length=60, blank=False, null=False)
    amount = models.DecimalField(blank=False, null=False, max_digits=20, decimal_places=2)
    file = models.FileField(upload_to='files/')
    
    def __str__(self):
        return f'{self.tran_type} - {self.doc_id} - {self.doc_date} - {self.amount}'

class ModelWithImageField(models.Model):
    """ 
    models.Model class represents a database table in Django's ORM (Object-Relational Mapping), it defines the structure of the data (fields) and the behaviors of the data (methods) stored in the database.
    Pillow package has be be installed for ImageField to work
    """
    image_name = models.CharField(max_length=500)
    # images will be uploaded to directory: root/project/media/image/, when MEDIA_ROOT is setup in the project settings
    # Note the upload_to parameter. The files will be automatically uploaded to MEDIA_ROOT/image/
    image = models.ImageField(upload_to='image/') 
    
    """
    It is important to add __str__() methods to models, not only for your own convenience when dealing with the interactive prompt, but also because objects representations are used throughout Djangos automatically-generated admin.
    """
    def __str__(self):
        return self.image_name


class ModelWithFileField(models.Model):
    file_name = models.CharField(max_length=500)
    # file will be uploaded to directory: root/project/media/image/, when MEDIA_ROOT is setup in the project settings
    # Note the upload_to parameter. The files will be automatically uploaded to MEDIA_ROOT/files/
    file = models.FileField(upload_to='files/')  

    """
    It is important to add __str__() methods to models, not only for your own convenience when dealing with the interactive prompt, but also because objects representations are used throughout Djangos automatically-generated admin.
    """
    def __str__(self):
        return self.file_name






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
