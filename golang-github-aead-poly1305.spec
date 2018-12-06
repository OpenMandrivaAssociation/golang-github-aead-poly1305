# Run tests in check section
%bcond_without check

%global goipath         github.com/aead/poly1305
%global commit          3fee0db0b63511234f7230da50b72414f6258f10

%global common_description %{expand:
The poly1305 message authentication code.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        The poly1305 message authentication code
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}


BuildRequires:  golang(golang.org/x/sys/cpu)

%description
%{common_description}


%package devel
Summary:       %{summary}

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Tue Jul 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180717git3fee0db
- Bump to commit 3fee0db0b63511234f7230da50b72414f6258f10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git969857f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180517git969857f
- First package for Fedora

