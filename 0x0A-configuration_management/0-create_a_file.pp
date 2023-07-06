# Create a file named school in the /tmp dir

file { '/tmp/school':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'

}
