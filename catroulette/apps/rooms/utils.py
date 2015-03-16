"""
.. module:: catroulette.apps.rooms.utils
   :synopsis: CatRoulette Room Utilities .

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>
.. moduleauthor:: Arnav Murulidhar <murulidhar@yahoo.com>

"""

import uuid

from django.contrib.auth import get_user_model

from django_ajax.decorators import ajax


@ajax
def match_cat(cat):
    match_found = False
    room_name = None

    # Keep trying to find a match
    while not match_found:
        # Is this cat already matched?
        if cat.room_name:
            room_name = cat.room_name
            cat.delete()
            match_found = True
        else:
            likely_match = None
            likely_match_score = None

            user_scores = [cat.vocalness, cat.intelligence, cat.energy]

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
                cat.delete()

    return room_name
