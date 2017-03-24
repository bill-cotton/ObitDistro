# Sample Startup script
print "Executing startup script "
import ObitTalkUtil

###################### Define ###################################
# Where is AIPS installed?
AIPS_ROOT    = "/export/data/aips/"
AIPS_VERSION = "31DEC17/"
DA00         = "/export/data/aips/DA00/PANTHER"
# Define OBIT_EXEC for access to Obit Software 
OBIT_EXEC    = None  # (def /usr/lib/obit/bin)
OBIT_EXEC    = "/export/data/users/bcotton/GitTest/obit-bcotton-1.1.561/lib/obit/"

# Define AIPS directories (URL, disk name)
# URL = None for local disks
aipsdirs = [ \
    (None, "/export/sdd/bcotton/SDD"), \
    (None, "/export/data/aips/DATA/PANTHER_1/"), \
]

# Define FITS directories (URL, disk name)
# URL = None for local disks
fitsdirs = [ \
    (None, "/export/sdd/bcotton/FITS")]

# setup environment
ObitTalkUtil.SetEnviron(AIPS_ROOT=AIPS_ROOT, AIPS_VERSION=AIPS_VERSION, \
                        DA00=DA00, OBIT_EXEC=OBIT_EXEC, \
                        aipsdirs=aipsdirs, fitsdirs=fitsdirs)

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
