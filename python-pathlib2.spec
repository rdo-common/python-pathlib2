%global modname	pathlib2

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%else
%bcond_with    python3
%endif


Name:           python-%{modname}
Version:        2.3.2
Release:        3%{?dist}
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
%if 0%{?rhel} == 7
BuildRequires:  python-test
%endif
BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-scandir
BuildRequires:  python2-six
Requires:  python2-scandir
Requires:  python2-six

%description -n python2-%{modname} %{_description}

Python 2 version.

%if %{with python3}
%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-six
Requires:  python3-six

%description -n python3-%{modname} %{_description}

Python 3 version.
%endif

%prep
%setup -q -n %{modname}-%{version}

%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%py2_install
%if %{with python3}
%py3_install
%endif

%check
# LANG has to be set here because otherwise file system encoding is
# ANSI_X3.4-1968 by default in mock build
LANG=C.utf8 %{__python2} -m pytest -v tests
%if %{with python3}
%{__python3} -m pytest -v tests
%endif

%files -n python2-%{modname}
%doc README.rst
%license LICENSE.rst
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-%{version}-py?.?.egg-info

%if %{with python3}
%files -n python3-%{modname}
%doc README.rst
%license LICENSE.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-py?.?.egg-info
%endif

%changelog
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-1
- Update to 2.3.2 (#1569508)
- Fix FTBFS (#1556245)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.7

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
