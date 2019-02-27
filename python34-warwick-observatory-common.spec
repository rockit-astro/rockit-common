#
# spec file for package python-warwickonemetre
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
Name:           python34-warwick-observatory-common
Version:        2.1.13
Release:        0
License:        GPL3
Summary:        Common backend code for the Warwick La Palma telescopes
Url:            https://github.com/warwick-one-metre/
BuildArch:      noarch
%if 0%{?suse_version}
Requires:       python3, python3-Pyro4
%endif
%if 0%{?centos_ver}
Requires:       python34, python34-Pyro4
%endif

%description
Part of the observatory software for the Warwick one-meter telescope and other La Palma facilities.

warwick-observatory-common holds the common backend code shared by the other utilities.

%prep

rsync -av --exclude=build .. .

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
