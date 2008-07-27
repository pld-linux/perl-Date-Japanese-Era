#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Japanese-Era
Summary:	Date::Japanese::Era - calculate dates in the Japanese-Era calendar
Summary(pl.UTF-8):	Date::Japanese::Era - obliczanie dat w kalendarzu ery japońskiej
Name:		perl-Date-Japanese-Era
Version:	0.06
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9b33e50cb76376680762c0765f93970c
URL:		http://search.cpan.org/dist/Date-Japanese-Era/
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Jcode
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Lingua-JA-Numbers
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date::Japanese::Era handles conversion between Japanese Era and
Gregorian calendar.

%description -l pl.UTF-8
Data::Japanese::Era obsługuje konwersję pomiędzy kalendarzem ery
japońskiej (Japanese-Era) a gregoriańskim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Date/Japanese/Era.pm
%dir %{perl_vendorlib}/Date/Japanese/Era
%{perl_vendorlib}/Date/Japanese/Era/Table.pm
%dir %{perl_vendorlib}/Date/Japanese/Era/Table
%{perl_vendorlib}/Date/Japanese/Era/Table/*.pm
%{_mandir}/man3/*
