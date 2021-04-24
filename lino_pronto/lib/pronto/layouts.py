# -*- coding: UTF-8 -*-
# Copyright 2017-2021 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""The default :attr:`custom_layouts_module
<lino.core.site.Site.custom_layouts_module>` for Lino Cosi.

"""

from lino.api import rt

rt.models.ledger.Accounts.column_names = "\
ref name purchases_allowed sheet_item *"

rt.models.countries.Places.detail_layout = """
name country
type parent zip_code id
PlacesByPlace contacts.PartnersByCity
"""
rt.models.ledger.Accounts.detail_layout = """
ref:10 name
sheet_item id default_amount:10 vat_class vat_column
needs_partner clearable purchases_allowed
ledger.MovementsByAccount
"""

rt.models.system.SiteConfigs.set_detail_layout("""
site_company next_partner_id:10
default_build_method simulate_today
""", window_size=(60, 'auto'))
