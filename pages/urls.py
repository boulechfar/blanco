from django.urls import path
from . import views
urlpatterns = [
   path('signup/',views.signup,name='signup'),
   path('profile/',views.profile,name='profile'),
   path('profile/edit',views.profile_edit,name='profile_edit'),

   path('',views.index,name='index'),
   path('about',views.about,name='about'),
   path('portfilo',views.portfilo,name='portfilo'),



]