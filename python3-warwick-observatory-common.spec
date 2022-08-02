Name:           python3-warwick-observatory-common
Version:        20220802
Release:        0
License:        GPL3
Summary:        Common backend code for the Warwick La Palma telescopes
Url:            https://github.com/warwick-one-metre/
BuildArch:      noarch
Requires:       python3 python3-jsonschema python3-Pyro4

%description

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
