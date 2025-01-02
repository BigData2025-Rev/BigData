# Hadoop Install

## 1) SSH Localhost

Make sure you can SSH to localhost

```
ssh localhost
```

If you encounter the error ssh: connect to host localhost port 22: Connection refused, run the following commands:

```
sudo apt remove openssh-server
sudo apt install openssh-server
sudo service ssh start
```

If you cannot ssh to localhost without a passphrase, run the following command to initialize your private and public keys:

```
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```

## 2) Java

Update the package index:
```
sudo apt update
```

Check whether Java is already installed:

```
java -version
```

If Java isn't installed:
```
sudo apt-get install openjdk-8-jdk
```

Check the version installed:
```
java -version
```

## 3) Download Hadoop Binary

Visit the Hadoop releases page to find a download URL for Hadoop (3.3.6):

https://hadoop.apache.org/releases.html

Run the following command to download the latest binary for Hadoop 3.3.6:

```
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
```

## 4) Unzip binary

Create a hadoop folder under the user home folder:

```
mkdir ~/hadoop
```

Unzip the binary package:

```
tar -xvzf hadoop-3.3.6.tar.gz -C ~/hadoop
cd ~/hadoop/hadoop-3.3.6/
```

## 5) Setup environment variables

```
vim ~/.bashrc
```

Setup Hadoop and Java environment variables at the end of the .bashrc file as below and then save the bash file and close it (make sure java home is correct):

```
#Set Hadoop-related environment variables
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=~/hadoop/hadoop-3.3.6
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
```

To apply changes, source the .bashrc file:
```
source ~/.bashrc
```

## 6) Configure for pseudo distributed mode

```
cd ~/hadoop/hadoop-3.3.6/etc/hadoop
```

### 1) Edit hadoop-env.sh

```
vim hadoop-env.sh
```

Set Java env variable as (where it is on your system):
```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

### 2) Edit core-site.xml

```
vim core-site.xml
```

Add the following configuration:
```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

### 3) Edit hdfs-site.xml

```
vim hdfs-site.xml
```
Add the following configuration:
```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

### 4) Edit mapred-site.xml

```
vim mapred-site.xml
```

Add the following configuration:
```
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
</configuration>
```

### 5) Edit yarn-site.xml
```
vim yarn-site.xml
```

Add the following configuration:
```
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>
```

### Format namenode

```
cd ~/hadoop/hadoop-3.3.6
bin/hdfs namenode -format
```

## 7) Start daemons
```
cd ~/hadoop/hadoop-3.3.6
```

```
sbin/start-dfs.sh
```

```
sbin/start-yarn.sh
```

Check daemons running using jps:
```
jps
```

## 8) Stop daemons

```
sbin/stop-yarn.sh
sbin/stop-dfs.sh
```


### (OPTIONAL) 9) POSSIBLE ERROR

if you get  call from ...localhost:9000 failed connection exception java.netConnectException: Connection refused

```
vim $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```


add in :
```

<property>
<name>dfs.namenode.name.dir</name>
<value>/home/<user>/hadoop/hadoop-3.3.6/dfs/namenode</value>
</property>
 
<property>
<name>dfs.datanode.data.dir</name>
<value>/home/<user>/hadoop/hadoop-3.3.6/dfs/datanode</value>
</property>
```
then
```
mkdir -p $HADOOP_HOME/dfs/namenode
mkdir -p $HADOOP_HOME/dfs/datanode

cd $HADOOP_HOME

chmod 755 dfs

cd bin

hdfs namenode -format
```
(also https://stackoverflow.com/questions/11889261/datanode-process-not-running-in-hadoop)