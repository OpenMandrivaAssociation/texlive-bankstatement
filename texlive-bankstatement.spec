Name:		texlive-bankstatement
Version:	38857
Release:	2
Summary:	A LaTeX class for bank statements based on csv data
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bankstatement
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bankstatement.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bankstatement.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
More and more banks allow their customers to download posting
records in various formats. By using the bankstatement class,
you can create bank statements, as long as a csv format is
available. At the moment, the csv-mt940 and csv-camt formats --
used by many german Sparkassen -- are supported. You can quite
easily add support for other csv formats. Simply define the
order of the keys in the csv data file and how to use them. The
terminology in this class -- such as BIC (Business Identifier
Code) or IBAN (International Bank Account Number) -- is based
on usage in the SEPA (Single Euro Payments Area). The user may
adjust the terminology to suit local needs.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bankstatement
%doc %{_texmfdistdir}/doc/latex/bankstatement

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
