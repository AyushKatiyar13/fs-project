from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kweet_list, name='kweet_list'),
    path('create/', views.kweet_create, name='kweet_create'),
    path('<int:kweet_id>/edit/', views.kweet_edit, name='kweet_edit'),
    path('<int:kweet_id>/delete/', views.kweet_delete, name='kweet_delete'),
    path('register/', views.register, name='register'),
    path('test/', views.test_view, name='test_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
