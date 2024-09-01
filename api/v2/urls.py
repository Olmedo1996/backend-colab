from django.urls import path, include

urlpatterns = [
    path('projects/', include('api.v2.projects.urls')),
]