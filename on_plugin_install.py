from datetime import datetime
import logging

from path_helpers import path
from pip_helpers import install


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    plugin_root = path(__file__).parent.abspath()
    logging.info('[%s] Processing post-install hook for: %s',
                 str(datetime.now()), plugin_root.name)
    requirements_file = plugin_root.joinpath('requirements.txt')
    if requirements_file.exists():
        # Install required packages using `pip`, with Wheeler Lab wheels server
        # for binary wheels not available on `PyPi`.
        print install(['--find-links', 'http://192.99.4.95/wheels',
                       '--trusted-host', '192.99.4.95', '-r',
                       requirements_file])
        print ('[%s] Completed post-install processing for: %s' %
               (str(datetime.now()), plugin_root.name))
        print 'Press <Enter> key to continue...'
        raw_input()
