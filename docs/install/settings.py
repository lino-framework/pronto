# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from lino_pronto.settings import *

class Site(Site):
    title = "My Lino Pronto site"

SITE = Site(globals())
