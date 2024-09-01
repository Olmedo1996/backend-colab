from django.urls import path, include

urlpatterns = [
    path('v2/', include('api.v2.urls')),
]