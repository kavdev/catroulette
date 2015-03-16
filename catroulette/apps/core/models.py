"""
.. module:: catroulette.apps.core.models
   :synopsis: CatRoulette Core Models.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.contrib.auth.models import AbstractBaseUser
from django.db.models.fields import PositiveSmallIntegerField, CharField


class CatRouletteCat(AbstractBaseUser):
    """A cat using the CatRoulette app."""

    vocalness = PositiveSmallIntegerField(verbose_name="Vocalness")
    intelligence = PositiveSmallIntegerField(verbose_name="Intelligence")
    energy = PositiveSmallIntegerField(verbose_name="Energy")
    room_name = CharField(max_length=32, blank=True, null=True, verbose_name="Room Name")

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['vocalness', 'intelligence', 'energy']

    class Meta:
        verbose_name = 'CatRoulette Cat'
        verbose_name_plural = 'CatRoulette Cats'

    def get_full_name(self):
        return self.get_username()

    def get_short_name(self):
        return self.get_username()
