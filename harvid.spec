Summary:	HTTP Ardour Video Daemon
Name:		harvid
Version:	0.8.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/x42/harvid/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b119406e6a42ed5649ac0658c72aac57
URL:		http://harvid.sf.net/
BuildRequires:	ffmpeg-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Harvid decodes still images from movie files and serves them via HTTP.

Its intended use-case is to efficiently provide frame-accurate data
and act as second level cache for rendering the video-timeline in
Ardour.

%prep
%setup -q

%build
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}" \
	bindir="%{_bindir}" \
	mandir="%{_mandir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_bindir}/harvid
%{_mandir}/man1/harvid.1*
