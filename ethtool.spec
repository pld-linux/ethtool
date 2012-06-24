Summary:	Utility to control ethernet cards
Summary(es):	Grupos de herramientas Ethernet para tarjetas SPARC HME
Summary(pl):	Narz�dzie do kontrolowania kart ethernet
Summary(pt_BR):	Ferramenta de configura��o para placas ethernet PCI
Name:		ethtool
Version:	1.4
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://prdownloads.sourceforge.net/gkernel/%{name}-%{version}.tar.gz
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ethtool is a small utility for examining and tuning your
ethernet-based network interface.

%description -l es
Grupos de herramientas Ethernet para tarjetas SPARC HME

%description -l pl
ethtool to niewielkie narz�dzie do kontroli i tuningu sieciowych kart
ethernet.

%description -l pt_BR
Este utilit�rio permite consulta e altera��o da configura��o de placas
ethernet, como velocidade, porta, negocia��o autom�tica e localiza��o
PCI.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
autoheader
automake -a -c -f
%configure

install -d $RPM_BUILD_ROOT
%{__make} RPMSRCS=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTH* Chan* NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
