%global ruby_version 3.0.3

# Bundled libraries versions
%global rubygems_version 3.2.32
%global rubygems_molinillo_version 0.7.0

# Default gems.
%global bundler_version 2.2.32
%global bundler_connection_pool_version 2.3.0
%global bundler_fileutils_version 1.4.1
%global bundler_molinillo_version 0.7.0
%global bundler_net_http_persistent_version 4.0.0
%global bundler_thor_version 1.1.0
%global bundler_tmpdir_version 0.1.0
%global bundler_uri_version 0.10.0

%global bigdecimal_version 3.0.0
%global did_you_mean_version 1.5.0

%global io_console_version 0.5.7
%global json_version 2.5.1
%global openssl_version 2.2.1
%global psych_version 3.3.2
%global rdoc_version 6.3.3
%global minitest_version 5.14.2
%global power_assert_version 1.2.0
%global rake_version 13.0.3
%global rbs_version 1.4.0
%global test_unit_version 3.3.7
%global rexml_version 3.2.5
%global rss_version 0.2.9
%global typeprof_version 0.15.2

Name:      ruby
Version:   %{ruby_version}
Release:   2
Summary:   Object-oriented scripting language interpreter
License:   (Ruby or BSD) and Public Domain and MIT and CC0 and zlib and UCD
URL:       https://www.ruby-lang.org/en/

Source0:   http://cache.ruby-lang.org/pub/ruby/3.0/%{name}-%{version}.tar.xz
Source1:   operating_system.rb
Source2:   libruby.stp
Source3:   ruby-exercise.stp
Source4:   macros.ruby
Source5:   macros.rubygems
Source6:   abrt_prelude.rb
Source8:   rubygems.attr
Source9:   rubygems.req
Source10:  rubygems.prov
Source11:  rubygems.con
Source12:  test_abrt.rb
Source13:  test_systemtap.rb

%{load:%{SOURCE4}}
%{load:%{SOURCE5}}

# Fix ruby_version abuse.
# https://bugs.ruby-lang.org/issues/11002
Patch0: ruby-2.3.0-ruby_version.patch
# http://bugs.ruby-lang.org/issues/7807
Patch1: ruby-2.1.0-Prevent-duplicated-paths-when-empty-version-string-i.patch
# Allows to override libruby.so placement. Hopefully we will be able to return
# to plain --with-rubyarchprefix.
# http://bugs.ruby-lang.org/issues/8973
Patch2: ruby-2.1.0-Enable-configuration-of-archlibdir.patch
# Force multiarch directories for i.86 to be always named i386. This solves
# some differencies in build between Fedora and RHEL.
Patch3: ruby-2.1.0-always-use-i386.patch
# Allows to install RubyGems into custom directory, outside of Ruby's tree.
# http://bugs.ruby-lang.org/issues/5617
Patch4: ruby-2.1.0-custom-rubygems-location.patch
# Make mkmf verbose by default
Patch5: ruby-1.9.3-mkmf-verbose.patch
# The ABRT hook used to be initialized by preludes via following patches:
# https://bugs.ruby-lang.org/issues/8566
# https://bugs.ruby-lang.org/issues/15306
# Unfortunately, due to https://bugs.ruby-lang.org/issues/16254
# and especially since https://github.com/ruby/ruby/pull/2735
# this would require boostrapping:
# https://lists.fedoraproject.org/archives/list/ruby-sig@lists.fedoraproject.org/message/LH6L6YJOYQT4Y5ZNOO4SLIPTUWZ5V45Q/
# For now, load the ABRT hook via this simple patch:
Patch6: ruby-2.7.0-Initialize-ABRT-hook.patch
# Workaround "an invalid stdio handle" error on PPC, due to recently introduced
# hardening features of glibc (rhbz#1361037).
# https://bugs.ruby-lang.org/issues/12666
Patch9: ruby-2.3.1-Rely-on-ldd-to-detect-glibc.patch
# Fix DWARF5 support.
# https://bugzilla.redhat.com/show_bug.cgi?id=1920533
# https://bugs.ruby-lang.org/issues/17585
# https://github.com/ruby/ruby/pull/4240
Patch15: ruby-3.1.0-Support-GCCs-DWARF-5.patch
# Fix segfaults with enabled LTO.
# https://bugs.ruby-lang.org/issues/18062
# https://github.com/ruby/ruby/pull/4716
Patch16: ruby-3.1.0-Get-rid-of-type-punning-pointer-casts.patch
# DWARF5/LTO fixes for SIGSEV handler.
# https://bugs.ruby-lang.org/issues/17052
# https://github.com/ruby/ruby/commit/72317b333b85eed483ad00bcd4f40944019a7c13
Patch17: ruby-3.1.0-Ignore-DW_FORM_ref_addr.patch
# https://bugs.ruby-lang.org/issues/17052#note-9
# https://bugs.ruby-lang.org/attachments/download/8974/ruby-addr2line-DW_FORM_ref_addr.patch
# https://github.com/ruby/ruby/commit/a9977ba2f9863e3fb1b2346589ebbca67d80536c
Patch18: ruby-3.1.0-addr2line-DW_FORM_ref_addr.patch
# Avoid possible timeout errors in TestBugReporter#test_bug_reporter_add.
# https://bugs.ruby-lang.org/issues/16492
Patch19: ruby-2.7.1-Timeout-the-test_bug_reporter_add-witout-raising-err.patch
# Add AC_PROG_CC to make C++ compiler dependency optional on autoconf >= 2.70.
# https://github.com/ruby/ruby/commit/912a8dcfc5369d840dcd6bf0f88ee0bac7d902d6
Patch20: ruby-3.1.0-autoconf-2.70-add-ac-prog-cc.patch
# Allow to exclude test with fully qualified name.
# https://bugs.ruby-lang.org/issues/16936
# https://github.com/ruby/ruby/pull/5026
Patch21: ruby-3.1.0-Properly-exclude-test-cases.patch
# Fix loading of default gems.
# https://bugzilla.redhat.com/show_bug.cgi?id=2027099
# https://github.com/rubygems/rubygems/pull/5154
Patch22: rubygems-3.2.33-Fix-loading-operating_system-rb-customizations-too-late.patch

# Fix test broken by wrongly formatted distinguished name submitted to
# `OpenSSL::X509::Name.parse`.
# https://github.com/ruby/openssl/issues/470
# https://github.com/rubygems/rubygems/pull/5030
Patch31: rubygems-3.2.30-Provide-distinguished-name-which-will-be-correctly-p.patch

# Refactor PEM/DER serialization code.
# https://github.com/ruby/openssl/pull/328
Patch40: ruby-3.1.0-Refactor-PEM-DER-serialization-code.patch
# Implement more 'generic' operations using the EVP API.
# https://github.com/ruby/openssl/pull/329
Patch41: ruby-3.1.0-Add-more-support-for-generic-pkey-types.patch
# Allow setting algorithm-specific options in #sign and #verify.
# https://github.com/ruby/openssl/pull/374
Patch42: ruby-3.1.0-Allow-setting-algorithm-specific-options-in-sign-and-verify.patch
# Use high level EVP interface to generate parameters and keys.
# https://github.com/ruby/openssl/pull/397
Patch43: ruby-3.1.0-Use-high-level-EVP-interface-to-generate-parameters-and-keys.patch
# Use EVP API in more places.
# https://github.com/ruby/openssl/pull/436
Patch44: ruby-3.1.0-Use-EVP-API-in-more-places.patch
# Implement PKey#{encrypt,decrypt,sign_raw,verify_{raw,verify_recover}}.
# https://github.com/ruby/openssl/pull/382
Patch45: ruby-3.1.0-Implement-PKey-encrypt-decrypt-sign_raw-verify_raw-and-verify_recover.patch
# Fix `OpenSSL::TestSSL#test_dup` test failure.
# https://github.com/ruby/openssl/commit/7b66eaa2dbabb6570dbbbdfac24c4dcdcc6793d7
Patch46: ruby-3.1.0-test-openssl-utils-remove-dup_public-helper-method.patch
# Fix `OpenSSL::TestDigest#test_digest_constants` test case.
# https://github.com/ruby/openssl/commit/a3e59f4c2e200c76ef1d93945ff8737a05715e17
Patch47: ruby-3.1.0-test-openssl-test_digest-do-not-test-constants-for-l.patch
# Fix `OpenSSL::TestSSL#test_connect_certificate_verify_failed_exception_message`
# test case.
# https://github.com/ruby/openssl/commit/b5a0a198505452c7457b192da2e5cd5dda04f23d
Patch48: ruby-3.1.0-test-openssl-test_ssl-relax-regex-to-match-OpenSSL-s.patch
# Fix `OpenSSL::TestPKCS12#test_{new_with_no_keys,new_with_one_key_and_one_cert}`
# test failures.
# https://github.com/ruby/openssl/commit/998406d18f2acf73090e9fd9d92a7b4227ac593b
Patch49: ruby-3.1.0-test-openssl-test_pkcs12-fix-test-failures-with-Open.patch
# Fix `OpenSSL::TestPKey#test_s_generate_key` test case.
# https://github.com/ruby/openssl/commit/c732387ee5aaa8c5a9717e8b3ffebb3d7430e99a
Patch50: ruby-3.1.0-test-openssl-test_pkey-use-EC-keys-for-PKey.generate.patch
# Miscellaneous changes for OpenSSL 3.0 support.
# https://github.com/ruby/openssl/pull/468
Patch51: ruby-3.1.0-Miscellaneous-changes-for-OpenSSL-3.0-support.patch
# Support OpenSSL 3.0.
# https://github.com/ruby/openssl/pull/399
Patch52: ruby-3.1.0-Support-OpenSSL-3.0.patch
# Fix `TestPumaControlCli#test_control_ssl` testcase in Puma.
# https://github.com/ruby/openssl/pull/399#issuecomment-966239736
Patch53: ruby-3.1.0-SSL_read-EOF-handling.patch

