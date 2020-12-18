from django import forms
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from datetime import date



class User(forms.Form):
    national_code = forms.CharField(min_length=10, max_length=10, validators=[RegexValidator(r'^\d+$')])
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    mobile_number = forms.CharField(min_length=11, max_length=11, validators=[RegexValidator(r'^\d+$')])
    current_money = forms.IntegerField()


class Participant(forms.Form):
    user = forms.CharField(min_length=10, max_length=10, validators=[RegexValidator(r'^\d+$')])
    education = forms.CharField()
    gender = forms.IntegerField()
    faviour_subject = forms.CharField()

class EventHolder(forms.Form):
    user = forms.CharField(min_length=10, max_length=10, validators=[RegexValidator(r'^\d+$')])
    social_account = forms.CharField(max_length=30)
    calling_number = forms.IntegerField()
    website = forms.CharField(max_length=30)


class Location(forms.Form):
    name = forms.CharField(max_length=30)
    country = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    street = forms.CharField(max_length=300)
    capacity = forms.IntegerField()

class Ticket(forms.Form):
    price = forms.IntegerField()
    type = forms.CharField(max_length=30)
    event = forms.IntegerField()


class Discountcode(forms.Form):
    percent = forms.IntegerField()
    expire_date = forms.DateField(widget=forms.SelectDateWidget(years=list(range(2000, timezone.now().year+1))))

class Event_description(forms.Form):
    event = forms.IntegerField()
    text = forms.CharField(max_length=3000)
    image = forms.CharField(max_length=300, required=False)
    video = forms.CharField(max_length=300, required=False)

class Transaction(forms.Form):
    type = forms.CharField(max_length=30)
    date = forms.DateField(widget=forms.SelectDateWidget(years=list(range(2000, timezone.now().year+1))))
    price = forms.IntegerField()
    user = forms.IntegerField()

class Event(forms.Form):
    title = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=30)
    date = forms.DateField(widget=forms.SelectDateWidget(years=list(range(2000, timezone.now().year+1))), initial = date.today)
    holder = forms.IntegerField()
    location = forms.IntegerField()

class Participate(forms.Form):
    event = forms.IntegerField()
    participant = forms.IntegerField()

class Follow(forms.Form):
    holder = forms.IntegerField()
    participant = forms.IntegerField()

class Commenting(forms.Form):
    event = forms.IntegerField()
    comment = forms.IntegerField()
    participant = forms.CharField(min_length=10, max_length=10, validators=[RegexValidator(r'^\d+$')])
    text = forms.CharField(max_length=300)
    rate = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Event_discountcode(forms.Form):
    discount = forms.IntegerField()
    event = forms.IntegerField()

class Query_elements(forms.Form):
    event_title = forms.CharField(max_length=50, required=False)
    location_name = forms.CharField(max_length=30, required=False)
    holder_email = forms.EmailField(max_length=30, required=False)
    score = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], required=False)
    subject = forms.CharField(max_length=30, required=False)