import somelib
import logging

'''
If the logging system gets configured, log messages will start to appear
Here, the root logger has been configured to only output messages at the ERROR level or
higher.
'''
logging.basicConfig()
somelib.func()

'''
Change the logging level for 'somelib' only.
The level of the logger for somelib has been separately configured to
output debugging messages. That setting takes precedence over the global setting.
'''
logging.getLogger('somelib').level=logging.DEBUG
somelib.func()