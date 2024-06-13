# This Puppet manifest configures Nginx to handle high loads


exec { 'increase-nginx-worker-connections':
    command => '/bin/sed -i "s/worker_connections 768;/worker_connections 4096;/" /etc/nginx/nginx.conf && service nginx restart',
    path    => ['/bin', '/usr/bin'],
}
