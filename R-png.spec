#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-png
Version  : 0.1
Release  : 22
URL      : http://cran.r-project.org/src/contrib/png_0.1-7.tar.gz
Source0  : http://cran.r-project.org/src/contrib/png_0.1-7.tar.gz
Summary  : Read and write PNG images
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
BuildRequires : clr-R-helpers
BuildRequires : pkgconfig(libpng)
BuildRequires : zlib-dev

%description
No detailed description available

%prep
%setup -q -c -n png

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library png
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library png


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/png/DESCRIPTION
/usr/lib64/R/library/png/INDEX
/usr/lib64/R/library/png/Meta/Rd.rds
/usr/lib64/R/library/png/Meta/hsearch.rds
/usr/lib64/R/library/png/Meta/links.rds
/usr/lib64/R/library/png/Meta/nsInfo.rds
/usr/lib64/R/library/png/Meta/package.rds
/usr/lib64/R/library/png/NAMESPACE
/usr/lib64/R/library/png/NEWS
/usr/lib64/R/library/png/R/png
/usr/lib64/R/library/png/R/png.rdb
/usr/lib64/R/library/png/R/png.rdx
/usr/lib64/R/library/png/help/AnIndex
/usr/lib64/R/library/png/help/aliases.rds
/usr/lib64/R/library/png/help/paths.rds
/usr/lib64/R/library/png/help/png.rdb
/usr/lib64/R/library/png/help/png.rdx
/usr/lib64/R/library/png/html/00Index.html
/usr/lib64/R/library/png/html/R.css
/usr/lib64/R/library/png/img/Rlogo.png
/usr/lib64/R/library/png/libs/png.so
/usr/lib64/R/library/png/libs/symbols.rds
