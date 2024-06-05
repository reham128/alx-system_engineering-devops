#script to fix typo error 'phpp' extension error to be only 
#'php' for WordPress file 'wp-settings.php'

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
