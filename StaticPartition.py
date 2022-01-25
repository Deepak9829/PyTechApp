import os
import subprocess


def HardDiskInfo():
	os.system("tput setab 2")
	os.system("fdisk -l")
	os.system("tput setaf 15")

def CreateStaticPart():
	DiskName = input("Enter CreatePart Disk Name : ")
	PartSize = input("Enter Partition Size : ")
	StaticPart = subprocess.getstatusoutput("printf 'p\nn\np\n\n\n+{}\nY\nw\n' | fdisk /dev/{}".format(PartSize,DiskName))
	if(StaticPart[0] == 0):
		os.system("tput setaf 11")
		print("[ Create Static Partition ]********************************************************************************************************************")
		print(StaticPart[1])
	else:
		os.system("tput setaf 1")
		print("[ Create Static Partition ]********************************************************************************************************************")
		print(StaticPart[1])
	os.system("tput setaf 15")


def ListOfPart():
	DiskPartName = input("Enter Disk Part Name : ")
	ListP = subprocess.getoutput("fdisk /dev/{} -l".format(DiskPartName))
	print("""
***************************************************************************************************************************************************************
     
       {}
        
***************************************************************************************************************************************************************
		""".format(ListP))
	

def DeleteStaticPart():
	DiskName = input("Enter DeletePart Disk Name : ")
	DeletePartName = input("Enter Part No. : ")
	DeletePart = subprocess.getstatusoutput("printf 'p\nd\n{}\nw' | fdisk /dev/{}".format(DeletePartName,DiskName))
	if(DeletePart[0] == 0):
		os.system("tput setaf 2")
		print("[ Delete Static Partition ]********************************************************************************************************************")
		print(DeletePart[1])
	else:
		os.system("tput setaf 1")
		print("[ Delete Static Partition ]********************************************************************************************************************")
		print(DeletePart[1])
	os.system("tput setaf 15")



def USEPartMount():
	ListOfPart()
	PartName = input("Enter Partition Name : ")
	MountPoint = input("Create Mount Point for the Partition : ")
	FormatType = input("Enter format Type : ")
	CreateMountPoint = subprocess.getstatusoutput("mkdir /{}".format(MountPoint))
	if(CreateMountPoint[0] == 0):
		os.system("tput setaf 11")
		print("[ MountPoint Created SuccessFully ]***********************************************************************************************************")
	else:
		os.system("tput setaf 2")
		print("[ MountPoint Already Exist ]*****************************************************************************************************************")
	FomatPartition = subprocess.getstatusoutput("echo y | mkfs.{} /dev/{}".format(FormatType,PartName))
	if(FomatPartition[0] == 0):
		os.system("tput setaf 11")
		print("[ Partion Formated SuccessFully ]************************************************************************************************************")
		print(FomatPartition[1])
	else:
		os.system("tput setaf 1")
		print("[ Patition Already Formated ]***************************************************************************************************************")
		print(FomatPartition[1])


	MountPart = subprocess.getstatusoutput("mount /dev/{}  /{}".format(PartName,MountPoint))
	if(MountPart[0] == 0):
		os.system("tput setaf 11")
		print("[ Partition Mounted SuccessFully with Mount point ]****************************************************************************************")
	else:
		os.system("tput setaf 1")
		print("[ Something went wrong Partition not Mounted ]*********************************************************************************************")
		print(MountPart[1])
	os.system("lsblk")
	os.system("tput setaf 15")

def MakePartitionOffline():
	MountPointN = input("Enter Mount Point for Make offline : ")
	OfflineMountP = subprocess.getstatusoutput("umount /{}".format(MountPointN))
	if(OfflineMountP[0] == 0):
		os.system("tput setaf 11")
		print("[ MountPoint offline ]********************************************************************************************************************")
	else:
		os.system("tput setaf 1")
		print("[ MountPoint Is yet Busy ]****************************************************************************************************************")
	os.system("tput setaf 15")


def CreateElasticStaticPart():
	DiskName = input("Enter CreatePart Disk Name : ")
	PartSize = input("Enter Partition Size : ")
	StaticPart = subprocess.getstatusoutput("printf 'p\nn\np\n\n\n+{}\nN\nw\n' | fdisk /dev/{}".format(PartSize,DiskName))
	if(StaticPart[0] == 0):
		os.system("tput setaf 11")
		print("[ Create Static Partition ]********************************************************************************************************************")
		print(StaticPart[1])
	else:
		os.system("tput setaf 1")
		print("[ Create Static Partition ]********************************************************************************************************************")
		print(StaticPart[1])
	os.system("tput setaf 15")


def ScanPartResizeMount():
	DiskName = input("Enter Disk Name : ")
	MountPoint = input("Enter Mount Point : ")
	Scan = subprocess.getoutput("e2fsck -f /dev/{}".format(DiskName))
	print(Scan)

	Resize = subprocess.getoutput("resize2fs /dev/{}".format(DiskName))
	print(Resize)

	Scan = subprocess.getoutput("e2fsck -f /dev/{}".format(DiskName))
	print(Scan)

	MountUse = subprocess.getoutput("mount /dev/{} /{}".format(DiskName,MountPoint))

	os.system("lsblk")

	os.system("ls -la /{}".format(MountPoint))


def ElasticStaticPartition():
	ListOfPart()
	DeleteStaticPart()
	CreateElasticStaticPart()
	ScanPartResizeMount()










	
#ElasticStaticPartition()
	


#ScanPartiton()

#CreateStaticPart()
#ListOfPart()
#DeleteStaticPart()
#ListOfPart()
#USEPartMount()
#MakePatitonOffline()

