# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from rj.site.testing import RJ_SITE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that rj.site is properly installed."""

    layer = RJ_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rj.site is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('rj.site'))

    def test_browserlayer(self):
        """Test that IRjSiteLayer is registered."""
        from rj.site.interfaces import IRjSiteLayer
        from plone.browserlayer import utils
        self.assertIn(IRjSiteLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RJ_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['rj.site'])

    def test_product_uninstalled(self):
        """Test if rj.site is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('rj.site'))

    def test_browserlayer_removed(self):
        """Test that IRjSiteLayer is removed."""
        from rj.site.interfaces import IRjSiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(IRjSiteLayer, utils.registered_layers())
