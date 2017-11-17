# executes pkill killmenow

exec {'killmenow':
  command => '/usr/bin/pkill -g $(/usr/bin/pgrep killmenow)'
}