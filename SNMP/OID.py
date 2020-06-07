#!/usr/bin/env python3

class oid:
    sysinfo = "1.3.6.1.2.1.1.1.0"
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
