Name:      ruby
Version:   2.5.8
Release:   3
Summary:   Object-oriented scripting language interpreter
License:   (Ruby or BSD) and Public Domain and MIT and CC0 and zlib and UCD
URL:       https://www.ruby-lang.org/

Source0:   http://cache.ruby-lang.org/pub/ruby/2.5/%{name}-%{version}.tar.xz
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

%{?load:%{SOURCE4}}
%{?load:%{SOURCE5}}

Patch0001: ruby-2.3.0-ruby_version.patch
Patch0002: ruby-2.1.0-Prevent-duplicated-paths-when-empty-version-string-i.patch
Patch0003: ruby-2.1.0-Enable-configuration-of-archlibdir.patch
Patch0004: ruby-2.1.0-always-use-i386.patch
Patch0005: ruby-2.1.0-custom-rubygems-location.patch
Patch0006: ruby-1.9.3-mkmf-verbose.patch
Patch0007: ruby-2.1.0-Allow-to-specify-additional-preludes-by-configuratio.patch
Patch0008: ruby-2.2.3-Generate-preludes-using-miniruby.patch
Patch0009: ruby-2.3.1-Rely-on-ldd-to-detect-glibc.patch
Patch0010: ruby-2.5.0-Add-Gem.operating_system_defaults.patch
Patch0011: ruby-2.6.0-library-options-to-MAINLIBS.patch
Patch0012: ruby-2.5.1-Avoid-need-of-C++-compiler-to-pass-the-test-suite.patch

Patch0013: CVE-2019-19204.patch
Patch0014: CVE-2019-19246.patch
Patch0015: CVE-2019-16163.patch
Patch0016: CVE-2020-25613.patch

Provides:  %{name}-libs = %{version}-%{release}
Obsoletes: %{name}-libs < %{version}-%{release}

Provides:  ruby(runtime_executable) = %{version} ruby(release) = %{version} bundled(ccan-build_assert)
Provides:  bundled(ccan-check_type) bundled(ccan-container_of) bundled(ccan-list)
Obsoletes: ruby-tcltk < 2.4.0

Suggests:   rubypick
Recommends: ruby(rubygems) >= 2.7.6 rubygem(bigdecimal) >= 1.3.4
Recommends: rubygem(did_you_mean) >= 1.2.0 rubygem(openssl) >= 2.1.0
Requires:   %{name}-help = %{version}-%{release}
BuildRequires: autoconf gdbm-devel gmp-devel libffi-devel openssl-devel libyaml-devel readline-devel
BuildRequires: procps git gcc systemtap-sdt-devel cmake

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
Version:    2.7.6
License:    Ruby or MIT
Requires:   ruby(release) rubygem(openssl) >= 2.1.0 rubygem(psych) >= 3.0.2
Recommends: rubygem(rdoc) >= 6.0.1.1 rubygem(io-console) >= 0.4.6
Provides:   gem = %{version}-%{release} ruby(rubygems) = %{version}-%{release} bundled(rubygem-molinillo) = 0.5.7
BuildArch:  noarch

%description -n rubygems
The Ruby standard for publishing and managing third party libraries provided by RubyGems.

%package -n rubygems-devel
Summary:    For packaging RubyGems
Version:    2.7.6
License:    Ruby or MIT
Requires:   ruby(rubygems) = %{version}-%{release} rubygem(json) >= 2.1.0 rubygem(rdoc) >= 6.0.1.1
BuildArch:  noarch

%description -n rubygems-devel
Provide macros and development tools for packaging RubyGems.

%package -n rubygem-rake
Summary:    make-like utility base on ruby
Version:    12.3.0
License:    MIT
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rake = %{version}-%{release} rubygem(rake) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-rake
Rake is a Make-like program implemented in Ruby,Tasks and dependencies are specified in standard Ruby syntax.

%package irb
Summary:    The Interactive Ruby
Version:    2.5.8
Requires:   %{name}-libs = 2.5.8
Provides:   irb = %{version}-%{release} ruby(irb) = %{version}-%{release}
BuildArch:  noarch

%description irb
The irb is acronym for Interactive Ruby,It evaluates ruby expression from the terminal.