Provides:  %{name}-libs = %{version}-%{release}
Obsoletes: %{name}-libs < %{version}-%{release}

Provides:  ruby(runtime_executable) = %{version} ruby(release) = %{version} bundled(ccan-build_assert)
Provides:  bundled(ccan-check_type) bundled(ccan-container_of) bundled(ccan-list)
Obsoletes: ruby-tcltk < 2.4.0

# The Net::Telnet and XMLRPC were removed. https://bugs.ruby-lang.org/issues/16484
Obsoletes: rubygem-net-telnet < 0.1.1-%{release}
Obsoletes: rubygem-xmlrpc < 0.3.0-%{release}

Suggests:   rubypick
Recommends: ruby(rubygems) >= %{rubygems_version} rubygem(bigdecimal) >= %{bigdecimal_version}
Recommends: rubygem(did_you_mean) >= 1.2.0 rubygem(openssl) >= %{openssl_version}
Requires:   %{name}-help = %{version}-%{release}
BuildRequires: autoconf gdbm-devel gmp-devel libffi-devel openssl-devel libyaml-devel readline-devel
BuildRequires: procps git gcc systemtap-sdt-devel cmake perl ruby

%description
Ruby is a fast and easy interpreted scripting language for object-oriented programming.
It has many functions for processing text Files and perform system management tasks (such as Perl).

%package devel
Summary:    Ruby development environment
Requires:   %{name} = %{version}-%{release}
Requires:   rubygems

%description devel
Headers and libraries for building extension libraries for extensions Ruby or Ruby embedded applications.

%package -n rubygems
Summary:    Ruby standard for wrapping ruby libraries
Version:    %{rubygems_version}
License:    Ruby or MIT
Requires:   ruby(release) rubygem(openssl) >= 2.1.0 rubygem(psych) >= %{psych_version} 
Recommends: rubygem(rdoc) >= %{rdoc_version} rubygem(io-console) >= %{io_console_version}
Provides:   gem = %{version}-%{release} ruby(rubygems) = %{version}-%{release} bundled(rubygem-molinillo) = %{rubygems_molinillo_version}
BuildArch:  noarch

%description -n rubygems
The Ruby standard for publishing and managing third party libraries provided by RubyGems.

%package -n rubygems-devel
Summary:    For packaging RubyGems
Version:    %{rubygems_version}
License:    Ruby or MIT
Requires:   ruby(rubygems) = %{version}-%{release} rubygem(json) >= %{json_version} rubygem(rdoc) >= %{rdoc_version}
BuildArch:  noarch

%description -n rubygems-devel
Provide macros and development tools for packaging RubyGems.

%package -n rubygem-rake
Summary:    make-like utility base on ruby
Version:    %{rake_version}
License:    MIT
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version}
Provides:   rake = %{version}-%{release} rubygem(rake) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-rake
Rake is a Make-like program implemented in Ruby,Tasks and dependencies are specified in standard Ruby syntax.

%package -n rubygem-rbs
Summary:    Type signature for Ruby
Version:    %{rbs_version}
License:    Ruby or BSD
Requires:   ruby(release)
Requires:   ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(rbs) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-rbs
RBS is the language for type signatures for Ruby and standard library
definitions.

%package irb
Summary:    The Interactive Ruby
Version:    %{ruby_version}
Requires:   %{name}-libs = %{ruby_version}
Provides:   irb = %{version}-%{release} ruby(irb) = %{version}-%{release}
BuildArch:  noarch

%description irb
The irb is acronym for Interactive Ruby,It evaluates ruby expression from the terminal.

%package -n rubygem-rdoc
Summary:    Generate HTML and command-line documentation for Ruby projects
Version:    %{rdoc_version}
License:    GPLv2 and Ruby and MIT and OFL
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version} ruby(irb) = 3.0.3 rubygem(io-console) >= %{io_console_version} rubygem(json) >= %{json_version}
Provides:   rdoc = %{version}-%{release} ri = %{version}-%{release} rubygem(rdoc) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-rdoc
RDoc generates HTML and command line documentation for Ruby projects.,RDoc contains "rdoc" and "ri" tools for generating
and displaying online documentation.

%package help
Summary:    Documentation for ruby
Requires:   rubygem-rdoc
Provides:   %{name}-doc = %{version}-%{release}
Obsoletes:  %{name}-doc < %{version}-%{release}
BuildArch:  noarch

%description help
This package provides documentation for ruby.

%package -n rubygem-bigdecimal
Summary:    Provide arbitrary-precision floating point decimal arithmetic
Version:    %{bigdecimal_version}
License:    Ruby or BSD
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(bigdecimal) = %{version}-%{release}

%description -n rubygem-bigdecimal
BigDecimal provides similar support for very large or very accurate floating point numbers.

%package -n rubygem-did_you_mean
Summary:    "Did you mean?" experience in Ruby
Version:    %{did_you_mean_version}
License:    MIT
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(did_you_mean) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-did_you_mean
The error message will tell you the right one when you misspelled something.

%package -n rubygem-io-console
Summary:    Simple console utilizing library
Version:    %{io_console_version}
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(io-console) = %{version}-%{release}

%description -n rubygem-io-console
IO / Console provides very simple and portable access to the console. It does not provide higher-level functions
such as curses and readline.

%package -n rubygem-json
Summary:    JSON implementation as a Ruby extension in C
Version:    %{json_version}
License:    (Ruby or GPLv2) and UCD
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(json) = %{version}-%{release}

%description -n rubygem-json
According to RFC 4627,this package implements the JSON specification.

%package -n rubygem-minitest
Summary:    Provide complete testing facilities
Version:    %{minitest_version}
License:    MIT
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(minitest) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-minitest
minitest/unit - Unit testing framework.
minitest/spec - Full-featured spec engine.
minitest/benchmark - Assert the performance of algorithms in a repeatable manner.
minitest/mock - Tiny mock object framework.
minitest/pride - Show pride in the test and add color to the test output.

%package -n rubygem-openssl
Summary:    Provide SSL、TLS and general purpose cryptography
Version:    %{openssl_version}
License:    Ruby or BSD
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(openssl) = %{version}-%{release}

%description -n rubygem-openssl
This package provides SSL、TLS and general purpose cryptography.

%package -n rubygem-power_assert
Summary:    Power Assert for Ruby
Version:    %{power_assert_version}
License:    Ruby or BSD
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(power_assert) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-power_assert
Power Assert displays each value of variables and method calls in expressions.This is very useful for testing,
it can indicate which value is incorrect when the condition is not met during testing.

