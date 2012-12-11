%define upstream_name	 Class-WhiteHole
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Base class to treat unhandled method calls as errors
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 680830
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 403016
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.04-6mdv2009.0
+ Revision: 241187
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-4mdv2008.0
+ Revision: 86177
- rebuild


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-3mdv2007.0
- Rebuild

* Thu Dec 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-2mdk
- spec rewrite

* Thu Mar 17 2005 Bruno Cornec <bcornec@mandrakesoft.org> 0.04-1mdk
- Initial build.

