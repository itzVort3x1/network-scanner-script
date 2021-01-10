#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether) ; used to list all the arguments of a function
    # using forward slash("/") we can combine both packets into one packet
    arp_request_bradcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_bradcast, timeout=1)
    print(answered.summary())


scan("10.0.2.5")