"""
These are utility functions written by Parker MacCready.
"""

from pathlib import Path
import shutil

def make_dir(pth, clean=False):
    """
    >>> WARNING: Be careful! This can delete whole directory trees. <<<
    
    Make a directory from the path "pth" which can:
    - be a string or a pathlib.Path object
    - be a relative path
    - have a trailing / or not
    
    Use clean=True to clobber the existing directory (the last one in pth).
    
    This function will create all required intermediate directories in pth.
    """
    if clean == True:
        shutil.rmtree(str(pth), ignore_errors=True)
    Path(pth).mkdir(parents=True, exist_ok=True)
