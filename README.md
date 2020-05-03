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

### unbound
Monitor statistics on single or multiple unbound DNS server.\
This module don't need to be installed on unbound server.\
Configurable variables:
- delay
- hosts: Hosts to get stats. Format: ["1.2.3.4@8953", "myhostname@8953"]. Default: ["localhost@8953"]

# InfluxDB reference
This part will be useful if you want to create dashboard.
## network
#### Tag table
| Key		| Values		| Description				|
|:---------:|:-------------:| ------------------------- |
| host		| _hostname_ 	| Server hostname			|
| mac		| _mac_ 		| Device MAC address		|

#### Field table
| Field		| Type	| Description						|
|:---------:|:-----:| --------------------------------- |
| rx_bytes	| float	| Receive bytes on interface		|
| tx_bytes	| float	| Transmitted bytes on interface	|

## network_info
This measurement is created or updated when you run `/opt/monigraf/network refresh`
#### Tag table
| Key		| Values		| Description				|
|:---------:|:-------------:| ------------------------- |
| host		| _hostname_	| Server hostname			|

#### Field table
| Field			| Type		| Description						|
|:-------------:|:---------:| --------------------------------- |
| controller	| string	| Actually the device controller	|
| driver		| string	| Driver exemple: e1000				|
| duplex		| string	| FULL or HALF duplex mode			|
| interface		| string	| Interface name exemple: eth0		|
| mac			| string	| MAC address						|
| mtu			| integer	| MTU value							|
| speed			| integer	| Interface operating speed			|

## smart
#### Tag table
| Key			| Values		| Description				|
|:-------------:|:-------------:| ------------------------- |
| host			| _hostname_	| Server hostname			|
| serial_number	| _drive_sn_	| Drive serial number		|

#### Field table
| Field			| Type		| Description								|
|:-------------:|:---------:| ----------------------------------------- |
| health		| integer	| SSD ONLY ! Health in %. HDD will return -1|
| power_on_hours| float		| How much time the drive is up in hours	|
| tbw			| float		| Terabytes Written in bytes				|
| temperature	| integer	| Drive temperature							|

## smart_info
This measurement is created or updated when you run `/opt/monigraf/smart refresh`
#### Tag table
| Key		| Values     | Description			|
|:---------:|:----------:| -------------------- |
| host		| _hostname_ | Server hostname		| 

#### Field table
| Field			| Type		| Description						|
|:-------------:|:---------:| --------------------------------- |
| capacity		| string	| Drive capacity					|
| drive			| string	| sda, sdb...						|
| firmware		| string	| Firmware							|
| model			| string	| Drive model						|
| serial_number	| string	| Drive serial number				|
| type			| string	| Returns SSD or Hard Drive			|

## system
#### Tag table
| Key			| Values		| Description					|
|:-------------:|:-------------:| ----------------------------- |
| host			| _hostname_	| Server hostname				|
| mountpoint	| _mountpoint_	| Mountpoint exemple: /, /tmp	|
| temp_sensor	| _sensor_		| All your hardware sensor.<br>Depending of your hardware, you may have less or more sensors. |
| usage			| <ul><li>core</li><li>memory</li><li>filesystem</li></ul>	| You can use one of these tags to graph easily |

#### Field table
You will find other field that are not listed below depending of your hardware.

