%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	IOWA mail library
Summary(pl):	IOWA - biblioteka do obs³ugi poczty
Name:		iowa
Version:	0.9.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1853/%{name}_%{version}.tar.gz
# Source0-md5:	cb27f0baa555c9e4f55ebb4a4a593c0a
Source1:	setup.rb
URL:		http://enigo.com/projects/iowa/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
Requires:	ruby-TMail
Requires:	ruby-LOG4R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iowa is a framework, written in the Ruby programming language, for 
the development of both web based applications and more general dynamic 
web content. 

%prep
%setup -q -n %{name}_%{version}

%build
cp %{SOURCE1} .
mkdir -p lib/{iowa,apache}
mv src/*.rb lib/iowa
mv mod_iowa.rb lib/apache
mv iowa*.rb lib/

ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README* lib/* --title "%{name} %{version}" --inline-source

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{_examplesdir}/%{name}-%{version}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a utils $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/* CONTRIBUTORS README-CGI VERSIONS ChangeLog README-FCGI 
%doc INSTALL README-MOD_RUBY README-WEBRICK README ToDo 
%{ruby_rubylibdir}/iowa
%{ruby_rubylibdir}/apache/*
%{ruby_rubylibdir}/*.rb
%{_examplesdir}/%{name}-%{version}
