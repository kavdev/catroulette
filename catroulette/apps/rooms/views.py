"""
.. module:: catroulette.apps.rooms.views
   :synopsis: CatRoulette Room Views.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django_ajax.decorators import ajax

from .utils import match_user
from django.contrib.auth import get_user_model


@ajax
def get_room(request):
    """
    User posted personality details. Create a user object in the
    database with those details and attempt to find a match
    """

    vocalness = request.POST["vocalness"]
    intelligence = request.POST["intelligence"]
    energy = request.POST["energy"]

    new_user = get_user_model()(vocalness=vocalness, intelligence=intelligence, energy=energy)
    new_user.save()

    return {"room_name": match_user(new_user)}
