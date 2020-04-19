# monigraf
Monitor Linux server and more !

## Installation
### Dependencies
* python3.7
* python3-pip

### Installation
```bash
git clone https://github.com/JackScripter/monigraf.git
cd monigraf
sudo bash install.sh
```
When you run the program for the first time, you will need to create the module info database in which you will find devices specifications.\
For each module that you want to enable, run something like `/./opt/monigraf/network refresh`.

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
Get Rx and Tx usage.\
Configurable variables:
- delay
- interfaces: Monitor specified interfaces. Format: ["eth0","eth1"] or all to monitor all interfaces. Default: all

### apcups
Monitor connected APC UPS:
- Inline voltage
- Load
- Timeleft

Configurable variables:
- delay

### smart
Monitor S.M.A.R.T of hard drive.\
Configurable variables:
- delay
- drives: Specifies each drive you want to monitor. Format: ["sda","sdc"]. Default: all

### system
This module monitor basic system statistics including:
- CPU core usage
- System temperature (depending of your hardware, you may have less or more sensors)
- Memory usage
- Filesystem usage

Configurable variables:
- delay
