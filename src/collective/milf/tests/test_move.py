import unittest2 as unittest
from plone import api

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.milf import utils

from collective.milf.testing import \
    COLLECTIVE_MILF_INTEGRATION_TESTING


class TestMove(unittest.TestCase):

    layer = COLLECTIVE_MILF_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ('Manager',))
        fr = api.content.create(type='Folder',
                title='fr',
                id='fr',
                language='fr',
                container=self.portal)

        en = api.content.create(type='Folder',
                title='en',
                id='en',
                language='en',
                container=self.portal)
        en.addTranslationReference(fr)

        docfr = api.content.create(
                type='Document',
                title='docfr',
                id='docfr',
                language='fr',
                container=self.portal)

        docen = api.content.create(
                type='Document',
                title='docen',
                id='docen',
                language='en',
                container=self.portal)
        docen.addTranslationReference(docfr)

    def test_no_movement(self):
        self.assertTrue(api.content.get(path='/docfr'))

    def test_movement(self):
        results = utils.move_all()
        self.assertTrue(api.content.get(path='/fr/docfr'))
        self.assertTrue(api.content.get(path='/docfr') is None)
