from django.urls import path

from . import views

urlpatterns = [
    path("skills/create/", views.CreateSkillView.as_view()),
    path("skills/", views.ListSkillsView.as_view()),
    path("skills/<int:pk>/", views.RUDSkillView.as_view()),
    path("skills/search/", views.SearchSkillView.as_view())
]