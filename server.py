import os
    try:
        rsd=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_DGRAM)
        
    except mysoc.error as err:
        exit()
hostname=input("Please tyep host name:")
# Define the port on which you want to receive  from  the server
    Rport = 50007
    myip = mysoc.gethostbyname(mysoc.gethostname())
# connect to the server on local machine
    server_binding=(myip, Rport)
    rsd.bind(server_binding)
    data,addr=rsd.recvfrom(1024)
    print(data.decode("utf-8"))

# Close the  receiver socket 
 rsd.close()
exit()
