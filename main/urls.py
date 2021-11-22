from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

                path('', views.VehicleList.as_view(), name="vehicle_list"),
                path('vehicle_detail/<int:pk>', views.VehicleDetail.as_view(), name="vehicle_detail"),
                path('manage_vehicle/', views.ManageVehicle.as_view(), name="manage_vehicle"),
                path('add_vehicle/', views.AddVehicle.as_view(), name="add_vehicle"),
                path('update_vehicle/<int:pk>',views.UpdateVehicle.as_view(), name="update_vehicle"),
                path('delete_vehicle/<int:pk>', views.DeleteVehicle.as_view(), name="delete_vehicle")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)