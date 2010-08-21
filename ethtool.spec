Summary:	Utility to control ethernet cards
Summary(es.UTF-8):	Grupos de herramientas Ethernet
Summary(pl.UTF-8):	Narzędzie do kontrolowania kart ethernet
Summary(pt_BR.UTF-8):	Ferramenta de configuração para placas ethernet PCI
Name:		ethtool
Version:	2.6.35
Release:	1
Epoch:		1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://downloads.sourceforge.net/gkernel/%{name}-%{version}.tar.gz
# Source0-md5:	e0f617779a58b77af061a9e5178d0b25
URL:		http://sourceforge.net/projects/gkernel/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
ethtool is a small utility for examining and tuning your
ethernet-based network interface.

%description -l es.UTF-8
Grupos de herramientas Ethernet.

%description -l pl.UTF-8
ethtool to niewielkie narzędzie do kontroli i tuningu sieciowych kart
ethernet.

%description -l pt_BR.UTF-8
Este utilitário permite consulta e alteração da configuração de placas
ethernet, como velocidade, porta, negociação automática e localização
PCI.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README
%attr(755,root,root) %{_sbindir}/ethtool
%{_mandir}/man8/ethtool.8*