%package -n rubygem-rdoc
Summary:    Generate HTML and command-line documentation for Ruby projects
Version:    6.0.1.1
License:    GPLv2 and Ruby and MIT and OFL
Requires:   ruby(release) ruby(rubygems) >= 2.7.6 ruby(irb) = 2.5.8 rubygem(io-console) >= 0.4.6 rubygem(json) >= 2.1.0
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
Version:    1.3.4
License:    Ruby or BSD
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rubygem(bigdecimal) = %{version}-%{release}

%description -n rubygem-bigdecimal
BigDecimal provides similar support for very large or very accurate floating point numbers.

%package -n rubygem-did_you_mean
Summary:    "Did you mean?" experience in Ruby
Version:    1.2.0
License:    MIT
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rubygem(did_you_mean) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-did_you_mean
The error message will tell you the right one when you misspelled something.

%package -n rubygem-io-console
Summary:    Simple console utilizing library
Version:    0.4.6
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rubygem(io-console) = %{version}-%{release}

%description -n rubygem-io-console
IO / Console provides very simple and portable access to the console. It does not provide higher-level functions
such as curses and readline.

%package -n rubygem-json
Summary:    JSON implementation as a Ruby extension in C
Version:    2.1.0
License:    (Ruby or GPLv2) and UCD
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rubygem(json) = %{version}-%{release}

%description -n rubygem-json
According to RFC 4627,this package implements the JSON specification.

%package -n rubygem-minitest
Summary:    Provide complete testing facilities
Version:    5.10.3
License:    MIT
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
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
Version:    2.1.2
License:    Ruby or BSD
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rubygem(openssl) = %{version}-%{release}

%description -n rubygem-openssl
This package provides SSL、TLS and general purpose cryptography.

%package -n rubygem-power_assert
Summary:    Power Assert for Ruby
Version:    1.1.1
License:    Ruby or BSD
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rubygem(power_assert) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-power_assert
Power Assert displays each value of variables and method calls in expressions.This is very useful for testing,
it can indicate which value is incorrect when the condition is not met during testing.

%package -n rubygem-psych
Summary:    Ruby's libyaml wrapper
Version:    3.0.2
License:    MIT
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rubygem(psych) = %{version}-%{release}

%description -n rubygem-psych
Psych is a YAML parser and emitter. According to wrapping libyaml, Psych knows how to
serialize and de-serialize most Ruby objects to and from the YAML format.

%package -n rubygem-net-telnet
Summary:    Provides telnet client functionality
Version:    0.1.1
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rubygem(net-telnet) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-net-telnet
This package provides telnet client functionality.

%package -n rubygem-test-unit
Summary:    Unit testing framework for Ruby
Version:    3.2.7
License:    (Ruby or BSD) and (Ruby or BSD or Python) and (Ruby or BSD or LGPLv2+)
Requires:   ruby(release) ruby(rubygems) >= 2.7.6 rubygem(power_assert)
Provides:   rubygem(test-unit) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-test-unit
Test::Unit (test-unit) is unit testing framework for Ruby based on xUnit principles. writing tests, checking results
and automated testing are provided in Ruby.

%package -n rubygem-xmlrpc
Summary:    Lightweight protocol enables remote procedure calls over HTTP
Version:    0.3.0
License:    Ruby or BSD
Requires:   ruby(release) ruby(rubygems) >= 2.7.6
Provides:   rubygem(xmlrpc) = %{version}-%{release}
BuildArch:  noarch

%description -n rubygem-xmlrpc
This package is a lightweight protocol which can enable remote procedure calls over HTTP.

%prep
%autosetup -n ruby-2.5.8 -p1

rm -rf ext/psych/yaml
rm -rf ext/fiddle/libffi*

cp -a %{SOURCE3} .
cp -a %{SOURCE6} .

%build
autoconf

%configure --with-rubylibprefix='%{ruby_libdir}' --with-archlibdir='%{_libdir}' --with-rubyarchprefix='%{ruby_libarchdir}' \
        --with-sitedir='%{ruby_sitelibdir}' --with-sitearchdir='%{ruby_sitearchdir}' --with-vendordir='%{ruby_vendorlibdir}' \
        --with-vendorarchdir='%{ruby_vendorarchdir}' --with-rubyhdrdir='%{_includedir}' -with-rubyarchhdrdir='%{_includedir}' \
        --with-sitearchhdrdir='$(sitehdrdir)/$(arch)' --with-vendorarchhdrdir='$(vendorhdrdir)/$(arch)' \
        --with-rubygemsdir='%{_datadir}/rubygems' --with-ruby-pc='%{name}.pc' --with-compress-debug-sections=no --disable-rpath \
        --enable-shared --with-ruby-version='' --enable-multiarch --with-prelude=./abrt_prelude.rb \

