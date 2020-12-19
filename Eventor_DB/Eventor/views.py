from django.shortcuts import redirect, render, HttpResponse
from .forms import *
from .models import *
from django.db import connection, transaction
from django import template
from django.db.models.query_utils import Q


register = template.Library()
@register.filter(name='get_class')
def get_class(value):
  return value.__class__.__name__


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
        print(query)
        if int(query) == 1:
            mylocation = form.data['location_name']
            res = Event.objects.filter(location__name=mylocation)
            form1 = EventForm()
            ctx = {
            'form': form1,
            'active_orders': res
            }
            return render(request, 'result_event.html', ctx)   

        if int(query) == 2:
            mylist=[]
            myevent = form.data['event_title']
            res = Participate.objects.filter(event__title=myevent)
            # print(res)
            for i in res:
                mylist.append(i.participant.user)
            form1 = UserForm()
            ctx = {
            'form': form1,
            'active_orders': mylist
            }
            return render(request, 'result_user.html', ctx) 

        if int(query) == 3:
            mylist=[]
            myrate = form.data['score']
            mycommenting = Commenting.objects.filter(rate__gte=myrate)
            for i in mycommenting:
                mylist.append(i.participant.user)
            form1 = UserForm()
            ctx = {
            'form': form1,
            'active_orders': mylist
            }
            return render(request, 'result_user.html', ctx) 

        if int(query) == 4:
            mylist=[]
            myevent = form.data['event_title']
            myticket = Ticket.objects.filter(event__title=myevent)
            # for i in mycommenting:
            #     mylist.append(i.participant.user)
            form1 = TicketForm()
            ctx = {
            'form': form1,
            'active_orders': myticket
            }
            return render(request, 'result_ticket.html', ctx) 

        if int(query) == 5:
            mylist=[]
            myevent = form.data['event_title']
            mycommenting = Commenting.objects.filter(event__title=myevent)
            print(mycommenting)
            # for i in mycommenting:
            #     mylist.append(i.participant.user)
            form1 = CommentingForm()
            ctx = {
            'form': form1,
            'active_orders': mycommenting
            }
            return render(request, 'result_comment.html', ctx) 

        if int(query) == 6:
            mylist=[]
            myemail = form.data['holder_email']
            myfollow = Follow.objects.filter(holder__user__email=myemail)
            # print(myfollow)
            for i in myfollow:
                mylist.append(i.participant.user)
            form1 = UserForm()
            ctx = {
            'form': form1,
            'active_orders': mylist
            }
            return render(request, 'result_user.html', ctx)


        if int(query) == 7:
            mylist=[]
            mysubject = form.data['subject']
            myevent = Event.objects.filter(subject=mysubject)
            # print(myfollow)
            # for i in myfollow:
            #     mylist.append(i.participant.user)
            form1 = EventForm()
            ctx = {
            'form': form1,
            'active_orders': myevent
            }
            return render(request, 'result_event.html', ctx) 

        if int(query) == 8:
            myusers = MyUser.objects.all()
            form1 = UserForm()
            ctx = {
            'form': form1,
            'active_orders': myusers
            }
            return render(request, 'result_user.html', ctx) 

        if int(query) == 9:
            mytrans = Transaction.objects.all()
            form1 = TransactionForm()
            ctx = {
            'form': form1,
            'active_orders': mytrans
            }
            return render(request, 'result_transaction.html', ctx)

        if int(query) == 10:
            myevent1 = form.data['event_title']
            print(myevent1)
            mydist = Event_description.objects.filter(event__title=myevent1)
            print(mydist)
            form1 = Event_descriptionForm()
            ctx = {
            'form': form1,
            'active_orders': mydist
            }
            return render(request, 'result_des.html', ctx)


    else:
        form = Query_elementsForm()
        return render(request, 'query.html', {'form': form})
