#! /bin/sh
# substitute $OBIT_ROOT for build directory
export rename="sed -i s#$PWD#\$OBIT_ROOT/#g"
echo "$rename"
#export rename='sed -i s#/export/data/users/bcotton/GitTest/obit-pkg/rhel6#\$OBIT_ROOT#g'
$rename src/Obit/config.log
$rename src/Obit/config.status
$rename src/Obit/Makefile
$rename src/Obit/src/Makefile
$rename src/Obit/tasks/Makefile
$rename src/Obit/python/Makefile
$rename src/Obit/python/setupdata.py
$rename src/Obit/python/setup.py

###$rename src/ObitSD/config.log
###$rename src/ObitSD/config.status
###$rename src/ObitSD/Makefile
###$rename src/ObitSD/src/Makefile
###$rename src/ObitSD/tasks/Makefile
###$rename src/ObitSD/python/Makefile
###$rename src/ObitSD/python/setupdata.py
###$rename src/ObitSD/python/setup.py

$rename src/ObitTalk/config.status
$rename src/ObitTalk/config.log
$rename src/ObitTalk/Makefile
$rename src/ObitTalk/bin/Makefile
$rename src/ObitTalk/bin/ObitTalk
$rename src/ObitTalk/bin/ObitTalkServer
$rename src/ObitView/config.status
$rename src/ObitView/config.log
$rename src/ObitView/Makefile
$rename src/ObitView/src/Makefile
