%define	module	scitools

Summary:	Python library for scientific computing
Name:		python-scitools
Version:	0.7
Release:	%mkrel 1
License:	BSD
Group:		Development/Python
Url:		http://scitools.googlecode.com
Source0:	http://scitools.googlecode.com/files/%{module}-%{version}.tar.gz
Requires:	python-gnuplot python-numpy
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SciTools is a Python package containing lots of useful tools for scientific
computing in Python. The package is built on top of other widely used packages
such as NumPy, SciPy, ScientificPython, Gnuplot, etc.

%prep
%setup -qn %{module}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE ChangeLog
%{_bindir}/pyreport
%{_bindir}/scitools
%{_mandir}/man1/pyreport.1*
%{_mandir}/man1/scitools.1*
%dir %{python_sitelib}/%{module}
%{python_sitelib}/%{module}/*.py*
%{python_sitelib}/%{module}/scitools.cfg
%dir %{python_sitelib}/%{module}/easyviz
%{python_sitelib}/%{module}/easyviz/*.py*
%{python_sitelib}/*.egg-info

