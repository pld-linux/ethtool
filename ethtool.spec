Summary:	Utility to control ethernet cards
Summary(es.UTF-8):	Grupos de herramientas Ethernet
Summary(pl.UTF-8):	Narzędzie do kontrolowania kart ethernet
Summary(pt_BR.UTF-8):	Ferramenta de configuração para placas ethernet PCI
Name:		ethtool
Version:	5.10
Release:	1
Epoch:		1
License:	GPL v2
Group:		Networking/Admin
Source0:	https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.xz
# Source0-md5:	3737d66105ab8d5b6552d98a510b4010
URL:		https://www.kernel.org/pub/software/network/ethtool/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libmnl-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%package -n bash-completion-%{name}
Summary:	Bash completion for ethtool command
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów polecenia ethtool
Group:		Applications/Shells
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-%{name}
Bash completion for ethtool command.

%description -n bash-completion-%{name} -l pl.UTF-8
Bashowe dopełnianie parametrów polecenia ethtool.

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

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/%{name}
