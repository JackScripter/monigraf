# monigraf
Monitor Linux server and more !

## Installation
in progress...

## Configuration
### DEFAULT
- MOD_PATH: Location of modules. Default: /opt/monigraf/modules/
- MOD_ENABLED: Specifies each modules enabled on this host. Format: ["module1","module2"]. Default: ["network","smart"]
- delay: Default delay before recollect stats. You can set this variable in modules configuration so a module can collect data more frequently. Value are in seconds. Default: 3600

### influxdb
- server: IP of influxdb server. Default: 127.0.0.1
- username: Username used to connect to influxdb. Default: monigraf
- password: Password associated with username. Use single quote around password. Ex: 'Secr3tPa$$'
- dbname: Database used to create measurements. Default: monigraf

Modules configuration
--
### network
- delay
- interfaces: Monitor specified interfaces. Format: ["eth0","eth1"] or all to monitor all interfaces. Default: all

### apcups
- delay

### smart
- delay
- drives: Specifies each drive you want to monitor. Format: ["sda","sdc"]. Default: all
