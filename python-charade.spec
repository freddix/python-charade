%define 	module	charade

Summary:	The Universal character encoding detector
Name:		python-%{module}
Version:	1.0.3
Release:	1
License:	LGPL 2.1+
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/c/charade/%{module}-%{version}.tar.gz
# Source0-md5:	79ac701a147705c09bdce31b79dfa12e
URL:		https://github.com/sigmavirus24/charade
BuildRequires:	python-modules
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Charade: The Universal character encoding detector. This is a port of
Mark Pilgrim's excellent chardet. Previous two versions needed to be
maintained: one that supported python 2.x and one that supported
python 3.x. With the minor amount of work placed into this port,
charade now supports both in one codebase. The base for the work was
Mark's last available copy of the chardet source for python 3000.

%package -n python3-charade
Summary:	The Universal character encoding detector
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-charade
Charade: The Universal character encoding detector. This is a port of
Mark Pilgrim's excellent chardet. Previous two versions needed to be
maintained: one that supported python 2.x and one that supported
python 3.x. With the minor amount of work placed into this port,
charade now supports both in one codebase. The base for the work was
Mark's last available copy of the chardet source for python 3000.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__python3} setup.py build -b python3 install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY.rst README.rst
%{py_sitescriptdir}/%{module}

%files -n python3-charade
%defattr(644,root,root,755)
%doc HISTORY.rst README.rst
%{py3_sitescriptdir}/%{module}

