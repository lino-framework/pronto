# -*- coding: utf-8 -*-
from lino.sphinxcontrib import configure
configure(globals(), 'lino_pronto.projects.yvonne.settings.demo')

extensions += ['lino.sphinxcontrib.logo']
project = "Lino Pronto website"
copyright = '2012-2021 Rumma & Ko Ltd'

html_context.update(public_url='https://pronto.lino-framework.org')
