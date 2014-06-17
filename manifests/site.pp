package { "httpd":
  ensure    => present
}

service { "httpd":
  ensure => present
}