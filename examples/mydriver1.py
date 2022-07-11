"""
This driver does not do any action.
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "furious1"


def drive(world):
    return actions.NONE
