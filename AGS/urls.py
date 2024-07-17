"""
URL configuration for AGS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add paths from the catalog application
from django.urls import include

urlpatterns += [
    path('CIS/', include('CIS.urls')),
    #path(r'^CIS/', include('CIS.urls')),

]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/CIS/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

    path('^accounts/login/$', include('django.contrib.auth.urls'), name='login'),
       
    path('^accounts/logout/$', include('django.contrib.auth.urls'), name='logout'),
    
    path('^accounts/password_change/$', include('django.contrib.auth.urls'), name='cambio password'),
   
    path('^accounts/password_change/done/$', include('django.contrib.auth.urls'), name='cambio pwd hecho'),
    path('^accounts/password_reset/$', include('django.contrib.auth.urls'), name='password_reset'),
    path('^accounts/password_reset/done/$', include('django.contrib.auth.urls'), name='password_reset_done'),
    path('^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', include('django.contrib.auth.urls'), name='password_reset_confirm'),
    path('^accounts/reset/done/$', include('django.contrib.auth.urls'), name='password_reset_complete'),
    
]

