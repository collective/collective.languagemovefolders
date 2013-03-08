from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectivemilfLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.milf
        xmlconfig.file(
            'configure.zcml',
            collective.milf,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.milf:default')

COLLECTIVE_MILF_FIXTURE = CollectivemilfLayer()
COLLECTIVE_MILF_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_MILF_FIXTURE,),
    name="collectivemilfLayer:Integration"
)
COLLECTIVE_MILF_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_MILF_FIXTURE, z2.ZSERVER_FIXTURE),
    name="collectivemilfLayer:Functional"
)
