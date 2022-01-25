import os
import subprocess

def HadoopNameNode():
    IP = input("Enter NameNode IP : ")

    subprocess.getoutput("printf '\n\n\n\n' | ssh-keygen")
    os.system("ssh-copy-id root@{}".format(IP))

    os.system("ssh root@{} figlet HADOOP NAMENODE".format(IP))
    Ndir = input("Enter Namenode Directory....:")
    os.system("ssh root@{} mkdir -p /Menu-Driven-P/Hasoft/".format(IP))
    Soft = os.system("scp -r /Menu-Driven-P/Hasoft/hadoop-1.2.1-1.x86_64.rpm root@{}:/Menu-Driven-P/Hasoft/".format(IP))

    Soft = os.system("scp -r /Menu-Driven-P/Hasoft/jdk-8u171-linux-x64.rpm root@{}:/Menu-Driven-P/Hasoft/".format(IP))
    """
    if(Soft[0] == 0):
        os.system("tput setaf 3")
        print("[ Upload the softwares ]********************************************************************\n\n\n")
    else:
        os.system("tput setaf 2")
        print("[ Upload the softwares ]********************************************************************\n\n\n")
    """
    HD=subprocess.getstatusoutput("ssh root@{} mkdir /{}".format(IP,Ndir))

    if(int(HD[0])==0):
        os.system("tput setaf 11")
        print("[ Create Namenode Directory ]*************************************************************************************************************\n\n\n")
    else:
        os.system("tput setaf 2")
        print("[ Create Namenode Directory ]*************************************************************************************************************\n\n\n")
        #print(HD[1])

    os.system("tput setaf 7")

    hsoft = subprocess.getstatusoutput("ssh root@{} rpm -ivh /Menu-Driven-P/Hasoft/hadoop-1.2.1-1.x86_64.rpm --force".format(IP))
    if(int(hsoft[0])==0):
        os.system("tput setaf 11")
        print("[ Installed Hadoop software ]*************************************************************************************************************\n\n\n")
    else:
        os.system("tput setaf 2")
        print("[ Install Hadoop software**********************************************************************************************************************]")
        print(hsoft[1],"\n\n\n")

    os.system("tput setaf 7")
    Java = subprocess.getstatusoutput("ssh root@{} rpm -ivh /Menu-Driven-P/Hasoft/jdk-8u171-linux-x64.rpm".format(IP))

    if(int(Java[0])==0):
        os.system("tput setaf 11")
        print("[ Installed Java software ]***************************************************************************************************************\n\n\n")
    else:
        os.system("tput setaf 2")
        print("[ Install Java software************************************************************************************************************************]")
        print(Java[1],"\n\n\n")


    os.system("tput setaf 11")
    print("[ Configure hdfs-site.xml File ]**************************************************************************************************************\n\n\n")

    os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /Menu-Driven-P/HadoopFiles/hdfs-site.xml")

    os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml")

    os.system('echo -e "\n<configuration>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')

    os.system('echo -e "<property>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')

    os.system('echo -e "<name>dfs.name.dir</name>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')

    os.system('echo -e "<value>/{}</value>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml'.format(Ndir))

    os.system('echo -e "</property>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')

    os.system('echo -e "</configuration>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')

    print("[ Configure Core-site.xml file ]**************************************************************************************************************\n\n\n")

    os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /Menu-Driven-P/HadoopFiles/core-site.xml")

    os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /Menu-Driven-P/HadoopFiles/core-site.xml")

    os.system('echo -e "\n<configuration>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

    os.system('echo -e "<property>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

    os.system('echo -e "<name>fs.default.name</name>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

    os.system('echo -e "<value>hdfs://0.0.0.0:9001</value>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

    os.system('echo -e "</property>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

    os.system('echo -e "</configuration>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

    print("[ upload the hdfs or core file to the hadoop directory ]******************************************************************************************\n")
    os.system("ssh root@{} rm -rf /etc/hadoop/hdfs-site.xml".format(IP))

    os.system("scp -r /Menu-Driven-P/HadoopFiles/hdfs-site.xml root@{}:/etc/hadoop".format(IP))

    os.system("ssh root@{} rm -rf /etc/hadoop/core-site.xml".format(IP))

    os.system("scp -r /Menu-Driven-P/HadoopFiles/core-site.xml root@{}:/etc/hadoop".format(IP))

    print("\n")
    """Format = subprocess.getstatusoutput("hadoop-daemon.sh stop namenode")
    if(int(Format[0])==0):
        os.system("tput setaf 3")
        print("[ Installed Hadoop software*****************************************************************]")
    else:
        os.system("tput setaf 1")
        print("[ NameNode Directory Formated***************************************************************]")
        print(Format[1])
    
    """

    Format = subprocess.getstatusoutput("ssh root@{} echo Y | hadoop namenode -format".format(IP))
    if(int(Format[0])==0):
        os.system("tput setaf 11")
        print("[ Format Namenode Directory********************************************************************************************************************]")
        print(Format[0])
    else:
        os.system("tput setaf 2")
        print("[ Format Namenode Directory********************************************************************************************************************]")
        #print(Format[1])
    print("\n\n\n")

    Service = subprocess.getstatusoutput("ssh root@{} hadoop-daemon.sh start namenode".format(IP))
    if(int(Service[0]==0)):
        os.system("tput setaf 11")
        print("[ Start Namenode service ]**********************************************************************************************************************")
    else:
        os.system("tput setaf 2")
        print("[ Start Namenode service ]**********************************************************************************************************************")

    print("\n\n\n")

    print("[ Run JPS CMD to verify ]***************************************************************************************************************************")
    os.system("sleep 10")
    os.system("ssh root@{} jps".format(IP))
    os.system("tput setaf 15")



#HadoopNameNode()
