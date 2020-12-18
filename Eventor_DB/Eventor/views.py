from django.shortcuts import redirect, render
from .forms import *


def participant(request):
    if request.method == 'POST':
        form = Participant(request.POST)
        
        if form.is_valid():
            print("ok!")
        else:
            print("error!")
            return render(request, 'error.html')
    else:
        form = Participant()
    return render(request, 'main.html', {'form': form, 't':"Participant"})

def eventholder(request):
    if request.method == 'POST':
        form = EventHolder(request.POST)
        print(form.data['first_name'])
        if form.is_valid():
            pass
    else:
        form = EventHolder()
    return render(request, 'main.html', {'form': form, 't':"EventHolder"})
    
def comment(request):
    if request.method == 'POST':
        form = Comment(request.POST)
        
        if form.is_valid():
            pass
    else:
        form = Comment()
    return render(request, 'main.html', {'form': form, 't':"Comment"})

def location(request):
    if request.method == 'POST':
        form = Location(request.POST)
        
        if form.is_valid():
            pass
    else:
        form = Location()
    return render(request, 'main.html', {'form': form, 't':"Location"})

def ticket(request):
    if request.method == 'POST':
        form = Ticket(request.POST)
        
        if form.is_valid():
            pass
    else:
        form = Ticket()
    return render(request, 'main.html', {'form': form, 't':"Ticket"})

def discountcode(request):
    if request.method == 'POST':
        form = Discountcode(request.POST)
        
        if form.is_valid():
            pass
    else:
        form = Discountcode()
    return render(request, 'main.html', {'form': form, 't':"DiscountCode"})

def event(request):
    if request.method == 'POST':
        form = Event(request.POST)
        
        if form.is_valid():
            pass
    else:
        form = Event()
    return render(request, 'main.html', {'form': form, 't':"Event"})

def transaction(request):
    if request.method == 'POST':
        form = Transaction(request.POST)
        print(form.data)
        if form.is_valid():
            pass
    else:
        form = Transaction()
    return render(request, 'main.html', {'form': form, 't':"Transaction"})

def participate(request):
    if request.method == 'POST':
        form = Participate(request.POST)
        
        if form.is_valid():
            pass
    else:
        form = Participate()
    return render(request, 'main.html', {'form': form, 't':"Participate"})

def follow(request):
    if request.method == 'POST':
        form = Follow(request.POST)
        
        if form.is_valid():
            pass
    else:
        form = Follow()
    return render(request, 'main.html', {'form': form, 't':"Follow"})

def commenting(request):
    if request.method == 'POST':
        form = Commenting(request.POST)
        
        if form.is_valid():
            pass
    else:
        form = Commenting()
    return render(request, 'main.html', {'form': form, 't':"Commentig"})

def event_description(request):
    if request.method == 'POST':
        form = Event_description(request.POST)
        
        if form.is_valid():
            pass
    else:
        form = Event_description()
    return render(request, 'main.html', {'form': form, 't':"Event Description"})

def get_query(request):
    # pass
    if request.method == 'POST':
        form = Query_elements(request.POST)
        print(request.POST)  
        # if (request.POST.get('queries') == 1):

        return redirect('https://google.com')      
    else:
        form = Query_elements()
        return render(request, 'query.html', {'form': form})
