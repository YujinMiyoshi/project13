from django.urls import path
from .views import Top, Login, Logout, UserCreate, UserCreateDone, UserCreateComplete, UserDetail, UserUpdate, PasswordChange, PasswordChangeDone

app_name = 'todo'

urlpatterns = [
    path('', Top.as_view(), name='top'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('user_create/', UserCreate.as_view(), name='user_create'),
    path('user_create/done/', UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', UserCreateComplete.as_view(), name='user_create_complete'),
    path('user_detail/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),
]