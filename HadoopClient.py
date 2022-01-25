import os
import subprocess

def HaClient():
    
    remote_IP = input("Enter your remote IP to Configure Hadoop Client: ")
    NameNoIP = input("Enter NameNode IP : ")
    
    Soft = subprocess.getstatusoutput("scp -r /Menu-Driven-P/Hasoft/ root@{}:/Menu-Driven-P/Hasoft/".format(remote_IP))
    if(Soft[0] == 0):
        os.system("tput setaf 3")
        print("[ Upload the softwares ]********************************************************************\n\n\n")
    else:
        os.system("tput setaf 2")
        print("[ Upload the softwares ]********************************************************************\n\n\n")


    Had = subprocess.getstatusoutput("ssh {}  rpm -ivh /Menu-Driven-P/Hasoft/hadoop-1.2.1-1.x86_64.rpm --force".format(remote_IP))
    if(Had[0] == 0):
        os.system("tput setaf 3")
        print("[ Installed Hadoop software ]***************************************************************\n\n\n")
    else:
        os.system("tput setaf 2")
        print("[ Installed Hadoop software ]***************************************************************\n\n\n")


    Java = subprocess.getstatusoutput("ssh {}  rpm -ivh /Menu-Driven-P/Hasoft/jdk-8u171-linux-x64.rpm".format(remote_IP))
    if(Java[0] == 0):
        os.system("tput setaf 3")
        print("[ Installed Java software ]*****************************************************************\n\n\n")
    else:
        os.system("tput setaf 2")
        print("[ Installed Java software ]*****************************************************************\n\n\n")


    DNodeM = subprocess.getstatusoutput("ssh {} mkdir -p /Menu-Driven-P/HadoopFiles/".format(remote_IP))
    if(DNodeM[0] == 0):
        os.system("tput setaf 3")
        print("[ Create a Directory to Manage the Hadoop core file ]******************************\n\n\n")
    else:
        os.system("tput setaf 2")
        print("[ Create a Directory to Manage the Hadoop core file ]******************************\n\n\n")

    def corehdfsfile():
        os.system("tput setaf 3")
        

        os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /Menu-Driven-P/HadoopFiles/core-site.xml")

        os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /Menu-Driven-P/HadoopFiles/core-site.xml")

        os.system('echo -e "\n<configuration>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

        os.system('echo -e "<property>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

        os.system('echo -e "<name>fs.default.name</name>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

        os.system('echo -e "<value>hdfs://{}:9001</value>" >> /Menu-Driven-P/HadoopFiles/core-site.xml'.format(NameNoIP))

        os.system('echo -e "</property>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

        os.system('echo -e "</configuration>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

    corehdfsfile()


    os.system("ssh {} rm -rf /etc/hadoop/core-site.xml".format(remote_IP))


    Tcore = subprocess.getstatusoutput("scp /Menu-Driven-P/HadoopFiles/core-site.xml root@{}:/etc/hadoop".format(remote_IP))
    if(Tcore[0] == 0):
        os.system("tput setaf 3")
        print("[ Transfer the core file to hadoop dir ]****************************************************\n\n\n")
    else:
        os.system("tput setaf 2")
        print("[ Transfer the core file to hadoop dir ]****************************************************\n\n\n")


    os.system("ssh {} figlet `jps`".format(remote_IP))
    os.system("tput setaf 4")
    os.system("ssh {} hadoop dfsadmin -report".format(remote_IP))
    os.system("tput setaf 7")


#DataNodefile()










