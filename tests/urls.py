from django.conf.urls import include, patterns, url
from django.contrib import admin

import nexus

admin.autodiscover()
nexus.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^nexus/', include(nexus.site.urls)),
)
