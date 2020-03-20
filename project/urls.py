
from django.contrib import admin
from django.urls import path,include
from place import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),


    path('place/<int:place_id>/',views.detail,name='detail'),
    path('place/<int:lan_id>/<int:place_id>/',views.lang,name='lang'),
    path('guide/<int:guide_id>/',views.guide,name='guide'),
    path('ticket/add/',views.tick,name='tick'),
    path('ticket/',views.ticket,name='ticket'),




]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
