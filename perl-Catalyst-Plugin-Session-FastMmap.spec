%define upstream_name    Catalyst-Plugin-Session-FastMmap
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	File storage backend for session data
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Catalyst-Plugin-Session-FastMmap
Source0:	https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Session-FastMmap-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(URI::Find)
BuildRequires:  perl(Cache::FastMmap)
BuildArch:	noarch

%description
Fast sessions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst/Plugin/Session/*
%{_mandir}/*/*

