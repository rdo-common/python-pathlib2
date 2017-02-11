%global modname	pathlib2

Name:           python-%{modname}
Version:        2.1.0
Release:        3%{?dist}
Summary:        Object-oriented filesystem paths
License:        MIT
URL:            https://github.com/mcmtroffaes/pathlib2/
Source0:        https://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

%global _description \
The old pathlib module on bitbucket is in bugfix-only mode. The goal of\
pathlib2 is to provide a backport of standard pathlib module which tracks\
the standard library module, so all the newest features of the standard\
pathlib can be used also on older Python versions.

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-six

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-six

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%setup -q -n %{modname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
for python in %{__python2} %{__python3}; do
    for test in test_pathlib2.py test_pathlib2_with_py2_unicode_literals.py; do
	$python $test
    done
done

%files -n python2-%{modname}
%doc README.rst
%license LICENSE.rst
%{python2_sitelib}/%{modname}.py*
%{python2_sitelib}/%{modname}-%{version}-py?.?.egg-info

%files -n python3-%{modname}
%doc README.rst
%license LICENSE.rst
%{python3_sitelib}/%{modname}.py*
%{python3_sitelib}/%{modname}-%{version}-py?.?.egg-info
%{python3_sitelib}/__pycache__/*

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-2
- Add %%check.
- Change URL from pathlib to pathlib2 page.

* Mon Nov 14 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-1
- Initial package.