%make_build COPY="cp -p" Q=

%install
%make_install

sed -i 's/Version: \${ruby_version}/Version: 2.5.8/' %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

for cert in rubygems.global.ssl.fastly.net/DigiCertHighAssuranceEVRootCA.pem \
  rubygems.org/AddTrustExternalCARoot.pem index.rubygems.org/GlobalSignRootCA.pem
do
  rm %{buildroot}%{_datadir}/rubygems/rubygems/ssl_certs/$cert
  rm -r $(dirname %{buildroot}%{_datadir}/rubygems/rubygems/ssl_certs/$cert)
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
mv %{buildroot}%{ruby_libdir}/gems %{buildroot}%{gem_dir}

install -d %{buildroot}%{_exec_prefix}/lib{,64}/gems/%{name}
install -d %{buildroot}%{gem_dir}/gems/rdoc-6.0.1.1/lib

mv %{buildroot}%{ruby_libdir}/rdoc* %{buildroot}%{gem_dir}/gems/rdoc-6.0.1.1/lib
mv %{buildroot}%{gem_dir}/specifications/default/rdoc-6.0.1.1.gemspec %{buildroot}%{gem_dir}/specifications

install -d %{buildroot}%{gem_dir}/gems/bigdecimal-1.3.4/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/bigdecimal-1.3.4
mv %{buildroot}%{ruby_libdir}/bigdecimal %{buildroot}%{gem_dir}/gems/bigdecimal-1.3.4/lib
mv %{buildroot}%{ruby_libarchdir}/bigdecimal.so %{buildroot}%{_libdir}/gems/%{name}/bigdecimal-1.3.4
mv %{buildroot}%{gem_dir}/specifications/default/bigdecimal-1.3.4.gemspec %{buildroot}%{gem_dir}/specifications
ln -s %{gem_dir}/gems/bigdecimal-1.3.4/lib/bigdecimal %{buildroot}%{ruby_libdir}/bigdecimal
ln -s %{_libdir}/gems/%{name}/bigdecimal-1.3.4/bigdecimal.so %{buildroot}%{ruby_libarchdir}/bigdecimal.so

install -d %{buildroot}%{gem_dir}/gems/io-console-0.4.6/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/io-console-0.4.6/io
mv %{buildroot}%{ruby_libdir}/io %{buildroot}%{gem_dir}/gems/io-console-0.4.6/lib
mv %{buildroot}%{ruby_libarchdir}/io/console.so %{buildroot}%{_libdir}/gems/%{name}/io-console-0.4.6/io
mv %{buildroot}%{gem_dir}/specifications/default/io-console-0.4.6.gemspec %{buildroot}%{gem_dir}/specifications
ln -s %{gem_dir}/gems/io-console-0.4.6/lib/io %{buildroot}%{ruby_libdir}/io
ln -s %{_libdir}/gems/%{name}/io-console-0.4.6/io/console.so %{buildroot}%{ruby_libarchdir}/io/console.so

install -d %{buildroot}%{gem_dir}/gems/json-2.1.0/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/json-2.1.0
mv %{buildroot}%{ruby_libdir}/json* %{buildroot}%{gem_dir}/gems/json-2.1.0/lib
mv %{buildroot}%{ruby_libarchdir}/json/ %{buildroot}%{_libdir}/gems/%{name}/json-2.1.0/
mv %{buildroot}%{gem_dir}/specifications/default/json-2.1.0.gemspec %{buildroot}%{gem_dir}/specifications
ln -s %{gem_dir}/gems/json-2.1.0/lib/json.rb %{buildroot}%{ruby_libdir}/json.rb
ln -s %{gem_dir}/gems/json-2.1.0/lib/json %{buildroot}%{ruby_libdir}/json
ln -s %{_libdir}/gems/%{name}/json-2.1.0/json/ %{buildroot}%{ruby_libarchdir}/json

install -d %{buildroot}%{gem_dir}/gems/openssl-2.1.2/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/openssl-2.1.2
mv %{buildroot}%{ruby_libdir}/openssl* %{buildroot}%{gem_dir}/gems/openssl-2.1.2/lib
mv %{buildroot}%{ruby_libarchdir}/openssl.so %{buildroot}%{_libdir}/gems/%{name}/openssl-2.1.2/
mv %{buildroot}%{gem_dir}/specifications/default/openssl-2.1.2.gemspec %{buildroot}%{gem_dir}/specifications

