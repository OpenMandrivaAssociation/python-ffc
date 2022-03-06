%define	module ffc

Summary:	A compiler for finite element variational forms
Name:		python-%{module}
Version:	2019.1.0
Release:	1
License:	LGPLv3+
Group:		Development/Python
URL:		http://fenicsproject.org
Source0:	https://bitbucket.org/fenics-project/%{module}/downloads/%{module}-%{version}.tar.gz
BuildArch:	noarch
	
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	gnupg2
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(fenics-fiat) >= %{fenics_version}
BuildRequires:	python3dist(fenics-ufl) >= %{fenics_version}
BuildRequires:	python3dist(fenics-dijitso) >= %{fenics_version}

#Requires:	python3egg(dijitso) >= %{version}
#Requires:	python3egg(fiat) >= %{version}
#Requires:	python3egg(instant) >= %{version}
#Requires:	python3egg(ufl) >= %{version}
#Requires:	python3egg(numpy)
#Requires:	python3egg(six)

%description
FFC is a compiler for finite element variational forms. From a high-level
description of the form, it generates efficient low-level C++ code that can
be used to assemble the corresponding discrete operator (tensor). In
particular, a bilinear form may be assembled into a matrix and a linear form
may be assembled into a vector. FFC may be used either from the command line 
by invoking the ffc command) or as a Python module (import ffc).

FFC is part of the FEniCS Project.

%files
%license COPYING
%license COPYING.LESSER
%doc README.rst
%doc AUTHORS
%{_bindir}/%{module}*
%{py_sitedir}/%{module}/
%{py_sitedir}/fenics_%{module}-%{version}-py%{python_version}.egg-info/
%{_mandir}/man1/%{module}.1*

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

