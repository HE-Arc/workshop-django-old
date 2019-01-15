from django.urls import path, include
from django.contrib import admin

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('soldiers', views.SoldierViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/soldiers', views.SoldierListView.as_view(), name='dashboard-soldiers'),
    path('dashboard/soldier/new', views.SoldierCreateView.as_view(), name='soldier-new'),
    path('dashboard/soldier/<pk>/', views.SoldierDetailView.as_view(), name='soldier-detail'),
    path('dashboard/soldier/<pk>/update', views.SoldierUpdateView.as_view(), name='soldier-update'),
    path('dashboard/soldier/<pk>/delete', views.SoldierDeleteView.as_view(), name='soldier-delete'),
    path('dashboard/soldier/deadonthefield', views.SoldierDeadOnTheField.as_view(), name='soldier-dead'),
    path('api/v1/', include(router.urls))
]
