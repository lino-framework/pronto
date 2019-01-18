from lino.api.shell import *
user_type = rt.models.users.UserTypes.get_by_value('900')
menu = settings.SITE.get_site_menu(user_type)
mi = menu.get_item('sales')
print mi, mi._defining_code

print dd.plugins.ledger
