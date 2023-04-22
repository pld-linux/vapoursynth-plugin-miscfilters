Summary:	Miscellaneous filter collection for Vapoursynth
Summary(pl.UTF-8):	Zestaw różnych filtrów dla programu Vapoursynth
Name:		vapoursynth-plugin-miscfilters
Version:	2
Release:	1
License:	GPL v2+
Group:		Libraries
%define	gitref	acdeca22038583d73d420ccf76d0658f06cae3c0
Source0:	https://github.com/vapoursynth/vs-miscfilters-obsolete/archive/R%{version}/vs-miscfilters-obsolete-R%{version}.tar.gz
# Source0-md5:	d8b2b296f789ad1cf9fd0abe1fb5c0cc
Patch0:		vs-miscfilters-obsolete-git.patch
URL:		https://github.com/vapoursynth/vs-miscfilters-obsolete
BuildRequires:	meson >= 0.48
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	ninja >= 1.5
BuildRequires:	vapoursynth-devel >= 55
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Miscellaneous Filters is a random collection of filters that mostly
are useful for Avisynth compatibility.

%description -l pl.UTF-8
Miscellaneous Filters to przypadkowy zbiór filtrów, przydatnych
głównie dla zgodności z programem Avisynth.

%prep
%setup -q -n vs-miscfilters-obsolete-R%{version}
%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/misc.rst
%attr(755,root,root) %{_libdir}/vapoursynth/libmiscfilters.so
