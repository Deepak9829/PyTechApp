import os
import getpass
import DockerCfg
import DockerContainer
import WebserverSetup
import LocalYumCfg
import NameNode
import DataNode
import HadoopClient
import StaticPartition
import LVM
os.system("tput setaf 2")
print("\t\t\t\t\t\t\t\t this is my TUI")
os.system("tput setaf 7")
#os.system("tput setab 0")
print("\t\t\t-------------------------------------------------------------------------------------------------")
#os.system("tput setab 0")

Passwd = getpass.getpass("Enter your Password: ")
Password="deepak"
if Passwd != Password:
    print("login incorrect")
    exit()

print("where you would like perform your tui thats life simple")
location=input("Enter location: ")
if location == "local":
    while True:
        print("""
        Press 1: Docker Configuration.
        Press 2: Docker Container Management.
        Press 3: Configure Apache Webserver.
        Press 4: Configure Local Yum Repo.
        Press 5: Configure Hadoop Cluster.
        Press 6: Create Static Partition.
        Press 7: Create LVM Partition.
        Press 8:exit""")

        print("Enter your Choice: ",end="")
        ch=int(input())
        

        if ch==1:
        	DockerCfg.DockerCfg()
        elif ch==2:
        	DockerContainer.DockerContManage()        
        elif ch==3:
            WebserverSetup.webserversetup()
        elif ch==4:
            LocalYumCfg.LocalYum()
        elif ch==5:
        	while True:
	        	print("""

	        		Press 1: Configure Hadoop NameNode.
	        		Press 2: Configure Hadoop DataNode.
	        		Press 3: Configure Hadoop Client.
	        		Press 4: Get Back to the Home Menu.

	        		""")
	        	ch = int(input("Enter your Choice : "))

	        	if(ch == 1):
	        		NameNode.HadoopNameNode()
	        	elif(ch == 2):
	        		DataNode.DataNodefile()
	        	elif(ch == 3):
	        		HadoopClient.HaClient()
	        	elif(ch == 4):
	        		break
	        	else:
	        		print("Option not Supported.......")
	        	input("Enter to Continue........")
	        	os.system("clear")

            
        elif ch==6:
        	while True:
        		print("""

        			Press 1: See Hard Disk Info.
        			Press 2: See the Partitions of Any Disk attached.
        			Press 3: Create Static Partition.
        			Press 4: Use Static Partition( Format, Mount).
        			Press 5: Make Partition Offline.
        			Press 6: Delete Static Partition.
        			Press 7: Create Elastic Static Parttion.
        			Press 8: Get Back To Home Menu.

        			""")
        		ch = int(input("Enter your Choice : "))
        		if(ch == 1):
        			StaticPartition.HardDiskInfo()
        		elif(ch == 2):
        			StaticPartition.ListOfPart()
        		elif(ch == 3):
        			StaticPartition.CreateStaticPart()
        		elif(ch == 4):
        			StaticPartition.USEPartMount()
        		elif(ch == 5):
        			StaticPartition.MakePartitionOffline()
        		elif(ch == 6):
        			StaticPartition.DeleteStaticPart()
        		elif(ch == 7):
        			StaticPartition.ElasticStaticPartition()
        		elif(ch == 8):
        			break
        		else:
        			print("Option Not Supported..")
        		input("Press Enter to Continue........")
        		os.system("clear")

        elif ch==7:
        	while True:
        		print("""
        			Press 1: See LVM Info.
        			Press 2: Create LVM Partition.
        			Press 3: Extend the Size of LVM Partition.
        			Press 4: Reduce the Size of LVM Partition.
        			Press 5: Remove The LVM Complete Envinornoment.
        			Press 6: Get Back to the Home Menu.

        			""")
        		ch = int(input("Enter your Choice : "))
        		if(ch == 1):
        			LVM.LvInfo()
        		elif(ch == 2):
        			LVM.LvCreate()
        		elif(ch == 3):
        			LVM.LvExtend()
        		elif(ch == 4):
        			LVM.LvReduce()
        		elif(ch == 5):
        			LVM.RemoveLVM()
        		elif(ch == 6):
        			break
        		else:
        			print("Option not Supported.........")

        		input("Enter to Continue......")
        		os.system("clear")

        elif ch==8:
            exit()
        else:
            print("Option not supported")
        input("Enter to continue...........")
        os.system("clear")
if location == "remote":
    remoteIP = input("Enter your IP : ")
    while True:
        print("""
        Press 1:check date
        Press 2:check cal
        Press 3:Webserver configure
        Press 4:start firefox
        Press 5:check directory
        Press 6:Create user
        Press 7:check how many user login
        Press 8:exit""")
        print("Enter your Choice: ",end="")
        ch=int(input())
        print(ch)
        if ch==1:
            os.system("ssh {} date".format(remoteIP))
        elif ch==2:
            os.system("ssh {} cal".format(remoteIP))
        elif ch==3:
            os.system("ssh {} yum install httpd".format(remoteIP))
        elif ch==4:
            os.system("ssh {} firefox".format(remoteIP))
        elif ch==5:
            os.system("ssh {} ls".format(remoteIP))
        elif ch==6:
            create_user = input()
            os.system("useradd {}".format(create_user))
        elif ch==7:
            os.system("ssh {} w".format(remoteIP))
        elif ch==8:
            exit()
        else:
            print("Option not supported")
        input("Enter to continue...........")
        os.system("clear")
