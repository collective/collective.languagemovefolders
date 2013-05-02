# -*- coding: utf-8 -*-
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.milf

MILF = PloneWithPackageLayer(
        zcml_filename="configure.zcml",
        zcml_package=collective.milf,
        additional_z2_products=('Products.LinguaPlone',),
        gs_profile_id='collective.milf:default',
        name="MILF")

MILF_INTEGRATION = IntegrationTesting(
                bases=(MILF,), name="MILF_INTEGRATION")

MILF_FUNCTIONAL = FunctionalTesting(
                bases=(MILF,), name="MILF_FUNCTIONAL")
