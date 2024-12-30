# MongoDB

- NoSQL query language
- NoSQL dbs include a lack of db schema, data clustering, replication support, eventual consistency, easily scalable
- MongoDB is a document based, NoSQL database

|RDBMS      |     MongoDB |
|-----------|-------------|
|Database    |    Database|
|Table       |    Collection|
|Row/record  |    Documents|
|Columns     |    Fields|
|JOIN        |    Embedded documents|

- BASE
    - Basically Available
        - Ensure availability of data by spreading and replicating data across nodes of the db cluster
    - Soft state
        - Due to lack of immediate consistency, data values may change over time. Developers are more
         responsible for enforcing consistency of data
    - Eventual consistency
        - Eventually, database will commit changes across the cluster to a consistent state

- In an RDBMS, we design our dbs using normalization
- In MongoDB, no rules for db design
    - Only thing that matters is making something that works for our application
- Sharding
    - Utilizing multiple systems to increase the resources in a server/cluster
    - Example of "horizontal scaling"