%package -n rubygem-psych
Summary:    Ruby's libyaml wrapper
Version:    %{psych_version}
License:    MIT
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(psych) = %{version}-%{release}

%description -n rubygem-psych
Psych is a YAML parser and emitter. According to wrapping libyaml, Psych knows how to
serialize and de-serialize most Ruby objects to and from the YAML format.

%package -n rubygem-bundler
Summary:    Library and utilities to manage a Ruby application's gem dependencies
Version:    %{bundler_version}
License:    MIT
Requires:   ruby(release)
Requires:   ruby(rubygems) >= %{rubygems_version}
Requires:   rubygem(io-console)
Provides:   rubygem(bundler) = %{version}-%{release}
# https://github.com/bundler/bundler/issues/3647
Provides:   bundled(rubygem-connection_pool) = %{bundler_connection_pool_version}
Provides:   bundled(rubygem-fileutils) = %{bundler_fileutils_version}
Provides:   bundled(rubygem-molinillo) = %{bundler_molinillo_version}
Provides:   bundled(rubygem-net-http-persisntent) = %{bundler_net_http_persistent_version}
Provides:   bundled(rubygem-thor) = %{bundler_thor_version}
Provides:   bundled(rubygem-tmpdir) = %{bundler_tmpdir_version}
Provides:   bundled(rubygem-uri) = %{bundler_uri_version}
BuildArch:  noarch

%description -n rubygem-bundler
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably.

%package -n rubygem-test-unit
Summary:    Unit testing framework for Ruby
Version:    %{test_unit_version}
License:    (Ruby or BSD) and (Ruby or BSD or Python) and (Ruby or BSD or LGPLv2+)
Requires:   ruby(release) ruby(rubygems) >= %{rubygems_version} rubygem(power_assert)
Provides:   rubygem(test-unit) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-test-unit
Test::Unit (test-unit) is unit testing framework for Ruby based on xUnit principles. writing tests, checking results
and automated testing are provided in Ruby.

%package -n rubygem-rexml
Summary:    An XML toolkit for Ruby
Version:    %{rexml_version}
License:    BSD
URL:        https://github.com/ruby/rexml
Requires:   ruby(release)
Requires:   ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(rexml) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-rexml
REXML was inspired by the Electric XML library for Java, which features an
easy-to-use API, small size, and speed. Hopefully, REXML, designed with the same
philosophy, has these same features. I've tried to keep the API as intuitive as
possible, and have followed the Ruby methodology for method naming and code
flow, rather than mirroring the Java API.

REXML supports both tree and stream document parsing. Stream parsing is faster
(about 1.5 times as fast). However, with stream parsing, you don't get access to
features such as XPath.

%package -n rubygem-rss
Summary:    Family of libraries that support various formats of XML "feeds"
Version:    %{rss_version}
License:    BSD
URL:        https://github.com/ruby/rss
Requires:   ruby(release)
Requires:   ruby(rubygems) >= %{rubygems_version}
Provides:   rubygem(rss) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-rss
Really Simple Syndication (RSS) is a family of formats that describe 'feeds',
specially constructed XML documents that allow an interested person to subscribe
and receive updates from a particular web service. This library provides tooling
to read and create these feeds.

%package -n rubygem-typeprof
Summary:    TypeProf is a type analysis tool for Ruby code based on abstract interpretation
Version:    %{typeprof_version}
License:    MIT
URL:        https://github.com/ruby/typeprof
Requires:   ruby(release)
Requires:   ruby(rubygems) >= %{rubygems_version}
Requires:   rubygem(rbs) >= %{rbs_version}
Provides:   rubygem(typeprof) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-typeprof
TypeProf performs a type analysis of non-annotated Ruby code.
It abstractly executes input Ruby code in a level of types instead of values,
gathers what types are passed to and returned by methods, and prints the
analysis result in RBS format, a standard type description format for Ruby
3.0.

%prep
%autosetup -n ruby-%{ruby_version} -p1

rm -rf ext/psych/yaml
rm -rf ext/fiddle/libffi*

cp -a %{SOURCE3} .

%build
autoconf

%configure --with-rubylibprefix='%{ruby_libdir}' --with-archlibdir='%{_libdir}' --with-rubyarchprefix='%{ruby_libarchdir}' \
        --with-sitedir='%{ruby_sitelibdir}' --with-sitearchdir='%{ruby_sitearchdir}' --with-vendordir='%{ruby_vendorlibdir}' \
        --with-vendorarchdir='%{ruby_vendorarchdir}' --with-rubyhdrdir='%{_includedir}' -with-rubyarchhdrdir='%{_includedir}' \
        --with-sitearchhdrdir='$(sitehdrdir)/$(arch)' --with-vendorarchhdrdir='$(vendorhdrdir)/$(arch)' \
        --with-rubygemsdir='%{_datadir}/rubygems' --with-ruby-pc='%{name}.pc' --with-compress-debug-sections=no --disable-rpath \
        --enable-shared --with-ruby-version='' --enable-multiarch \


%make_build COPY="cp -p" Q=

%install
%make_install

sed -i 's/Version: \${ruby_version}/Version: %{ruby_version}/' %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

# Kill bundled certificates, as they should be part of ca-certificates.
for cert in \
  rubygems.org/GlobalSignRootCA.pem \
  rubygems.org/GlobalSignRootCA_R3.pem
do
  rm %{buildroot}%{_datadir}/rubygems/rubygems/ssl_certs/$cert
  rm -d $(dirname %{buildroot}%{_datadir}/rubygems/rubygems/ssl_certs/$cert) || :
done

test ! "$(ls -A  %{buildroot}%{_datadir}/rubygems/rubygems/ssl_certs/ 2>/dev/null)"

install -d %{buildroot}%{_rpmconfigdir}/macros.d
install -m 644 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/macros.d/macros.ruby
install -m 644 %{SOURCE5} %{buildroot}%{_rpmconfigdir}/macros.d/macros.rubygems
sed -i "s/%%{name}/%{name}/" %{buildroot}%{_rpmconfigdir}/macros.d/macros.ruby
sed -i "s/%%{name}/%{name}/" %{buildroot}%{_rpmconfigdir}/macros.d/macros.rubygems

install -d %{buildroot}%{_rpmconfigdir}/fileattrs
install -m 644 %{SOURCE8} %{buildroot}%{_rpmconfigdir}/fileattrs
install -m 755 %{SOURCE9} %{buildroot}%{_rpmconfigdir}
install -m 755 %{SOURCE10} %{buildroot}%{_rpmconfigdir}
install -m 755 %{SOURCE11} %{buildroot}%{_rpmconfigdir}

install -d %{buildroot}%{_datadir}/rubygems/rubygems/defaults
cp %{SOURCE1} %{buildroot}%{_datadir}/rubygems/rubygems/defaults
if [ -d %{buildroot}%{ruby_libdir}/gems ]; then
  mv %{buildroot}%{ruby_libdir}/gems %{buildroot}%{gem_dir}
fi

install -d %{buildroot}%{_exec_prefix}/lib{,64}/gems/%{name}
install -d %{buildroot}%{gem_dir}/gems/rdoc-%{rdoc_version}/lib

mv %{buildroot}%{ruby_libdir}/rdoc* %{buildroot}%{gem_dir}/gems/rdoc-%{rdoc_version}/lib
mv %{buildroot}%{gem_dir}/specifications/default/rdoc-%{rdoc_version}.gemspec %{buildroot}%{gem_dir}/specifications

install -d %{buildroot}%{gem_dir}/gems/bigdecimal-%{bigdecimal_version}/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/bigdecimal-%{bigdecimal_version}
mv %{buildroot}%{ruby_libdir}/bigdecimal %{buildroot}%{gem_dir}/gems/bigdecimal-%{bigdecimal_version}/lib
mv %{buildroot}%{ruby_libarchdir}/bigdecimal.so %{buildroot}%{_libdir}/gems/%{name}/bigdecimal-%{bigdecimal_version}
mv %{buildroot}%{gem_dir}/specifications/default/bigdecimal-%{bigdecimal_version}.gemspec %{buildroot}%{gem_dir}/specifications
ln -s %{gem_dir}/gems/bigdecimal-%{bigdecimal_version}/lib/bigdecimal %{buildroot}%{ruby_libdir}/bigdecimal
ln -s %{_libdir}/gems/%{name}/bigdecimal-%{bigdecimal_version}/bigdecimal.so %{buildroot}%{ruby_libarchdir}/bigdecimal.so

