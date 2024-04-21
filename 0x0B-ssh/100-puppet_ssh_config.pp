# Replaces line in file
include stdlib

file_line {'Turn_off_passwd_auth':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '	PasswordAuthentication no'
;
'key_location':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '	IdentityFile ~/.ssh/school'
}
