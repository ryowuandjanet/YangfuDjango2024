from django.urls import path
from .views import *

app_name='app'

urlpatterns = [
  path('yfcases/', YfcaseList.as_view(), name='list_yfcases'),
  path('create/', YfcaseCreate.as_view(), name='create_yfcase'),
  path('update/<int:pk>/', YfcaseUpdate.as_view(), name='update_yfcase'),
  path('delete/<int:pk>/', YfcaseDelete.as_view(), name='delete_yfcase'),
  path('delete-land/<int:pk>/', delete_land, name='delete_land'),
  path('delete-build/<int:pk>/', delete_build, name='delete_build'),
  path('delete-person/<int:pk>/', delete_person, name='delete_person'),
]