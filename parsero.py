import os, sys, random, argparse, time, random, re

if len(sys.argv) != 3:
    print("Usage: %s entrada salida\n"%(sys.argv[0]))
    sys.exit(0)

entrada = sys.argv[1]
sortida = sys.argv[2]


a = open(entrada, "r")
linies = a.readlines()
a.close()

portRegex = re.compile(r'(\d\d\d\d\d)')
port = portRegex.search(linies[16])
if port:
    resultat = port.group(0)
    print port.group(0)

f=open(sortida, "w+")
f.write('10.0.0.1:'+resultat)
f.close()
