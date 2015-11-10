__author__ = 'sibi'

import pynotify

''' libnotify needs some init value,
it really can be anything, it just uses it
to differentiate between the popups
'''
pynotify.init("Basic")

n = pynotify.Notification("Get up",
  "Drink Water ;)"
)

n.show()