| Field			| Type		| Description																		|
|:-------------:|:---------:| --------------------------------------------------------------------------------- |
| Core_*		| float		| Depending of the tag, it can be temperature or core usage 						|
| active		| integer	| Memory that has been used more recently and usually not swapped out or reclaimed	|
| available		| integer	| An estimate of how much memory is available for starting new applications, without swapping |
| buffers		| integer	| Memory in buffer cache, so relatively temporary storage for raw disk blocks		|
| cached		| integer	| Memory in the pagecache (Diskcache and Shared Memory								|
| free			| integer	| The amount of physical memory not used by the system								|
| inactive		| integer	| Memory that has not been used recently and can be swapped out or reclaimed		|
| shared		| integer	| Total used shared memory															|
| slab			| integer	| In-kernel data structures cache													|
| total			| integer	| Total usable memory																|
| used			| integer	| Total used memory																	|

## system_info
This measurement is created or updated when you run `/opt/monigraf/system refresh`
#### Tag table
| Key		| Values		| Description						|
|:---------:|:-------------:| --------------------------------- |
| host		| _hostname_	| Server hostname					|
| part		| <ul><li>cpu</li><li>mobo</li><li>mem</li></ul>	| Information related to these parts | 

#### Field table
| Field				| Type		| Description							|
|:-----------------:|:---------:| ------------------------------------- |
| cpu_L1_cache		| string	| CPU L1 Cache							|
| cpu_L2_cache		| string	| CPU L2 Cache							|
| cpu_L3_cache		| string	| CPU L3 Cache							|
| cpu_family		| string	| CPU family							|
| cpu_id			| string	| Just an ID to make something unique in this measurement. This value is pretty useless |
| cpu_model			| string	| CPU model								|
| cpu_socket		| string	| CPU socket, like AM4 or LGA2011		|
| cpu_total_core	| string	| Total number of physical and virtual core |
| mem_location		| string	| Memory location. On which slot.		|
| mem_part_number	| string	| Memory part number					|
| mem_serial_number	| string	| Memory serial number					|
| mem_size			| string	| Memory size. Exemple 8192 MB			|
| mem_speed			| string	| Memory speed							|
| mem_type			| string	| Memory type. DDR3, DDR4...			|
| mobo_manufacturer	| string	| Motherboard manufacturer				|
| mobo_model		| string	| Motherboard model						|
| mobo_serial_number| string	| Motherboard serial model				|
| mobo_version		| string	| Motherboard version/revision			|

## apcups
#### Tag table
| Key			| Values		| Description							|
|:-------------:|:-------------:| ------------------------------------- |
| host			| _hostname_	| Server hostname						|
| serial_number	| *serial_number* | APC UPS serial number				|

#### Field table
| Field			| Type		| Description								|
|:-------------:|:---------:| ----------------------------------------- |
| batt_charge	| float		| Percent of battery charged				|
| inline_volt	| float		| Current inline voltage. In volt.			|
| load			| float		| UPS load in percent.						|
| time_left		| float		| UPS on battery timeleft 					|

## apcups_info
This measurement is created or updated when you run `/opt/monigraf/apcups refresh`
#### Tag table
| Key	| Values		| Description		|
|:-----:|:-------------:| ----------------- |
| host	| _hostname_	| Server hostname	|

#### Field table
| Field			| Type		| Description					|
|:-------------:|:---------:| ----------------------------- |
| batt_date		| string	| Battery date					|
| maxpower		| string	| UPS max power output			|
| model			| string	| UPS model						|
| serial_number	| string	| UPS serial number				|
| ups_name		| string	| UPS name						|
| version		| string	| UPS driver/program version	|	

## unbound
#### Tag table
| Key		| Values		| Description								|
|:---------:|:-------------:| ----------------------------------------- |
| host		| _hostname_	| Server hostname							|
| target	| _host_		| Unbound DNS host							|

#### Field table
| Field						| Type		| Description																|
|:-------------------------:|:---------:| ------------------------------------------------------------------------- |
| thread*X*_cachehits		| integer	| Number of queries that were successfully answered using a cache lookup	|
| thread*X*_prefetch		| integer	| Number of cache prefetches performed										|
| thread*X*_queries			| integer	| Number of queries received by thread										|
| thread*X*_recursion_time	| float		| Average time it took to answer queries that needed recursive processing. Note that queries that were answered from the cache are not in this average. |
| thread*X*_tcpusage		| float		| The currently held tcp buffers for incoming connections. A spot value on the time of the request. |
| total_cachehits			| integer	| Cache hits total value for all threads									|
| total_prefetch			| integer	| Prefetch total value for all threads										|
| total_queries				| integer	| Total queries for all threads												|
| total_recursion_time		| float		| Average recursion time for all threads									|
| total_tcpusage			| float		| Total TCP buffers for all threads											|
