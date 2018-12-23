#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-png
Version  : 0.1.7
Release  : 55
URL      : http://cran.r-project.org/src/contrib/png_0.1-7.tar.gz
Source0  : http://cran.r-project.org/src/contrib/png_0.1-7.tar.gz
Summary  : Read and write PNG images
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-png-lib
BuildRequires : clr-R-helpers
BuildRequires : pkgconfig(libpng)

%description
No detailed description available

%package lib
Summary: lib components for the R-png package.
Group: Libraries

%description lib
lib components for the R-png package.


%prep
%setup -q -c -n png

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502417162

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502417162
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library png
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library png
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library png
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/png/DESCRIPTION
/usr/lib64/R/library/png/INDEX
/usr/lib64/R/library/png/Meta/Rd.rds
/usr/lib64/R/library/png/Meta/features.rds
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
/usr/lib64/R/library/png/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/png/libs/png.so
/usr/lib64/R/library/png/libs/png.so.avx2
