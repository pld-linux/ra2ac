#
# TODO:
# - make proper nice banner
# - make some way to have obsoletes on that package
Summary:	Ra -> Ac converter
Summary(pl):	Konwerter Ra -> Ac
Name:		ra2ac
Version:	0.9
Release:	0.9
License:	GPL v2
Group:		Applications/System
Source0:	http://piorun.ds.pg.gda.pl/~blues/SOURCES/%{name}-%{version}.tar.gz
# Source0-md5:	c6ba2eceeb90f683a6a96e3ad73d7d0f
URL:		http://www.pld-linux.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Set of upgrade scripts to make upgrade from PLD Ra (1.x) to PLD Ac
(2.0). This is really useful when you want to switch to never line of
PLD.

Remember that you use that upgrade scripts at your own risk!
It's really only helper.

%description -l pl
Zestaw skryptów do robienia upgrade z PLD Ra (1.x) do PLD Ac (2.0).
Jest to naprawdê przydatne, je¿eli chcia³by¶ siê przesi±¶æ na nowsz±
liniê PLD.

Pamiêtaj, ¿e u¿ywasz tych skryptów na w³asn± odpowiedzialno¶æ!
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
%doc ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
