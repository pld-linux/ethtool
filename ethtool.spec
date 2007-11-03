Summary:	Utility to control ethernet cards
Summary(es.UTF-8):	Grupos de herramientas Ethernet
Summary(pl.UTF-8):	Narzędzie do kontrolowania kart ethernet
Summary(pt_BR.UTF-8):	Ferramenta de configuração para placas ethernet PCI
Name:		ethtool
Version:	6
Release:	2
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/gkernel/%{name}-%{version}.tar.gz
# Source0-md5:	3b721ec27f17ebf320ba8c505cf66d9c
URL:		http://sourceforge.net/projects/gkernel/
BuildRequires:	autoconf
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
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
