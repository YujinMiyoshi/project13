from django.urls import path
from .views import Top, Login, Logout, UserCreate, UserCreateDone, UserCreateComplete, UserDetail, UserUpdate, PasswordChange, PasswordChangeDone, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete, EmailChange, EmailChangeDone, EmailChangeComplete, ToDoList, ToDoListWithPK, ToDoDetail, ToDoCreate, ToDoUpdate, ToDoDelete

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
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('email/change/', EmailChange.as_view(), name='email_change'),
    path('email/change/done/', EmailChangeDone.as_view(), name='email_change_done'),
    path('email/change/complete/<str:token>/', EmailChangeComplete.as_view(), name='email_change_complete'),
    path('todo/', ToDoList.as_view(), name='todo_list'),
    path('todo/<int:pk>', ToDoListWithPK.as_view(), name='todo_pk_list'),
    path('todo/detail/<int:pk>/', ToDoDetail.as_view(), name='todo_detail'),
    path('todo/create/<int:pk>/', ToDoCreate.as_view(), name='todo_create'),
    path('todo/update/<int:pk>/', ToDoUpdate.as_view(), name='todo_update'),
    path('todo/delete/<int:pk>/', ToDoDelete.as_view(), name='todo_delete'),
]