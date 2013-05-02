import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.milf import utils

from collective.milf.testing import MILF_INTEGRATION


def create(container=None,
        type=None,
        title=None,
        language='en'):
    content_id = title
    container.invokeFactory(type, content_id, title=title, language=language)
    return container[content_id]


class TestMove(unittest.TestCase):

    layer = MILF_INTEGRATION

    def setUp(self):
        self.portal = self.layer['portal']
        #self.setRoles(['Manager'])
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Member'])
        fr = create(type='Folder',
                title='fr',
                language='fr',
                container=self.portal)

        en = create(type='Folder',
                title='en',
                language='en',
                container=self.portal)
        en.addTranslationReference(fr)

        docfr = create(
                type='Document',
                title='docfr',
                language='fr',
                container=self.portal)

        docen = create(
                type='Document',
                title='docen',
                language='en',
                container=self.portal)
        docen.addTranslationReference(docfr)

    def test_no_movement(self):
        self.assertTrue(getattr(self.portal, 'docfr'))

    def test_movement(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Member'])
        results = utils.move_all(self.portal)
        self.assertTrue(getattr(self.portal, 'fr'))
        self.assertEqual(getattr(self.portal, 'docfr', None), None)
