from django.urls import path

from . import views

app_name = 'restaurant_homepage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('staff/', views.StaffView.as_view(), name='staff'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('legal_notice/', views.LegalNoticeView.as_view(), name='legal_notice'),
    path('data_privacy/', views.DataPrivacyView.as_view(), name='data_privacy'),
    path('terms_and_conditions/', views.TermsandConditionsView.as_view(), name='terms_and_conditions'),
    path('about/', views.AboutView.as_view(), name='about'),
]