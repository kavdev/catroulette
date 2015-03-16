"""
.. module:: catroulette.apps.core.admin
   :synopsis: CatRoulette Core Admin Configuration.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.contrib import admin

from .models import CatRouletteCat


class CatRouletteCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'vocalness', 'intelligence', 'energy')

admin.site.register(CatRouletteCat, CatRouletteCatAdmin)
