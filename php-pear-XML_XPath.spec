%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	XPath
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XPath/DOM XML manipulation, maneuvering and query interface
Summary(pl.UTF-8):	%{_pearname} - interfejs do obróbki i zapytań XPath/DOM XML
Name:		php-pear-%{_pearname}
Version:	1.2.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b0af5c50625373a13400db23b85b4924
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/XML_XPath/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(domxml)
Requires:	php-common < 3:5.0.0
Requires:	php-common >= 3:4.2.1
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
<http://sourceforge.net/projects/phpxpath/>.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa PEAR::XML_XPath udostępnia interfejs do obróbki, manewrowania i
zapytań XPath/DOM XML.

Klasa ta pozwala na łatwe manipulowanie, manewrowanie i odpytywanie
drzewa DOMXML przy użyciu zapytań XPath i funkcji chodzących DOM.
Używa wewnętrznego wskaźnika dla wszystkich metod, na których jest
wykonywana akcja. Wyniki zapytań DOM/XPath są zwracane jako obiekt
XPath_Result, który zawiera wewnętrzną tablicę węzłów DOM i rozszerza
ogólną klasę DOM, przez co zawiera wszystkie funkcje DOM z głównego
obiektu, które można uruchamiać na każdym z elementów wewnętrznej
tablicy. Ta klasa próbuje być najbliżej rekomendacji DOM na ile to
możliwe. Aby używać tej klasy, trzeba mieć rozszerzenie domxml.

Klasa XML_XPath była inspirowana klasą phpxpath utrzymywaną przez
Nigela Swinsona. Klasa phpxpath nie polega na funkcjach PHP xmldom,
dlatego jest siostrzana dla tej klasy:
<http://sourceforge.net/projects/phpxpath/>.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}
%patch0 -p2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
