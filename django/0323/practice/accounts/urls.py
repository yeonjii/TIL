from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),  # 계정삭제(탈퇴)
    path('update/', views.update, name='update'),  # 회원정보 수정
    path('password/', views.update_password, name='update_password'),
]