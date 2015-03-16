"""
.. module:: catroulette.apps.rooms.utils
   :synopsis: CatRoulette Room Utilities .

.. moduleauthor:: Arnav Murulidhar <murulidhar@yahoo.com>

"""

from django.contrib.auth import get_user_model

from django_ajax.decorators import ajax


@ajax
def match_user(user):

    # get the traits of the user
    user.vocalness
    user.intelligence
    user.energy
    user.room_name

    # Is this user already matched?
    if user.room_name:
        user.delete()
        room_name = user.room_name
    else:
        for other_user in get_user_model().objects.all():
            # Algorithm
            pass

        room_name = "room name"

    return room_name
