"""principal_travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin
from travel.views import HomeView, TripDetail, TripList, trip_new, event_new, principal_new, trip_edit
from rest_framework import routers
from django.contrib.staticfiles import views


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home_view'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    #url(r'^accounts/', include('registration.backends.simple.urls')), #Using simple urls now for one-step registration. Option below to be used for future use of two-step method
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^itineraries/$', TripList.as_view(), name='trip_list'),
    url(r'^itineraries/(?P<pk>[0-9]+)/$', TripDetail.as_view(),  name='trip_detail'),
    url(r'^itineraries/new/$', trip_new, name="trip_new"),
    url(r'^itineraries/(?P<pk>[0-9]+)/edit/$', trip_edit, name="trip_edit"),
    url(r'^events/new/$', event_new, name="event_new"),
    url(r'^principals/new/$', principal_new, name="principal_new")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^static/(?P<path>.*)$', views.serve),
    )
