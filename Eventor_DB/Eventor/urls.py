from django.urls import path
from Eventor import views as eventor_view

urlpatterns = [
    path('participant/', eventor_view.participant),
    path('eventholder/', eventor_view.eventholder),
    path('comment/', eventor_view.comment),
    path('location/', eventor_view.location),
    # path('ticket/', eventor_view.ticket),
    # path('discountcode/', eventor_view.discountcode),
    # path('event/', eventor_view.event),
    # path('transaction/', eventor_view.transaction),
    # path('participate/', eventor_view.participate),
    # path('follow/', eventor_view.follow),
    # path('commenting/', eventor_view.commenting),
    # path('event_description/', eventor_view.event_description),

]

