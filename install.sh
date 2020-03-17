#!/bin/bash
cp -v monigraf.service /lib/systemd/system/
mkdir -vp /etc/monigraf/modules.d
cp -vr conf/* /etc/monigraf/
chmod -v 600 /etc/monigraf/monigraf.conf
