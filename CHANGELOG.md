# Changelog
## [0.3.0] - 2020-xx-xx
### New Features
- Added alerting services such as Telegram and Discord.
- Support SNMP Ubiquiti switch
### Changes
- Removed some value to monitor in system module (Slab/Inactive/Active/Shared/Available Memory)
- In system module, cpu usage includes all cores instead of single core
- Removed the need to run a module with "refresh" argument"

## [0.2.0] - 2020-07-15
### New Features
- Added Elasticsearch as a new datasource !
### New modules
- raw_logs
- certificates_expiration
- snmp_monitoring
### Fixes
- Store temporary data in a dictionary instead of multiple single variable
- Remove unused python module
- Support CentOS and Debian

## [0.1.1] - 2020-05-09
### New modules
- unbound
### Fixes
- Set shebang to /usr/bin/env python3 instead of /usr/bin/python3.7

## [0.1.0] - 2020-04-19
### New modules
- system
### Improvements
- Added a function in BodyBuilder to delete a tag in the body.

## [0.10a] - 2020-04-12
First release.
