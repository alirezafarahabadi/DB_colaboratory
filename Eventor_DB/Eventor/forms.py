from django import forms
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from datetime import date
from .models import *



class UserForm(forms.ModelForm):
    national_code = forms.CharField(min_length=10, max_length=10, validators=[RegexValidator(r'^\d+$')])
    mobile_number = forms.CharField(min_length=11, max_length=11, validators=[RegexValidator(r'^\d+$')])
    current_money = forms.CharField(widget = forms.HiddenInput(), required = False)
    
    class Meta:
        model = User
        fields = ('national_code', 'first_name', 'last_name', 'email', 'mobile_number', 'current_money')
        # read_only_fields = ('current_money',)
        # write_only_fields = ('current_money',)


class ParticipantForm(forms.ModelForm):
    user = forms.CharField(min_length=10, max_length=10, validators=[RegexValidator(r'^\d+$')])
    
    class Meta:
        model = Participant
        fields = ('user', 'education', 'gender', 'faviour_subject')

class EventHolderForm(forms.Form):
    user = forms.CharField(min_length=10, max_length=10, validators=[RegexValidator(r'^\d+$')])
    
    class Meta:
        model = EventHolder
        fields = ('user', 'social_account', 'calling_number', 'website')


class LocationForm(forms.Form):
    class Meta:
        model = Location
        fields = ('name', 'country', 'city', 'street', 'capacity')

class EventForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(years=list(range(2000, timezone.now().year+1))), initial = date.today)

    class Meta:
        model = Event
        fields = ('title' ,'subject', 'date', 'holder', 'location')


class TicketForm(forms.Form):
    class Meta:
        model = Ticket
        fields = ('price', 'type', 'event')


class DiscountcodeForm(forms.Form):
    expire_date = forms.DateField(widget=forms.SelectDateWidget(years=list(range(2000, timezone.now().year+1))), initial = date.today)

    class Meta:
        model = Discountcode
        fields = ('percent', 'expire_date')

class Event_descriptionForm(forms.Form):
    image = forms.CharField(max_length=300, required=False)
    video = forms.CharField(max_length=300, required=False)

    class Meta:
        model = Event_description
        fields = ('event', 'text', 'image', 'video')

class TransactionForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget(years=list(range(2000, timezone.now().year+1))), initial = date.today)

    class Meta:
        model = Transaction
        fields = ('type', 'date', 'price', 'user')

class ParticipateForm(forms.Form):
    class Meta:
        model = Participate
        fields = ('event', 'participant')

class FollowForm(forms.Form):
    class Meta:
        model = Follow
        fields = ('holder', 'participant')

class CommentingForm(forms.Form):
    class Meta:
        model = Commenting
        fields = ('event', 'participant', 'text', 'rate')

class Event_discountcodeForm(forms.Form):
    class Meta:
        model = Event_discountcode
        fields = ('discount', 'event')

class Query_elementsForm(forms.Form):
    event_title = forms.CharField(max_length=50, required=False)
    location_name = forms.CharField(max_length=30, required=False)
    holder_email = forms.EmailField(max_length=30, required=False)
    score = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], required=False)
    subject = forms.CharField(max_length=30, required=False)