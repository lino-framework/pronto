# -*- coding: UTF-8 -*-
# Copyright 2013-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
.. autosummary::
   :toctree:

    lib
    projects

"""

from .setup_info import SETUP_INFO

__version__ = SETUP_INFO['version']

intersphinx_urls = dict(docs="http://pronto.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/pronto/blob/master/%s'
doc_trees = ['docs']
