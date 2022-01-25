def LocalYum():
	import os
	import subprocess


	Lyum = os.system("echo -e '[Repo1]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream/\ngpgcheck=0' > /etc/yum.repos.d/yum.repo")
	Lyum = os.system("echo -e '\n\n[Repo2]\nbaseurl = file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS/\ngpgcheck=0' >> /etc/yum.repos.d/yum.repo")



	x = subprocess.getoutput("yum repolist")

	print("""
*******************************************************************************************************************************
	        {}																												  	  
*******************************************************************************************************************************
		""".format(x))

