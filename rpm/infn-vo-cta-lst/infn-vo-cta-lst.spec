Name: infn-vo-cta-lst
Version: 1.0.0
Release: 1%{?dist}
Summary: VOMS configuration for the cta-lst VO

Group: Applications/Internet
License: ASL 2.0

Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package provides VOMS client configurations files for the cta-lst VO

%prep
%setup -c 

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/vomsdir/cta-lst
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/vomses/

cd %{name}-%{version}/rpm/%{name}

install -m 644 -p *.lsc $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/vomsdir/cta-lst/
install -m 644 -p *.vomses  $RPM_BUILD_ROOT%{_sysconfdir}/vomses/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/grid-security/vomsdir
%{_sysconfdir}/vomses

%changelog
* Fri Nov 19 2021 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.0-1
- Initial release
