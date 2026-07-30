%define upstream_name	 Class-WhiteHole
%define upstream_version 0.04
Name:		perl-%{upstream_name}
Version:	0.04
Release:	1

Summary:	Base class to treat unhandled method calls as errors
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        https://metacpan.org/dist/Class-WhiteHole
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/Class-WhiteHole-0.04.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Its possible to accidentally inherit an AUTOLOAD method.  Often this
will happen if a class somewhere in the chain uses AutoLoader or
defines one of their own.  This can lead to confusing error messages
when method lookups fail.

Sometimes you want to avoid this accidental inheritance.  In that
case, inherit from Class::WhiteHole.  All unhandled methods will
produce normal Perl error messages.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Class
%{_mandir}/*/*


