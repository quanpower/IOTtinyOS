print "********************************************";
print "*        wirelesslights TOSSIM script      *";
print "*       IOT 2012 Zavatta Marco 766437      *";
print "********************************************";

# Proceed to create three motes
# Full connected topology fetched from topology.txt
# Noise model fetched from meyer-heavy.txt
# 
# Output log file into wirelesslights_SIMlog.txt

import sys;
import time;

from TOSSIM import *;

t = Tossim([]);

print "Initializing mac....";
mac = t.mac();
print "Initializing radio channels....";
radio=t.radio();
print "Initializing simulator....";
t.init();

topology="topology.txt";
print "Using topology file: ",topology

#simulation_outfile = "wirelesslights_SIMlog.txt";
#print "Saving simulation output to: ", simulation_outfile;
#out = open(simulation_outfile, "w");

out = sys.stdout;

#Add debug channel
print "Activate debug message on channel cpanel"
t.addChannel("cpanel",out);
print "Activate debug message on channel light1"
t.addChannel("light1",out);
print "Activate debug message on channel light2"
t.addChannel("light2",out);

print "Creating Control Panel (1)...";
node1 =t.getNode(1);
node1.bootAtTime(0);
print ">>>Will boot at time",  0, "[sec]";
#print ">>>Will boot at time",  time1/t.ticksPerSecond(), "[sec]";

print "Creating node Light1 (2)...";
node2 = t.getNode(2);
node2.bootAtTime(0);
print ">>>Will boot at time", 0, "[sec]";

print "Creating node Light2 (3)...";
node3 = t.getNode(3);
node3.bootAtTime(0);
print ">>>Will boot at time", 0, "[sec]";

print "Creating radio channels..."
f = open(topology, "r");
lines = f.readlines()
for line in lines:
  s = line.split()
  if (len(s) > 0):
    print ">>>Setting radio channel from node ", s[0], " to node ", s[1], " with gain ", s[2], " dBm"
    radio.add(int(s[0]), int(s[1]), float(s[2]))

noise = open("meyer-heavy.txt", "r")
for line in noise:
  str1 = line.strip()
  if str1:
    val = int(str1)
    for i in range(1, 4):
      t.getNode(i).addNoiseTraceReading(val)

for i in range(1, 4):
  print "Creating noise model for ",i;
  t.getNode(i).createNoiseModel()

print "Start simulation with TOSSIM! \n\n\n";

for i in range(0,1000000):
	t.runNextEvent()
	
print "\n\n\nSimulation finished!";
