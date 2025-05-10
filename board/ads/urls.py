from django.urls import path
from .views import (
   ad_list,
   ad_detail,
   ad_create,
   ad_update,
   ad_delete,
)

urlpatterns = [
   path('', ad_list, name='ad_list'),
   path('ad/<int:ad_id>/', ad_detail, name='ad_detail'),
   path('ad/create/', ad_create, name='ad_create'),
   path('ad/<int:ad_id>/update/', ad_update, name='ad_update'),
   path('ad/<int:ad_id>/delete/', ad_delete, name='ad_delete'),
]
