"""
.. module:: catroulette.apps.rooms.utils
   :synopsis: CatRoulette Room Utilities.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>
.. moduleauthor:: Arnav Murulidhar <murulidhar@yahoo.com>

"""

import logging
import uuid

from django.contrib.auth import get_user_model as get_cat_model


logger = logging.getLogger(__name__)


def check_for_match(cat_id):
    cat = get_cat_model().objects.get(id=cat_id)
    if cat.room_name:
        logger.debug("Match found for cat " + str(cat.id) + ": " + cat.room_name)
        cat.delete()
        return cat.room_name

    return None


def match_cat(cat):
    match_found = False
    room_name = None
    likely_match = None

    # Keep trying to find a match
    while not match_found:
        # Is this cat already matched?
        previously_matched_room = check_for_match(cat.id)
        if previously_matched_room:
            room_name = previously_matched_room
            match_found = True
        else:
            likely_match = None
            likely_match_score = None
            previously_matched_room = None

            cat_scores = [cat.vocalness, cat.intelligence, cat.energy]

#             ## DEBUG ##
#             all_cats = get_cat_model().objects.exclude(id=cat.id).filter(room_name=None)
#             numcats = all_cats.count()
#             logger.debug("cat " + str(cat.id) + " is searching for a match with " + str(numcats) + " cats. [" + str([cat.id for cat in all_cats]) + "]")
#             ## END DEBUG ##

            previously_matched_room = check_for_match(cat.id)
            if previously_matched_room:
                room_name = previously_matched_room
                match_found = True
                break  # break out of while loop

            for other_cat in get_cat_model().objects.exclude(id=cat.id).filter(room_name=None):
                other_cat_scores = [other_cat.vocalness, other_cat.intelligence, other_cat.energy]
                combined_scores = [abs(x - y) for x, y in zip(cat_scores, other_cat_scores)]

                aggregate_score = sum(combined_scores)

                if not(likely_match and aggregate_score >= likely_match_score):
                    # Is this cat already matched?
                    previously_matched_room = check_for_match(cat.id)
                    if previously_matched_room:
                        room_name = previously_matched_room
                        match_found = True
                        break  # break out of for loop
                    else:
                        logger.debug("Found a possible match with cat " + str(other_cat.id))
                        logger.debug("\tprev score: " + str(likely_match_score))
                        logger.debug("\tnew score: " + str(aggregate_score))
                        likely_match = other_cat
                        likely_match_score = aggregate_score

                    match_found = True
                else:
                    logger.debug("Didn't match with cat " + str(other_cat.id))
                    logger.debug("\tprev score: " + str(likely_match_score))
                    logger.debug("\tnew score: " + str(aggregate_score))

            if likely_match and not previously_matched_room:
                # Generate room_name
                room_name = str(uuid.uuid4().hex)
                logger.debug("room: " + room_name)

                # "signal" a match to the other user
                likely_match.room_name = room_name
                likely_match.save()

                # remove this user from the user list
                cat.delete()

#     cat.room_name = room_name
#     cat.save()

    return room_name, likely_match, True if previously_matched_room else False
