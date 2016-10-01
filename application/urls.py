from django.conf.urls import include, url
from django.contrib import admin
from jet.dashboard.dashboard_modules import google_analytics_views

admin.autodiscover()

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
]
