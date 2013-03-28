use strict;
use warnings;
use utf8;
use Encode;

sub { 
    [
        200,
        ['text/html; charset=utf-8'],
        [Encode::encode('euc-jp', '<html><head><title>psgiアプリ</title></head><body><h2>これはなんと！PSGIアプリです！</h2></body></html>')]
    ] 
};
