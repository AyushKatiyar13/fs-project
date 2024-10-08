"""
URL configuration for kwitter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth.urls import views as auth_views
# # from .views import kweet_list

# urlpatterns = [
#     # path('Hello_MR_Katiyar/', admin.site.urls),
#     path('', include('kweet.urls')),
#     path('kweet/', include("kweet.urls")),
#     path('accounts/', include('django.contrib.auth.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('kweet.urls')),  # Your app URLs
#     path('accounts/', include('django.contrib.auth.urls')),  # Auth URLs including logout
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kweet.urls')),  # Your app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Auth URLs including logout
]

# Only include media URL serving in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
