# This Puppet manifest configures Nginx to handle high loads


exec { 'increase-nginx-worker-connections':
    command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
