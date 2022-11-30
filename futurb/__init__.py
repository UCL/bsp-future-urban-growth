"""
 This script initializes the plugin, making it known to QGIS.
"""
from qgis.gui import QgisInterface

from .plugin.futurb import Futurb


def classFactory(iface: QgisInterface):  # pylint: disable=invalid-name
    """ """
    return Futurb(iface)
