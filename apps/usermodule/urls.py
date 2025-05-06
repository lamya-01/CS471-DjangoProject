from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
urlpatterns = [ 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login_view')), name='logout'),
    
]