Summary:	Python Packet Capture and Injection Library
Summary(pl.UTF-8):	Biblioteka Pythona do przechwytywania i wstrzykiwania pakietów
Name:		python-pycap
Version:	0.1.6
Release:	3
License:	BSD
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pycap/pycap-%{version}.tar.gz
# Source0-md5:	c90bc5382dede1a941e023e7bc27c473
URL:		http://pycap.sourceforge.net/
BuildRequires:	libnet-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the ability to capture packets from, and inject
packets onto, network interfaces. It supports commonly found protocols
such as Ethernet, PPP, IP, ARP, TCP, UDP, and ICMP.

%description -l pl.UTF-8
Ten pakiet daje możliwość przechwytywania pakietów oraz wstrzykiwania
ich poprzez interfejsy sieciowe. Obsługuje często spotykane protokoły
takie jak Ethernet, PPP, IP, ARP, TCP, UDP i ICMP.

%prep
%setup -q -n pycap-%{version}

%build
env CFLAGS="%{rpmcflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.html docs/*.css
%dir %{py_sitedir}/pycap
%{py_sitedir}/*.egg-info
%attr(755,root,root) %{py_sitedir}/pycap/*.so
%{py_sitedir}/pycap/*.py[co]
%dir %{py_sitedir}/pycap/constants
%{py_sitedir}/pycap/constants/*.py[co]
