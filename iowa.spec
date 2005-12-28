Summary:	IOWA mail library
Summary(pl):	IOWA - biblioteka do obs³ugi poczty
Name:		iowa
Version:	0.9.9p1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/6037/%{name}_%{version}.tar.bz2
# Source0-md5:	53023be19e138c774e0806c95d890e53
Source1:	http://rubyforge.org/frs/download.php/6048/skeleton_%{version}.tar.bz2
Source2:	setup.rb
URL:		http://enigo.com/projects/iowa/
BuildRequires:	rpmbuild(macros) >= 1.272
BuildRequires:	ruby-devel
Requires:	ruby-modules
Requires:	ruby-LOG4R
Requires:	ruby-TMail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iowa is a framework, written in the Ruby programming language, for the
development of both web based applications and more general dynamic
web content.

%description -l pl
Iowa to napisany w jêzyku programowania Ruby szkielet do tworzenia
zarówno aplikacji opartych na WWW jak i bardziej ogólnej dynamicznej
zawarto¶ci stron WWW.

%prep
%setup -q -n %{name}_%{version} -a 1
cp %{SOURCE2} .
mkdir -p lib/{iowa,apache}
mv src/*.rb lib/iowa
mv mod_iowa.rb lib/apache
mv iowa*.rb lib/

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README* lib/* --title "%{name} %{version}" --inline-source

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{_examplesdir}/%{name}-%{version}/skeleton}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a skeleton_%{version}/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/skeleton
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
