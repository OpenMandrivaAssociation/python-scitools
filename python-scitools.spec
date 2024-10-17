%define	module	scitools

Summary:	Python library for scientific computing
Name:		python-scitools
Version:	0.8
Release:	2
License:	BSD
Group:		Development/Python
Url:		https://scitools.googlecode.com
Source0:	http://scitools.googlecode.com/files/%{module}-%{version}.tar.gz
Requires:	python-gnuplot python-numpy python-matplotlib
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SciTools is a Python package containing lots of useful tools for scientific
computing in Python. The package is built on top of other widely used packages
such as NumPy, SciPy, ScientificPython, Gnuplot, etc.

%prep
%setup -qn %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}
mv doc/easyviz/easyviz_sphinx_html html
%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE ChangeLog html/ examples/
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



%changelog
* Fri Dec 02 2011 Lev Givon <lev@mandriva.org> 0.8-1mdv2011.0
+ Revision: 737282
- Update to 0.8.
  Require python-matplotlib.

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - import python-scitools

