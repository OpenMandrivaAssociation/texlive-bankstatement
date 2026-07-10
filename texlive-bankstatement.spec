%global tl_name bankstatement
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9.2
Release:	%{tl_revision}.1
Summary:	A LaTeX class for bank statements based on csv data
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bankstatement
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bankstatement.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bankstatement.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
More and more banks allow their customers to download posting records in
various formats. By using the bankstatement class, you can create bank
statements, as long as a csv format is available. At the moment, the
csv-mt940 and csv-camt formats -- used by many german Sparkassen -- are
supported. You can quite easily add support for other csv formats.
Simply define the order of the keys in the csv data file and how to use
them. The terminology in this class -- such as BIC (Business Identifier
Code) or IBAN (International Bank Account Number) -- is based on usage
in the SEPA (Single Euro Payments Area). The user may adjust the
terminology to suit local needs.

