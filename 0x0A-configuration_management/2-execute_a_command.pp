# Runs a command that kills a process
exec {'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
}
