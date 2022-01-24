FROM teamfruit/nginx-fcgiwrap

ADD ./nginx_files/default.conf /etc/nginx/conf.d
COPY ./nginx_files/index.html /var/www/
ADD ./test.py /var/www/cgi-bin/test.cgi

RUN chmod +x /var/www/cgi-bin/test.cgi \
&&apt-get update \
&& apt-get install -y python3 python3-pip mc \
&& pip3 install art

EXPOSE 80/tcp
