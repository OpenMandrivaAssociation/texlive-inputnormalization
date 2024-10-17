Name:		texlive-inputnormalization
Version:	59850
Release:	2
Summary:	Wrapper for XeTeX's and LuaTeX's input normalization
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/inputnormalization
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputnormalization.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputnormalization.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputnormalization.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a cross engine interface to normalizing
input before it's read by TeX. It is based on XeTeX's
\XeTeXinputnormalization primitive and lua-uni-algos for
LuaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/inputnormalization
%{_texmfdistdir}/tex/latex/inputnormalization
%doc %{_texmfdistdir}/doc/latex/inputnormalization

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
