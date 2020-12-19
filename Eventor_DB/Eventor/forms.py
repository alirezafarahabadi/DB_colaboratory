from django import forms
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from datetime import date
from .models import *


GENDER_CHOICES = (
    (True, 'Female'),
    (False, 'Male')
)



class UserForm(forms.ModelForm):
    national_code = forms.CharField(min_length=10, max_length=10)
    mobile_number = forms.CharField(min_length=11, max_length=11)
    current_money = forms.CharField(widget = forms.HiddenInput(), initial=0, required=False)
    
    class Meta:
        model = MyUser
        fields = ('national_code', 'first_name', 'last_name', 'email', 'mobile_number', 'current_money')
        # read_only_fields = ('current_money',)
        # write_only_fields = ('current_money',)


class ParticipantForm(forms.ModelForm):
    user = forms.CharField(min_length=10, max_length=10, validators=[RegexValidator(r'^\d+$')], label='national code')
    gender = forms.ChoiceField(choices = GENDER_CHOICES, initial='', widget=forms.Select())

    class Meta:
        model = Participant
        fields = ('user', 'education', 'gender', 'faviour_subject')

class EventHolderForm(forms.ModelForm):
    user = forms.CharField(min_length=10, max_length=10, validators=[RegexValidator(r'^\d+$')], label='national code')
    
    class Meta:
        model = EventHolder
        fields = ('user', 'social_account', 'calling_number', 'website')


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'country', 'city', 'street', 'capacity')

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(years=list(range(2000, timezone.now().year+1))), initial = date.today)

    class Meta:
        model = Event
        fields = ('title' ,'subject', 'date', 'holder', 'location')


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('price', 'type', 'event')


class DiscountcodeForm(forms.ModelForm):
    expire_date = forms.DateField(widget=forms.SelectDateWidget(years=list(range(2000, timezone.now().year+1))), initial = date.today)

    class Meta:
        model = Discountcode
        fields = ('percent', 'expire_date')

class Event_descriptionForm(forms.ModelForm):
    image = forms.CharField(max_length=300, required=False)
    video = forms.CharField(max_length=300, required=False)

    class Meta:
        model = Event_description
        fields = ('event', 'text', 'image', 'video')

class TransactionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(years=list(range(2000, timezone.now().year+1))), initial = date.today)

    class Meta:
        model = Transaction
        fields = ('type', 'date', 'price', 'user')

class ParticipateForm(forms.ModelForm):
    class Meta:
        model = Participate
        fields = ('event', 'participant')

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ('holder', 'participant')

class CommentingForm(forms.ModelForm):
    class Meta:
        model = Commenting
        fields = ('event', 'participant', 'text', 'rate')

class Event_discountcodeForm(forms.ModelForm):
    class Meta:
        model = Event_discountcode
        fields = ('discount', 'event')

class Query_elementsForm(forms.Form):
    event_title = forms.CharField(max_length=50, required=False)
    location_name = forms.CharField(max_length=30, required=False)
    holder_email = forms.EmailField(max_length=30, required=False)
    score = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], required=False)
    subject = forms.CharField(max_length=30, required=False)