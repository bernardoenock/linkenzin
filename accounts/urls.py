from django.urls import path

from . import views as account_views
from educations import views as education_views



urlpatterns = [
    path("accounts/register/", account_views.RegisterAccountView.as_view()),
    path("accounts/", account_views.ListAllAccountsView.as_view()),
    path("accounts/<int:pk>/", account_views.RUDAccountView.as_view()),
    path("accounts/login/", account_views.LoginAccountsView.as_view()),


    path("accounts/education/", education_views.ListCreateEducationsView.as_view()),
    path("accounts/education/<int:pk>/", education_views.RUDEducationsView.as_view())


]