from django.db import models
from django.utils.translation import gettext_lazy as _


"""
https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-choices


"""


class TransactionType(models.TextChoices):
    PAYMENT = "PMT", _("Payment") 
    INVOICE = "INV", _("Invoice")
    CREDIT = "CRN", _("Credit Note")
    REFUND = "REF", _("Refund")
