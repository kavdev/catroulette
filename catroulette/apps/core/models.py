"""
.. module:: catroulette.apps.core.models
   :synopsis: CatRoulette Core Models.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.contrib.auth.models import AbstractBaseUser
from django.db.models.fields import PositiveSmallIntegerField


class CatRouletteUser(AbstractBaseUser):
    """CatRoulette User Model"""

    vocalness = PositiveSmallIntegerField(verbose_name="Vocalness")
    intelligence = PositiveSmallIntegerField(verbose_name="Intelligence")
    energy = PositiveSmallIntegerField(verbose_name="Energy")

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['vocalness', 'intelligence', 'energy']

    class Meta:
        verbose_name = 'CatRoulette User'
        verbose_name_plural = 'CatRoulette Users'

    def get_full_name(self):
        return self.get_username()

    def get_short_name(self):
        return self.get_username()
