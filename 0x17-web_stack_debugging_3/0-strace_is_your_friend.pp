# fixes typo in wp-settings.php

exec {'fixwp':
  command => '/bin/sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php'
}
