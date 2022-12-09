from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    full_name = models.CharField(max_length=50)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=5)
    reg_date = models.DateField()
    blocked = models.BooleanField(default=False)
    def __str__(self):
        """String for representing the Model object."""
        return self.login

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('user-detail', args=[str(self.user_id)])
class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)
    short_name = models.CharField(max_length=3)
    in_rubs = models.FloatField()
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('currency-detail', args=[str(self.currency_id)])
class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('country-detail', args=[str(self.country_id)])
class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('bank-detail', args=[str(self.bank_id)])
class Check(models.Model):
    check_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    number = models.CharField(max_length=16, unique=True)
    balance = models.FloatField()
    csv = models.CharField(max_length=3)
    limit = models.DateField()
    def __str__(self):
        """String for representing the Model object."""
        return self.number

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('check-detail', args=[str(self.check_id)])
class Operation(models.Model):
    op_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    receive_bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    send_check_id = models.ForeignKey(Check, on_delete=models.CASCADE)
    receive_number = models.CharField(max_length=16)
    receive_full_name = models.CharField(max_length=50)
    received_money = models.ForeignKey(Currency, on_delete=models.CASCADE)
    sent_money = models.FloatField()
    comission = models.FloatField()
    date = models.DateTimeField()
    def __str__(self):
        """String for representing the Model object."""
        return self.op_id

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('operation-detail', args=[str(self.op_id)])
class Active(models.Model):
    active_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    active_type = models.CharField(max_length=20)
    balance = models.FloatField()
    date = models.DateField()
    term = models.IntegerField()
    def __str__(self):
        """String for representing the Model object."""
        return self.active_type

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('active-detail', args=[str(self.active_id)])