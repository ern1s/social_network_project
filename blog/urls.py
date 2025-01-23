from django.urls import path

from . import views

urlpatterns = {
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>', views.CategoryListCreateAPIView.as_view()),
    path('publications/', views.PublicationListCreateAPIVew.as_view()),
}