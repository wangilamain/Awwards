from django.urls import path,include
from django.contrib.auth.views import LogoutView
from .views import home, register, profile,edit_profile,postdetail,search_results,index
from django.conf.urls import url

                     
urlpatterns=[
    path(r'^$', index, name = 'index'),
    path('' ,home, name = 'home'),
    path('register/', register, name='register'),
    path('profile/<username>/',profile, name='profile'),
    path('profile/<username>/edit', edit_profile, name='edit'),
    path('details/<post_id>/', postdetail, name='details'),
    path('search/',search_results, name='search_results'),
    path('logout/', LogoutView.as_view(), name='logout'),
]