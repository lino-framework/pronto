from atelier.invlib import setup_from_tasks
ns = setup_from_tasks(
    globals(), "lino_pronto",
    languages="en de fr et nl".split(),
    # tolerate_sphinx_warnings=True,
    blogref_url="http://luc.lino-framework.org",
    locale_dir='lino_pronto/lib/pronto/locale',
    revision_control_system='git',
    cleanable_files=['docs/api/lino_pronto.*'],
    demo_projects=[
        'lino_pronto.projects.yvonne'])


