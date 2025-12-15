# mysite/urls.py
from django.contrib import admin
from django.urls import path, include # Pastikan include di-import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # Tambahkan baris ini
]