install -d %{buildroot}%{gem_dir}/gems/io-console-%{io_console_version}/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/io-console-%{io_console_version}/io
mv %{buildroot}%{ruby_libdir}/io %{buildroot}%{gem_dir}/gems/io-console-%{io_console_version}/lib
mv %{buildroot}%{ruby_libarchdir}/io/console.so %{buildroot}%{_libdir}/gems/%{name}/io-console-%{io_console_version}/io
mv %{buildroot}%{gem_dir}/specifications/default/io-console-%{io_console_version}.gemspec %{buildroot}%{gem_dir}/specifications
ln -s %{gem_dir}/gems/io-console-%{io_console_version}/lib/io %{buildroot}%{ruby_libdir}/io
ln -s %{_libdir}/gems/%{name}/io-console-%{io_console_version}/io/console.so %{buildroot}%{ruby_libarchdir}/io/console.so

install -d %{buildroot}%{gem_dir}/gems/json-%{json_version}/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/json-%{json_version}
mv %{buildroot}%{ruby_libdir}/json* %{buildroot}%{gem_dir}/gems/json-%{json_version}/lib
mv %{buildroot}%{ruby_libarchdir}/json/ %{buildroot}%{_libdir}/gems/%{name}/json-%{json_version}/
mv %{buildroot}%{gem_dir}/specifications/default/json-%{json_version}.gemspec %{buildroot}%{gem_dir}/specifications
ln -s %{gem_dir}/gems/json-%{json_version}/lib/json.rb %{buildroot}%{ruby_libdir}/json.rb
ln -s %{gem_dir}/gems/json-%{json_version}/lib/json %{buildroot}%{ruby_libdir}/json
ln -s %{_libdir}/gems/%{name}/json-%{json_version}/json/ %{buildroot}%{ruby_libarchdir}/json

install -d %{buildroot}%{gem_dir}/gems/openssl-%{openssl_version}/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/openssl-%{openssl_version}
mv %{buildroot}%{ruby_libdir}/openssl* %{buildroot}%{gem_dir}/gems/openssl-%{openssl_version}/lib
mv %{buildroot}%{ruby_libarchdir}/openssl.so %{buildroot}%{_libdir}/gems/%{name}/openssl-%{openssl_version}/
mv %{buildroot}%{gem_dir}/specifications/default/openssl-%{openssl_version}.gemspec %{buildroot}%{gem_dir}/specifications

install -d %{buildroot}%{ruby_libdir}/openssl
find %{buildroot}%{gem_dir}/gems/openssl-%{openssl_version}/lib/openssl -maxdepth 1 -type f -exec \
  sh -c 'ln -s %{gem_dir}/gems/openssl-%{openssl_version}/lib/openssl/`basename {}` %{buildroot}%{ruby_libdir}/openssl' \;
ln -s %{gem_dir}/gems/openssl-%{openssl_version}/lib/openssl.rb %{buildroot}%{ruby_libdir}/openssl.rb
ln -s %{_libdir}/gems/%{name}/openssl-%{openssl_version}/openssl.so %{buildroot}%{ruby_libarchdir}/openssl.so

install -d %{buildroot}%{gem_dir}/gems/psych-%{psych_version}/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/psych-%{psych_version}
mv %{buildroot}%{ruby_libdir}/psych* %{buildroot}%{gem_dir}/gems/psych-%{psych_version}/lib
mv %{buildroot}%{ruby_libarchdir}/psych.so %{buildroot}%{_libdir}/gems/%{name}/psych-%{psych_version}/
mv %{buildroot}%{gem_dir}/specifications/default/psych-%{psych_version}.gemspec %{buildroot}%{gem_dir}/specifications
ln -s %{gem_dir}/gems/psych-%{psych_version}/lib/psych %{buildroot}%{ruby_libdir}/psych
ln -s %{gem_dir}/gems/psych-%{psych_version}/lib/psych.rb %{buildroot}%{ruby_libdir}/psych.rb
ln -s %{_libdir}/gems/%{name}/psych-%{psych_version}/psych.so %{buildroot}%{ruby_libarchdir}/psych.so

find %{buildroot}%{gem_dir}/extensions/*-%{_target_os}/%{version}/* -maxdepth 0 \
  -exec mv '{}' %{buildroot}%{_libdir}/gems/%{name}/ \; || echo "No gem binary extensions to move."

sed -i '/^end$/ i\
  s.extensions = ["json/ext/parser.so", "json/ext/generator.so"]' %{buildroot}%{gem_dir}/specifications/json-%{json_version}.gemspec

mv %{buildroot}%{gem_dir}/gems/rake-%{rake_version}/doc/rake.1 %{buildroot}%{_mandir}/man1

install -d %{buildroot}%{_datadir}/systemtap/tapset
sed -e "s|@LIBRARY_PATH@|%(echo %{_libdir} | sed 's/64//')*/libruby.so.3.0|" \
  %{SOURCE2} > %{buildroot}%{_datadir}/systemtap/tapset/libruby.so.3.0.stp

sed -i -r "s|( \*.*\*)\/(.*)|\1\\\/\2|" %{buildroot}%{_datadir}/systemtap/tapset/libruby.so.3.0.stp

find doc -maxdepth 1 -type f ! -name '.*' ! -name '*.ja*' > .ruby-doc.en
echo 'doc/images' >> .ruby-doc.en
echo 'doc/syntax' >> .ruby-doc.en

find doc -maxdepth 1 -type f -name '*.ja*' > .ruby-doc.ja
echo 'doc/irb' >> .ruby-doc.ja
echo 'doc/pty' >> .ruby-doc.ja

sed -i 's/^/%doc /' .ruby-doc.*
sed -i 's/^/%lang(ja) /' .ruby-doc.ja

%check

[ "`make runruby TESTRUN_SCRIPT='bin/gem -v' | tail -1`" == '%{rubygems_version}' ]

[ "`make runruby TESTRUN_SCRIPT=\"-e \\\" module Gem; module Resolver; end; end; \
  require 'rubygems/resolver/molinillo/lib/molinillo/gem_metadata'; \
  puts Gem::Resolver::Molinillo::VERSION\\\"\" | tail -1`" == '%{rubygems_molinillo_version}' ]

touch abrt.rb

make runruby TESTRUN_SCRIPT="--enable-gems %{SOURCE12}"
make runruby TESTRUN_SCRIPT=%{SOURCE13}

%files
%license BSDL COPYING GPL LEGAL
%doc README.md 
%lang(ja) %license COPYING.ja

%{_bindir}/{erb,ruby}

%dir %{ruby_vendorlibdir}
%dir %{ruby_vendorarchdir}
%dir %{ruby_libdir}
%{ruby_libdir}/{*.rb,cgi,digest,drb,fiddle,forwardable,matrix,net,optparse,racc,rexml}
%{ruby_libdir}/{rinda,ripper,rss,shell,syslog,unicode_normalize,uri,webrick,yaml}

%{_libdir}/libruby.so.*
%dir %{ruby_libarchdir}

%dir %{ruby_libarchdir}/digest
%{ruby_libarchdir}/digest/{bubblebabble.so,md5.so,rmd160.so,sha1.so,sha2.so}

