%define Name sfdc
%define Version 1.11e

Name        	: gg-%{Name}
Version     	: %{Version}
Release     	: 1

Summary     	: Compile SFD files into someting useful
Group       	: Development/Tools
Copyright   	: GPL
URL         	: http://www.lysator.liu.se/~lcs/files/gg-cross/

Source0		: http://www.lysator.liu.se/~lcs/files/gg-cross/%{Name}-%{Version}.tar.gz
BuildRoot   	: /tmp/%{Name}-%{Version}

BuildRequires   : perl

%description
sfdc is an open source replacement for Amiga, Inc.'s sfd tool,
distributed with NDK 3.9. It is also an replacement for fd2inline.

The basis for all work performed by sfdc is the SFD file, which contains
all required information about the module and the functions provided.
From this information, sfdc can:

*   Generate an old-style FD file for futher processing with other
    tools.

*   Generate a C prototype file, such as those normally found in the
    Include/clib/ directory.

*   Generate gcc inlines (actually preprocessor macros) or pragmas for
    direct library function calls (without going via library stubs).

*   Generate the Include/proto/ file, which includes the
    Include/clib/ file and either the inlines or pragmas.

*   Generate an assembler LVO file, which contains the library offset of
    all functions in the library.

*   Generate C stubs, which can be compiled and archived into a stub
    library.

*   Generate library gateway stubs, which can be used as part of your
    module as glue between the module function table and your C
    functions.

Additionally, sfdc does all this for several Amiga-like operating
systems: traditional AmigaOS, native Amithlon, AROS and MorphOS.


%prep
%setup -q -n %{Name}-%{Version}

%build
%configure
make all


%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root)
%doc COPYING sfdc.txt
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Sep 12 2005 Martin Blom <martin@blom.org> -
- Updated to 1.4.

* Fri Nov 12 2004 Martin Blom <martin@blom.org>
- Updated to 1.3.

* Thu Jul 27 2003 Martin Blom <martin@blom.org>
- Initial rpm.
