from django.urls import path
from . import views

urlpatterns = [
    # path (url_pattern, function, name(optional))
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finch_details, name='details'),
]