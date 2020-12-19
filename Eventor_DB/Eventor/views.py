from django.shortcuts import redirect, render, HttpResponse
from .forms import *
from django.db import connection, transaction


def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print("ok!")
            print(form.data)
            instance = form.save(commit=False)
            instance.current_money = 0
            instance.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'main.html', {'form': form, 't':"User"})

def participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = ParticipantForm()
    return render(request, 'main.html', {'form': form, 't':"Participant"})

def eventholder(request):
    if request.method == 'POST':
        form = EventHolderForm(request.POST)
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = EventHolderForm()
    return render(request, 'main.html', {'form': form, 't':"EventHolder"})
    

def location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = LocationForm()
    return render(request, 'main.html', {'form': form, 't':"Location"})

def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = TicketForm()
    return render(request, 'main.html', {'form': form, 't':"Ticket"})

def discountcode(request):
    if request.method == 'POST':
        form = DiscountcodeForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = DiscountcodeForm()
    return render(request, 'main.html', {'form': form, 't':"DiscountCode"})

def event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
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
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = TransactionForm()
    return render(request, 'main.html', {'form': form, 't':"Transaction"})

def participate(request):
    if request.method == 'POST':
        form = ParticipateForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = ParticipateForm()
    return render(request, 'main.html', {'form': form, 't':"Participate"})

def follow(request):
    if request.method == 'POST':
        form = FollowForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = FollowForm()
    return render(request, 'main.html', {'form': form, 't':"Follow"})

def commenting(request):
    if request.method == 'POST':
        form = CommentingForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = CommentingForm()
    return render(request, 'main.html', {'form': form, 't':"Commentig"})

def event_description(request):
    if request.method == 'POST':
        form = Event_descriptionForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            print(form.data)
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = Event_descriptionForm()
    return render(request, 'main.html', {'form': form, 't':"Event Description"})

def get_query(request):
    
    if request.method == 'POST':
        cursor = connection.cursor()
        form = Query_elementsForm(request.POST)
        query = request.POST['queries']
        if int(query) == 1:
            mylocation = form.data['location_name']
            a = Event.objects.filter(location__name=mylocation)
            # for w in a:
            form = EventForm(a)
            # print(aa)
            
            # print(a)
            # cursor.execute('SELECT "Eventor_event"."title" FROM "Eventor_event" inner join "Eventor_location" ON ( Eventor_event.location_id = "Eventor_location".id ) WHERE "Eventor_location"."name" = {}'.format(location))
            # cursor.execute('select title from "Eventor_event" join "Eventor_location" on ')
            # row = cursor.fetchone()
            # print(row)
            return render(request, 'result.html', {'form': form})      
    else:
        form = Query_elementsForm()
        return render(request, 'query.html', {'form': form})
