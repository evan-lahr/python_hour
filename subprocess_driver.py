"""
This is an example of using many simultaneous subprocess jobs to
speed up a task.

Parker MacCready
"""
# imports
import sys, os
import argparse
from subprocess import Popen as Po
from subprocess import PIPE as Pi
from time import time
import numpy as np

pid = os.getpid()
print(' subprocess_driver '.center(60,'='))
print('PID for this job = ' + str(pid))

# command line arugments
parser = argparse.ArgumentParser()
# number of jobs to run
parser.add_argument('-N', type=int, default=100) 
# max number of subprocesses to run at any time
parser.add_argument('-Nproc', type=int, default=50)
args = parser.parse_args()
N = args.N
Nproc = args.Nproc

# run the jobs
tt0 = time()
proc_list = []
for ii in range(N):
    cmd_list = ['sleep','3']
    proc = Po(cmd_list, stdout=Pi, stderr=Pi)
    proc_list.append(proc)

    # screen output about progress
    if (np.mod(ii,10) == 0) and ii>0:
        print(str(ii), end=', ')
        sys.stdout.flush()
    if (np.mod(ii,50) == 0) and (ii > 0):
        print('') # line feed
        sys.stdout.flush()
    if (ii == N-1):
        print(str(ii))
        sys.stdout.flush()
        
    # Nproc controls how many ncks subprocesses we allow to stack up
    # before we require them all to finish.
    if ((np.mod(ii,Nproc) == 0) and (ii > 0)) or (ii == N-1):
        for proc in proc_list:
            stdout, stderr = proc.communicate()
            if len(stdout) > 0:
                print('\n'+stdout.decode())
            if len(stderr) > 0:
                print('\n'+stderr.decode())
        # make sure everyone is finished before continuing
        proc_list = []
print('Time to run %d jobs = %0.2f sec' % (N, time()-tt0))
