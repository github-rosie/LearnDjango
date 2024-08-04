from django.db import models
from django.utils.translation import gettext_lazy as _


"""
https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-choices


"""


class TransactionType(models.TextChoices):
    PAYMENT = "PMT", _("Payment") 
    INVOICE = "INV", _("Invoice")
    CREDIT = "CRN", _("Credit Note")
    REFUND = "RFD", _("Refund")

class PaymentMethod(models.TextChoices):
    EFT = "EFT", _("EFT") 
    BPAY = "BPAY", _("BPAY") 
    POST_BILLPAY = "PBPAY", _("Post Billpay")
    TELEGRAPHIC_TRANSFER = "TT", _("Telegraphic Transfer")  # International Funds Transfer
    CREDIT_CARD = "CC", _("Credit Card")
    DIRECT_DEBIT = "DD", _("Direct Debit")

