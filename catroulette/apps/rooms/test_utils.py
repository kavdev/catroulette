"""
.. module:: catroulette.apps.rooms.test_utils
   :synopsis: CatRoulette Room Utility Tests.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.contrib.auth import get_user_model
from django.test import TestCase

from .utils import match_cat


class CatMatchTest(TestCase):
    """Tests the matching algorithm on a 1-10 scale."""

    def test_six_cats(self):
        cat1 = get_user_model().objects.create(vocalness=3, intelligence=5, energy=8)
        cat2 = get_user_model().objects.create(vocalness=1, intelligence=5, energy=3)
        cat3 = get_user_model().objects.create(vocalness=1, intelligence=5, energy=3)
        cat4 = get_user_model().objects.create(vocalness=7, intelligence=2, energy=3)
        cat5 = get_user_model().objects.create(vocalness=8, intelligence=8, energy=8)
        cat6 = get_user_model().objects.create(vocalness=4, intelligence=1, energy=5)

        room1 = match_cat(cat1)
        room2 = match_cat(cat2)
        room3 = match_cat(cat3)
        room4 = match_cat(cat4)
        room5 = match_cat(cat5)
        room6 = match_cat(cat6)

        self.assertEqual(room1, room2, "Cats 1 and 2 didn't match!")
        self.assertEqual(room3, room4, "Cats 3 and 4 didn't match!")
        self.assertEqual(room5, room6, "Cats 5 and 6 didn't match!")

    def test_six_cats_non_sequential(self):
        cat1 = get_user_model().objects.create(vocalness=1, intelligence=5, energy=3)
        cat2 = get_user_model().objects.create(vocalness=1, intelligence=5, energy=3)
        cat3 = get_user_model().objects.create(vocalness=8, intelligence=8, energy=8)
        cat4 = get_user_model().objects.create(vocalness=4, intelligence=1, energy=5)
        cat5 = get_user_model().objects.create(vocalness=3, intelligence=5, energy=8)
        cat6 = get_user_model().objects.create(vocalness=7, intelligence=2, energy=3)

        room1 = match_cat(cat1)
        room2 = match_cat(cat2)
        room3 = match_cat(cat3)
        room4 = match_cat(cat4)
        room5 = match_cat(cat5)
        room6 = match_cat(cat6)

        self.assertEqual(room1, room2, "Cats 1 and 2 didn't match!")
        self.assertEqual(room3, room5, "Cats 3 and 5 didn't match!")
        self.assertEqual(room4, room6, "Cats 4 and 6 didn't match!")

    def test_six_cats_really_non_sequential(self):
        cat1 = get_user_model().objects.create(vocalness=1, intelligence=5, energy=3)
        cat2 = get_user_model().objects.create(vocalness=1, intelligence=5, energy=3)
        cat3 = get_user_model().objects.create(vocalness=8, intelligence=8, energy=8)
        cat4 = get_user_model().objects.create(vocalness=4, intelligence=1, energy=5)
        cat5 = get_user_model().objects.create(vocalness=3, intelligence=5, energy=8)
        cat6 = get_user_model().objects.create(vocalness=7, intelligence=3, energy=2)

        room1 = match_cat(cat1)
        room2 = match_cat(cat2)
        room3 = match_cat(cat3)
        room4 = match_cat(cat4)
        room5 = match_cat(cat5)
        room6 = match_cat(cat6)

        self.assertEqual(room1, room2, "Cats 1 and 2 didn't match!")
        self.assertEqual(room3, room5, "Cats 3 and 5 didn't match!")
        self.assertEqual(room4, room6, "Cats 4 and 6 didn't match!")

    def test_three_cats_predefined_rooms(self):
        room_name_1 = "test_room_1"
        room_name_2 = "test_room_2"

        cat1_pre = get_user_model().objects.create(vocalness=3, intelligence=5, energy=8, room_name=room_name_1)
        cat2_pre = get_user_model().objects.create(vocalness=3, intelligence=5, energy=8, room_name=room_name_2)
        cat3_pre = get_user_model().objects.create(vocalness=1, intelligence=5, energy=3, room_name=room_name_1)

        self.assertEqual(room_name_1, match_cat(cat1_pre))
        self.assertEqual(room_name_2, match_cat(cat2_pre))
        self.assertEqual(room_name_1, match_cat(cat3_pre))
