import unittest2 as unittest
from plone import api

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.milf import utils

from collective.milf.testing import \
    COLLECTIVE_MILF_INTEGRATION_TESTING


def create(container=None,
        type=None,
        title=None,
        language='en'):
    content_id = title
    container.invokeFactory(type, content_id, title=title, language=language)
    return container[content_id]


def TestMove(unittest.TestCase):

    layer = COLLECTIVE_MILF_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ('Manager',))
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
        self.assertTrue(api.content.get(path='/docfr'))

    def test_movement(self):
        results = utils.move_all(self.portal)
        self.assertTrue(api.content.get(path='/fr/docfr'))
        self.assertTrue(api.content.get(path='/docfr') is None)
