# -*- coding: UTF-8 -*-
# Copyright 2011-2019 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)


"""Default settings module for a :ref:`pronto` project. This is being
inherited by the demo projects in :mod:`lino_pronto.projects`.

"""

from __future__ import unicode_literals

import lino_pronto
from lino.projects.std.settings import *


class Site(Site):
    """Base class for a :ref:`pronto` application.

    """

    verbose_name = "Lino Pronto"
    version = lino_pronto.SETUP_INFO['version']
    url = lino_pronto.SETUP_INFO['url']

    demo_fixtures = 'std few_countries minimal_ledger demo demo2'.split()

    # languages = 'en de fr'
    languages = 'en'

    user_types_module = 'lino_pronto.lib.pronto.user_types'
    custom_layouts_module = 'lino_pronto.lib.pronto.layouts'

    default_build_method = 'weasy2pdf'

    # textfield_format = 'html'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        # yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        yield 'lino_xl.lib.countries'
        yield 'lino_pronto.lib.contacts'
        #~ yield 'lino_xl.lib.households'

        yield 'lino_xl.lib.excerpts'

        # yield 'lino_xl.lib.outbox'
        yield 'lino.modlib.uploads'
        yield 'lino.modlib.weasyprint'
        yield 'lino.modlib.export_excel'
        yield 'lino.modlib.tinymce'
        # yield 'lino.modlib.wkhtmltopdf'

        # ledger must come before sales because its demo fixture
        # creates journals (?)

        # yield 'lino.modlib.ledger'
        yield 'lino_pronto.lib.products'
        yield 'lino_xl.lib.sales'
        # yield 'lino_xl.lib.invoicing'
        yield 'lino_xl.lib.ledger'
        yield 'lino_xl.lib.sepa'
        yield 'lino_xl.lib.vat'
        yield 'lino_xl.lib.finan'
        yield 'lino_xl.lib.bevat'
        #~ 'lino.modlib.journals',
        #~ 'lino_xl.lib.projects',
        #~ yield 'lino_xl.lib.blogs'
        #~ yield 'lino.modlib.tickets'
        #~ 'lino.modlib.links',
        #~ 'lino_xl.lib.thirds',
        #~ yield 'lino_xl.lib.postings'
        # yield 'lino_xl.lib.pages'
        # yield 'lino_pronto.lib.pronto'

    def setup_plugins(self):
        """
        Change the default value of certain plugin settings.

        """
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(hide_region=True)
        self.plugins.ledger.configure(use_pcmn=True)
        self.plugins.countries.configure(country_code='BE')
        self.plugins.products.configure(menu_group='sales')

