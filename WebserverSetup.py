def webserversetup():
	import os
	import subprocess

	os.system("figlet WEBSERVER CONFIGURE")
	InstallHttpd = subprocess.getstatusoutput("yum install httpd -y")
	if(InstallHttpd[0] == 0):
		os.system("tput setaf 3")
		print("[ Installed Apache Httpd ]***********************************************************************************\n\n")
	else:
		os.system("tput setaf 2")
		print("[ Installed Apache Httpd ]***********************************************************************************\n\n")

	Service = subprocess.getstatusoutput("systemctl restart httpd")
	if(Service[0] == 0):
		os.system("tput setaf 3")
		print("[ Start httpd service ]*************************************************************************************\n\n")
	else:
		os.system("tput setaf 2")
		print("[ Start httpd service ]*************************************************************************************\n\n")
	os.system("tput setaf 2")
	Statushttpd = subprocess.getoutput("systemctl status httpd")
	#os.system("systemctl status httpd")
	print(Statushttpd,"\n\n")

	DeployWeb = subprocess.getstatusoutput("cp web.html /var/www/html/web.html")
	if(DeployWeb[0] == 0):
		os.system("tput setaf 3")
		print("[ DeployWeb web content ]************************************************************************************\n\n")
	else:
		os.system("tput setaf 2")
		print("[ DeployWeb web content ]************************************************************************************\n\n")
	os.system("tput setaf 7")

#webserversetup()