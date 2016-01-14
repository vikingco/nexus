from django.conf.urls import include, url
from django.contrib import admin

import nexus
from nexus.compat import subinclude

urlpatterns = [
    url(r'^admin/', subinclude(admin.site.urls)),
    url(r'^nexus/', include(nexus.site.urls)),
]
