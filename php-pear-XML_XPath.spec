%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	XPath
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XPath/DOM XML manipulation, maneuvering and query interface
Summary(pl):	%{_pearname} - interfejs do obróbki i zapytañ XPath/DOM XML
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	916f60741d5db46b190512e1ba72964c
URL:		http://pear.php.net/package/XML_XPath/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::XML_XPath class provides an XPath/DOM XML manipulation,
maneuvering and query interface.

The class allows for easy manipulation, maneuvering and querying of a
DOMXML tree using both XPath queries and DOM walk functions. It uses
an internal pointer for all methods on which the action is performed.
Results from an DOM/XPath query are returned as an XPath_Result
object, which contains an internal array of DOM nodes and which
extends the common DOM class and hence contains all the DOM functions
from the main object to run on each of the elements in the internal
array. This class tries to hold as close as possible to the DOM
Recommendation. You MUST have the domxml extension to use this class.

The XML_XPath class was inspired by a class maintained by Nigel
Swinson called phpxpath. The phpxpath class does not rely on PHP
xmldom functions and is therefore a sibling to this class:
http://sourceforge.net/projects/phpxpath/.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa PEAR::XML_XPath udostêpnia interfejs do obróbki, manewrowania i
zapytañ XPath/DOM XML.

Klasa ta pozwala na ³atwe manipulowanie, manewrowanie i odpytywanie
drzewa DOMXML przy u¿yciu zapytañ XPath i funkcji chodz±cych DOM.
U¿ywa wewnêtrznego wska¼nika dla wszystkich metod, na których jest
wykonywana akcja. Wyniki zapytañ DOM/XPath s± zwracane jako obiekt
XPath_Result, który zawiera wewnêtrzn± tablicê wêz³ów DOM i rozszerza
ogóln± klasê DOM, przez co zawiera wszystkie funkcje DOM z g³ównego
obiektu, które mo¿na uruchamiaæ na ka¿dym z elementów wewnêtrznej
tablicy. Ta klasa próbuje byæ najbli¿ej rekomendacji DOM na ile to
mo¿liwe. Aby u¿ywaæ tej klasy, trzeba mieæ rozszerzenie domxml.

Klasa XML_XPath by³a inspirowana klas± phpxpath utrzymywan± przez
Nigela Swinsona. Klasa phpxpath nie polega na funkcjach PHP xmldom,
dlatego jest siostrzana dla tej klasy:
http://sourceforge.net/projects/phpxpath/.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{,%{_subclass}}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
