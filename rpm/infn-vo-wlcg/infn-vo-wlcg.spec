Name: infn-vo-wlcg
Version: 1.0.0
Release: 0%{?dist}
Summary: VOMS configuration for the WLCG VO

Group: Applications/Internet
License: ASL 2.0
URL: https://wlcg-authz-wg.github.io/wlcg-authz-docs

Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package provides VOMS client configurations files for the WLCG VO

%prep
%setup -c 

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/vomsdir/wlcg
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/vomses/

cd %{name}-%{version}/rpm/%{name}

install -m 644 -p *.lsc $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/vomsdir/wlcg/
install -m 644 -p *.vomses  $RPM_BUILD_ROOT%{_sysconfdir}/vomses/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/grid-security/vomsdir
%{_sysconfdir}/vomses

%changelog
* Fri Oct 23 2020  Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.0-0
- Initial release
