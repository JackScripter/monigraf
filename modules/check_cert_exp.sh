#!/bin/bash

target="$1"; days_warn=$2; days_crit=$3

expirationdate=$(date -d "$(: | openssl s_client -connect $target -servername $target 2> /dev/null \
        | openssl x509 -text \
        | grep 'Not After' \
        | awk '{print $4,$5,$7}')" '+%s');
expirein_warn=$(($(date +%s) + (86400*$days_warn)))
expirein_crit=$(($(date +%s) + (86400*$days_crit)))

# 0=OK	1=WARNING	2=CRITICAL
if [ $expirein_crit -gt $expirationdate ]; then
	echo "$(date -d @$expirationdate '+%F %T');2"
elif [ $expirein_warn -gt $expirationdate ]; then
	echo "$(date -d @$expirationdate '+%F %T');1"
else
	echo "$(date -d @$expirationdate '+%F %T');0"
fi
