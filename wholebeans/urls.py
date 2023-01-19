"""url paths"""
from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('coffee.urls'), name='coffee-urls'),
    path('accounts/', include('allauth.urls')), 
]

HANDLER404 = 'wholebeans.views.custom_404_error'
HANDLER500 = 'wholebeans.views.custom_500_error'