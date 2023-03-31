Name:		texlive-ebgaramond-maths
Version:	52168
Release:	2
Summary:	LaTeX support for EBGaramond fonts in mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ebgaramond-maths
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebgaramond-maths.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebgaramond-maths.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides some LaTeX support for the use of
EBGaramond12 in mathematics. It is based on, and requires,
ebgaramond. The package was created in response to a question
at TeX-stackexchange. and tested in the form of an answer in
the same forum.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ebgaramond-maths
%{_texmfdistdir}/fonts/tfm/public/ebgaramond-maths
%{_texmfdistdir}/fonts/map/dvips/ebgaramond-maths
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond-maths
%doc %{_texmfdistdir}/doc/fonts/ebgaramond-maths

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
