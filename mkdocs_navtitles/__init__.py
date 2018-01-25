__version__ = '0.1.0'

from mkdocs.plugins import BasePlugin
import mkdocs.utils as utils
import os.path
import copy

class NavTitleLoader(BasePlugin):

    def on_nav(self, site_navigation, config):
        for page in site_navigation.pages:
            page.read_source(config)

