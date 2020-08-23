# installs and configures and Nginx server using Puppet
exec {'apt-get update':
    path => '/usr/bin/env',
}
exec {'apt-get -y install nginx':
    path => '/usr/bin/env',
}
exec {'ufw allow \'Nginx HTTP\'':
    path => '/usr/bin/env',
}
exec {'echo \"Holberton School\" > /var/www/html/index.html':
    path => '/usr/bin/env',
}
exec {'echo \"Ceci n\'est pas une page\" > /var/www/html/404code.html':
    path => '/usr/bin/env',
}
exec {'sed -i \'/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\' /etc/nginx/sites-available/default':
    path => '/usr/bin/env',
}
exec {'sed -i \'/listen 80 default_server/a error_page 404 /404code.html;\' /etc/nginx/sites-available/default':
    path => '/usr/bin/env',
}
exec {'service nginx start':
    path => '/usr/bin/env',
}
