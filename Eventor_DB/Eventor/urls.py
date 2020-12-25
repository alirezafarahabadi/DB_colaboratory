from django.urls import path
from Eventor import views as eventor_view

urlpatterns = [
    path('insert/user/', eventor_view.user),
    path('insert/participant/', eventor_view.participant),
    path('insert/eventholder/', eventor_view.eventholder),
    path('insert/location/', eventor_view.location),
    path('insert/ticket/', eventor_view.ticket),
    path('insert/discountcode/', eventor_view.discountcode),
    path('insert/event/', eventor_view.event),
    path('insert/transaction/', eventor_view.transaction),
    path('insert/participate/', eventor_view.participate),
    path('insert/follow/', eventor_view.follow),
    path('insert/commenting/', eventor_view.commenting),
    path('insert/event_description/', eventor_view.event_description),
    path('insert/event_discountcode/', eventor_view.event_discountcode),
    path('query/', eventor_view.get_query),

]

