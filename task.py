def list_ifname_ip():
	list_ifname_ip=[]
	with open("running-config.cfg","rt") as in_file:
		for interface in in_file:
			list_ifname_ip.append(interface)
 
interface=[]
vlan=[]
macaddress=[]
ipaddress=[]

for i in l:
	a=""
	b=""
	t.split=""
	if(t[0]=="interface"):
		interface.append(t[1])
	if(t[0]=="vlan"):
		vlan.append(t[1])
	if(t[0]=="macaddress"):
		macaddress.append(t[2])
	if(t[0] == "ipaddress"):
		ipaddress.append(t[3])

print(interface)
print(vlan)
print(name)
print(macaddress)
