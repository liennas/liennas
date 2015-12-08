%define version         1.0
%define buildroot       /home/gitus/project
%define buil		/home/gitus/rpmbuild/

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

%prep

find %{buil} -maxdepth 1 -mindepth 1 -type d | grep -vP "(SOURCES|SPECS)" | while read line; do rm -rf $line; done
mkdir %{buil}BUILD %{buil}SRPMS %{buil}RPMS
tar -xvf %{buil}SOURCES/liennas.tar.gz -C %{buil}BUILD/

find %{buil}BUILD/ -type f | while read line; do mv $line %{buil}BUILD/; done


%build
make

%install
make install prefix=$RPM_BUILD_ROOT
%files
%defattr(-,root,root)
/hello.exe
