from django.shortcuts import render
from django.views import generic
from .models import Image, Staff, Dish, Menu, Reservation
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'restaurant_homepage/index.html'
    context_object_name = 'test'
        
    def get_queryset(self):
        return "Hello World"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['index_images'] = Image.objects.filter(index=True).all()
        context['gallery_images'] = Image.objects.filter(index=False).all()[:4]
        context['staff_list'] = Staff.objects.filter().all()[:5]
        context['menu_list'] = {menu: list(menu.dish_set.all())[:5] for menu in Menu.objects.all()}
        return context

class AboutView(generic.ListView):
    template_name = 'restaurant_homepage/about.html'
    context_object_name = 'test'
        
    def get_queryset(self):
        return "Hello World"
    
class MenuView(generic.ListView):
    template_name = 'restaurant_homepage/menu.html'
    context_object_name = 'menu_list'
        
    def get_queryset(self):
        return {menu: list(menu.dish_set.all()) for menu in Menu.objects.all()}

class StaffView(generic.ListView):
    template_name = 'restaurant_homepage/staff.html'
    context_object_name = 'staff_list'
        
    def get_queryset(self):
        return Staff.objects.all()

#TODO: Prettify Gallery    
class GalleryView(generic.ListView):
    template_name = 'restaurant_homepage/gallery.html'
    context_object_name = 'gallery_images'
        
    def get_queryset(self):
        return Image.objects.filter(index=False).all()
        
class ContactView(generic.CreateView):
    model = Reservation
    fields = ['name','groupsize','email','appointment','miscellaneous']
    template_name = 'restaurant_homepage/contact.html'
    
    def form_valid(self, form):
        reservation = form.save(commit=False)
        reservation.save()
        return HttpResponseRedirect(reverse('restaurant_homepage:index'))
    
class LegalNoticeView(generic.ListView):
    template_name = 'restaurant_homepage/legal_notice.html'
    context_object_name = 'test' 
        
    def get_queryset(self):
        return "Hello World"
   
class DataPrivacyView(generic.ListView):
    template_name = 'restaurant_homepage/data_privacy.html'
    context_object_name = 'test'
        
    def get_queryset(self):
        return "Hello World"
    
class TermsandConditionsView(generic.ListView):
    template_name = 'restaurant_homepage/terms_and_conditions.html'
    context_object_name = 'test'
        
    def get_queryset(self):
        return "Hello World"