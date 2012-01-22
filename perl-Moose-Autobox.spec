#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Moose
%define	pnam	Autobox
Summary:	Moose::Autobox - Autoboxed wrappers for Native Perl datatypes
Summary(pl.UTF-8):	Moose:Autobox = Autoboxowane opakowania dla natywnych typów danych perla
Name:		perl-Moose-Autobox
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Moose-Autobox-%{version}.tar.gz
# Source0-md5:	9d2e237c2cbe7e2cfe3afe8f0bbf75e7
URL:		http://search.cpan.org/dist/Moose-Autobox/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(autobox) >= 2.23
BuildRequires:	perl(Perl6::Junction) >= 1.40000
BuildRequires:	perl-Moose >= 0.42
BuildRequires:	perl-Test-Exception >= 0.21
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moose::Autobox provides an implementation of SCALAR, ARRAY, HASH &
CODE for use with autobox. It does this using a hierarchy of roles in
a manner similar to what Perl 6 might do. This module, like Class::MOP
and Moose, was inspired by my work on the Perl 6 Object Space, and the
'core types' implemented there.

The autobox module provides the ability for calling 'methods' on
normal Perl values like Scalars, Arrays, Hashes and Code references.
This gives the illusion that Perl's types are first-class objects.
However, this is only an illusion, albeit a very nice one. I created
this module because autobox itself does not actually provide an
implementation for the Perl types but instead only provides the
'hooks' for others to add implementation too.

Several people are using this module in serious applications and it
seems to be quite stable. The underlying technologies of autobox and
Moose::Role are also considered stable. There is some performance hit,
but as I am fond of saying, nothing in life is free. If you have any
questions regarding this module, either email me, or stop by #moose on
irc.perl.org and ask around.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Moose
%{perl_vendorlib}/Moose/*.pm
%{perl_vendorlib}/Moose/Autobox
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
