# somelib.py

import logging
'''
The call to creates a logger module that has the same name as
getLogger(__name__) the calling module. Since all modules are 
unique, this creates a dedicated logger that is likely to be 
separate from other loggers.
'''
log = logging.getLogger(__name__)
'''
The
operation attaches a null handler to log.addHandler(logging.NullHandler())
the just created logger object. A null handler ignores all logging messages by default.
Thus, if the library is used and logging is never configured, no messages or warnings
will appear.
'''
log.addHandler(logging.NullHandler())

# Example function (for testing)
def func():
    log.critical("A Critical Error!")
    log.debug("A debug message")
