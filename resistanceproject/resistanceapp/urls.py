from django.urls import path
from django.contrib import admin

from . import views

# TODO-ADV-1-3 Uncomment thos four lines used by restframework
#from rest_framework import routers
#router = routers.DefaultRouter()
#router.register('users', views.UserViewSet)
#router.register('soldiers', views.SoldierViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),

    # TODO-3-1 - Add route for the previously created soldier list view. Name it dashboard-soldiers
    path('dashboard/soldiers',views.SoldierListView.as_view(), name='dashboard-soldiers'),
    # TODO-3-3 - Add route for the previously created soldier detail view. Name soldier-detail
    path('dashboard/soldier/<pk>/',views.SoldierDetailView.as_view(), name='soldier-detail'),
    # TODO-4-1 - Add route for the previously created soldier create view
    path('dashboard/soldier/new',views.SoldierCreateView.as_view(), name='soldier-create'),
    # TODO-4-3 - Add route for the previously created soldier update view
    path('dashboard/soldier/<pk>/update',views.SoldierUpdateView.as_view(), name='soldier-update'),
    # TODO-4-5 - Add route for the previously created soldier delete view
    path('dashboard/soldier/<pk>/delete',views.SoldierDeleteView.as_view(), name='soldier-delete'),
    # TODO-8-1 - Add route for SoldierDeadOnTheField
    path('dashboard/soldier/kill',views.SoldierDeadOnTheField.as_view(), name='soldier-dead'),

    path('board/soldier/resucite',views.SoldierResucite.as_view(), name='soldier-alive'),
    # TODO-ADV-1-4 Add restframework API router urls
]
