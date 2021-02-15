from lino.utils.pythontest import TestCase


class TestCase(TestCase):

    demo_projects_root = 'lino_pronto/projects'

    def test_mentori1(self):
        self.do_test_demo_project('yvonne')