install -d %{buildroot}%{ruby_libdir}/openssl
find %{buildroot}%{gem_dir}/gems/openssl-2.1.2/lib/openssl -maxdepth 1 -type f -exec \
  sh -c 'ln -s %{gem_dir}/gems/openssl-2.1.2/lib/openssl/`basename {}` %{buildroot}%{ruby_libdir}/openssl' \;
ln -s %{gem_dir}/gems/openssl-2.1.2/lib/openssl.rb %{buildroot}%{ruby_libdir}/openssl.rb
ln -s %{_libdir}/gems/%{name}/openssl-2.1.2/openssl.so %{buildroot}%{ruby_libarchdir}/openssl.so

install -d %{buildroot}%{gem_dir}/gems/psych-3.0.2/lib
install -d %{buildroot}%{_libdir}/gems/%{name}/psych-3.0.2
mv %{buildroot}%{ruby_libdir}/psych* %{buildroot}%{gem_dir}/gems/psych-3.0.2/lib
mv %{buildroot}%{ruby_libarchdir}/psych.so %{buildroot}%{_libdir}/gems/%{name}/psych-3.0.2/
mv %{buildroot}%{gem_dir}/specifications/default/psych-3.0.2.gemspec %{buildroot}%{gem_dir}/specifications
ln -s %{gem_dir}/gems/psych-3.0.2/lib/psych %{buildroot}%{ruby_libdir}/psych
ln -s %{gem_dir}/gems/psych-3.0.2/lib/psych.rb %{buildroot}%{ruby_libdir}/psych.rb
ln -s %{_libdir}/gems/%{name}/psych-3.0.2/psych.so %{buildroot}%{ruby_libarchdir}/psych.so

find %{buildroot}%{gem_dir}/extensions/*-%{_target_os}/2.5.8/* -maxdepth 0 \
  -exec mv '{}' %{buildroot}%{_libdir}/gems/%{name}/ \; || echo "No gem binary extensions to move."

sed -i '/^end$/ i\
  s.extensions = ["json/ext/parser.so", "json/ext/generator.so"]' %{buildroot}%{gem_dir}/specifications/json-2.1.0.gemspec

mv %{buildroot}%{gem_dir}/gems/rake-12.3.3/doc/rake.1 %{buildroot}%{_mandir}/man1

install -d %{buildroot}%{_datadir}/systemtap/tapset
sed -e "s|@LIBRARY_PATH@|%(echo %{_libdir} | sed 's/64//')*/libruby.so.2.5|" \
  %{SOURCE2} > %{buildroot}%{_datadir}/systemtap/tapset/libruby.so.2.5.stp

sed -i -r "s|( \*.*\*)\/(.*)|\1\\\/\2|" %{buildroot}%{_datadir}/systemtap/tapset/libruby.so.2.5.stp

find doc -maxdepth 1 -type f ! -name '.*' ! -name '*.ja*' > .ruby-doc.en
echo 'doc/images' >> .ruby-doc.en
echo 'doc/syntax' >> .ruby-doc.en

find doc -maxdepth 1 -type f -name '*.ja*' > .ruby-doc.ja
echo 'doc/irb' >> .ruby-doc.ja
echo 'doc/pty' >> .ruby-doc.ja

sed -i 's/^/%doc /' .ruby-doc.*
sed -i 's/^/%lang(ja) /' .ruby-doc.ja

%check

[ "`make runruby TESTRUN_SCRIPT='bin/gem -v' | tail -1`" == '2.7.6.2' ]

[ "`make runruby TESTRUN_SCRIPT=\"-e \\\" module Gem; module Resolver; end; end; \
  require 'rubygems/resolver/molinillo/lib/molinillo/gem_metadata'; \
  puts Gem::Resolver::Molinillo::VERSION\\\"\" | tail -1`" == '0.5.7' ]

touch abrt.rb

make runruby TESTRUN_SCRIPT="--enable-gems %{SOURCE12}"
make runruby TESTRUN_SCRIPT=%{SOURCE13}

%files
%license BSDL COPYING GPL LEGAL
%doc README.md NEWS
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

