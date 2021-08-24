#!/usr/bin/env python3

import os, time


os.system('sudo apt install conntrack nload htop tcpdump -y')



os.system("clear")
home_ip = input('Please enter your home IP so I can whitelist it for your ssh: ')
os.system("clear")
server_ip = input('Please enter your server\'s IPv4 address: ')
os.system("clear")

os.system("curl -O https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh")
os.system("chmod +x openvpn-install.sh")
os.system("AUTO_INSTALL=y ./openvpn-install.sh")
#this script was made by sgomgitsyo please dont take credit

os.system(f'iptables -I INPUT -p tcp --dport 22 -s {home_ip} -j ACCEPT')
os.system('iptables -A PREROUTING -t mangle -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT')
os.system('iptables -A PREROUTING -t mangle -i tun+ -j ACCEPT')
os.system('iptables -A PREROUTING -t mangle -i lo -j ACCEPT')
os.system('iptables -A INPUT -p tcp --dport 22 -j DROP')
os.system('/sbin/sysctl -w net.ipv4.icmp_ignore_bogus_error_responses=1 > /dev/null')
os.system('/sbin/sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1 > /dev/null')
os.system('/sbin/sysctl -w net.ipv4.conf.default.rp_filter=1 > /dev/null')
os.system('/sbin/sysctl -w net.ipv4.icmp_echo_ignore_all=1 > /dev/null')
os.system('/sbin/sysctl -w net.ipv4.conf.all.rp_filter=1 > /dev/null')
os.system('/sbin/sysctl -w net/ipv4/tcp_timestamps=1 > /dev/null')
os.system('/sbin/sysctl -w net.ipv4.tcp_syncookies=1 > /dev/null')

print("Your ip has been whitelisted to ssh openvpn has been installed and firewalls have been applied (; this script was made by SG")