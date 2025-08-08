from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({
        "message": "Welcome to the JWT Auth API! Use /api/register/, /api/login/, etc."
    })

urlpatterns = [
    path('', home_view), 
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
]
