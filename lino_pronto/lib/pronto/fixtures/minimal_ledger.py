# -*- coding: UTF-8 -*-
# Copyright 2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


"""
Creates more journals specific to pronto

"""

from __future__ import unicode_literals

from lino.api import dd, rt, _
from lino_xl.lib.ledger.utils import DEBIT, CREDIT
# from lino_xl.lib.ledger import choicelists as pcmn
from lino_xl.lib.ledger.choicelists import CommonAccounts

# from lino.utils import Cycler

# accounts = dd.resolve_app('accounts')
vat = dd.resolve_app('vat')
sales = dd.resolve_app('sales')
ledger = dd.resolve_app('ledger')
finan = dd.resolve_app('finan')
bevat = dd.resolve_app('bevat')
bevats = dd.resolve_app('bevats')


# ~ partners = dd.resolve_app('partners')


def objects():
    JournalGroups = rt.models.ledger.JournalGroups
    Company = rt.models.contacts.Company

    # JOURNALS

    kw = dict(journal_group=JournalGroups.sales)
    MODEL = sales.VatProductInvoice
    kw.update(trade_type='sales')
    kw.update(ref="OFF", dc=CREDIT)
    kw.update(printed_name=_("Offer"))
    kw.update(dd.str2kw('name', _("Offers")))
    yield MODEL.create_journal(**kw)

    kw = dict(journal_group=JournalGroups.sales)
    MODEL = sales.VatProductInvoice
    kw.update(trade_type='sales')
    kw.update(ref="CMP", dc=CREDIT)
    kw.update(printed_name=_("Component sheet"))
    kw.update(dd.str2kw('name', _("Component sheets")))
    yield MODEL.create_journal(**kw)

