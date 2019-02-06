import math
def list_ifname_ip():
    myfile = open('running-config.cfg')
    nameifdict=dict()

    for line in myfile:
        if "nameif" in line:
            myfilelist = line.split()

            next(myfile)
            templine = next(myfile)
            mylist= templine.split()

            if myfilelist[0]=='nameif':
                if mylist[0] == 'ip':
                    mytuple=(mylist[2:])
                    nameifdict[myfilelist[1]]=mytuple

    return (nameifdict)

ipconfigs = list_ifname_ip()
print(ipconfigs)


