# This Puppet manifest increases the file descriptor limit for the holberton user


exec { 'increase-file-hard-limit':
  path    => '/bin',
  command => 'sed -i "s/nofile 5/nofile 7000/" /etc/security/limits.conf'
}

exec { 'increase-file-soft-limit':
  path    => '/bin',
  command => 'sed -i "s/nofile 4/nofile 4096/" /etc/security/limits.conf'
}
