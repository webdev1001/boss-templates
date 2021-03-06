"""@project@ main application entry point."""

from cement.core import foundation
from cement.utils.misc import init_defaults
from cement.core.exc import FrameworkError, CaughtSignal
from @module@.core import exc

# Application default.  Should update config/@module@.conf to reflect any
# changes, or additions here.
defaults = init_defaults('@module@')

# All internal/external plugin configurations are loaded from here
defaults['@module@']['plugin_config_dir'] = '/etc/@module@/plugins.d'

# External plugins (generally, do not ship with application code)
defaults['@module@']['plugin_dir'] = '/var/lib/@module@/plugins'

# External templates (generally, do not ship with application code)
defaults['@module@']['template_dir'] = '/var/lib/@module@/templates'


class @class_prefix@App(foundation.CementApp):
    class Meta:
        label = '@module@'
        config_defaults = defaults

        # All built-in application bootstrapping (always run)
        bootstrap = '@module@.cli.bootstrap'

        # Optional plugin bootstrapping (only run if plugin is enabled)
        plugin_bootstrap = '@module@.cli.plugins'

        # Internal templates (ship with application code)
        template_module = '@module@.cli.templates'

        # Internal plugins (ship with application code)
        plugin_bootstrap = '@module@.cli.plugins'


class @class_prefix@TestApp(@class_prefix@App):
    """A test app that is better suited for testing."""
    class Meta:
        argv = []
        config_files = []


# Define the applicaiton object outside of main, as some libraries might wish
# to import it as a global (rather than passing it into another class/func)
app = @class_prefix@App()

def main():
    try:
        # Default our exit status to 0 (non-error)
        code = 0

        # Setup the application
        app.setup()

        # Run the application
        app.run()
    except exc.@class_prefix@Error as e:
        # Catch our application errors and exit 1 (error)
        code = 1
        print(e)
    except FrameworkError as e:
        # Catch framework errors and exit 1 (error)
        code = 1
        print(e)
    except CaughtSignal as e:
        # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
        code = 0
        print(e)
    finally:
        # Print an exception (if it occurred) and --debug was passed
        if app.debug:
            import sys
            import traceback

            exc_type, exc_value, exc_traceback = sys.exc_info()
            if exc_traceback is not None:
                traceback.print_exc()

        # Close the application
        app.close(code)

if __name__ == '__main__':
    main()
