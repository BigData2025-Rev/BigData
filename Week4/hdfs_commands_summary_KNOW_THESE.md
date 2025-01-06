## HDFS COMMANDS

hdfs fsck [location]
	- To check the health of our filesystem at a location 

hdfs dfs [-command]
	- Used to interact with hdfs

hdfs dfs -ls [hdfs location]
	- list files/dir in hdfs location

hdfs dfs -cat [hdfs file]
	- print file contents to terminal 

hdfs dfs -copyFromLocal [local file] [hdfs location]
	- Copy file from local fs and save to hdfs location

hdfs dfs -copyToLocal [hdfs file] [local location]
	- Copy file from hdfs and save to local location

hdfs dfs -mkdir [hdfs location]
	- Creates directory at hdfs location

hdfs dfs -rm [hdfs file]
	- Removes file in hdfs

hdfs dfs -rmdir [hdfs location]
	- Removes directory in hdfs 

hdfs dfs -help
	- Lists common commands/options for use with interacting with hdfs

hdfs dfs -put
	- Functionally same as copyFromLocal

hdfs dfs -get
	- Functionally same as copyToLocal






