#!/usr/bin/env python
import os
import sys
platform_name = sys.platform
if platform_name == 'win32':
    print '平台是windows'
elif platform_name == 'linux2':
    print '平台是linux'
else:
    print 'unkown'
