from django.urls import path, include
from basic_app.views import user_login 
from basic_app import views 

# TEMPLATE URLS  
app_name = 'basic_app' # this is for the html url referencing

urlpatterns = [
    path('register/', views.register, name = 'register'), 
    path('user_login/', views.user_login, name = 'user_login'),

]