import unittest2 as unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.milf import utils

from collective.milf.testing import MILF_INTEGRATION


def create(container, type, title, language):
    content_id = title
    container.invokeFactory(type, content_id, title=title, language=language)
    content = container[content_id]
    content.processForm()
    return content


class TestMove(unittest.TestCase):

    layer = MILF_INTEGRATION

    def setUp(self):
        self.portal = self.layer['portal']
        #self.portal.portal_languages.addSupportedLanguage('en')
        #self.portal.portal_languages.addSupportedLanguage('fr')
        #self.portal.portal_languages.addSupportedLanguage('nl')
        #self.setRoles(['Manager'])
        setRoles(self.portal, TEST_USER_ID, ['Manager', 'Owner'])
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
        results = utils.move_all(self.portal)
        self.assertTrue(getattr(self.portal, 'fr'))
        self.assertEqual(getattr(self.portal, 'docfr', None), None)
