from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


PAYMENT = 'payment'
INVOICE = 'invoice'
CREDIT_NOTE = 'credit_note'
REFUND = 'refund'
""" A debit note is a document issued by a buyer to a seller, indicating a return of goods received or a correction of an invoice, resulting in a reduction in the amount payable. 
"""
DEBIT_NOTE = 'debit_note' 
PREPAYMENT = 'prepayment'
ADJUSTMENT = 'adjustment'

LINE_TYPE_CHOICES = [
    (PAYMENT, 'Payment'),
    (INVOICE, 'Invoice'),
    (CREDIT_NOTE, 'Credit Note'),
    (REFUND, 'Refund'),    
    (DEBIT_NOTE, 'Debit Note'), 
    (PREPAYMENT, 'Prepayment'),
    (ADJUSTMENT, 'Adjustment'),
    ]


EFT = 'EFT'
INTERNATIONAL_EFT = 'International EFT'
BPAY = 'BPAY'
POST_BILLPAY = 'Post Billpay'
CREDIT_CARD = 'Credit Card'
DIRECT_DEBIT = 'Direct Debit'

PAYMENT_TYPE_CHOICES = [
    (EFT, 'EFT'),
    (INTERNATIONAL_EFT, 'International EFT'),
    (BPAY, 'BPAY'),
    (POST_BILLPAY, 'Post Billpay'),
    (CREDIT_CARD, 'Credit Card'),
    (DIRECT_DEBIT, 'Direct Debit'),
    ]


class PaymentBatchLineItem(models.Model):
    line_id = models.CharField(max_length=100)
    line_type = models.CharField(max_length=20, choices=LINE_TYPE_CHOICES, null=False, blank=False)
    vendor_id = models.CharField(max_length=50)
    vendor_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False) # date must <= timezone.now()
    due_date = models.DateField(auto_now=False)
    external_doc_id = models.CharField(max_length=100)
    system_id = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    amount_due_foreign_currency = models.DecimalField(max_digits=10, decimal_places=2)
    tax_foreign_currency = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=30, choices=PAYMENT_TYPE_CHOICES)

    
    

