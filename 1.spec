%define version         1.0
%define buildroot       /home/gitus/project

Name:   HelloW
Version:        %{version}
Release:        1
Summary:        GNU HelloW
BuildRoot:      %{buildroot}
Group:          Try
License:        None
Source:         liennas.tar.gz
Prefix:         /usr

%description
Echo "Hello World"


%build
make

%pre
#!/bin/sh
useradd hellower
echo "1234" | passwd hellower --stdin
%end

%install
make install prefix=$RPM_BUILD_ROOT
%files
%defattr(-,root,root)
/hello.exe


