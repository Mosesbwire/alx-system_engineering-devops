# kills the specified running process

exec { 'kill process':
  command => '/usr/bin/pkill killmenow',
}
