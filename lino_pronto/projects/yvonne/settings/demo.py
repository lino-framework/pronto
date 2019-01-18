import datetime
from ..settings import *
class Site(Site):
    is_demo_site = True
    the_demo_date = datetime.date(2019, 1, 18)
    languages  = "en de fr"

    
SITE = Site(globals())

DEBUG = True
