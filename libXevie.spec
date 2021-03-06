# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       libXevie
Summary:    X.Org X11 libXevie runtime library
Version:    1.0.3
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
Source100:  libXevie.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(evieproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig


%description
X Event Interception Extension runtime Library


%package devel
Summary:    X.Org X11 libXevie development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(pre): xorg-x11-filesystem >= 0.99.2-3

%description devel
X Event Interception Extension runtime development files


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING README
%{_libdir}/libXevie.so.1
%{_libdir}/libXevie.so.1.0.0
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/X11/extensions/Xevie.h
%{_libdir}/libXevie.so
%{_libdir}/pkgconfig/xevie.pc
%doc %{_mandir}/man3/*.3*
# << files devel

