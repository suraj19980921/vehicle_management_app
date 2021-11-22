from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView)
from django.views.generic.base import View
from django.views.generic.edit import FormMixin
from main import models
from main import forms
import json
from django.core.serializers import serialize
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

class VehicleList(ListView):
    model = models.Vehicle
    template_name = 'main/vehicle_list.html'
    context_object_name = 'vehicles'
    paginate_by = 5
    

    
    def get(self, request, *args, **kwargs):

        vehicles = models.Vehicle.objects.all()
        paginator = Paginator(vehicles,self.paginate_by)
        
        page = self.request.GET.get('page')
        
        if self.request.path_info != '/' :
            try:
                paginator.page(page)
            except PageNotAnInteger:
                if 'manage_vehicle' in self.request.META.get('HTTP_REFERER').split('/'):
                    path = '/manage_vehicle/?page=' + str(paginator.num_pages)
                    return redirect(path)
                else:
                    path = '/manage_vehicle/?page=1'
                    return redirect(path)
            except EmptyPage:
                page = int(page)-1
                path = '/manage_vehicle/?page=' + str(page)
                return redirect(path)
        
        return super().get(request, *args, **kwargs)
        


class VehicleDetail(View):
   
   def get(self,request,pk):
        vehicle = models.Vehicle.objects.filter(id = pk)
    
        if request.is_ajax():
            data = json.loads(serialize('json',vehicle))
            return JsonResponse({'vehicle':data})
        else:
            context = {'vehicle_details':vehicle}
            return render(request,'main/vehicle_detail.html',context)


class ManageVehicle(VehicleList, FormMixin, ListView):
    model = models.Vehicle
    form_class = forms.VehicleForm
    template_name = 'main/vehicle_manage.html'
    

class AddVehicle(CreateView):
    model = models.Vehicle
    template_name = 'main/vehicle_manage.html'
    form_class = forms.VehicleForm
    success_url = '/manage_vehicle/'

class UpdateVehicle(UpdateView):
    model = models.Vehicle
    form_class = forms.VehicleForm
    template_name = 'main/vehicle_manage.html'
    success_url = '/manage_vehicle/'

    def get_success_url(self):
        path = self.request.META.get('HTTP_REFERER')
        return path

class DeleteVehicle(DeleteView):
    model = models.Vehicle
    
    def get_success_url(self):
        path = self.request.META.get('HTTP_REFERER')
        return path
        
        




