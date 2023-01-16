"""url paths"""
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]
