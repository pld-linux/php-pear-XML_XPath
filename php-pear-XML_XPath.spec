%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       XPath
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - provides an XPath/DOM XML manipulation, maneuvering and query interface
Name:		php-pear-%{_pearname}
Version:	1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::XML_XPath class provided an XPath/DOM XML manipulation,
maneuvering and query interface.

The class allows for easy manipulation, maneuvering and querying of a
domxml tree using both xpath queries and DOM walk functions. It uses
an internal pointer for all methods on which the action is performed.
Results from an dom/xpath query are returned as an XPath_Result
object, which contains an internal array of DOM nodes and which
extends the common DOM class and hence contains all the DOM functions
from the main object to run on each of the elements in the internal
array. This class tries to hold as close as possible to the DOM
Recommendation. You MUST have the domxml extension to use this class.

The XML_XPath class was inspired by a class maintained by Nigel
Swinson called phpxpath. The phpxpath class does not rely on PHP
xmldom functions and is therefore a sibling to this class:
http://sourceforge.net/projects/phpxpath

This class has in PEAR status: %{_status}.

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
