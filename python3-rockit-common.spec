Name:           python3-rockit-common
Version:        %{_version}
Release:        1%{dist}
Summary:        Common backend code for the Robotic Observatory Control Kit
License:        GPL3
Url:            https://github.com/rockit-astro/rockit-common
BuildArch:      noarch
BuildRequires:  python3-devel

%description

%prep
rsync -av --exclude=build --exclude=.git --exclude=.github .. .

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rockit

%files -f %{pyproject_files}
