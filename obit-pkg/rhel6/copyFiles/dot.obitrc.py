# Sample Startup script -  needs editing where ***EDIT*** indicated
print ("Executing startup script ")
import ObitTalkUtil

###################### Define ###################################
# Where is AIPS installed?
AIPS_ROOT    = "/export/data/aips/"             # ***EDIT***
AIPS_VERSION = "31DEC20/"                       # ***EDIT***
DA00         = "/export/data/aips/DA00/PANTHER" # ***EDIT***
# Define OBIT_EXEC for access to Obit Software 
OBIT_EXEC    = None  # (def /usr/lib/obit/bin)
OBIT_EXEC    = "/export/data/users/bcotton/GitTest/obit-distro-1.1.630/lib/obit/" # ***EDIT***

# Define AIPS directories (URL, disk name)
# URL = None for local disks
# ***EDIT*** aipsdirs, list of AIPS data directories
aipsdirs = [ \
    (None, "/export/sdd/bcotton/SDD"), \
    (None, "/export/data/aips/DATA/PANTHER_1/"), \
]

# Define FITS directories (URL, disk name)
# URL = None for local disks
# ***EDIT*** fitsdirs, list of FITS data directories
fitsdirs = [ \
    (None, "/export/sdd/bcotton/FITS")]

# setup environment
ObitTalkUtil.SetEnviron(AIPS_ROOT=AIPS_ROOT, AIPS_VERSION=AIPS_VERSION, \
                        DA00=DA00, OBIT_EXEC=OBIT_EXEC, ARCH="LNX64", \
                        aipsdirs=aipsdirs, fitsdirs=fitsdirs)

# Make sure AIPS Tasks enabled
if 'LD_LIBRARY_PATH' in os.environ:
    os.environ['LD_LIBRARY_PATH'] = os.environ['AIPS_ROOT']+os.environ['AIPS_VERSION']+os.environ['ARCH']+'/LIBR/INTELCMP/:'+os.environ['LD_LIBRARY_PATH']
else:
    os.environ['LD_LIBRARY_PATH'] = os.environ['AIPS_ROOT']+os.environ['AIPS_VERSION']+os.environ['ARCH']+'/LIBR/INTELCMP/'

# List directories
ObitTalkUtil.ListAIPSDirs()
ObitTalkUtil.ListFITSDirs()

# Any other customization goes here
import math
Amcat   = AMcat
Aucat   = AUcat
setnams = setname
setn    = setname
getnams = getname
getn    = getname
# For Python3, to replace execfile - sorta
def exec_file(filepath):
    import os
    global_namespace = {
        "__file__":filepath,
        "__name__":"__main__",
    }
    with open(filepath, "rb") as file:
        exec(compile(file.read(), filepath, "exec"), global_namespace)

# end exec_file
