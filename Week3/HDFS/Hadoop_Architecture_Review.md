1)  Components of HDFS (Hadoop Distributed File System)

    a.  NameNode

        i.  A master server that manages the file system namespace and
            regulates access to files by clients

        ii. Manages all of the DataNodes on a HDFS cluster

        iii. Only one per cluster, but there can be any number of backup
             NameNodes

    b.  DataNodes

        i.  Manages storage attached to the node it is running on.

        ii. Data is stored in blocks (128 MB by default) which are
            replicated across other DataNodes in the cluster (3
            replications by default

2)  Components of YARN (Yet Another Resource Negotiator)

    a.  Resource Manager

        i.  Manage resources across all the nodes working in Hadoop

        ii. Manage the Node Managers

        iii. SCHEDULER

             1.  Fair Scheduler

                 a.  Schedule tasks based on a FIFO system

             2.  Capacity Scheduler

                 a.  Schedule tasks based on size of resources

        iv. APPLICATIONS MANAGER

            1.  Manages running of Application Master (inside of Node
                Manager) and helps to restart Application Master when it
                fails

    b.  Node Manager

        i.  \- Responsible for the execution of the task in each
            DataNode.

        ii. \- Manages workflow and user jobs on a specific node

        iii. \- Send a heartbeat to the Resource Manager with
             information of the resources in each container.

        iv. Container

            1.  Set of resources (RAM, CPU, Storage) on a single node.

            2.  Resources are allocated by the Resource Manager and
                monitored by the Node Manager

        v.  Application Master

            1.  Monitor the execution of tasks running on each node in
                the cluster.

            2.  Main responsibility is to negotiate resources from the
                Resource Manager

3)  Description of Unix

    a.  Unix is an operating system which allows us to write commands in
        a terminal that are interpreted into readable instructions for
        our processor. Linux is a family of open-source Unix-like OSs.
        On Windows, we run a distribution of Linux (Ubuntu) on a Virtual
        Machine (VM) (WSL). We write instructions using the shell
        (terminal), which communicates with the kernel to execute those
        instructions.
