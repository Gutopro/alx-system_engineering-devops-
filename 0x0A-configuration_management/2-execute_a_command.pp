# terminate process using pkill and exec in puppet

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => '/usr/bin/pgrep killmenow',
}
