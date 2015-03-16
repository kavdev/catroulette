"""
.. module:: catroulette.apps.rooms.views
   :synopsis: CatRoulette Room Views.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.contrib.auth import get_user_model as get_cat_model
from django.http.response import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django_ajax.decorators import ajax

from .utils import match_cat


@ajax
@csrf_exempt
@require_POST
def get_room(request):
    """
    Cat posted personality details. Create a cat object in the
    database with those details and attempt to find a match.
    """

    try:
        vocalness = int(request.POST.get("vocalness"))
        intelligence = int(request.POST.get("intelligence"))
        energy = int(request.POST.get("energy"))
    except TypeError:
        return HttpResponseBadRequest()
    else:
        new_cat = get_cat_model()(vocalness=vocalness, intelligence=intelligence, energy=energy)
        new_cat.save()

        room, match, prev_matched, in_if, mod_likely, mod_likely_val, mod_cat, mod_cat_val = match_cat(new_cat)

        return {"room_name": room, "cat": new_cat.id, "other_cat": match.id if match else None,
                "previously_matched": prev_matched, "in_if": in_if,
                "mod_likely": mod_likely, "mod_likely_val": mod_likely_val,
                "mod_cat": mod_cat, "mod_cat_val": mod_cat_val}
