from django.urls import path
from .views import Top, login, Logout

app_name = 'todo'

urlpatterns = [
    path('', Top.as_view(), name='top'),
    path('login/', login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]