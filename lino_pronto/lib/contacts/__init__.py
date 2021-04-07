# Copyright 2019 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""
Lino Pronto extension of :mod:`lino_xl.lib.contacts`

.. autosummary::
   :toctree:

    fixtures.std
    fixtures.demo

"""

from lino_xl.lib.contacts import Plugin


class Plugin(Plugin):

    # extends_models = ['Partner', 'Person', 'Company']
    needs_plugins = ['lino_pronto.lib.pronto']
    
