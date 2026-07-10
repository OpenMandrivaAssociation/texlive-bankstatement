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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bankstatement
%dir %{_datadir}/texmf-dist/tex/latex/bankstatement
%doc %{_datadir}/texmf-dist/doc/latex/bankstatement/201412.csv
%doc %{_datadir}/texmf-dist/doc/latex/bankstatement/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bankstatement/bankstatement-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bankstatement/bankstatement-example.tex
%doc %{_datadir}/texmf-dist/doc/latex/bankstatement/bankstatement.dtx
%doc %{_datadir}/texmf-dist/doc/latex/bankstatement/bankstatement.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bankstatement/makefile
%doc %{_datadir}/texmf-dist/doc/latex/bankstatement/stmlogo.jpg
%{_datadir}/texmf-dist/tex/latex/bankstatement/bankstatement.cls
%{_datadir}/texmf-dist/tex/latex/bankstatement/csv-camt.def
%{_datadir}/texmf-dist/tex/latex/bankstatement/csv-mt940.def
%{_datadir}/texmf-dist/tex/latex/bankstatement/csv-standard-bank-na.def
%{_datadir}/texmf-dist/tex/latex/bankstatement/stmenglish.def
%{_datadir}/texmf-dist/tex/latex/bankstatement/stmgerman.def
%{_datadir}/texmf-dist/tex/latex/bankstatement/stmnamibian.def
