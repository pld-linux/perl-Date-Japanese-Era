
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define pnam	Japanese-Era
Summary:	Date::Japanese::Era - Calculate dates in the Japanese-Era calendar
Name:		perl-Date-Japanese-Era
Version:	0.03
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0fbf6c6990fa9646b7ddc749c2e76e86
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl(Jcode)
BuildRequires:	perl(Date::Calc)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date::Japanese::Era handles conversion between Japanese Era and Gregorian calendar.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Date/Japanese/Era.pm
%dir %{perl_vendorlib}/Date/Japanese/Era
%{perl_vendorlib}/Date/Japanese/Era/Table.pm
%dir %{perl_vendorlib}/Date/Japanese/Era/Table
%{perl_vendorlib}/Date/Japanese/Era/Table/*.pm
%{_mandir}/man3/*
