# This Puppet manifest increases the file descriptor limit for the holberton user


exec { 'increase-file-descriptor-limit':
    command => 'echo "holberton hard nofile 65536" >> /etc/security/limits.conf && echo "holberton soft nofile 65536" >> /etc/security/limits.conf && echo "session required pam_limits.so" >> /etc/pam.d/common-session',
    unless  => 'grep -q "holberton hard nofile 65536" /etc/security/limits.conf',
    path    => ['/bin', '/usr/bin'],
}
