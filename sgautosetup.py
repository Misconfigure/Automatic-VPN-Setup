U
    ???aJ  ?                   @   s?   d dl Z d dlZe ?d? e ?d? ed?Ze ?d? ed?Ze ?d? e ?d? e ?d? e ?d? e ?d	e? d
?? e ?d? e ?d? e ?d? e ?d? e ?d? e ?d? e ?d? e ?d? e ?d? e ?d? e ?d? ed? dS )?    Nz0sudo apt install conntrack nload htop tcpdump -y?clearz>Please enter your home IP so I can whitelist it for your ssh: z)Please enter your server's IPv4 address: z]curl -O https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.shzchmod +x openvpn-install.shz#AUTO_INSTALL=y ./openvpn-install.shz'iptables -I INPUT -p tcp --dport 22 -s z
 -j ACCEPTzUiptables -A PREROUTING -t mangle -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPTz2iptables -A PREROUTING -t mangle -i tun+ -j ACCEPTz0iptables -A PREROUTING -t mangle -i lo -j ACCEPTz+iptables -A INPUT -p tcp --dport 22 -j DROPzH/sbin/sysctl -w net.ipv4.icmp_ignore_bogus_error_responses=1 > /dev/nullzB/sbin/sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1 > /dev/nullz=/sbin/sysctl -w net.ipv4.conf.default.rp_filter=1 > /dev/nullz;/sbin/sysctl -w net.ipv4.icmp_echo_ignore_all=1 > /dev/nullz9/sbin/sysctl -w net.ipv4.conf.all.rp_filter=1 > /dev/nullz5/sbin/sysctl -w net/ipv4/tcp_timestamps=1 > /dev/nullz5/sbin/sysctl -w net.ipv4.tcp_syncookies=1 > /dev/nullz|Your ip has been whitelisted to ssh openvpn has been installed and firewalls have been applied (; this script was made by SG)?os?time?system?inputZhome_ipZ	server_ip?print? r   r   ?sgautosetup.py?<module>   s,   

















