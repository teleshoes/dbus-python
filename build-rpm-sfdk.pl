#!/usr/bin/perl
use strict;
use warnings;

my $IS_64_BIT = 1;
my $ARCH = $IS_64_BIT ? "aarch64" : "armv7hl";
my $SPEC = $IS_64_BIT ? "RPM/SPEC/python2-dbus-64bit.spec" : "RPM/SPEC/python2-dbus-32bit.spec";
my $TARGET = "SailfishOS-4.3.0.12-$ARCH";

my $SFDK = "$ENV{HOME}/SailfishOS/bin/sfdk";

my $SIP_PATCH_GLOB = "build-sip-patches/*";

my @PKG_DEPS = qw(
  python
  python-devel
  autoconf
  automake
  autoconf-archive
  pkgconfig
  libtool
  m4
);

my @RPM_DEPS = (
);

my @PKG_TOOLS = qw(
  git
  vim-enhanced
);

sub getPkgInfo();
sub sfdkCmd(@);
sub run(@);

sub main(@){
  run "$SFDK config --push target $TARGET";
  for my $pkg(@PKG_TOOLS, @PKG_DEPS){
    run "$SFDK tools package-install $TARGET $pkg";
  }

  for my $rpmFile(@RPM_DEPS){
    run "$SFDK tools package-install $TARGET $rpmFile";
  }

  my $pkg = getPkgInfo();
  my $rpmName = "$$pkg{name}-$$pkg{version}-$$pkg{release}.$$pkg{arch}";

  my $buildRoot = "/home/mersdk/rpmbuild/BUILDROOT/$rpmName";

  sfdkCmd "./autogen.sh", "--prefix=/usr";
  sfdkCmd "make", "-j8";
  sfdkCmd "make", "DESTDIR=$buildRoot", "install";
  sfdkCmd "rpmbuild", "-bb", "--buildroot=$buildRoot", $SPEC;
  sfdkCmd "cp", "/home/mersdk/rpmbuild/RPMS/$$pkg{arch}/$rpmName.rpm", ".";
}

sub getPkgInfo(){
  my $out = `cat $SPEC 2>/dev/null`;
  my $pkg = {};
  $$pkg{name}    = $1 if $out =~ /^Name:      \s* (\S+)$/mx;
  $$pkg{arch}    = $1 if $out =~ /^BuildArch: \s* (\S+)$/mx;
  $$pkg{version} = $1 if $out =~ /^Version:   \s* (\S+)$/mx;
  $$pkg{release} = $1 if $out =~ /^Release:   \s* (\S+)$/mx;

  for my $key(qw(name arch version release)){
    die "ERROR: could not parse $key in $SPEC\n" if not defined $$pkg{$key};
  }

  return $pkg;
}

sub sfdkCmd(@){
  print "\n";
  run($SFDK, "build-shell", @_);
}

sub run(@){
  print "@_\n";
  system @_;
}

&main(@ARGV);
