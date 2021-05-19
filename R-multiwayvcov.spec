#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-multiwayvcov
Version  : 1.2.3
Release  : 31
URL      : https://cran.r-project.org/src/contrib/multiwayvcov_1.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/multiwayvcov_1.2.3.tar.gz
Summary  : Multi-Way Standard Error Clustering
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-sandwich
BuildRequires : R-sandwich
BuildRequires : buildreq-R

%description
multi-way clustering using the method suggested by Cameron, Gelbach, &
    Miller (2011) and cluster (or block)
    bootstrapping for estimating variance-covariance matrices. Normal one and
    two-way clustering matches the results of other common statistical
    packages.  Missing values are handled transparently and rudimentary
    parallelization support is provided.

%prep
%setup -q -c -n multiwayvcov
cd %{_builddir}/multiwayvcov

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589581066

%install
export SOURCE_DATE_EPOCH=1589581066
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library multiwayvcov
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library multiwayvcov
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library multiwayvcov
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc multiwayvcov || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/multiwayvcov/DESCRIPTION
/usr/lib64/R/library/multiwayvcov/INDEX
/usr/lib64/R/library/multiwayvcov/LICENSE
/usr/lib64/R/library/multiwayvcov/Meta/Rd.rds
/usr/lib64/R/library/multiwayvcov/Meta/data.rds
/usr/lib64/R/library/multiwayvcov/Meta/features.rds
/usr/lib64/R/library/multiwayvcov/Meta/hsearch.rds
/usr/lib64/R/library/multiwayvcov/Meta/links.rds
/usr/lib64/R/library/multiwayvcov/Meta/nsInfo.rds
/usr/lib64/R/library/multiwayvcov/Meta/package.rds
/usr/lib64/R/library/multiwayvcov/NAMESPACE
/usr/lib64/R/library/multiwayvcov/NEWS
/usr/lib64/R/library/multiwayvcov/R/multiwayvcov
/usr/lib64/R/library/multiwayvcov/R/multiwayvcov.rdb
/usr/lib64/R/library/multiwayvcov/R/multiwayvcov.rdx
/usr/lib64/R/library/multiwayvcov/data/petersen.rda
/usr/lib64/R/library/multiwayvcov/help/AnIndex
/usr/lib64/R/library/multiwayvcov/help/aliases.rds
/usr/lib64/R/library/multiwayvcov/help/multiwayvcov.rdb
/usr/lib64/R/library/multiwayvcov/help/multiwayvcov.rdx
/usr/lib64/R/library/multiwayvcov/help/paths.rds
/usr/lib64/R/library/multiwayvcov/html/00Index.html
/usr/lib64/R/library/multiwayvcov/html/R.css
