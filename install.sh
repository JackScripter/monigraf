#!/bin/bash
# Color
declare -r RED='\e[91m'
declare -r DEF='\e[39m'

# Configuration file path
MODULES_PATH='/opt/monigraf'
CONFIG_PATH='/etc/monigraf'

function centos() {
	if ! rpm -q inotify-tools; then
		if ! yum repolist | grep epel; then yum install epel-release; yum update; fi
		yum install -y inotify-tools
	fi
	if ! rpm -q net-snmp-utils; then yum install -y net-snmp-utils; fi
}

function debian() {
	if ! dpkg -l inotify-tools; then apt install -y inotify-tools; fi
}

function general() {
	pip3 install -r requirements.txt
	cp -v monigraf.service /lib/systemd/system/

	mkdir -vp ${CONFIG_PATH}
	mkdir -vp ${MODULES_PATH}

	cp -v modules/* ${MODULES_PATH}/
	cp -rv ES ${MODULES_PATH}/
	cp -rv SNMP ${MODULES_PATH}/
	cp -rv BodyBuilder ${MODULES_PATH}/
        cp -rv alerts ${MODULES_PATH}/
        mv -v ${MODULES_PATH}/alerts/*/ ${MODULES_PATH}/
	cp -v monigraf.py ${MODULES_PATH}/

	if ! [ -f ${CONFIG_PATH}/monigraf.ini ]; then
		cp -v conf/monigraf.ini ${CONFIG_PATH}/
		chmod -v 600 ${CONFIG_PATH}/monigraf.ini
	fi
}

# Check Linux distro
os_release=`cat /etc/*-release | grep ID`
case $os_release in
	*"debian"*) distro="debian";;
	*"centos"*) distro="centos";;
	*) distro="";;
esac
if [[ $distro == "" ]]; then
	echo -e "${RED}Cannot find a supported Linux distribution !${DEF}"
	echo "If you think one of the following distro should work, choose one."
	echo "- debian"
	echo "- centos"
	distro=`read -p "Distro: "`
fi
case $distro in
	"debian") debian;;
	"centos") centos;;
	*) exit;;
esac
general
