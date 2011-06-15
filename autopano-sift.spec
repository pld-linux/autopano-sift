# NOTE: libsift is also available separately at
# http://user.cs.tu-berlin.de/~nowozin/libsift/
# it should be separate package when other packages use it
%include	/usr/lib/rpm/macros.mono
Summary:	SIFT Feature Detection implementation
Summary(pl.UTF-8):	Implementacja algorytmu SIFT do wykrywania cech obrazu
Name:		autopano-sift
Version:	2.4
Release:	4
License:	GPL, but SIFT algorithm may require license in some countries
Group:		X11/Applications/Graphics
Source0:	http://user.cs.tu-berlin.de/~nowozin/autopano-sift/%{name}-%{version}.tar.gz
# Source0-md5:	e497074d0cb5586cdc66506d782ccbd7
URL:		http://user.cs.tu-berlin.de/~nowozin/autopano-sift/
# uses {glib,atk,gdk,gtk,glade}-sharp
BuildRequires:	dotnet-gtk-sharp-devel >= 1.0
BuildRequires:	mono-csharp >= 1.0
BuildRequires:	rpmbuild(monoautodeps)
Requires:	dotnet-gtk-sharp >= 1.0
Requires:	libgdiplus >= 1.0
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SIFT algorithm provides the capability to identify key feature
points within arbitrary images. It further extracts highly distinct
information for each such point and allows to characterize the point
invariant to a number of modifications to the image. It is invariant
to contrast/brightness changes, to rotation, scaling and partially
invariant to other kinds of transformations. The algorithm can be
flexibly used to create input data for image matching, object
identification and other computer vision related algorithms.

This package provides an implementation of the SIFT algorithm and a
set of utilities to utilize the algorithm to match two or more images.
As output, a number of control points are created, which specify one
and the same image location in two images. The output is created as
project file for the hugin panorama stitching software, which is
available in hugin package.

%description -l pl.UTF-8
Algorytm SIFT daje możliwość określenia kluczowych punktów
charakterystycznych na dowolnych zdjęciach. Następnie wydobywa
informacje wyodrębniające dla każdego takiego punktu i pozwala
scharakteryzować ten punkt niezależnie od liczby modyfikacji obrazu.
Jest niezależny od zmian kontrastu/jasności, obrotów, skalowania i
częściowo niezależny od innych rodzajów przekształceń. Algorytm może
być elastycznie używany do tworzenia danych wejściowych do
dopasowywania obrazów, identyfikowania obiektów i innych algorytmów
związanych z grafiką komputerową.

Ten pakiet dostarcza implementację algorytmu SIFT i zestaw narzędzi
wykorzystujących ten algorytm do dopasowywania dwóch lub większej
liczby zdjęć. Na wyjściu tworzony jest zbiór punktów kontrolnych
określających to samo miejsce na dwóch zdjęciach. Wyjście jest
tworzone w formacie pliku projektu dla programu do sklejania panoram
hugin, dostępnego w pakiecie o tej samej nazwie.

%prep
%setup -q 

%build
%{__make} -C src -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man{1,7}}

install src/libsift.dll $RPM_BUILD_ROOT%{_libdir}
install src/bin/autopano-complete.sh $RPM_BUILD_ROOT%{_bindir}
install src/util/{autopano,generatekeys,generatekeys-sd,showone,showtwo}.exe \
	$RPM_BUILD_ROOT%{_bindir}
install src/util/monoopt.sh $RPM_BUILD_ROOT%{_bindir}
install src/util/autopanog/autopanog.exe $RPM_BUILD_ROOT%{_bindir}
install src/util/man/{autopano-complete,autopano,autopanog,generatekeys,showone,showtwo}.1 \
	$RPM_BUILD_ROOT%{_mandir}/man1
install src/util/man/autopano-sift.7 $RPM_BUILD_ROOT%{_mandir}/man7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*.sh
# blegh, cannot be run directly (caught by WINE in PLD)
%attr(755,root,root) %{_bindir}/*.exe
%{_libdir}/libsift.dll
%{_mandir}/man1/*
%{_mandir}/man7/autopano-sift.7*
