Summary:	lwIP - a lightweight TCP/IP stack
Summary(pl.UTF-8):	lwIP - lekki stos TCP/IP
Name:		lwip
Version:	1.4.1
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/lwip/%{name}-%{version}.zip
# Source0-md5:	9b0710ae9cd6313d00290ae89b0d3396
Source1:	http://download.savannah.gnu.org/releases/lwip/contrib-%{version}.zip
# Source1-md5:	49dd5df953dba2f632158383cfd1697f
Patch0:		%{name}-nohardcodedconfig.patch
URL:		http://savannah.nongnu.org/projects/lwip/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lwIP is a small independent implementation of the TCP/IP protocol
suite that has been developed by Adam Dunkels at the Computer and
Networks Architectures (CNA) lab at the Swedish Institute of Computer
Science (SICS).

The focus of the lwIP TCP/IP implementation is to reduce the RAM usage
while still having a full scale TCP. This making lwIP suitable for use
in embedded systems with tens of kilobytes of free RAM and room for
around 40 kilobytes of code ROM.

%description -l pl.UTF-8
lwIP to mała, niezależna implementacja zbioru protokołów TCP/IP,
rozwijana przez Adama Dunkelsa w laboratorium CNA (Computer and
Network Architectures - architektur komputerów i sieci) SICS (Swedish
Institute of Computer Science - Szwedzkiego Instytutu Informatyki).

Celem implementacji TCP/IP lwIP jest ograniczenie wykorzystania
pamięci RAM przy pozostawieniu pełnego TCP. Czyni to lwIP nadającym
się do użycia w systemach wbudowanych z dziesiątkami kilobajtów
wolnej pamięci RAM oraz miejscem na około 40 kilobajtów w pamięci ROM
kodu.

%package devel
Summary:	Header files for lwIP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lwIP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for lwIP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lwIP.

%prep
%setup -q -c -a1
%{__mv} lwip-%{version} lwip
%{__mv} contrib-%{version} contrib
%patch0 -p1

%build
%{__make} -C contrib/ports/unix/proj/lib \
	CC="%{__cc}" \
	CCDEP="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -DIPv4 -I\$(LWIPDIR)/include -I\$(LWIPARCH)/include -I\$(LWIPDIR)/include/ipv4 -I\$(LWIPDIR) -I."

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

install -D contrib/ports/unix/proj/lib/liblwip.so $RPM_BUILD_ROOT%{_libdir}/liblwip.so
cp -a lwip/src/include $RPM_BUILD_ROOT%{_includedir}/lwip

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc lwip/{CHANGELOG,COPYING,README} lwip/doc/{rawapi,snmp_agent,sys_arch}.txt
%attr(755,root,root) %{_libdir}/liblwip.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/lwip
