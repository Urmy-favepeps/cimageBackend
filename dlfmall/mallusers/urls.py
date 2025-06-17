from django.urls import path

from mallusers import views

urlpatterns = [
    path("signup/", views.userSignup.as_view()),
    path("getmembershipDetails/<email>",views.usermembership.as_view())
]