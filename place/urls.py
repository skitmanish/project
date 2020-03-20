
from django.urls import path
from . import views

urlpatterns = [

            path('place/<int:place_id>/',views.detail,name='detail'),
            path('place/<int:lan_id>/<int:place_id>/',views.lang,name='lang'),
            path('guide/<int:guide_id>/',views.guide,name='guide'),
            path('ticket/',views.ticket,name='ticket'),







]
