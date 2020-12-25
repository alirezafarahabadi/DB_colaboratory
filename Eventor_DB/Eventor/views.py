from django.shortcuts import redirect, render, HttpResponse
from .forms import *
from .models import *
from django.db import connection, transaction
from django import template
from django.db.models.query_utils import Q
from django.db.models.query import QuerySet, RawQuerySet
# from psycopg2.extras import NamedTupleCursor 
# import django.db.backends.postgresql_psycopg2 as psycopg2


register = template.Library()
@register.filter(name='get_class')
def get_class(value):
  return value.__class__.__name__

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]


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

def event_discountcode(request):
    if request.method == 'POST':
        form = Event_discountcodeForm(request.POST)
        
        if form.is_valid():
            print("ok!")
            form.save()
            return render(request, 'success.html')
        else:
            print("error!")
            print(form.errors)
            return render(request, 'error.html', {'form': form})
    else:
        form = Event_discountcodeForm()
    return render(request, 'main.html', {'form': form, 't':"Event Description"})

def get_query(request):
    
    if request.method == 'POST':
        # cursor = connection.cursor()
        form = Query_elementsForm(request.POST)
        query = request.POST['queries']
        print(query)
        if int(query) == 1:
            mylocation = form.data['location_name']
            with connection.cursor() as cursor:
                cursor.execute("""SELECT "Eventor_event"."title", "Eventor_event"."subject", "Eventor_event"."date","Eventor_event"."holder_id", "Eventor_location"."name" FROM "Eventor_event" INNER JOIN "Eventor_location" ON ( "Eventor_event"."location_id" = "Eventor_location"."id" ) WHERE "Eventor_location"."name" = %s""", [mylocation])
                row = dictfetchall(cursor)
            ctx = {
            'active_orders': row
            }
            return render(request, 'result_event.html', ctx)   

        if int(query) == 2:
            mylist=[]
            myevent = form.data['event_title']
            with connection.cursor() as cursor:
                cursor.execute("""SELECT u."first_name", u."last_name", u."email" from "Eventor_myuser" u inner join "Eventor_participant" p on ( p."user_id" = u."id" ) inner join "Eventor_participate" pp on ( pp."participant_id" = p."id" ) inner join "Eventor_event" e on ( e."id" = pp."event_id" ) where e."title" = %s""", [myevent])
                row = dictfetchall(cursor)
            ctx = {
            'active_orders': row
            }
            return render(request, 'result_user.html', ctx) 

        if int(query) == 3:
            mylist=[]
            myevent = form.data['event_title']
            myrate = form.data['score']
            with connection.cursor() as cursor:
                cursor.execute("""SELECT u."first_name", u."last_name", u."email", c."rate" from "Eventor_myuser" u inner join "Eventor_participant" p on ( p."user_id" = u."id" ) inner join "Eventor_commenting" c on ( c."participant_id" = p."id" ) inner join "Eventor_event" e on ( e."id" = c."event_id" ) where e."title" = %s and c."rate" >= %s""", [myevent, myrate])
                row = dictfetchall(cursor)
            ctx = {
            'active_orders': row
            }
            return render(request, 'result_user.html', ctx) 

        if int(query) == 4:
            mylist=[]
            myevent = form.data['event_title']
            with connection.cursor() as cursor:
                cursor.execute("""SELECT t."price", t."type" from "Eventor_ticket" t inner join "Eventor_event" e on ( e."id" = t."event_id" ) where e."title" = %s""", [myevent])
                row = dictfetchall(cursor)
            ctx = {
            'active_orders': row
            }
            return render(request, 'result_ticket.html', ctx) 

        if int(query) == 5:
            mylist=[]
            myevent = form.data['event_title']
            with connection.cursor() as cursor:
                cursor.execute("""SELECT c."text", c."rate", c."participant_id" from "Eventor_commenting" c inner join "Eventor_event" e on ( e."id" = c."event_id" ) where e."title" = %s""", [myevent])
                row = dictfetchall(cursor)
            ctx = {
            'active_orders': row
            }
            return render(request, 'result_comment.html', ctx) 

        if int(query) == 6:
            mycompany = form.data['holder_company']
            with connection.cursor() as cursor:
                cursor.execute("""SELECT u."first_name", u."last_name", u."email" from "Eventor_myuser" u inner join "Eventor_participant" p on ( p."user_id" = u."id" ) inner join "Eventor_follow" f on ( f."participant_id" = p."id" ) inner join "Eventor_eventholder" h on ( h."id" = f."holder_id" ) where h."company_name" = %s """, [mycompany])
                row = dictfetchall(cursor)
            ctx = {
            'active_orders': row
            }
            return render(request, 'result_user.html', ctx)


        if int(query) == 7:
            mysubject = form.data['subject']
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Eventor_event" e where e."subject" = %s""", [mysubject])
                row = dictfetchall(cursor)
                print(row)

            ctx = {
            'active_orders': row
            }
            return render(request, 'result_event.html', ctx) 

        if int(query) == 8:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Eventor_myuser" """)
                row = dictfetchall(cursor)
            ctx = {
            'active_orders': row
            }
            return render(request, 'result_user.html', ctx) 

        if int(query) == 9:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Eventor_transaction" """)
                row = dictfetchall(cursor)
            ctx = {
            'active_orders': row
            }
            return render(request, 'result_transaction.html', ctx)

        if int(query) == 10:
            myevent = form.data['event_title']
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM "Eventor_event" e inner join "Eventor_location" l on (l."id" = e."location_id") where e."title" = %s""", [myevent])
                row = dictfetchall(cursor)
            ctx = {
            'active_orders': row
            }
            return render(request, 'result_event.html', ctx)


    else:
        form = Query_elementsForm()
        return render(request, 'query.html', {'form': form})