%dir %{ruby_libarchdir}/enc
%{ruby_libarchdir}/enc/*.so

%dir %{ruby_libarchdir}/enc/trans
%{ruby_libarchdir}/enc/trans/*.so

%dir %{ruby_libarchdir}/cgi
%{ruby_libarchdir}/cgi/escape.so

%dir %{ruby_libarchdir}/io
%{ruby_libarchdir}/io/{nonblock.so,wait.so}

%dir %{ruby_libarchdir}/racc
%{ruby_libarchdir}/racc/cparse.so

%dir %{ruby_libarchdir}/rbconfig
%{ruby_libarchdir}/rbconfig.rb
%{ruby_libarchdir}/rbconfig/sizeof.so

%{ruby_libarchdir}/{continuation.so,coverage.so,date_core.so,dbm.so,monitor.so}
%{ruby_libarchdir}/{etc.so,fcntl.so,fiber.so,fiddle.so,gdbm.so,digest.so,nkf.so,objspace.so,pathname.so,pty.so}
%{ruby_libarchdir}/{readline.so,ripper.so,sdbm.so,socket.so,stringio.so,strscan.so,syslog.so,zlib.so}

%{_datadir}/systemtap

%exclude %{ruby_sitelibdir}
%exclude %{ruby_sitearchdir}
%exclude %{ruby_libdir}/irb.rb
%exclude %{ruby_libdir}/json.rb
%exclude %{ruby_libdir}/openssl.rb
%exclude %{ruby_libdir}/psych.rb
%exclude %{ruby_libdir}/irb

%{_bindir}/racc
%{gem_dir}/gems/erb-2.2.0/libexec/erb
%{gem_dir}/gems/irb-1.3.5/exe/irb
%{gem_dir}/gems/racc-1.5.2/bin/racc
%{ruby_libdir}/benchmark/version.rb
%{ruby_libdir}/csv/core_ext/array.rb
%{ruby_libdir}/csv/core_ext/string.rb
%{ruby_libdir}/csv/delete_suffix.rb
%{ruby_libdir}/csv/fields_converter.rb
%{ruby_libdir}/csv/match_p.rb
%{ruby_libdir}/csv/parser.rb
%{ruby_libdir}/csv/row.rb
%{ruby_libdir}/csv/table.rb
%{ruby_libdir}/csv/version.rb
%{ruby_libdir}/csv/writer.rb
%{ruby_libdir}/logger/errors.rb
%{ruby_libdir}/logger/formatter.rb
%{ruby_libdir}/logger/log_device.rb
%{ruby_libdir}/logger/period.rb
%{ruby_libdir}/logger/severity.rb
%{ruby_libdir}/logger/version.rb
%{ruby_libdir}/reline/ansi.rb
%{ruby_libdir}/reline/config.rb
%{ruby_libdir}/reline/general_io.rb
%{ruby_libdir}/reline/history.rb
%{ruby_libdir}/reline/key_actor.rb
%{ruby_libdir}/reline/key_actor/base.rb
%{ruby_libdir}/reline/key_actor/emacs.rb
%{ruby_libdir}/reline/key_actor/vi_command.rb
%{ruby_libdir}/reline/key_actor/vi_insert.rb
%{ruby_libdir}/reline/key_stroke.rb
%{ruby_libdir}/reline/kill_ring.rb
%{ruby_libdir}/reline/line_editor.rb
%{ruby_libdir}/reline/unicode.rb
%{ruby_libdir}/reline/unicode/east_asian_width.rb
%{ruby_libdir}/reline/version.rb
%{ruby_libdir}/reline/windows.rb
%{ruby_libdir}/set/sorted_set.rb

%files devel
%license BSDL COPYING GPL LEGAL
%lang(ja) %license COPYING.ja

%{_rpmconfigdir}/macros.d/macros.ruby

%{_includedir}/*
%{_libdir}/libruby.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n rubygems
%{_bindir}/gem
%dir %{_datadir}/rubygems
%{_datadir}/rubygems/rubygems
%{_datadir}/rubygems/rubygems.rb

%dir %{gem_dir}
%dir %{gem_dir}/build_info
%dir %{gem_dir}/cache
%dir %{gem_dir}/doc
%dir %{gem_dir}/extensions
%dir %{gem_dir}/gems
%dir %{gem_dir}/specifications
%dir %{gem_dir}/specifications/default
%dir %{_exec_prefix}/lib*/gems
%dir %{_exec_prefix}/lib*/gems/ruby

