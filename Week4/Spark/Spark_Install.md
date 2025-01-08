# Spark Installation Instructions

## 1) Download and untar Spark binaries

```
wget https://dlcdn.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz

tar -xvzf spark-3.5.3-bin-hadoop3.tgz
```

## 2) Move spark directory

```
cd ~

sudo mv spark-3.5.3-bin-hadoop3 /opt/spark
```

## 3) Setup environment variables

```
sudo vim ~/.bashrc
```

Place theses exports at the bottom of the file:

```
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```

Save and exit, then source the bashrc file:

```
source ~/.bashrc
```

## 4) Install python (if not installed)
Install pip3 as well.

```
sudo apt install python3 -y
sudo apt install python3-pip -y
```

## 5) Install pySpark using pip

```
pip3 install pyspark
```