"""
Examples of how to use pathlib Path objects.  Path objects can be used almost anywhere
that you use a path string, e.g. when feeding a filename to 
xarray.open_dataset(path_to_netcdf_file).

They are easier to type and manipulate than text path strings.  They should also
allow you to write code that will cleanly work on any operating system (windows, mac, linux).

Parker MacCready
"""

from pathlib import Path
import sys

# local imports
import pm_tools

# Here is how to get the full path to this file:
pth = Path(__file__).absolute()

print('\nPath to this file:')
print(pth)

print('\nTest if it is a file:')
print(pth.is_file())

print('\nName of the file:')
print(pth.name)

print('\nPath of the directory it lives in:')
print(pth.parent)

print('\nTest if it is a directory:')
print(pth.parent.is_dir())

# Here is how to add a path to the python search path, e.g. to allow you to
# import a module from a different directory.  In the example we are adding this directory,
# which is not needed, but we could be adding any directory.
print('\n' + ' Original path '.center(60,'-'))
[print(item) for item in sys.path]
mydir = pth.parent
if str(mydir) not in sys.path:
    sys.path.append(str(mydir))
# NOTE: sys.path requires the string form of the Path object
print('\n' + ' New path '.center(60,'-'))
[print(item) for item in sys.path]

# Create and then remove another directory
newdir = pth.parent.parent / 'python_hour_temp'
# note the use of "/" to create the new path
pm_tools.make_dir(newdir)
print('\nPath to newdir:')
print(newdir)
print('\nTest if newdir is a directory:')
print(newdir.is_dir())
# make a file in newdir
fn = newdir / 'test.txt'
with open(fn, 'w') as f:
    f.write('hello\n')
print('\nTest if fn is a file:')
print(fn.is_file())
# remove fn
fn.unlink(missing_ok=True)
print('\nTest if we removed fn:')
print(fn.is_file())
# get rid of newdir (must be empty)
newdir.rmdir()


