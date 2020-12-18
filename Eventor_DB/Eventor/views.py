from django.shortcuts import redirect, render
from .forms import *


def user(request):
    if request.method == 'POST':
        print("aassaa1")
        form = UserForm(request.POST)
        print("aassaa")
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = UserForm()
    return render(request, 'main.html', {'form': form, 't':"User"})

def participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = ParticipantForm()
    return render(request, 'main.html', {'form': form, 't':"Participant"})

def eventholder(request):
    if request.method == 'POST':
        form = EventHolderForm(request.POST)
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = EventHolderForm()
    return render(request, 'main.html', {'form': form, 't':"EventHolder"})
    

def location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = LocationForm()
    return render(request, 'main.html', {'form': form, 't':"Location"})

def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = TicketForm()
    return render(request, 'main.html', {'form': form, 't':"Ticket"})

def discountcode(request):
    if request.method == 'POST':
        form = DiscountcodeForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = DiscountcodeForm()
    return render(request, 'main.html', {'form': form, 't':"DiscountCode"})

def event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = EventForm()
    return render(request, 'main.html', {'form': form, 't':"Event"})

def transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        print(form.data)
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = TransactionForm()
    return render(request, 'main.html', {'form': form, 't':"Transaction"})

def participate(request):
    if request.method == 'POST':
        form = ParticipateForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = ParticipateForm()
    return render(request, 'main.html', {'form': form, 't':"Participate"})

def follow(request):
    if request.method == 'POST':
        form = FollowForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = FollowForm()
    return render(request, 'main.html', {'form': form, 't':"Follow"})

def commenting(request):
    if request.method == 'POST':
        form = CommentingForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = CommentingForm()
    return render(request, 'main.html', {'form': form, 't':"Commentig"})

def event_description(request):
    if request.method == 'POST':
        form = Event_descriptionForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = Event_descriptionForm()
    return render(request, 'main.html', {'form': form, 't':"Event Description"})

def get_query(request):
    # pass
    if request.method == 'POST':
        form = Query_elementsForm(request.POST)
        print(request.POST)  
        # if (request.POST.get('queries') == 1):

        return redirect('https://google.com')      
    else:
        form = Query_elementsForm()
        return render(request, 'query.html', {'form': form})
