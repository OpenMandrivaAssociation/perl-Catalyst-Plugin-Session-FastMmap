%define realname Catalyst-Plugin-Session-FastMmap
%define name perl-%{realname}
%define version 0.12
%define release %mkrel 2

Summary:	File storage backend for session data
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		/%{realname}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Catalyst
BuildRequires:	perl-Catalyst-Plugin-Session
BuildRequires:	perl-URI-Find
BuildRequires:  perl-Cache-FastMmap
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
Fast sessions.

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Catalyst/Plugin/Session/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