%{ruby_libarchdir}/{continuation.so,coverage.so,date_core.so,dbm.so}
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
%{gem_dir}/gems/rake-12.3.3
%{gem_dir}/specifications/rake-12.3.3.gemspec

%files irb
%{_bindir}/irb
%{ruby_libdir}/{irb.rb,irb}

%files -n rubygem-rdoc
%{_bindir}/{rdoc,ri}
%{gem_dir}/gems/rdoc-6.0.1.1
%{gem_dir}/specifications/rdoc-6.0.1.1.gemspec

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
%{_libdir}/gems/%{name}/bigdecimal-1.3.4
%{gem_dir}/gems/bigdecimal-1.3.4
%{gem_dir}/specifications/bigdecimal-1.3.4.gemspec

%files -n rubygem-did_you_mean
%{gem_dir}/gems/did_you_mean-1.2.0
%{gem_dir}/specifications/did_you_mean-1.2.0.gemspec
%exclude %{gem_dir}/gems/did_you_mean-1.2.0/.*

%files -n rubygem-io-console
%{ruby_libdir}/io
%{ruby_libarchdir}/io/console.so
%{_libdir}/gems/%{name}/io-console-0.4.6
%{gem_dir}/gems/io-console-0.4.6
%{gem_dir}/specifications/io-console-0.4.6.gemspec

%files -n rubygem-json
%{ruby_libdir}/json*
%{ruby_libarchdir}/json*
%{_libdir}/gems/%{name}/json-2.1.0
%{gem_dir}/gems/json-2.1.0
%{gem_dir}/specifications/json-2.1.0.gemspec

%files -n rubygem-minitest
%{gem_dir}/gems/minitest-5.10.3
%{gem_dir}/specifications/minitest-5.10.3.gemspec
%exclude %{gem_dir}/gems/minitest-5.10.3/.*

%files -n rubygem-openssl
%{ruby_libdir}/openssl
%{ruby_libdir}/openssl.rb
%{ruby_libarchdir}/openssl.so
%{_libdir}/gems/%{name}/openssl-2.1.2
%{gem_dir}/gems/openssl-2.1.2
%{gem_dir}/specifications/openssl-2.1.2.gemspec

%files -n rubygem-power_assert
%{gem_dir}/gems/power_assert-1.1.1
%{gem_dir}/specifications/power_assert-1.1.1.gemspec
%exclude %{gem_dir}/gems/power_assert-1.1.1/.*

%files -n rubygem-psych
%{ruby_libdir}/psych
%{ruby_libdir}/psych.rb
%{ruby_libarchdir}/psych.so
%{_libdir}/gems/%{name}/psych-3.0.2
%{gem_dir}/gems/psych-3.0.2
%{gem_dir}/specifications/psych-3.0.2.gemspec

%files -n rubygem-net-telnet
%{gem_dir}/gems/net-telnet-0.1.1
%{gem_dir}/specifications/net-telnet-0.1.1.gemspec
%exclude %{gem_dir}/gems/net-telnet-0.1.1/.*

%files -n rubygem-test-unit
%{gem_dir}/gems/test-unit-3.2.7
%{gem_dir}/specifications/test-unit-3.2.7.gemspec

%files -n rubygem-xmlrpc
%license %{gem_dir}/gems/xmlrpc-0.3.0/LICENSE.txt
%doc %{gem_dir}/gems/xmlrpc-0.3.0/README.md
%dir %{gem_dir}/gems/xmlrpc-0.3.0

%{gem_dir}/gems/xmlrpc-0.3.0/{Gemfile,Rakefile,bin,lib,xmlrpc.gemspec}
%{gem_dir}/specifications/xmlrpc-0.3.0.gemspec
%exclude %{gem_dir}/gems/xmlrpc-0.3.0/.*

%changelog
* Thu Nov 5 2020 wutao <wutao61@huawei.com> - 2.5.8-3
- fix CVE-2020-25613
- WEBrick,a simple HTTP server bundled with Ruby,had not
- checked the transfer-encoding header value rigorously.
- An attacker may potentially exploit this issue to bypass
- a reverse proxy,which may lead to an HTTP Request Smuggling
- attack.

* Fri Nov 06 2020 liuweibo <liuweibo10@huawei.com> - 2.5.8-2
- append doc require to ruby

* Tue Aug 04 2020 shanzhikun <shanzhikun@huawei.com> - 2.5.8-1
- upgrade ruby to 2.5.8.

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
