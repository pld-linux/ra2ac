#
# TODO:
# - make proper nice banner
# - make some way to have obsoletes on that package
Summary:	Ra -> Ac converter
Summary(pl.UTF-8):   Konwerter Ra -> Ac
Name:		ra2ac
Version:	0.10
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://piorun.ds.pg.gda.pl/~blues/SOURCES/%{name}-%{version}.tar.gz
# Source0-md5:	e254c3ade7655401ed3c26279d3ef6b5
URL:		http://www.pld-linux.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Set of upgrade scripts to make upgrade from PLD Ra (1.x) to PLD Ac
(2.0). This is really useful when you want to switch to never line of
PLD.

Remember that you use that upgrade scripts at your own risk!
It's really only helper.

%description -l pl.UTF-8
Zestaw skryptów do robienia upgrade z PLD Ra (1.x) do PLD Ac (2.0).
Jest to naprawdę przydatne, jeżeli chciałbyś się przesiąść na nowszą
linię PLD.

Pamiętaj, że używasz tych skryptów na własną odpowiedzialność!
To tylko pomoc dla ciebie.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install ra2ac $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README* TODO
%attr(755,root,root) %{_sbindir}/*
