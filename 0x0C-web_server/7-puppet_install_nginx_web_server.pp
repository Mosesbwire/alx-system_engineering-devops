#installs and configures an nginx server

exec { 'apt-get update':
  command => '/usr/bin/apt-get -y update'
}

package { 'nginx':
  ensure  => "installed",
  require => Exec['apt-get update']
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
  require => Package['nginx']
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}

