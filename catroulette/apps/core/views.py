"""
.. module:: catroulette.apps.core.views
   :synopsis: CatRoulette Core Views.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""


def handler500(request):
    """500 error handler which includes ``request`` in the context."""

    from django.template import RequestContext, loader
    from django.http import HttpResponseServerError

    template = loader.get_template('500.html')

    return HttpResponseServerError(template.render(RequestContext(request)))
