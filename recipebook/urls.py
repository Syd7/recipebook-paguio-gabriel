from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ledger.urls', namespace = 'ledger')),
    path('admin/', admin.site.urls),
]
