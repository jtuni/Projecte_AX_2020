from scapy.all import *
import random
import sys

dest = sys.argv[1]

if sys.argv[2]:
    getStr = 'GET / HTTP/1.1\r\nHost: '+dest+'\r\nAccept-Encoding: gzip, deflate\r\n\r\n'

if sys.argv[3]:
    source = open(sys.argv[3],"r")

counter = 0
max = 3
while counter < max:
    #SEND SYN
    syn = IP(dst=dest,src=source ) / TCP(sport=random.randint(1025,65500), dport=80, flags='S')
    print("syn")
    #GET SYNACK
    syn_ack = sr1(syn, timeout=20)
    print("syn_ack")
    #Send ACK
    out_ack = send(IP(dst=dest, src=source) / TCP(dport=80, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A'))
    print("out_ack")
    #Send the HTTP GET
    sr1(IP(dst=dest, src=source) / TCP(dport=80, sport=syn_ack[TCP].dport,seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='P''A') / getStr)
    print("sr1")
    counter += 1
