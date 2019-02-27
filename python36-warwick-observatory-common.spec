Name:           python36-warwick-observatory-common
Version:        2.1.13
Release:        0
License:        GPL3
Summary:        Common backend code for the Warwick La Palma telescopes
Url:            https://github.com/warwick-one-metre/
BuildArch:      noarch
Requires:       python36, python36-Pyro4

%description
Part of the observatory software for the Warwick one-meter telescope and other La Palma facilities.

warwick-observatory-common holds the common backend code shared by the other utilities.

%prep

rsync -av --exclude=build .. .

%build
%{__python3_other} setup.py build

%install
%{__python3_other} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_other_sitelib}/*

%changelog
