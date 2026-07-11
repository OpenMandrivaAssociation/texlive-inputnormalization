%global tl_name inputnormalization
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Wrapper for XeTeXs and LuaTeXs input normalization
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/generic/inputnormalization
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inputnormalization.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inputnormalization.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/inputnormalization.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a cross engine interface to normalizing input
before it's read by TeX. It is based on XeTeX's \XeTeXinputnormalization
primitive and lua-uni-algos for LuaTeX.

