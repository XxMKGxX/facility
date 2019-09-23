from django.urls import path
from . import views

app_name = 'facilityapp'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('facility-create/', views.FacilityCreate.as_view(),
        name='facility-create'),
    path('facility-detail/<int:pk>', views.FacilityDetail.as_view(),
        name='facility-detail'),
    path('facility-update/<int:pk>', views.FacilityUpdate.as_view(),
        name='facility-update'),
    path('facility-list', views.FacilityList.as_view(), name = 'facility-list'),
    path('facility/delete/<int:pk>', views.FacilityDelete.as_view(), 
        name='facility-delete'),
]