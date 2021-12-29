# NMap Sequel

- Scan network for open ports.
- Fetch detailed info about a device.

## Pre-requisite
[ip.txt](https://github.com/abrasham-chowdhury/NMapSequel/blob/main/ip.txt) - List of IPs to scan for open ports (Use
new line for each IP)

## Run
- sudo python3 nmap_sequel.py

## Dependency
- [python-nmap](https://pypi.org/project/python-nmap/)

## Example
**Option 1:**

    GENERAL INFO

    -> MAC address: 0C:88:DB:BD:04:51
    -> Operating system: Linux 3.2 - 4.0
    -> Device uptime: Tue Feb 18 02:49:34 2020

    PORTS

    -> 22 |ssh | open
    -> 23 | telnet | closed
    -> 80 | http | closed
    -> 161 | snmp | open
    -> 179 | bgp | closed
    -> 443 | https | closed
    -> 639 | msdp | closed
    -> 646 | ldp | closed
    -> 830 | netconf-ssh | closed

    OTHER INFO
    
    -> NMAP command: nmap -oX - -p 1-1024 -v -sS -sV -O -A ${IP}\
    -> NMAP version: 7.1
    -> Time elapsed: 51.68seconds
    -> Time of scan: Tue Feb 18 06:24:29 2020


**Option 2:**

    Ports open on ${IP_1}
    -->22|ssh
    -->161|snmp
    
    Ports open on ${IP_2}
    -->22|ssh
    -->80|http
