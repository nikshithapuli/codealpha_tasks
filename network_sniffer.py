from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("=" * 50)
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)

        if packet.haslayer(TCP):
            print("Protocol       : TCP")
        elif packet.haslayer(UDP):
            print("Protocol       : UDP")
        else:
            print("Protocol       : Other")

        print("Packet Length  :", len(packet), "bytes")

print("Starting Network Sniffer...")
print("Press Ctrl + C to stop.\n")

sniff(prn=packet_callback, store=False)