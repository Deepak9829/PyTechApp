def DockerContManage():
	import os
	import subprocess
	import json
	ImageName = input("Enter Container Imagename : ")
	OsName = input("Enter OS Name : ")
	while True:
		D = subprocess.getoutput("figlet Docker Manager")
		print("\t\t{}".format(D))
		os.system("tput setaf 5")
		print("""
			*********************************************************
			$	Press 1: Pull Docker Image from Docker HUB	            
			*********************************************************
			$	Press 2: Run Docker Containers          
			*********************************************************
			$	Press 3: Delete Docker Contaner       
			*********************************************************
			$	Press 4: Remove All Docker Containers        
			*********************************************************
			$	Press 5: See Runnig Containers           
			*********************************************************
			$	Press 6: See Downloaded Docker os images	   
			*********************************************************
			$	Press 7: Exit from program					  
			*********************************************************
			""")
		os.system("tput setaf 7")
		Choice = int(input("Enter your choice :"))

		if(Choice == 1):
			PullDImage = subprocess.getstatusoutput("docker pull {}".format(ImageName))
			if(PullDImage[0] == 0):
				os.system("tput setaf 3")
				print("[ Pull Docker Image ]***************************************************************************************\n\n")
				print(PullDImage[1])
			else:
				os.system("tput setaf 2")
				print("[ Pull Docker Image ]***************************************************************************************\n\n")
				print(PullDImage[1])

			os.system("tput setaf 7")
		elif(Choice == 2):
			LaunchContainer = subprocess.getstatusoutput("docker run -dit --name {} {}".format(OsName,ImageName))
			if(LaunchContainer[0] == 0):
				os.system("tput setaf 3")
				print("[ Launch Docker Container ]********************************************************************************\n\n")
				print(LaunchContainer[1])
			else:
				os.system("tput setaf 3")
				print("[ Launch Docker Container ]********************************************************************************\n\n")
				print(LaunchContainer[1])

	        
		elif(Choice == 3):
			DeleteContainer = subprocess.getstatusoutput("docker rm -f {}".format(OsName))
			if(DeleteContainer[0] == 0):
				os.system("tput setaf 3")
				print("[ Delete Docker Container ]********************************************************************************\n\n")
			else:
				os.system("tput setaf 2")
				print("[ Delete Docker Container ]********************************************************************************\n\n")

		elif(Choice == 4):
			DeleteAllContainer = subprocess.getstatusoutput("docker rm -f `docker ps -qa`")
			if(DeleteAllContainer[0] == 0):
				os.system("tput setaf 3")
				print("[ Delete All Container ]***********************************************************************************\n\n")
				print(DeleteAllContainer[1])
			else:
				os.system("tput setaf 3")
				print("[ Delete All Container ]***********************************************************************************\n\n")
				print(DeleteAllContainer[1])

		elif(Choice == 5):
			os.system("docker ps")

		elif(Choice == 6):
			os.system("docker images")

		elif(Choice == 7):
			break

		else:
			print("Option not supported...")


		os.system("tput setaf 7")
		print("\n\n")
		input("Press Enter to Continue.........")
		os.system("clear")


#DockerContLaunch()