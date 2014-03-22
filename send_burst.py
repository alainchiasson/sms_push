#!/usr/bin/env python
# -*- coding: ascii -*-

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'Joe Author (joe.author@website.org)'
__copyright__ = 'Copyright (c) 2009-2010 Joe Author'
__license__ = 'New-style BSD'
__vcs_id__ = '$Id$'
__version__ = '1.2.3' #Versioning: http://www.python.org/dev/peps/pep-0386/

#
## Code goes here.
#
import time

def send_burst( msgs ) :
    start = time.time()

    for x in range(0, msgs):
        print x

    end = time.time()
    delta =  end - start
    time.sleep ( 1 - delta )

def test():
    """ Testing Docstring"""

    start = time.time()

    send_burst( 100 )
    
    total = time.time()
    print total - start
    pass

if __name__=='__main__':
    test()


