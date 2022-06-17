# encoding: utf-8
from ckan.common import CKANConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class DBCATheme(plugins.SingletonPlugin):
    '''DBCATheme plugin.

    '''
    pass


from ckan.plugins import toolkit, IConfigurer, SingletonPlugin, implements

class DBCATheme(SingletonPlugin):
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config: CKANConfig):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "static")
        
