Summary:	Utility to control ethernet cards
Summary(es):	Grupos de herramientas Ethernet
Summary(pl):	Narzêdzie do kontrolowania kart ethernet
Summary(pt_BR):	Ferramenta de configuração para placas ethernet PCI
Name:		ethtool
Version:	2
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/gkernel/%{name}-%{version}.tar.gz
# Source0-md5:	b169ab16a9f011ff4b2f8aab81226ad3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ethtool is a small utility for examining and tuning your
ethernet-based network interface.

%description -l es
Grupos de herramientas Ethernet.

%description -l pl
ethtool to niewielkie narzêdzie do kontroli i tuningu sieciowych kart
ethernet.

%description -l pt_BR
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
