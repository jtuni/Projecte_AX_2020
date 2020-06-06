#!/usr/bin/python
from mininet.topo import topo
from mininet.net import Mininet
from mininet.node import RemoteController, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.util import custom
import scapy.all as scapy
import time, os, sys

#todo
#transformar projectTopo() en la classe My_topo()
#fer una funcio per afegir els links, i imprimir la comanda links
#fer una funcio amb els comandos per encendre servers
#afegir el puto controlador
#trobar la manera que els comandos no pengin el terminal (CLI? cmd??)
#encapsular scapy
#el wget del server 2 ha de guardar el html amb un nom != index.html



#def projecteTopo():
logging.getLogger().setLevel(logging.INFO)


class My_topo(Topo):
    def __init__(self):
        Topo.__init__(self)
        host_list = []

        info( '*** Adding controller\n' )
        net.addController( 'c0' )
        info('      c0\n')

        info( '*** Adding switch\n' )
        s1 = net.addSwitch( 's1' )
        info('      s1\n')

        info( '*** Adding hosts\n' )
        server1 = net.addHost( 'server1', ip='10.0.0.1/24' )
        host_list.append(server1)
        server2 = net.addHost( 'server2', ip='10.0.10.2/24' )
        host_list.append(server2)
        h1 = net.addHost('h1', ip='10.0.0.2/24')
        host_list.append(h1)
        info('      server1   server2     h1\n')
        #s1.cmd('sudo python controlador.py')

def links(net, server1, server2, h1, s1):
    info( '*** Creating links\n' )
    net.addLink( h1, server1 , intfName1='h1-eth0')
    net.addLink( h1, s1 , intfName1='h1-eth1')
    net.addLink( s1, server2 )
    info('      h1<->server1\n')
    info('      h1<->s1\n')
    info('      s1<->server2\n')
    h1.cmd('ifconfig h1-eth1 10.0.10.1 netmask 255.255.255.0')
#######################################

def network(net, server1, server2, h1, s1):
    
    info( '*** Starting network\n')
    net.start()


    #server1.cmd('sudo python Flask_server1.py')
    #time.sleep(4)
    info('48\n')
    #h1.cmd('wget -o - http://0.0.0.0:2000')
    #server2.cmd('sudo python Flask_server2.py')
    info(h1.cmd('cat index.html'))
    info('\n')

    info( '*** Running CLI\n' )
    CLI( net )

    #info(h1.cmd('sudo scapy paquet.py'))
    #info(ds)

    #time.sleep(5)
    #host.CLI('sudo scapy')

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topo = My_topo()
    net = Mininet(topo)
    links(net, server1, server2, h1, s1)