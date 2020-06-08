from scapy.all import *
import os, sys, random, argparse, time, random

#todo:

#Atac_server_2 ha d'enviar un HTTP request amb el wget -o...:dstPort etc

dstIP = sys.argv[1]

dstPort = sys.argv[2]

file = open(sys.argv[3],"r")
obert = file.readlines()
srcIP = obert[0]
file.close()

srcPort = sys.argv[4]
print(type(dstIP))
print(type(srcIP))


int(dstPort)
int(srcPort)
print(srcIP)
if len(sys.argv) != 5: #sudo python atac.py 10.0.0.2 80 llista.txt 666
    print("Usage: %s destinationIP destinationPort sourceIP sourcePort"%(sys.argv[0]))
    sys.exit(0)

def Atac_server_2(dstIP,srcIP,srcPort,dstPort):
    syn = IP(dst=dstIP, src=srcIP)/TCP(dport=dstPort, sport=srcPort, flags='S')
    syn
    syn_ack = sr1(syn)
    syn_ack
    getStr = 'GET / HTTP/1.1\r\nHost: 10.0.10.2\r\n\r\n'
    request = IP(dst=dstIP, src=srcIP)/TCP(dport=dstPort, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq +1, flags='A') / getStr

    print(request)

if __name__=="__main__":
    Atac_server_2(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
