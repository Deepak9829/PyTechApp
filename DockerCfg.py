import os
import subprocess

def DockerCfg():
	os.system("tput setaf 10")
	os.system("figlet Docker Configuration")
	os.system("tput setaf 15")
	print("\n\n")
	Drepo = subprocess.getstatusoutput("echo -e '[docker]\nbaseurl = https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0' > /etc/yum.repos.d/docker.repo")
	if(Drepo[0] == 0 ):
		os.system("tput setaf 3")
		print("[ Configure Docker Repo ]**************************************************************************************\n\n")
	else:
		os.system("tput setaf 2")
		print("[ Configure Docker Repo ]**************************************************************************************\n\n")


	DInstall = subprocess.getstatusoutput("yum install docker-ce --nobest")
	if( DInstall[0] == 0):
		os.system("tput setaf 3")
		print("[ Docker Installed ]*******************************************************************************************\n\n")
	else:
		os.system("tput setaf 2")
		print("[ Docker Installed ]*******************************************************************************************\n\n")

	Service = subprocess.getstatusoutput("systemctl start docker")
	if(Service[0] == 0):
		os.system("tput setaf 3")
		print("[ Docker Engine start ]****************************************************************************************\n\n")
	else:
		os.system("tput setaf 2")
		print("[ Docker Engine start ]****************************************************************************************\n\n")
	


	os.system("tput setaf 7")

#DockerCfg()