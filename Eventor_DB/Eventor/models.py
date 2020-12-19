from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from datetime import date

TRANSACTION_CHOICES = (
    ('buy', 'BUY'),
    ('sell', 'SELL'),
    ('donate', 'donate')
)

class MyUser(models.Model):
    national_code = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d+$')])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile_number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d+$')])
    current_money = models.IntegerField(default=0)

    def __str__(self):
        ret = self.first_name + "  "+self.last_name
        return ret


class Participant(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    education = models.CharField(max_length=50)
    gender = models.BooleanField()
    faviour_subject = models.CharField(max_length=50)

    def __str__(self):
        ret = self.user.first_name + "  "+self.user.last_name
        return ret

class EventHolder(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    social_account = models.CharField(max_length=30)
    calling_number = models.IntegerField()
    website = models.CharField(max_length=30)

    def __str__(self):
        ret = self.user.first_name + "  "+self.user.last_name
        return ret


class Location(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=300)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=30)
    date = models.DateField(default=date.today)
    holder = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        ret = self.title + "  , subject: " + self.subject
        return ret


class Ticket(models.Model):
    price = models.IntegerField()
    type = models.CharField(max_length=30)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        ret = self.event.title + "  , price: " + str(self.price)
        return ret


class Discountcode(models.Model):
    percent = models.IntegerField()
    expire_date = models.DateField(default=date.today)

    def __str__(self):
        ret = "percent: " + str(self.percent) + "  , expire: " + str(self.expire_date)
        return ret


class Event_description(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.CharField(max_length=3000)
    image = models.CharField(max_length=300, null=True)
    video = models.CharField(max_length=300, null=True)

class Transaction(models.Model):
    type = models.CharField(max_length=30, choices=TRANSACTION_CHOICES)
    date = models.DateField(default=date.today)
    price = models.IntegerField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        ret = self.type + "  , date: " + str(self.date)
        return ret



class Participate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

class Follow(models.Model):
    holder = models.ForeignKey(EventHolder, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

class Commenting(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Event_discountcode(models.Model):
    discount = models.ForeignKey(Discountcode, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

