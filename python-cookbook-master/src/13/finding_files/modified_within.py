#!/usr/bin/env python3.3

import os
import time

def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)
            

if __name__ == '__main__':
    import sys
    #os.path.basename(filename)
    #os.path.dirname(filename)
    #os.path.split(filename)
    #os.path.join('/new/dir', os.path.basename(filename))
    #os.path.expanduser('~/guido/programs/spam.py')
    if len(sys.argv) != 3:
        print('Usage: {} dir seconds'.format(os.path.basename(sys.argv[0])))
        raise SystemExit(1)
    
    modified_within(sys.argv[1], float(sys.argv[2]))

    

    
