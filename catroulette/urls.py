"""
.. module:: catroulette.urls
   :synopsis: CatRoulette URLs.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

import logging

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
from django.views.generic.base import RedirectView, TemplateView
from django.views.defaults import permission_denied, page_not_found

from .apps.core.views import handler500

admin.autodiscover()

logger = logging.getLogger(__name__)


# Core
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="core/index.html"), name='home'),
    url(r'^favicon\.ico$', RedirectView.as_view(url=staticfiles('img/favicon.ico')), name='favicon'),
    url(r'^robots\.txt$', RedirectView.as_view(url=staticfiles('robots.txt')), name='robots'),
    url(r'^zoidberg/', include(admin.site.urls)),  # admin site urls, masked
    url(r'^admin/', TemplateView.as_view(template_name="honeypot.html"), name="honeypot"),  # admin site urls, honeypot
]

# Hooks to intentionally raise errors
urlpatterns += [
    url(r'^500/$', handler500, name="500"),
    url(r'^403/$', permission_denied, name="403"),
    url(r'^404/$', page_not_found, name="404"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
