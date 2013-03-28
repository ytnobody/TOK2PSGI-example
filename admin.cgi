#!/usr/bin/perl
$| = 1;
use strict;
use warnings;
use constant HOME => '/home/member/ytnobody';
use CGI;

$ENV{PATH} = join ':', $ENV{PATH}, HOME.'/local/bin', HOME.'/bin';
$ENV{PERL5LIB} = HOME.'/local/lib/perl5';
$ENV{PERL_CPANM_HOME} = HOME.'/.cpanm';

my $this = __FILE__;
my $c = CGI->new;
my $cm = $c->param('c');

my $proc = `ps xfh`;
my $out = length($cm) > 0 ? `nice -n 15 $cm 2>&1` : '';

print <<EOF;
Content-Type: text/html; charset=euc-jp

<html>
<head>
  <title>testです！！！！＞＜</title>
</head>
<body onLoad="document.f1.c.focus()">
  <h2>proc</h2>
  <textarea readonly style=\"width:100%;height:300px;\">$proc</textarea>
  <h2>output</h2>
  <textarea readonly style=\"width:100%;height:200px;\">$out</textarea>
  <form name="f1" action="./$this" method="post">
    cmd: <input name="c" type="text" value="$cm" style="width:240px;"><input type="submit">
  </form>
</body>
</html>
EOF

exit;
