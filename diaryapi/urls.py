from django.urls import path
from .import views 

urlpatterns = [
    path('diary/', views.DiaryView.as_view()),
    path('diary/<str:id>',views.DiaryDetailView.as_view()),
    path('register/', views.RegisterUserView.as_view())
]
