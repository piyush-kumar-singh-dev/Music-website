from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view()),
    path('<int:pk>',views.Songdetail.as_view()),
    path("music/signup",views.signup),
    path("music/signin",views.signin),

    ]