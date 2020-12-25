#!/usr/bin/env python3

class oid:
    sysinfo = "1.3.6.1.2.1.1.1.0"
    sysinfo_cp = "1.3.6.1.4.1.2620.1.6.5.1.0"
    class CiscoCatalyst:
        # System
        cpu_usage = "1.3.6.1.4.1.9.9.109.1.1.1.1.3"
        # Environment
        env_temp_status_desc = "1.3.6.1.4.1.9.9.13.1.3.1.2"
        env_temp_status_value = "1.3.6.1.4.1.9.9.13.1.3.1.3"
        # Interface
        if_desc = "1.3.6.1.2.1.2.2.1.2"
        total_in_octets = "1.3.6.1.2.1.31.1.1.1.6"
        total_out_octets = "1.3.6.1.2.1.31.1.1.1.10"
        ifInErrors = "1.3.6.1.2.1.2.2.1.14"
        ifOutErrors = "1.3.6.1.2.1.2.2.1.20"
        ifInDiscards = "1.3.6.1.2.1.2.2.1.13"
        ifOutDiscards = "1.3.6.1.2.1.2.2.1.19"

    class Linux:
        # System
        cpu_usage = "1.3.6.1.4.1.2021.10.1.3.1"
        mem_total = "1.3.6.1.4.1.2021.4.5.0"
        mem_used = "1.3.6.1.4.1.2021.4.6.0"
        # Environment Sensor

        # Interface
        if_desc = "1.3.6.1.2.1.2.2.1.2"
        total_in_octets = "1.3.6.1.2.1.2.2.1.10"
        total_out_octets = "1.3.6.1.2.1.2.2.1.16"
        ifInErrors = "1.3.6.1.2.1.2.2.1.14"
        ifOutErrors = "1.3.6.1.2.1.2.2.1.20"
        ifInDiscards = "1.3.6.1.2.1.2.2.1.13"
        ifOutDiscards = "1.3.6.1.2.1.2.2.1.19"

    class CheckPoint:
        sysinfo = "1.3.6.1.4.1.2620.1.6.5.1.0"
        cpu_usage = "1.3.6.1.4.1.2620.1.6.7.2.4"
        env_temp_status_desc = "1.3.6.1.4.1.2620.1.6.7.8.1.1.2"
        env_temp_status_value = "1.3.6.1.4.1.2620.1.6.7.8.1.1.3"
        env_fan_desc = "1.3.6.1.4.1.2620.1.6.7.8.2.1.2"
        env_fan_value = "1.3.6.1.4.1.2620.1.6.7.8.2.1.3"
        if_desc = "1.3.6.1.2.1.2.2.1.2"
        total_in_octets = "1.3.6.1.2.1.2.2.1.10"
        total_out_octets = "1.3.6.1.2.1.2.2.1.16"
        ifInErrors = "1.3.6.1.2.1.2.2.1.14"
        ifOutErrors = "1.3.6.1.2.1.2.2.1.20"
        ifInDiscards = "1.3.6.1.2.1.2.2.1.13"
        ifOutDiscards = "1.3.6.1.2.1.2.2.1.19"

    class Ubiquiti:
        cpu_usage = "1.3.6.1.4.1.4413.1.1.1.1.4.9.0"
        mem_free = "1.3.6.1.4.1.4413.1.1.1.1.4.1.0"
        mem_total = "1.3.6.1.4.1.4413.1.1.1.1.4.2.0"
        if_desc = "1.0.8802.1.1.2.1.3.7.1.3"
        #total_in_octets = "1.3.6.1.4.1.4413.1.1.1.1.8.1.1.1"  # Bits
        #total_out_octets = "1.3.6.1.4.1.4413.1.1.1.1.8.1.1.2"  # Bits
        total_in_octets = "1.3.6.1.2.1.2.2.1.10"
        total_out_octets = "1.3.6.1.2.1.2.2.1.16"
        ifInErrors = "1.3.6.1.2.1.2.2.1.14"
        ifOutErrors = "1.3.6.1.2.1.2.2.1.20"
        ifInDiscards = "1.3.6.1.2.1.2.2.1.13"
        ifOutDiscards = "1.3.6.1.2.1.2.2.1.19"
