"""
Fixer that changes os.getcwdu() to os.getcwd().
"""
# Author: Victor Stinner

# Local imports
from .. import fixer_base
from ..fixer_util import Name

class FixGetcwdu(fixer_base.BaseFix):

    PATTERN = """
              power< 'os' trailer< dot='.' name='getcwdu' > any* >
              """

    def transform(self, node, results):
        name = results["name"]
        name.replace(Name(u"getcwd", prefix=name.prefix))
