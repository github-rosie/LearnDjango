from django.test import TestCase


# Create Super User 
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.create_superuser('admin', 'admin@email.com', '****') # replace with your email and password
user.save()

user
user.username
user.password
user.email