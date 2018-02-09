%global modname	pathlib2

Name:           python-%{modname}
Version:        2.3.0
Release:        2%{?dist}
Summary:        Object-oriented filesystem paths
License:        MIT
URL:            https://github.com/mcmtroffaes/pathlib2/
Source0:        https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
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
BuildRequires:  python2-mock
BuildRequires:  python2-scandir
BuildRequires:  python2-six
BuildRequires:  python2-test
Requires:  python2-scandir
Requires:  python2-six

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-scandir
BuildRequires:  python3-six
BuildRequires:  python3-test
Requires:  python3-scandir
Requires:  python3-six

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
        # LANG has to be set here because otherwise file system encoding is
        # ANSI_X3.4-1968 by default in mock build
        LANG=C.utf8 $python $test
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
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Lumír Balhar <lbalhar@redhat.com> - 2.3.0-1
- New upstream version
- Fixed source URL
- Fixed FTBFS (missing test dependency)
- Fixed missing requires RHBZ#1410657
- Fixed tests execution (LANG setting)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-2
- Add %%check.
- Change URL from pathlib to pathlib2 page.

* Mon Nov 14 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-1
- Initial package.
