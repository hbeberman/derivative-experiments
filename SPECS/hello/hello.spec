%define debug_package %{nil}

Name:    hello
Summary: This is a short summary of hello
License: MIT
Version: 1
Release: 1
Source0: hello.tar.gz
#         | hello-1/
#         | hello-1/hello.txt

%description
 This is a (slightly) longer description about what the package is.

%prep
%setup

%build
echo "Not actually building anything"

%install
mkdir -p %{buildroot}/%{_sysconfdir}
install -m 644 hello.txt %{buildroot}%{_sysconfdir}

%files
%{_sysconfdir}/hello.txt

%changelog
* Mon Sep 14 2020 Henry Beberman <henry.beberman@microsoft.com> 1-1
-  Initial version of hello
