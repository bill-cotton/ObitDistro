# $Id$
#-----------------------------------------------------------------------
#;  Copyright (C) 2017
#;  Associated Universities, Inc. Washington DC, USA.
#;
#;  This program is free software; you can redistribute it and/or
#;  modify it under the terms of the GNU General Public License as
#;  published by the Free Software Foundation; either version 2 of
#;  the License, or (at your option) any later version.
#;
#;  This program is distributed in the hope that it will be useful,
#;  but WITHOUT ANY WARRANTY; without even the implied warranty of
#;  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#;  GNU General Public License for more details.
#;
#
#;  You should have received a copy of the GNU General Public
#;  License along with this program; if not, write to the Free
#;  Software Foundation, Inc., 675 Massachusetts Ave, Cambridge,
#;  MA 02139, USA.
#;
#;  Correspondence concerning this software should be addressed as follows:
#;         Internet email: bcotton@nrao.edu
#;         Postal address: W. D. Cotton
#;                         National Radio Astronomy Observatory
#;                         520 Edgemont Road
#;                         Charlottesville, VA 22903-2475 USA
#-----------------------------------------------------------------------
#
#    Obit: Merx mollis mortibus nuper
#
#----------------------------------------------------
# Build linux binary distribution of Obit
# Svn revision number
ver = 567
TARGET := obit-distro-1.1.$(ver).tar
all: target
version:
	echo "ver=$(ver)"

target: 
	cd deps/src/plplot; ./SETUP.plplot
	svn co https://github.com/bill-cotton/Obit.git/trunk/ObitSystem src
	./SETUP.Obit
	./SETUP.ObitSD
	./SETUP.ObitTalk	
	./SETUP.ObitView	
	./rename.sh	
	./mkapp version=1.1.$(ver)
	# If plplot version changes, modify template/bin/ObitTalk
	cp -p -r deps/lib/plplot5.8.0 distro/obit-distro-1.1.$(ver)/lib/
	cp -p copyFiles/* distro/obit-distro-1.1.$(ver)/
	cd distro; tar cf $(TARGET) obit-distro-1.1.$(ver)
	cd distro; pigz -p 2 -9 $(TARGET)

upload:
	scp -p distro/$(TARGET).gz smeagle.cv.nrao.edu:/home/svn.cv.nrao.edu/content/obit/linux_distro

update:
	scp -p polaris:xfer/Makefile.Obit.lib src/Obit/lib/Makefile
	scp -p polaris:xfer/Makefile.ObitSD.lib src/ObitSD/lib/Makefile
	scp -p polaris:xfer/ObitTalk.in src/ObitTalk/bin/ObitTalk.in

clean:
	#cd deps/src/plplot/plplot-5.8.0; $(MAKE) clean uninstall
	cd deps/src/plplot/; rm -r -f plplot-5.8.0
	cd deps/share; rm -r -f plplot-5.8.0
	cd deps/lib; rm -r -f *
	cd deps/include; rm -r -f *
	cd ../../../..
	chmod +w -R src/
	rm -r -f src
	mkdir src
	rm -r -f distro/*
