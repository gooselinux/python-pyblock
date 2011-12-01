%global realname pyblock
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%global dmrver 1.0.0.rc15
%global dmver 1.02.27

Summary: Python modules for dealing with block devices
Name: python-%{realname}
Version: 0.48
Release: 1%{?dist}
Source0: %{realname}-%{version}.tar.bz2
License: GPLv2 or GPLv3
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: python-devel, gettext
BuildRequires: device-mapper-libs >= %{dmver}, device-mapper-devel >= %{dmver}
BuildRequires: dmraid-devel >= %{dmrver}, libselinux-devel, libsepol-devel
Requires: device-mapper-libs >= %{dmver}, pyparted >= 3.0

%description
The pyblock contains Python modules for dealing with block devices.

%prep
%setup -q -n %{realname}-%{version}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} SITELIB=%{python_sitearch} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc %{_docdir}/pyblock-%{version}
%{python_sitearch}/block

%changelog
* Sun Jul 25 2010 Hans de Goede <hdegoede@redhat.com> - 0.48-1
- Create mappings for ext. partitions like kpartx (#617593)
  Resolves: #617593
  Related: #584272

* Wed Apr 21 2010 Hans de Goede <hdegoede@redhat.com> - 0.47-1
- Don't create a mapping for extended partitions (#584272)
  Resolves: #584272

* Tue Feb 16 2010 Hans de Goede <hdegoede@redhat.com> - 0.46-1
- When a stripe set is missing disks it is not degraded, but broken,
  add a check for broken sets (#564305)
  Resolves: #564305
- Various specfile fixes / cleanups

* Wed Jan 20 2010 Hans de Goede <hdegoede@redhat.com> - 0.45-3
- Rebuild for dmraid soname change
  Related: rhbz#556860

* Wed Jan 13 2010 David Cantrell <dcantrell@redhat.com> - 0.45-2
- Rebuild for pyparted-3.0
  Related: rhbz#523954

* Tue Jan  5 2010 Hans de Goede <hdegoede@redhat.com> - 0.45-1
- Remove libbdevid-python usage and dependency (#549102)
  Resolves: #549102
- Stop linking against zlib (unused)

* Tue Dec 15 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.44-1.1
- Rebuilt for RHEL 6

* Wed Oct  7 2009 Hans de Goede <hdegoede@redhat.com> - 0.44-1
- Use dmraid's status instead of figuring out if a set is degraded ourselves
  (#524168)
- Fix typo causing backtrace when doing activate deactivate 2x for dmraid 10

* Fri Sep 18 2009 Hans de Goede <hdegoede@redhat.com> - 0.43-2
- Rebuild for new dmraid

* Fri Sep  4 2009 Hans de Goede <hdegoede@redhat.com> - 0.43-1
- Catch dmraid.GroupingError in getRaidSets() (#521033)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr  2 2009 Hans de Goede <hdegoede@redhat.com> - 0.42-1
- Create assertion function to return PyErrors (jgranados)
- Do a thorough search for the Raid Sets (jgranados)
- RaidSet.level is broken atm (hansg)

* Thu Mar 19 2009 Joel Granados <jgranado@redhat.com> - 0.41-1
- Make build/tagging easier (jgranados).
- Do not try to find and activate partitions on raid subsets (hansg).

* Thu Mar 12 2009 Joel Granados <jgranado@redhat.com> - 0.40-1
- Fix the build for python-2.6 (jgranados)
- Add an automated way to tag when building (jgranados)

* Thu Mar 12 2009 Joel Granados <jgranado@redhat.com> - 0.39-1
- Fix the way we handle pyparted disk label errors (jgranados)

* Mon Mar  9 2009 Hans de Goede <hdegoede@redhat.com> - 0.38-1
- Add additional functionality for the anaconda storage rewrite (jgranados)
- Do not Py_DECREF imported dm module reference (hansg)
- Only install our own dm_log handler while doing dm stuff (hansg)

* Fri Feb 27 2009 Hans de Goede <hdegoede@redhat.com> - 0.37-1
- Handle dmraid dm table's with multiple rows / targets properly, this fixes
  dmraid jbod configurations (hansg)
- Various small cleanups and bugfixes (hansg)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Joel Granados <jgranado@redhat.com> - 0.36-1
- Correct syntax error (jgranado).
- Get version number from spec file (jgranado).

* Thu Feb 19 2009 Joel Granados <jgranado@redhat.com> - 0.35-1
- Make pyblock compatible with new pyparted (jgranado).
- Stop confusing raiddevs and raidsets (hansg).
- pyparted now trhows an IOException when it does not recognize the part (hansg).
- Fix traceback when activating already active dmraid set (hansg).
- Refactor and make functional the getDmDeps and getDmTarget functions (dlehman).
- Implement compare function for dm-tables (jgranado).

* Tue Feb  3 2009 Hans de Goede <hdegoede@redhat.com> - 0.34-1
- Add functions that relate dm nodes and dm names (jgranados)
- Make dmraid devices recursive (fixes dmraid 10 / 01) (jgranados)
- When importing dm from C-code import it as block.dm, this fixes pyblock
  not working with python 2.6 (hansg)

* Mon Jan 19 2009 Hans de Goede <hdegoede@redhat.com> - 0.33-1
- Allow use as non root (for pychecker)
- Forward port: "ERROR: only one argument allowed for this option"
  workaround from RHEL-5 (#468649, #474399)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.32-2
- Rebuild for Python 2.6

* Tue Sep 30 2008 Peter Jones <pjones@redhat.com> - 0.32-1
- Update for libdmraid 1.0.0.rc15 .

* Fri Jul 04 2008 Peter Jones <pjones@redhat.com> - 0.31-4
- Move dmraid dep to point at dmraid-libs.

* Thu Apr 17 2008 Jeremy Katz <katzj@redhat.com> - 0.31-3
- Own the doc dir (#363351)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.31-2
- Autorebuild for GCC 4.3

* Thu Jan 24 2008 Chris Lumens <clumens@redhat.com> 0.31-1
- Fix traceback when scanning disks (#429713).

* Mon Aug 27 2007 Peter Jones <pjones@redhat.com> - 0.30-1
- Fix link error due to Makefile changes.

* Wed Aug 23 2007 Peter Jones <pjones@redhat.com> - 0.29-1
- Fix device mapper build deps.

* Wed Aug 22 2007 Peter Jones <pjones@redhat.com> - 0.28-1
- Update license tag.
- Change MPath sorting.
- Improve exception handling.

* Thu Feb 15 2007 Peter Jones <pjones@redhat.com> - 0.27-3
- Make it a BuildRequires on device-mapper-devel but a Requires on
  device-mapper-libs .

* Mon Feb  5 2007 Alasdair Kergon <agk@redhat.com> - 0.27-2
- Add build dependency on new device-mapper-devel package.

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.27-1
- fix build for other python versions, build against python 2.5
- fix for Py_ssize_t changes in python 2.5

* Fri Oct 20 2006 Peter Jones <pjones@redhat.com> - 0.25-1
- fix refcounting of map names and partition building for new maps (#210412)
- fix naming so device names on a single controller are in LUN order

* Fri Sep 29 2006 Peter Jones <pjones@redhat.com> - 0.24-1
- add block.load() to load specific bdevid probes instead of always
  doing loadAll() (#208423)
- make block.getMPaths() return a sorted list (#208337, #208431)

* Mon Sep 25 2006 Peter Jones <pjones@redhat.com> - 0.23-1
- Link against zlib

* Sun Sep 24 2006 Jeremy Katz <katzj@redhat.com> - 0.22-2
- rebuild against new dmraid

* Wed Sep 13 2006 Peter Jones <pjones@redhat.com> - 0.22-1
- Fix partition removal when we've changed the partition table out from
  under a RaidSet or MultiPath.

* Fri Sep  8 2006 Peter Jones <pjones@redhat.com> - 0.21-1
- Be more picky about unique IDs for multipath

* Mon Aug 28 2006 Peter Jones <pjones@redhat.com> - 0.20-1
- Fix error with map naming and deletion

* Wed Aug 23 2006 Peter Jones <pjones@redhat.com> - 0.19-1
- Make RaidSet deactivation work like MultiPath deactivation.  Fixes a
  traceback when removing partition maps.

* Thu Aug 17 2006 Peter Jones <pjones@redhat.com> - 0.18-2
- No s390/s390x excludearch

* Thu Aug  3 2006 Peter Jones <pjones@redhat.com> - 0.18-1
- Fixes for multiple multipaths

* Fri Jul 28 2006 Peter Jones <pjones@redhat.com> - 0.17-2
- Require dmraid, since we're using the .so now.

* Wed Jul 26 2006 Peter Jones <pjones@redhat.com> - 0.17-1
- make multipath support more robust
- fix leaky file descriptor on volumes without partition tables

* Wed Jul 19 2006 Jeremy Katz <katzj@redhat.com> - 0.16-2
- require libbdevid

* Mon Jul 17 2006 Peter Jones <pjones@redhat.com> - 0.16-1
- new release with rudamentary support for multipath

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.15-2.1
- rebuild

* Mon Jun 05 2006 Jesse Keating <jkeating@redhat.com> - 0.15-2
- Add missing BuildRequires of zlib-devel

* Wed Feb 22 2006 Peter Jones <pjones@redhat.com> - 0.15-1
- Fix use of devices in /tmp to avoid duplicates. (fixes console spew during
  install)

* Mon Feb 13 2006 Peter Jones <pjones@redhat.com> - 0.14-1
- remove member partitions when we activate, rebuild them when we deactivate
- add another "count_devices(ctx->lc, NATIVE)" in discover_raiddevs.  it
  seems to help...

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.13-1.1
- bump again for double-long bug on ppc(64)

* Mon Feb  6 2006 Peter Jones <pjones@redhat.com> - 0.13-1
- partition naming/creation/detection fixes
- fixes for isw (ICH[4567]R) "groups"

* Tue Jan 31 2006 Peter Jones <pjones@redhat.com> - 0.12-1
- split __init__.py into separate files according to function
- disable "nosync" hack for now
- fix a refcounting bug in pydmraid_raidset_get_dm_table()
- add block.RaidDev.__cmp__()
- fix some type errors gcc can't check for when using pyblock_potoll
- be a little pickier about types for mode, devices, and sizes.
- add make rules for debugging
- fix "_init__" typo
- always use local import paths, and be much more strict about namespaces
- always make a new dm.device in BlockDev.From*()
- better defaults in BlockDev.create()
- add setter for block.dmraid.raidset.name, and rework RaidSet.set_name()
- rework RaidDev.get_bdev()
- rework "prefix" for RaidSet and RaidDev
- add getter for block.dmraid.raidset.map
- change arg order on block.dm.map.__init__() since there's no way to pass
  keyword args through the "abstract" interface.
- use self.name not self.rs.name in the RaidSet, and make changing the name
  work.
- make pydm_map_compare() compare names _last_, so we can compare a map
  that's been renamed with its earlier instantiations correctly.
- mark a device as degraded if there's any descrepancy at all between
  the number of members we find vs what we expect

* Thu Jan  5 2006 Peter Jones <pjones@redhat.com> - 0.11-1
- never trust dmraid on sync vs nosync; right now, always transform the
  table to "default" (no argument), which is to sync only when necessary,
  whatever that means.  Seems to lock up less often.
    
* Wed Jan  4 2006 Peter Jones <pjones@redhat.com> - 0.10-1
- fix checking for "degraded" raids

* Mon Dec 19 2005 Peter Jones <pjones@redhat.com> - 0.9-1
- fix some backwards isinstance() calls that cause RaidSet.get_valid()
  to fail

* Thu Dec 15 2005 Peter Jones <pjones@redhat.com> - 0.8-1
- prevent getRaidSets() from returning devices with missing members
- add "make flat_install" to make installing in RHupdates easier ;)

* Sun Dec 11 2005 Peter Jones <pjones@redhat.com> - 0.7-1
- merge debugging work from last several weeks

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> - 0.6-3.1
- rebuilt

* Sun Dec  4 2005 Peter Jones <pjones@redhat.com> - 0.6-3
- rebuild for newer libs

* Thu Nov 17 2005 Peter Jones <pjones@redhat.com> - 0.6-2
- temporarily mask exceptions

* Thu Nov 17 2005 Peter Jones <pjones@redhat.com> - 0.6-1
- fix RaidSets/getRaidSets

* Wed Nov 16 2005 Peter Jones <pjones@redhat.com> - 0.5-2
- rebuild for newer libdevmapper.a

* Fri Nov 11 2005 Peter Jones <pjones@redhat.com> - 0.5-1
- make it possible to easily build dm maps from dmraid tables
- support for partition table scanning

* Thu Nov 10 2005 Peter Jones <pjones@redhat.com> - 0.4-1
- minor fixups before adding to the distro

* Wed Nov  9 2005 Peter Jones <pjones@redhat.com> - 0.3-1
- make dmraid probing much simpler

* Thu Sep 22 2005 Peter Jones <pjones@redhat.com> - 0.2-2
- flush out dmraid mappings, add a lot of wrapper code in the toplevel

* Tue Sep 13 2005 Peter Jones <pjones@redhat.com> - 0.2-1
- add deps on libdevmapper and libdmraid

* Fri Sep  9 2005 Peter Jones <pjones@redhat.com> - 0.1-1
- initial package
