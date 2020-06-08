#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, Node, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.util import custom
import scapy.all as scapy
import time, os, sys

'''Usage:
1. ryu-manager --ofp-tcp-listen-port 6633
2. sudo python projecteTest.py
3. quan s'executi tot i s'obri el CLI, anar fent cat als txt i xml'''

def projecteTopo(cip):
    net = Mininet(controller = RemoteController, switch=OVSSwitch)

    info( '*** Starting network\n')
    net.start()

    info( '\n*** Adding controller\n' )
    net.addController( name='c0',ip=cip, port=6633 )
    info('      c0\n')

    info( '\n*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )
    info('      s1\n')

    info( '\n*** Adding hosts\n' )
    server1 = net.addHost( 'server1', ip='10.0.0.1' )
    server2 = net.addHost( 'server2', ip='10.0.10.2' )
    h1 = net.addHost('h1', ip='10.0.0.2')
    info('\n      server1   server2     h1\n')

    info( '\n*** Creating links\n' )
    net.addLink( h1, server1 , intfName1='h1-eth0')
    net.addLink( h1, s1 , intfName1='h1-eth1')
    net.addLink( s1, server2, intfName1='s1-eth2' )
    info('      h1<->server1\n')
    info('      h1<->s1\n')
    info('      s1<->server2\n')

    server1.cmd('ifconfig server1-eth0 10.0.0.1 netmask 255.255.255.0')
    server2.cmd('ifconfig server2-eth0 10.0.10.2 netmask 255.255.255.0')
    h1.cmd('ifconfig h1-eth0 10.0.0.2 netmask 255.255.255.0')
    h1.cmd('ifconfig h1-eth1 10.0.11.1 netmask 255.255.255.0')

    s1.cmd('ifconfig s1-eth1 10.0.10.1 netmask 255.255.255.0')
    s1.cmd('ifconfig s1-eth2 10.0.11.2 netmask 255.255.255.0')

    server2.cmd('sudo ip route add 10.0.11.0/24 dev server2-eth0 via 10.0.10.1')
    h1.cmd('sudo ip route add 10.0.10.0/24 dev h1-eth0 via 10.0.11.2')

    h1 = net.get('h1')
    server1 = net.get('server1')
    server2 = net.get('server2')
    s1 = net.get('s1')
    c0 = net.get('c0')
    net.build()

    info('\n***Controlador\n') #esta ences en un altre terminal
    s1.start([ c0 ])
    info("\n***Flask_server1\n")
    server1.cmdPrint('sudo python Flask_server1.py &') #encenem server1
    info("\n***Wait 5 seconds\n") #donem temps a encendre el server1
    time.sleep(5)
    info('\n***Scanning\n')
    h1.cmdPrint('nmap -sV 10.0.0.1 -p 10020-11080 -oX port.txt') #escaneja ports de la ip de server1, entre 10020 i 11080, output a port.txt
    h1.cmdPrint('sudo python parsero.py port.txt parsedPortAndIP.txt') #neteja port.txt i retorna parsedPortAndIP.txt
    h1.cmdPrint('cat parsedPortAndIP.txt')
    info("\n***wget\n")
    h1.cmdPrint("wget -O llista.txt -i parsedPortAndIP.txt") #wget del server i port que hi ha a parsedPortAndIP.txt, output a llista.txt
    h1.cmdPrint("cat llista.txt")
    info("\n***Flask_server2\n")#encenem server2
    server2.cmdPrint("sudo python Flask_server2.py &")
    info("\n***Wait 5 seconds\n")#donem temps a encendre server2
    time.sleep(5)
    info("\n***Scapy\n")
    h1.cmdPrint('sudo python remix.py 10.0.10.2 get llista.txt') #script per fer wget a server2 port 80 des de la ip de la llista.txt, que es una ip permesa
    h1.cmdPrint('cat index.html')

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network\n' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    IP_controlador = "127.0.0.1"
    projecteTopo(IP_controlador)
