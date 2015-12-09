
%define version         1.8
%define buil		/home/gitus/rpmbuild/

%define nam         nginx-01d52c2b460d

Name:   nginx
Version:        %{version}
Release:        1
Summary:        GNU nginx
BuildRoot:      %{buil}
Group:          Try
License:        None
Source:         nginx-01d52c2b460d.tar.gz

%description
THIS IS NGINX!

%prep
%setup -q -n nginx-01d52c2b460d

%build
./auto/configure \
			--with-pcre=auto/lib/pcre \
			--with-zlib=auto/lib/zlib
		

%install
make install prefix=$RPM_BUILD_ROOT
%files
%defattr(-,root,root)
%doc README
