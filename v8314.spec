%{!?scl:%global scl v8314}
%scl_package %scl

%global install_scl 1

Name:		%scl_name
Version:	1
Release:	4%{?dist}
Summary:	%scl Software Collection
License:	MIT

%if %{?install_scl} > 0
Requires: %{scl_prefix}gyp
Requires: %{scl_prefix}v8
Requires: %{scl_prefix}v8-devel
Requires: %{scl_prefix}runtime
%endif

BuildRequires:	scl-utils-build
BuildRequires:  python-devel

%description
This is the main package for %scl Software Collection.

%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils

%description runtime
Package shipping essential scripts to work with %scl Software Collection.
 
%package build
Summary: Package shipping basic build configuration
Requires: scl-utils-build
 
%description build
Package shipping essential configuration macros to build %scl Software Collection.

%package scldevel
Summary: Package shipping development files for %scl

%description scldevel
Package shipping development files, especially usefull for development of
packages depending on %scl Software Collection.

%prep
%setup -T -c

%install
rm -rf %{buildroot}
%scl_install

mkdir -p %{buildroot}%{_scl_scripts}/root
cat >> %{buildroot}%{_scl_scripts}/enable << EOF
export PATH=%{_bindir}\${PATH:+:\${PATH}} 
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export PYTHONPATH=%{_scl_root}%{python_sitelib}\${PYTHONPATH:+:\${PYTHONPATH}}
export MANPATH=%{_mandir}:\$MANPATH
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig\${PKG_CONFIG_PATH:+:\${PKG_CONFIG_PATH}}
export CPATH=%{_includedir}\${CPATH:+:\${CPATH}}
export LIBRARY_PATH=%{_libdir}\${LIBRARY_PATH:+:\${LIBRARY_PATH}}
EOF

cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel << EOF
%%scl_%{scl_name_base} %{scl}
%%scl_prefix_%{scl_name_base} %{scl_prefix}
EOF


# scl doesn't include this directory
#mkdir -p %{buildroot}%{_scl_root}%{python_sitelib}
#mkdir -p %{buildroot}%{_libdir}/pkgconfig

%files

%files runtime
%scl_files
 
%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

%changelog
* Mon Jan 27 2014 Tomas Hrcka <thrcka@redhat.com> - 1-4
- Add -scldevel sub-package.

* Mon Dec 16 2013 Tomas Hrcka <thrcka@redhat.com> - 1-3
- Install collection packages as dependency

* Tue Nov 26 2013 Honza Horak <hhorak@redhat.com> - 1-2
- Provide CPATH and LIBRARY_PATH in the enable scriptlet

* Tue Oct 29 2013 thrcka@redhat.com - 1-1
- Initial version of the V8 Software Collection
