from django.urls import path
from clients import views

urlpatterns = [
                path('application/', views.ApplicationList.as_view(), name = views.ApplicationList.name),
                path('application/<int:pk>',views.ApplicationDetail.as_view(), name=views.ApplicationDetail.name),
                path('client/', views.ClientList.as_view(), name=views.ClientList.name),
                path('client/<int:pk>', views.ClientDetail.as_view(), name=views.ClientDetail.name),
                path('', views.ApiRoot.as_view(),  name=views.ApiRoot.name),
                ]