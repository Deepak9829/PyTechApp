import os
import subprocess
from Inventory import ListofDN

def DataNodefile():
    for remote_IP in ListofDN:
        subprocess.getoutput("printf '\n\n\n\n' | ssh-keygen")
        os.system("ssh-copy-id root@{}".format(remote_IP))
        Ddir = input("Enter DataNode Directory....:")
        NameNoIP = input(" Enter NameNode Public IP : ")
        
        DirData = subprocess.getstatusoutput("ssh root@{} mkdir /{}".format(remote_IP,Ddir))
        if(DirData[0] == 0 ):
            os.system("tput setaf 3")
            print("[ DataNode Directory Created ]**************************************************************\n\n\n")
        else:
            os.system("tput setaf 2")
            print("[ DataNode Directory Created ]**************************************************************\n\n\n")

        os.system("ssh root@{} mkdir -p /Menu-Driven-P/Hasoft/".format(remote_IP))

        Soft = os.system("scp -r /Menu-Driven-P/Hasoft/hadoop-1.2.1-1.x86_64.rpm root@{}:/Menu-Driven-P/Hasoft/".format(remote_IP))

        Soft = os.system("scp -r /Menu-Driven-P/Hasoft/jdk-8u171-linux-x64.rpm root@{}:/Menu-Driven-P/Hasoft/".format(remote_IP))
        """
        if(Soft[0] == 0):
            os.system("tput setaf 3")
            print("[ Upload the softwares ]********************************************************************\n\n\n")
        else:
            os.system("tput setaf 2")
            print("[ Upload the softwares ]********************************************************************\n\n\n")
        """

        Had = subprocess.getstatusoutput("ssh root@{}  rpm -ivh /Menu-Driven-P/Hasoft/hadoop-1.2.1-1.x86_64.rpm --force".format(remote_IP))
        if(Had[0] == 0):
            os.system("tput setaf 3")
            print("[ Installed Hadoop software ]***************************************************************\n\n\n")
        else:
            os.system("tput setaf 2")
            print("[ Installed Hadoop software ]***************************************************************\n\n\n")


        Java = subprocess.getstatusoutput("ssh root@{}  rpm -ivh /Menu-Driven-P/Hasoft/jdk-8u171-linux-x64.rpm".format(remote_IP))
        if(Java[0] == 0):
            os.system("tput setaf 3")
            print("[ Installed Java software ]*****************************************************************\n\n\n")
        else:
            os.system("tput setaf 2")
            print("[ Installed Java software ]*****************************************************************\n\n\n")


        DNodeM = subprocess.getstatusoutput("ssh root@{} mkdir -p /Menu-Driven-P/HadoopFiles/".format(remote_IP))
        if(DNodeM[0] == 0):
            os.system("tput setaf 3")
            print("[ Create a Directory to Manage the Hadoop core and hdfs file ]******************************\n\n\n")
        else:
            os.system("tput setaf 2")
            print("[ Create a Directory to Manage the Hadoop core and hdfs file ]******************************\n\n\n")

        def corehdfsfile():
            os.system("tput setaf 3")
            os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /Menu-Driven-P/HadoopFiles/hdfs-site.xml")

            os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml")

            os.system('echo -e "\n<configuration>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')

            os.system('echo -e "<property>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')

            os.system('echo -e "<name>dfs.data.dir</name>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')

            os.system('echo -e "<value>/{}</value>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml'.format(Ddir))

            os.system('echo -e "</property>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')

            os.system('echo -e "</configuration>" >> /Menu-Driven-P/HadoopFiles/hdfs-site.xml')


            os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /Menu-Driven-P/HadoopFiles/core-site.xml")

            os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /Menu-Driven-P/HadoopFiles/core-site.xml")

            os.system('echo -e "\n<configuration>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

            os.system('echo -e "<property>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

            os.system('echo -e "<name>fs.default.name</name>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

            os.system('echo -e "<value>hdfs://{}:9001</value>" >> /Menu-Driven-P/HadoopFiles/core-site.xml'.format(NameNoIP))

            os.system('echo -e "</property>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

            os.system('echo -e "</configuration>" >> /Menu-Driven-P/HadoopFiles/core-site.xml')

        corehdfsfile()



        os.system("ssh root@{} rm -rf /etc/hadoop/hdfs-site.xml".format(remote_IP))

        Thdfs = subprocess.getstatusoutput("scp /Menu-Driven-P/HadoopFiles/hdfs-site.xml root@{}:/etc/hadoop".format(remote_IP))
        if(Thdfs[0] == 0):
            os.system("tput setaf 3")
            print("[ Transfer the hdfs file to hadoop dir ]****************************************************\n\n\n")
        else:
            os.system("tput setaf 2")
            print("[ Transfer the hdfs file to hadoop dir ]****************************************************\n\n\n")

        os.system("ssh root@{} rm -rf /etc/hadoop/core-site.xml".format(remote_IP))


        Tcore = subprocess.getstatusoutput("scp /Menu-Driven-P/HadoopFiles/core-site.xml root@{}:/etc/hadoop".format(remote_IP))
        if(Tcore[0] == 0):
            os.system("tput setaf 3")
            print("[ Transfer the core file to hadoop dir ]****************************************************\n\n\n")
        else:
            os.system("tput setaf 2")
            print("[ Transfer the core file to hadoop dir ]****************************************************\n\n\n")



        Service = subprocess.getstatusoutput("ssh root@{} hadoop-daemon.sh start datanode".format(remote_IP))
        if(Service[0] == 0):
            os.system("tput setaf 3")
            print("[ Start DataNode Service ]******************************************************************\n\n\n")
        else:
            os.system("tput setaf 2")
            print("[ Start DataNode Service ]******************************************************************\n\n\n")

        Jps = subprocess.getstatusoutput("ssh root@{} jps".format(remote_IP))
        if(Jps[0] == 0):
            os.system("tput setaf 3")
            print("[ JPS verify Datanode ]*********************************************************************\n\n\n")
        else:
            os.system("tput setaf 2")
            print("[ JPS verify Datanode ]*********************************************************************\n\n\n")

        os.system("sleep 11")
        os.system("ssh root@{} figlet `jps`".format(remote_IP))

        os.system("tput setaf 4")
        os.system("ssh root@{} hadoop dfsadmin -report".format(remote_IP))
        os.system("tput setaf 7")

#DataNodefile()
