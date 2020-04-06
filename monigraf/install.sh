#!/bin/bash
MODULES_PATH='/opt/monigraf'
CONFIG_PATH='/etc/monigraf'

cp -v monigraf.service /lib/systemd/system/
mkdir -vp ${CONFIG_PATH}
mkdir -vp ${MODULES_PATH}
cp -vr conf/* ${CONFIG_PATH}/
chmod -v 600 ${CONFIG_PATH}/monigraf.ini
