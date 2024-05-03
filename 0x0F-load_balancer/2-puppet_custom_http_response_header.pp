# Configures a clean install ubuntu pc
exec {'update_packages':
command => '/usr/bin/apt-get update -y'
}

package {'nginx':
ensure => installed
}

file {'/var/www/html/index.nginx-debian.html':
ensure  => present,
content => "Hello World!\n"
}

exec {'add_header':
command => '/bin/sed -i "/^\tlocation \/ {.*/a \\\t \tadd_header X-Served-By \$hostname;" /etc/nginx/sites-available/default; /usr/sbin/service nginx restart'
}

exec {'redirect':
command => '/bin/sed -i "/^\tserver_name _.*/a \\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default; /usr/sbin/service nginx restart'
}

file {'/var/www/html/error404.html':
ensure  => present,
content => "this page doesn't exist\n"
}

exec {'error404':
command => '/bin/sed -i "/^\tserver_name _.*/a \\\terror_page 404 /error404.html;" /etc/nginx/sites-available/default; /usr/sbin/service nginx restart'
}
