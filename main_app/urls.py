from django.urls import path
from . import views

urlpatterns = [
    # path (url_pattern, function, name(optional))
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finch_details, name='details'),
    path('finches/create', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('birdhouses/', views.BirdhouseList.as_view(), name='birdhouses_list'),
    path('birdhouses/<int:pk>/', views.BirdhouseDetail.as_view(), name='birdhouses_detail'),
    path('birdhouses/create/', views.BirdhouseCreate.as_view(), name='birdhouses_create'),
    path('birdhouses/<int:pk>/update/', views.BirdhouseUpdate.as_view(), name='birdhouses_update'),
    path('birdhouses/<int:pk>/delete/', views.BirdhouseDelete.as_view(), name='birdhouses_delete'),
    # associate a toy with a cat (M:M)
    path('finches/<int:finch_id>/assoc_toy/<int:birdhouse_id>/', views.assoc_birdhouse, name='assoc_birdhouse'),
    path('finches/<int:finch_id>/unassoc_toy/<int:birdhouse_id>/', views.unassoc_birdhouse, name='unassoc_birdhouse'),
]