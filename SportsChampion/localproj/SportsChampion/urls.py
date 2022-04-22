from django.urls import path, include
from SportsChampion.views import *

app_name = 'SportsChampion'
urlpatterns = [
    path('', index, name = 'index'),
    path('Events', Events, name = 'Events.html'),
    path('News', News, name = 'News.html'),
    path('Sports', Sports, name = 'Sports.html'),
    path('ContactUs', ContactUs, name = 'ContactUs.html'),
    path('Form', Form, name = 'Form.html'),
    path('testlang', testlang, name = 'testlang')

]