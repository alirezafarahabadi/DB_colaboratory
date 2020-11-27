from django import forms

class Participant(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    national_code = forms.IntegerField()
    mobile_number = forms.IntegerField()
    education = forms.CharField()
    gender = forms.IntegerField()
    faviour_subject = forms.CharField()

class EventHolder(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    national_code = forms.IntegerField()
    mobile_number = forms.IntegerField()
    social_account = forms.CharField(max_length=30)
    calling_number = forms.IntegerField()
    website = forms.CharField(max_length=30)



class Comment(forms.Form):
    text = forms.CharField(max_length=30)
    rate = forms.IntegerField()

class Location(forms.Form):
    name = forms.CharField(max_length=30)
    country = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    street = forms.CharField(max_length=300)
    capacity = forms.IntegerField()