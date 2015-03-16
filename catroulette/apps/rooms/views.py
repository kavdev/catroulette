"""
.. module:: catroulette.apps.rooms.views
   :synopsis: CatRoulette Room Views .

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django_ajax.decorators import ajax

from .utils import match_user


@ajax
def get_room(request):
    """
    User posted personality details. Create a user object in the
    database with those details and attempt to find a match
    """

    return {"room_name": match_user(None)}
