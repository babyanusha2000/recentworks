from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('signup',views.signup,name='signup'),
    path('login',views.loginview,name='login'),
    path('userpage',views.user_page,name='userpage'),
    path('createrecipe',views.recipe_create,name='createrecipe'),
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipe/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('logout',views.log_out,name='logout')
]
