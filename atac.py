from scapy.all import *
import os, sys, random, argparse, time, random

#todo:
#fer que es pugui executar amb scapy
#pillar el srcIP i dstPort de la llista
#srcport
#Atac_server_2 ha d'enviar un HTTP request amb el wget -o...:dstPort etc

srcIP = '179.45.148.12'
dstIP = '10.0.10.2'
srcPort = random.randint(1024,40000)
dstPort = '20906'
#srcIP,dstIP,srcPort,dstPort
def Atac_server_2():
    print("Comensa el test ...")
    load_layer("http")
    http_request("0.0.0.0:20906","/",display=True)
    print("Esperant 10s")
    time.sleep(10)

if __name__=="__main__":
    Atac_server_2()
