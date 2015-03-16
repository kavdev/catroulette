"""
.. module:: catroulette.apps.rooms.utils
   :synopsis: CatRoulette Room Utilities .

.. moduleauthor:: Arnav Murulidhar <murulidhar@yahoo.com>

"""

import uuid

from django.contrib.auth import get_user_model

from django_ajax.decorators import ajax


@ajax
def match_user(user):
    match_found = False
    room_name = None

    # Keep trying to find a match
    while not match_found:
        # Is this user already matched?
        if user.room_name:
            room_name = user.room_name
            user.delete()
            match_found = True
        else:
            likely_match = None
            likely_match_score = None

            user_scores = [user.vocalness, user.intelligence, user.energy]

            for other_user in get_user_model().objects.filter(room_name=None):
                other_user_scores = [other_user.vocalness, other_user.intelligence, other_user.energy]
                combined_scores = [abs(x - y) for x, y in zip(user_scores, other_user_scores)]

                aggregate_score = sum(combined_scores)

                if not likely_match or aggregate_score < likely_match_score:
                    likely_match = other_user
                    likely_match_score = aggregate_score
                    match_found = True

            if match_found:
                # Generate room_name
                room_name = uuid.uuid4().hex

                # "signal" a match to the other user
                likely_match.room_name = room_name
                likely_match.save()

                # remove this user from the user list
                user.delete()

    return room_name
