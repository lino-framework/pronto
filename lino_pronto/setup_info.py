# -*- coding: UTF-8 -*-
# Copyright 2014-2019 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

SETUP_INFO = dict(
    name='lino-pronto',
    version='19.1.0',
    install_requires=['lino-xl','django-iban', 'lxml'],
    tests_require=['beautifulsoup4',],
    test_suite='tests',
    description="A Lino application for assembling and selling products",
    long_description=u"""

**Lino Pronto** is a free Lino application for assembling and selling products.


- For *introductions* and *commercial information*
  please see `www.saffre-rumma.net
  <http://www.saffre-rumma.net/pronto/>`__.

- You can try it yourself in `our demo sites
  <http://www.lino-framework.org/demos.html>`__

- The central project homepage is http://pronto.lino-framework.org

""",
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="https://github.com/lino-framework/pronto",
    license_files=['COPYING'],
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 1 - Planning
Environment :: Web Environment
Framework :: Django :: 1.11
Intended Audience :: Developers
Intended Audience :: System Administrators
License :: OSI Approved :: GNU Affero General Public License v3
Operating System :: OS Independent
Topic :: Office/Business :: Financial :: Accounting
""".splitlines())

SETUP_INFO.update(packages=[
    'lino_pronto',
    'lino_pronto.lib',
    'lino_pronto.lib.pronto',
    'lino_pronto.lib.contacts',
    'lino_pronto.lib.contacts.fixtures',
    'lino_pronto.lib.products',
    'lino_pronto.lib.products.fixtures',
    'lino_pronto.lib.contacts.management',
    'lino_pronto.lib.contacts.management.commands',
    'lino_pronto.projects',
    'lino_pronto.projects.yvonne',
    'lino_pronto.projects.yvonne.settings',
])

SETUP_INFO.update(message_extractors={
    'lino_pronto': [
        ('**/cache/**', 'ignore', None),
        ('**.py', 'python', None),
        ('**.js', 'javascript', None),
        ('**/templates_jinja/**.html', 'jinja2', None),
    ],
})

SETUP_INFO.update(
    # package_data=dict(),
    zip_safe=False,
    include_package_data=True)


# def add_package_data(package, *patterns):
#     l = SETUP_INFO['package_data'].setdefault(package, [])
#     l.extend(patterns)
#     return l


# ~ add_package_data('lino_pronto',
# ~ 'config/patrols/Patrol/*.odt',
# ~ 'config/patrols/Overview/*.odt')

# l = add_package_data('lino_pronto.lib.pronto')
# for lng in 'de fr'.split():
#     l.append('lino_pronto/lib/pronto/locale/%s/LC_MESSAGES/*.mo' % lng)

# l = add_package_data('lino_xl.lib.sepa',
#                      'lino_xl.lib/sepa/config/iban/*')
                     # 'config/iban/*')
# print 20160820, SETUP_INFO['package_data']
# raw_input()
