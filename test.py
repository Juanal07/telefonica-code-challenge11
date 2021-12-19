from scapy.all import *

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('icmps.pcap')
# print(packets)
# Let's iterate through every packet
for packet in packets:
    print(packets)
    # We're only interested packets with a DNS Round Robin layer
    if packet.haslayer(DNSRR):
        # If the an(swer) is a DNSRR, print the name it replied with.
        if isinstance(packet.an, DNSRR):
            print(packet.an.rrname)
