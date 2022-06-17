# encoding: utf-8
from ckan.common import CKANConfig
from ckan import plugins
from ckan.plugins import toolkit


class DBCATheme(plugins.SingletonPlugin):
    """A custom theme and scheming datasets for DBCA."""
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config: CKANConfig):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "static")
        
