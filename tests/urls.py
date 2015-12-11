from django.conf.urls import include, url
from django.contrib import admin

import nexus

admin.autodiscover()
nexus.autodiscover()

urlpatterns = [
    url(r'^nexus/', include(nexus.site.urls)),
]
