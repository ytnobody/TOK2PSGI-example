#!/usr/bin/perl

use strict;
use warnings;

use lib ("./local/lib/perl5");
use Plack::Loader;

my $app = Plack::Util::load_psgi('./app.psgi');
Plack::Loader->auto->run($app);
