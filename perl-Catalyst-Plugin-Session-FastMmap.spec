%define upstream_name    Catalyst-Plugin-Session-FastMmap
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	File storage backend for session data
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

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

