FROM alpine:edge

RUN apk add --no-cache alsa-utils bluez bluez-alsa bluez-alsa-utils supervisor 

RUN adduser -S -H -D -u 1000 -G messagebus -s /sbin/nologin bluealsa
RUN mkdir -p /var/run/dbus \
    && chown messagebus:messagebus /var/run/dbus

RUN /usr/bin/dbus-uuidgen --ensure
COPY files/system-local.conf /etc/dbus-1/system-local.conf
COPY files/supervisord.conf /etc/supervisord.conf

CMD ["supervisord", "-c", "/etc/supervisord.conf"]
