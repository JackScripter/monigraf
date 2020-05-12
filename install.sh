#!/bin/bash
MODULES_PATH='/opt/monigraf'
CONFIG_PATH='/etc/monigraf'

pip3 install -r requirements.txt
cp -v monigraf.service /lib/systemd/system/
mkdir -vp ${CONFIG_PATH}
mkdir -vp ${MODULES_PATH}
cp -v modules/* ${MODULES_PATH}/
cp -rv ES ${MODULES_PATH}/
cp -rv BodyBuilder ${MODULES_PATH}/
cp -v monigraf.py ${MODULES_PATH}/

if ! [ -f ${CONFIG_PATH}/monigraf.ini ]; then
	cp -v conf/monigraf.ini ${CONFIG_PATH}/
	chmod -v 600 ${CONFIG_PATH}/monigraf.ini
fi
