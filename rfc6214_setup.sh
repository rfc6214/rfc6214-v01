#!/bin/bash

#
# Setup rfc6214 networking interface, environment.
#

set -x

# cleanup
ip -6 link set rfc6214 down
ip -6 tuntap del mode tun name rfc6214

# add
ip -6 tuntap add mode tun name rfc6214
# disable multicast
ip -6 link change dev rfc6214 multicast off
# disable RA
sysctl -w net.ipv6.conf.rfc6214.autoconf=0
sysctl -w net.ipv6.conf.rfc6214.accept_ra=0
ip -6 address add dev rfc6214 fda7:5420:cd16:e671::$1/127 nodad
ip -6 link set rfc6214 up

exit 0