%exclude %{gem_dir}/cache/*

%{gem_dir}/specifications/default/*

%files -n rubygems-devel
%{_rpmconfigdir}/macros.d/macros.rubygems
%{_rpmconfigdir}/fileattrs/rubygems.attr
%{_rpmconfigdir}/{rubygems.req,rubygems.prov,rubygems.con}

%files -n rubygem-rake
%{_bindir}/rake
%{gem_dir}/gems/rake-13.0.3
%{gem_dir}/specifications/rake-13.0.3.gemspec

%files -n rubygem-rbs
%{_bindir}/rbs
%dir %{gem_dir}/gems/rbs-%{rbs_version}
%exclude %{gem_dir}/gems/rbs-%{rbs_version}/.*
%license %{gem_dir}/gems/rbs-%{rbs_version}/BSDL
%doc %{gem_dir}/gems/rbs-%{rbs_version}/CHANGELOG.md
%license %{gem_dir}/gems/rbs-%{rbs_version}/COPYING
%{gem_dir}/gems/rbs-%{rbs_version}/Gemfile
%doc %{gem_dir}/gems/rbs-%{rbs_version}/README.md
%{gem_dir}/gems/rbs-%{rbs_version}/Rakefile
%{gem_dir}/gems/rbs-%{rbs_version}/Steepfile
%{gem_dir}/gems/rbs-%{rbs_version}/core
%doc %{gem_dir}/gems/rbs-%{rbs_version}/docs
%{gem_dir}/gems/rbs-%{rbs_version}/exe
%{gem_dir}/gems/rbs-%{rbs_version}/goodcheck.yml
%{gem_dir}/gems/rbs-%{rbs_version}/lib
%{gem_dir}/gems/rbs-%{rbs_version}/schema
%{gem_dir}/gems/rbs-%{rbs_version}/sig
%{gem_dir}/gems/rbs-%{rbs_version}/stdlib
%{gem_dir}/gems/rbs-%{rbs_version}/steep
%{gem_dir}/specifications/rbs-%{rbs_version}.gemspec

%files irb
%{_bindir}/irb
%{ruby_libdir}/{irb.rb,irb}

%files -n rubygem-rdoc
%{_bindir}/{rdoc,ri}
%{gem_dir}/gems/rdoc-%{rdoc_version}
%{gem_dir}/specifications/rdoc-%{rdoc_version}.gemspec

%files help -f .ruby-doc.en -f .ruby-doc.ja
%doc README.md ChangeLog ruby-exercise.stp
%{_datadir}/ri
%{_mandir}/man1/ri*
%{_mandir}/man1/erb*
%{_mandir}/man1/irb.1*
%{_mandir}/man1/rake.1*
%{_mandir}/man1/ruby*

%files -n rubygem-bigdecimal
%{ruby_libdir}/bigdecimal
%{ruby_libarchdir}/bigdecimal.so
%{_libdir}/gems/%{name}/bigdecimal-3.0.0
%{gem_dir}/gems/bigdecimal-3.0.0
%{gem_dir}/specifications/bigdecimal-3.0.0.gemspec

%files -n rubygem-did_you_mean
%{ruby_libdir}/did_you_mean/core_ext/name_error.rb
%{ruby_libdir}/did_you_mean/experimental.rb
%{ruby_libdir}/did_you_mean/formatters/plain_formatter.rb
%{ruby_libdir}/did_you_mean/formatters/verbose_formatter.rb
%{ruby_libdir}/did_you_mean/jaro_winkler.rb
%{ruby_libdir}/did_you_mean/levenshtein.rb
%{ruby_libdir}/did_you_mean/spell_checker.rb
%{ruby_libdir}/did_you_mean/spell_checkers/key_error_checker.rb
%{ruby_libdir}/did_you_mean/spell_checkers/method_name_checker.rb
%{ruby_libdir}/did_you_mean/spell_checkers/name_error_checkers.rb
%{ruby_libdir}/did_you_mean/spell_checkers/name_error_checkers/class_name_checker.rb
%{ruby_libdir}/did_you_mean/spell_checkers/name_error_checkers/variable_name_checker.rb
%{ruby_libdir}/did_you_mean/spell_checkers/null_checker.rb
%{ruby_libdir}/did_you_mean/spell_checkers/require_path_checker.rb
%{ruby_libdir}/did_you_mean/tree_spell_checker.rb
%{ruby_libdir}/did_you_mean/verbose.rb
%{ruby_libdir}/did_you_mean/version.rb

%files -n rubygem-io-console
%{ruby_libdir}/io
%{ruby_libarchdir}/io/console.so
%{_libdir}/gems/%{name}/io-console-%{io_console_version}
%{gem_dir}/gems/io-console-%{io_console_version}
%{gem_dir}/specifications/io-console-%{io_console_version}.gemspec

%files -n rubygem-json
%{ruby_libdir}/json*
%{ruby_libarchdir}/json*
%{_libdir}/gems/%{name}/json-%{json_version}
%{gem_dir}/gems/json-%{json_version}
%{gem_dir}/specifications/json-%{json_version}.gemspec

%files -n rubygem-minitest
%{gem_dir}/gems/minitest-%{minitest_version}
%{gem_dir}/specifications/minitest-%{minitest_version}.gemspec
%exclude %{gem_dir}/gems/minitest-%{minitest_version}/.*

%files -n rubygem-openssl
%{ruby_libdir}/openssl
%{ruby_libdir}/openssl.rb
%{ruby_libarchdir}/openssl.so
%{_libdir}/gems/%{name}/openssl-%{openssl_version}
%{gem_dir}/gems/openssl-%{openssl_version}
%{gem_dir}/specifications/openssl-%{openssl_version}.gemspec

%files -n rubygem-power_assert
%{gem_dir}/gems/power_assert-%{power_assert_version}
%{gem_dir}/specifications/power_assert-%{power_assert_version}.gemspec
%exclude %{gem_dir}/gems/power_assert-%{power_assert_version}/.*

%files -n rubygem-psych
%{ruby_libdir}/psych
%{ruby_libdir}/psych.rb
%{ruby_libarchdir}/psych.so
%{_libdir}/gems/%{name}/psych-%{psych_version}
%{gem_dir}/gems/psych-%{psych_version}
%{gem_dir}/specifications/psych-%{psych_version}.gemspec

%files -n rubygem-bundler
%{_bindir}/bundle
%{_bindir}/bundler
%{gem_dir}/gems/bundler-%{bundler_version}
%{ruby_libdir}/bundler/build_metadata.rb
%{ruby_libdir}/bundler/capistrano.rb
%{ruby_libdir}/bundler/cli.rb
%{ruby_libdir}/bundler/cli/add.rb
%{ruby_libdir}/bundler/cli/binstubs.rb
%{ruby_libdir}/bundler/cli/cache.rb
%{ruby_libdir}/bundler/cli/check.rb
%{ruby_libdir}/bundler/cli/clean.rb
%{ruby_libdir}/bundler/cli/common.rb
%{ruby_libdir}/bundler/cli/config.rb
%{ruby_libdir}/bundler/cli/console.rb
%{ruby_libdir}/bundler/cli/doctor.rb
%{ruby_libdir}/bundler/cli/exec.rb
%{ruby_libdir}/bundler/cli/fund.rb
%{ruby_libdir}/bundler/cli/gem.rb
%{ruby_libdir}/bundler/cli/info.rb
%{ruby_libdir}/bundler/cli/init.rb
%{ruby_libdir}/bundler/cli/inject.rb
%{ruby_libdir}/bundler/cli/install.rb
%{ruby_libdir}/bundler/cli/issue.rb
%{ruby_libdir}/bundler/cli/list.rb
%{ruby_libdir}/bundler/cli/lock.rb
%{ruby_libdir}/bundler/cli/open.rb
%{ruby_libdir}/bundler/cli/outdated.rb
%{ruby_libdir}/bundler/cli/platform.rb
%{ruby_libdir}/bundler/cli/plugin.rb
%{ruby_libdir}/bundler/cli/pristine.rb
%{ruby_libdir}/bundler/cli/remove.rb
%{ruby_libdir}/bundler/cli/show.rb
%{ruby_libdir}/bundler/cli/update.rb
%{ruby_libdir}/bundler/cli/viz.rb
%{ruby_libdir}/bundler/compact_index_client.rb
%{ruby_libdir}/bundler/compact_index_client/cache.rb
%{ruby_libdir}/bundler/compact_index_client/gem_parser.rb
%{ruby_libdir}/bundler/compact_index_client/updater.rb
%{ruby_libdir}/bundler/constants.rb
%{ruby_libdir}/bundler/current_ruby.rb
%{ruby_libdir}/bundler/definition.rb
%{ruby_libdir}/bundler/dep_proxy.rb
%{ruby_libdir}/bundler/dependency.rb
%{ruby_libdir}/bundler/deployment.rb
%{ruby_libdir}/bundler/deprecate.rb
%{ruby_libdir}/bundler/digest.rb
%{ruby_libdir}/bundler/dsl.rb
%{ruby_libdir}/bundler/endpoint_specification.rb
%{ruby_libdir}/bundler/env.rb
%{ruby_libdir}/bundler/environment_preserver.rb
%{ruby_libdir}/bundler/errors.rb
%{ruby_libdir}/bundler/feature_flag.rb
%{ruby_libdir}/bundler/fetcher.rb
%{ruby_libdir}/bundler/fetcher/base.rb
%{ruby_libdir}/bundler/fetcher/compact_index.rb
%{ruby_libdir}/bundler/fetcher/dependency.rb
%{ruby_libdir}/bundler/fetcher/downloader.rb
%{ruby_libdir}/bundler/fetcher/index.rb
%{ruby_libdir}/bundler/friendly_errors.rb
%{ruby_libdir}/bundler/gem_helper.rb
%{ruby_libdir}/bundler/gem_helpers.rb
%{ruby_libdir}/bundler/gem_tasks.rb
%{ruby_libdir}/bundler/gem_version_promoter.rb
%{ruby_libdir}/bundler/gemdeps.rb
%{ruby_libdir}/bundler/graph.rb
%{ruby_libdir}/bundler/index.rb
%{ruby_libdir}/bundler/injector.rb
%{ruby_libdir}/bundler/inline.rb
%{ruby_libdir}/bundler/installer.rb
%{ruby_libdir}/bundler/installer/gem_installer.rb
%{ruby_libdir}/bundler/installer/parallel_installer.rb
%{ruby_libdir}/bundler/installer/standalone.rb
%{ruby_libdir}/bundler/lazy_specification.rb
%{ruby_libdir}/bundler/lockfile_generator.rb
%{ruby_libdir}/bundler/lockfile_parser.rb
%{ruby_libdir}/bundler/man/bundle-add.1
%{ruby_libdir}/bundler/man/bundle-add.1.ronn
%{ruby_libdir}/bundler/man/bundle-binstubs.1
%{ruby_libdir}/bundler/man/bundle-binstubs.1.ronn
%{ruby_libdir}/bundler/man/bundle-cache.1
%{ruby_libdir}/bundler/man/bundle-cache.1.ronn
%{ruby_libdir}/bundler/man/bundle-check.1
%{ruby_libdir}/bundler/man/bundle-check.1.ronn
%{ruby_libdir}/bundler/man/bundle-clean.1
%{ruby_libdir}/bundler/man/bundle-clean.1.ronn
%{ruby_libdir}/bundler/man/bundle-config.1
%{ruby_libdir}/bundler/man/bundle-config.1.ronn
%{ruby_libdir}/bundler/man/bundle-doctor.1
%{ruby_libdir}/bundler/man/bundle-doctor.1.ronn
%{ruby_libdir}/bundler/man/bundle-exec.1
%{ruby_libdir}/bundler/man/bundle-exec.1.ronn
%{ruby_libdir}/bundler/man/bundle-gem.1
%{ruby_libdir}/bundler/man/bundle-gem.1.ronn
%{ruby_libdir}/bundler/man/bundle-info.1
%{ruby_libdir}/bundler/man/bundle-info.1.ronn
%{ruby_libdir}/bundler/man/bundle-init.1
%{ruby_libdir}/bundler/man/bundle-init.1.ronn
%{ruby_libdir}/bundler/man/bundle-inject.1
%{ruby_libdir}/bundler/man/bundle-inject.1.ronn
%{ruby_libdir}/bundler/man/bundle-install.1
%{ruby_libdir}/bundler/man/bundle-install.1.ronn
%{ruby_libdir}/bundler/man/bundle-list.1
%{ruby_libdir}/bundler/man/bundle-list.1.ronn
%{ruby_libdir}/bundler/man/bundle-lock.1
%{ruby_libdir}/bundler/man/bundle-lock.1.ronn
%{ruby_libdir}/bundler/man/bundle-open.1
%{ruby_libdir}/bundler/man/bundle-open.1.ronn
%{ruby_libdir}/bundler/man/bundle-outdated.1
%{ruby_libdir}/bundler/man/bundle-outdated.1.ronn
%{ruby_libdir}/bundler/man/bundle-platform.1
%{ruby_libdir}/bundler/man/bundle-platform.1.ronn
%{ruby_libdir}/bundler/man/bundle-pristine.1
%{ruby_libdir}/bundler/man/bundle-pristine.1.ronn
%{ruby_libdir}/bundler/man/bundle-remove.1
%{ruby_libdir}/bundler/man/bundle-remove.1.ronn
%{ruby_libdir}/bundler/man/bundle-show.1
%{ruby_libdir}/bundler/man/bundle-show.1.ronn
%{ruby_libdir}/bundler/man/bundle-update.1
%{ruby_libdir}/bundler/man/bundle-update.1.ronn
%{ruby_libdir}/bundler/man/bundle-viz.1
%{ruby_libdir}/bundler/man/bundle-viz.1.ronn
%{ruby_libdir}/bundler/man/bundle.1
%{ruby_libdir}/bundler/man/bundle.1.ronn
%{ruby_libdir}/bundler/man/gemfile.5
%{ruby_libdir}/bundler/man/gemfile.5.ronn
%{ruby_libdir}/bundler/match_platform.rb
%{ruby_libdir}/bundler/mirror.rb
%{ruby_libdir}/bundler/plugin.rb
%{ruby_libdir}/bundler/plugin/api.rb
%{ruby_libdir}/bundler/plugin/api/source.rb
%{ruby_libdir}/bundler/plugin/dsl.rb
%{ruby_libdir}/bundler/plugin/events.rb
%{ruby_libdir}/bundler/plugin/index.rb
%{ruby_libdir}/bundler/plugin/installer.rb
%{ruby_libdir}/bundler/plugin/installer/git.rb
%{ruby_libdir}/bundler/plugin/installer/rubygems.rb
%{ruby_libdir}/bundler/plugin/source_list.rb
%{ruby_libdir}/bundler/process_lock.rb
%{ruby_libdir}/bundler/psyched_yaml.rb
%{ruby_libdir}/bundler/remote_specification.rb
%{ruby_libdir}/bundler/resolver.rb
%{ruby_libdir}/bundler/resolver/spec_group.rb
%{ruby_libdir}/bundler/retry.rb
%{ruby_libdir}/bundler/ruby_dsl.rb
%{ruby_libdir}/bundler/ruby_version.rb
%{ruby_libdir}/bundler/rubygems_ext.rb
%{ruby_libdir}/bundler/rubygems_gem_installer.rb
%{ruby_libdir}/bundler/rubygems_integration.rb
%{ruby_libdir}/bundler/runtime.rb
%{ruby_libdir}/bundler/settings.rb
%{ruby_libdir}/bundler/settings/validator.rb
%{ruby_libdir}/bundler/setup.rb
%{ruby_libdir}/bundler/shared_helpers.rb
%{ruby_libdir}/bundler/similarity_detector.rb
%{ruby_libdir}/bundler/source.rb
%{ruby_libdir}/bundler/source/gemspec.rb
%{ruby_libdir}/bundler/source/git.rb
%{ruby_libdir}/bundler/source/git/git_proxy.rb
%{ruby_libdir}/bundler/source/metadata.rb
%{ruby_libdir}/bundler/source/path.rb
%{ruby_libdir}/bundler/source/path/installer.rb
%{ruby_libdir}/bundler/source/rubygems.rb
%{ruby_libdir}/bundler/source/rubygems/remote.rb
%{ruby_libdir}/bundler/source/rubygems_aggregate.rb
%{ruby_libdir}/bundler/source_list.rb
%{ruby_libdir}/bundler/source_map.rb
%{ruby_libdir}/bundler/spec_set.rb
%{ruby_libdir}/bundler/stub_specification.rb
%{ruby_libdir}/bundler/templates/Executable
%{ruby_libdir}/bundler/templates/Executable.bundler
%{ruby_libdir}/bundler/templates/Executable.standalone
%{ruby_libdir}/bundler/templates/Gemfile
%{ruby_libdir}/bundler/templates/gems.rb
%{ruby_libdir}/bundler/templates/newgem/CHANGELOG.md.tt
%{ruby_libdir}/bundler/templates/newgem/CODE_OF_CONDUCT.md.tt
%{ruby_libdir}/bundler/templates/newgem/Gemfile.tt
%{ruby_libdir}/bundler/templates/newgem/LICENSE.txt.tt
%{ruby_libdir}/bundler/templates/newgem/README.md.tt
%{ruby_libdir}/bundler/templates/newgem/Rakefile.tt
%{ruby_libdir}/bundler/templates/newgem/bin/console.tt
%{ruby_libdir}/bundler/templates/newgem/bin/setup.tt
%{ruby_libdir}/bundler/templates/newgem/circleci/config.yml.tt
%{ruby_libdir}/bundler/templates/newgem/exe/newgem.tt
%{ruby_libdir}/bundler/templates/newgem/ext/newgem/extconf.rb.tt
%{ruby_libdir}/bundler/templates/newgem/ext/newgem/newgem.c.tt
%{ruby_libdir}/bundler/templates/newgem/ext/newgem/newgem.h.tt
%{ruby_libdir}/bundler/templates/newgem/github/workflows/main.yml.tt
%{ruby_libdir}/bundler/templates/newgem/gitignore.tt
%{ruby_libdir}/bundler/templates/newgem/gitlab-ci.yml.tt
%{ruby_libdir}/bundler/templates/newgem/lib/newgem.rb.tt
%{ruby_libdir}/bundler/templates/newgem/lib/newgem/version.rb.tt
%{ruby_libdir}/bundler/templates/newgem/newgem.gemspec.tt
%{ruby_libdir}/bundler/templates/newgem/rspec.tt
%{ruby_libdir}/bundler/templates/newgem/rubocop.yml.tt
%{ruby_libdir}/bundler/templates/newgem/spec/newgem_spec.rb.tt
%{ruby_libdir}/bundler/templates/newgem/spec/spec_helper.rb.tt
%{ruby_libdir}/bundler/templates/newgem/standard.yml.tt
%{ruby_libdir}/bundler/templates/newgem/test/minitest/newgem_test.rb.tt
%{ruby_libdir}/bundler/templates/newgem/test/minitest/test_helper.rb.tt
%{ruby_libdir}/bundler/templates/newgem/test/test-unit/newgem_test.rb.tt
%{ruby_libdir}/bundler/templates/newgem/test/test-unit/test_helper.rb.tt
%{ruby_libdir}/bundler/templates/newgem/travis.yml.tt
%{ruby_libdir}/bundler/ui.rb
%{ruby_libdir}/bundler/ui/rg_proxy.rb
%{ruby_libdir}/bundler/ui/shell.rb
%{ruby_libdir}/bundler/ui/silent.rb
%{ruby_libdir}/bundler/uri_credentials_filter.rb
%{ruby_libdir}/bundler/vendor/connection_pool/lib/connection_pool.rb
%{ruby_libdir}/bundler/vendor/connection_pool/lib/connection_pool/timed_stack.rb
%{ruby_libdir}/bundler/vendor/connection_pool/lib/connection_pool/version.rb
%{ruby_libdir}/bundler/vendor/connection_pool/lib/connection_pool/wrapper.rb
%{ruby_libdir}/bundler/vendor/fileutils/lib/fileutils.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/delegates/resolution_state.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/delegates/specification_provider.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph/action.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph/add_edge_no_circular.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph/add_vertex.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph/delete_edge.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph/detach_vertex_named.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph/log.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph/set_payload.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph/tag.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/dependency_graph/vertex.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/errors.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/gem_metadata.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/modules/specification_provider.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/modules/ui.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/resolution.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/resolver.rb
%{ruby_libdir}/bundler/vendor/molinillo/lib/molinillo/state.rb
%{ruby_libdir}/bundler/vendor/net-http-persistent/lib/net/http/persistent.rb
%{ruby_libdir}/bundler/vendor/net-http-persistent/lib/net/http/persistent/connection.rb
%{ruby_libdir}/bundler/vendor/net-http-persistent/lib/net/http/persistent/pool.rb
%{ruby_libdir}/bundler/vendor/net-http-persistent/lib/net/http/persistent/timed_stack_multi.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/actions.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/actions/create_file.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/actions/create_link.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/actions/directory.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/actions/empty_directory.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/actions/file_manipulation.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/actions/inject_into_file.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/base.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/command.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/core_ext/hash_with_indifferent_access.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/error.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/group.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/invocation.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/line_editor.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/line_editor/basic.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/line_editor/readline.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/nested_context.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/parser.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/parser/argument.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/parser/arguments.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/parser/option.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/parser/options.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/rake_compat.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/runner.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/shell.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/shell/basic.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/shell/color.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/shell/html.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/util.rb
%{ruby_libdir}/bundler/vendor/thor/lib/thor/version.rb
%{ruby_libdir}/bundler/vendor/tmpdir/lib/tmpdir.rb
%{ruby_libdir}/bundler/vendor/tsort/lib/tsort.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/common.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/file.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/ftp.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/generic.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/http.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/https.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/ldap.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/ldaps.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/mailto.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/rfc2396_parser.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/rfc3986_parser.rb
%{ruby_libdir}/bundler/vendor/uri/lib/uri/version.rb
%{ruby_libdir}/bundler/vendored_fileutils.rb
%{ruby_libdir}/bundler/vendored_molinillo.rb
%{ruby_libdir}/bundler/vendored_persistent.rb
%{ruby_libdir}/bundler/vendored_thor.rb
%{ruby_libdir}/bundler/vendored_tmpdir.rb
%{ruby_libdir}/bundler/vendored_tsort.rb
%{ruby_libdir}/bundler/vendored_uri.rb
%{ruby_libdir}/bundler/version.rb
%{ruby_libdir}/bundler/version_ranges.rb
%{ruby_libdir}/bundler/vlad.rb
%{ruby_libdir}/bundler/worker.rb
%{ruby_libdir}/bundler/yaml_serializer.rb

%files -n rubygem-test-unit
%{gem_dir}/gems/test-unit-%{test_unit_version}
%{gem_dir}/specifications/test-unit-%{test_unit_version}.gemspec

%files -n rubygem-rexml
%dir %{gem_dir}/gems/rexml-%{rexml_version}
%license %{gem_dir}/gems/rexml-%{rexml_version}/LICENSE.txt
%doc %{gem_dir}/gems/rexml-%{rexml_version}/NEWS.md
%doc %{gem_dir}/gems/rexml-%{rexml_version}/doc
%{gem_dir}/gems/rexml-%{rexml_version}/lib
%{gem_dir}/specifications/rexml-%{rexml_version}.gemspec
%doc %{gem_dir}/gems/rexml-%{rexml_version}/README.md

%files -n rubygem-rss
%dir %{gem_dir}/gems/rss-%{rss_version}
%exclude %{gem_dir}/gems/rss-%{rss_version}/.*
%license %{gem_dir}/gems/rss-%{rss_version}/LICENSE.txt
%doc %{gem_dir}/gems/rss-%{rss_version}/NEWS.md
%{gem_dir}/gems/rss-%{rss_version}/lib
%{gem_dir}/specifications/rss-%{rss_version}.gemspec
%doc %{gem_dir}/gems/rss-%{rss_version}/Gemfile
%doc %{gem_dir}/gems/rss-%{rss_version}/README.md
%doc %{gem_dir}/gems/rss-%{rss_version}/Rakefile
%doc %{gem_dir}/gems/rss-%{rss_version}/test

%files -n rubygem-typeprof
%dir %{gem_dir}/gems/typeprof-%{typeprof_version}
%{_bindir}/typeprof
%exclude %{gem_dir}/gems/typeprof-%{typeprof_version}/.*
%license %{gem_dir}/gems/typeprof-%{typeprof_version}/LICENSE
%{gem_dir}/gems/typeprof-%{typeprof_version}/exe
%{gem_dir}/gems/typeprof-%{typeprof_version}/lib
%doc %{gem_dir}/gems/typeprof-%{typeprof_version}/smoke
%doc %{gem_dir}/gems/typeprof-%{typeprof_version}/tools
%{gem_dir}/specifications/typeprof-%{typeprof_version}.gemspec
%doc %{gem_dir}/gems/typeprof-%{typeprof_version}/Gemfile*
%doc %{gem_dir}/gems/typeprof-%{typeprof_version}/README.md
%doc %{gem_dir}/gems/typeprof-%{typeprof_version}/Rakefile
%doc %{gem_dir}/gems/typeprof-%{typeprof_version}/doc
%lang(ja) %doc %{gem_dir}/gems/typeprof-%{typeprof_version}/doc/doc.ja.md
%doc %{gem_dir}/gems/typeprof-%{typeprof_version}/testbed

%changelog
* Thu Jan 06 2022 shangyibin <shangyibin1@huawei.com> - 3.0.3-2
- Delete libruby.so.2.5 file

* Fri Dec 31 2021 shangyibin <shangyibin1@huawei.com> - 3.0.3-1
- Upgrade to version 3.0.3

* Sat Jul 31 2021 shixuantong <shixuantong@huawei.com> - 2.5.8-114
- fix CVE-2021-31799 CVE-2021-31810 CVE-2021-32066

* Fri Apr 30 2021 Shinwell_Hu <huxinwei@huawei.com> - 2.5.8-113
- Upgrade bundled REXML gem to fix CVE-2021-28965, which is an XML
  round-trip vulnerability in REXML.

* Tue Apr 20 2021 shixuantong <shixuantong@huawei.com> - 2.5.8-112
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:change release number for rebuild

* Thu Nov 5 2020 wutao <wutao61@huawei.com> - 2.5.8-4
- fix CVE-2020-25613
- WEBrick,a simple HTTP server bundled with Ruby,had not
- checked the transfer-encoding header value rigorously.
- An attacker may potentially exploit this issue to bypass
- a reverse proxy,which may lead to an HTTP Request Smuggling
- attack.

* Fri Aug 7 2020 shixuantong <shixuantong@huawei.com> - 2.5.8-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix rdoc and ri command error problem

* Tue Aug 4 2020 shixuantong <shixuantong@huawei.com> - 2.5.8-2
- Type:NA
- ID:NA
- SUG:NA
- DESC:change package irb version

* Mon Jul 27 2020 shixuantong <shixuantong@huawei.com> - 2.5.8-1
- Type:NA
- ID:NA
- SUG:NA
- DESC:update to 2.5.8

*Wed Jul 08 2020 zhangjiapeng <zhangjiapeng9@huawei.com> - 2.5.1-107
- Type:N/A
- ID:N/A
- SUG:N/A
- DESC:modify patch information in spec file

* Mon Jun 22 2020 zhanghua <zhanghua40@huawei.com> - 2.5.1-106
- Type:cves
- ID:CVE-2020-10663
- SUG:restart
- DESC:fix CVE-2020-10663

* Thu May 07 2020 huanghaitao <huanghaitao@huawei.com> - 2.5.1-105
- Type:cves
- ID:CVE-2020-10933
- SUG:restart
- DESC:fix CVE-2020-10933

* Mon Feb 03 2020 openEuler Buildteam <buildteam@openeuler.org> - 2.5.1-104
- Type:cves
- ID:CVE-2019-16163 CVE-2019-19204 CVE-2019-16255 CVE-2019-19246
- SUG:N/A
- DESC:fix CVE-2019-16163CVE-2019-19204CVE-2019-16255CVE-2019-19246

* Mon Feb 03 2020 Yiru Wang <wangyiru1@huawei.com> - 2.5.1-103
- Type:cves
- ID:CVE-2019-16254
- SUG:N/A
- DESC:fix CVE-2019-16254

* Thu Jan 16 2020 fengbing <fengbing7@huawei.com> - 2.5.1-102
- Type:N/A
- ID:N/A
- SUG:N/A
- DESC:modify source0 in spec file

* Mon Dec 30 2019 lihao openEuler Buildteam <buildteam@openeuler.org> - 2.5.1-101
- Type:N/A
- ID:N/A
- SUG:N/A
- DESC:modify info in patch

* Wed Dec 25 2019 lihao <lihao129@huawei.com> - 2.5.1-100
- Type:cves
- ID:CVE-2019-15845 CVE-2019-16201
- SUG:N/A
- DESC:fix CVE-2019-15845 CVE-2019-16201

* Sat Nov 30 2019 fengbing <fengbing7@huawei.com> - 2.5.1-99
- Package init
