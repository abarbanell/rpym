# Proxy configuration

to send data to limitless garden you can send normal http traffic to an internal nginx proxy. In our case it is located at rpi01:8118.

The nginx proxy configuraltion in file /etc/nginx/sites-enabled/proxy: 

```
 proxy server for selected stuff from /api folder, giving 404 on everything else

server {
        listen 8118;
        location /api {
                # client_body_in_file_only on;
                # client_body_temp_path /var/log/nginx/client_temp;
                proxy_pass      https://lg.dokku.abarbanell.de/api;
        }
        location / {
                return  404;
        }
}
```

Reason: Although a Raspberry Pi is strong enough to encrypt https traffic, an arduino is normally not. So I take the risk of unencrypted traffic locally and let nginx do the encryption.


