from django.urls import path
from . import views
urlpatterns = [ path("customer",views.index ,name='index') ]