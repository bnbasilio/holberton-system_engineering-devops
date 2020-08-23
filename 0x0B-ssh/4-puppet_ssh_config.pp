# sets up config file to not require password with ssh
file_line {'Identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/holberton',
}

file_line {'Password authentication':
    encure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no',
}
