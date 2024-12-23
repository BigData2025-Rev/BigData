## Databases

A Database is an application that provides long term data storage and functionality to efficiently access the stored data.  Typically, we write applications that communicate with databases, though databases will also allow us to *query* them directly.  Querying lets us Create, Retrieve, Update, and Delete data in the database (CRUD).  End users do not communicate with your database.  An application (written in Scala) that runs on a server might only stay alive for an hour, day, week, month, ...  When that application goes down, all the values it has stored in memory disappear.  The database provides storage that persists through multiple application lifetimes.

Why not write to file instead of using a database?  The first reason is efficient access.  Data stored in a file is just stored sequentially, without any useful additional structure.  Any DB we use is going to give us the tools to quickly access/query the data stored within.  There are other benefits as well.  Your DB is an application that can communicate with other applications over a network, so multiple applications can use a single DB for their long term storage.  Most DBs also provide access control features.


## JSON: JavaScript Object Notation

An object with properties (key-value pairs) that demonstrate JSON data types:
{
    "string": "myString",
    "number": 123,
    "object": {},
    "array": [],
    "boolean": true,
    "null": null
}

valid JSON:
[{}, {}]

JSON is text.  It's useful because it contains a little bit of structure, but not too much (it's not like an XML document).

For adding to MongoDB collection:
{
    "_id": {
        "$oid": "5f85c72ca1756421a027327f"
    },
    "title": "neat comic"
}
{
    "_id": {
        "$oid": "5f85d1b2a1756421a0273281"
    },
    "title": "example title"
}

## CRUD

Create, Retrieve/Read, Update, Delete.  We talk about CRUD operations with respect to databases, they are just the basic operations that let us save new data, modify data, read data, and remove data.  For mongo scala: find(), deleteMany(), replaceOne(), insertMany(), ...

## CAP Theorem

CAP is Consistency, Availability, and Partition Tolerance.  The CAP Theorem says that we can only ever have 2 of the 3 guaranteed in a distrbuted data store.
- Consistency : every read receives the most recent write or an error.
- Availability : every request receives a non-error response.  It may not contain the most recent write.
- Partition Tolerance : the system continues to operate despite some network failure.
Every distributed data store, when there are no network problems, gives us consistency and availability.  However, network problems can and do always occur.  Different distributed data stores make different tradeoffs when this happens.  Due to CAP theorem, when a network failure occurs we need Partition Tolerance, which means we give up either Consistency or Availability.  This is a decision we make when setting up the cluster (including by deciding what distributed data store to use).

## Transactions and atomicity

A transaction is an interaction with the database.  What exactly a transaction provides differs based on the data store you are using and configuration options on that data store.  We often use the word "atomic" to refer to transactions or other operations on a data store.  Anything that is atomic is indivisible, which means it succeeds or fails as a single unit.  In MongoDB this is easy, operations on a single document are atomic, operations otherwise (with one exception) are not.  If I replaceOne for a document in a Mongo collection, either that document will be entirely replaced, or no change will occur.  We'll never encounter a half-replaced document.  If I update two different documents with an updateMany, it's entirely possible that one update will succeed and the other will fail.  This behaviour is something we need to consider when we're deciding on our data model.  Two documents that are modified at the same time frequently should probably be embedded.  Modifications to embedded documents are atomic, modifications to documents related by a reference are not.

In recent versions of Mongo they offer support for multi-document transactions, which can give us atomicity for operations across multiple documents.  This is slower than the default single-document atomic operations.

## RDBMS Intro

RDBMS is Relational DataBase Management System.  RDBMS is a SQL database, as opposed to a NoSQL database.  SQL databases have been around for a long time and are widely used.  In general, an RDBMS requires a lot more structure than a NoSQL database.  In our RDBMS we strictly define tables contained in schema contained in databases, providing exactly the datatypes necessary for each record.  RDBMSs use SQL (Structured Query Language) to achieve CRUD functionality.  Each RDBMS vendor has a slightly different version of SQL, but base SQL is widespread and used even outside of RDBMSs.

In an RDBMS, we have less flexibility with the structure of our records than in Mongo.  In addition, we have strict rules for our data model.  There rules are called *normalization* and are described in a series of *normal forms*.  We should know that RDBMSs are normalized but we don't need to know all the specifics.  We do need to know that normalization means there are no embedded records in an RDBMS, all multiplicity relationships are achieved using references (Foreign keys).

Interactions with an RDBMS take place in Transactions, and transaction in an RDBMS have ACID properties:

## ACID

- Atomicity : a transaction succeeds or fails and a single unit
- Consistency : a transaction takes the database from one valid state to another (NOT the same as CAP Consistency)
- Isolation : multiple transactions taking place at the same time don't interfere with each other
- Durability : transactions satisfy ACID even in the case of disaster (power shut off to DB)
It's useful to start thinking about ACID as a property of SQL databases, but really SQL and NoSQL databases both implement useful features of the other.  Mongo introduced multi-document transactions with atomicity in 4.4.  In PostgreSQL (an RDBMS) you can store and index nested JSON, similar to a mongoDB document without any of the typical RDBMS structure.  We can say ACID favors Consistency and Partition Tolerance in a distributed database, as opposed to...

## BASE

- Basically Available : reads and writes are available as much as possible, using multiple machines in a cluster
- Soft state : records stored in the database may be inconsistent across a cluster, some may be more up to date than others
- Eventual consistency : if the databases runs long enough, it will achieve consistent data across the cluster
BASE favors Availability and Partition Tolerance in a distributed database.

## Aside: Lazy vs Eager fetching/loading

Loading something *eagerly* means that it is retireved immediately.  You say "I want this content from the database/file/datasource/..." and the content is retrieved.  Loading something lazily means it is retrieved only when it is actually used.  You say "I want this content from the database/file/datasource/..." and a proxy for that data is retrieved.  You can use the proxy exactly the same as you would use the real data, but the real data isn't populated until you actually use the proxy for something.  Both are reasonable strategies, it depends on context.  
If the connection is closed in the meantime, it will cause you problems for lazily loaded data.

## SQL : Structured Query Language
SQL is a query language, which means its used to query for data.  It's declarative, in that we tell our database the data we want using SQL rather than specifying exactly what we want to DB to do.  (Almost) every DB has a query planner or similar that will show you the DB's actual plan for resolving your declared query.

The are many different "dialects" of SQL.  Each major RDBMS has its own implementation, so major RBDMSs differ on their execution of some SQL functionality.  There's "core SQL" or "ANSI SQL" that is very nearly the same across DBs, and then each DB provides their own additional functionality outside of this.  We often divide SQL into sublanguages, just for organization.  Those would be:
- Data Manipulation Language (DML) : used to manipulate data, adds/removes/edits records contained within tables
- Data Definition Language (DDL) : used to manipulate tables, adds/removes/modifies tables themselves
- Data Query Language (DQL) : used to retrieve data.  Sometimes lumped in with DML.
Two more that I'll list here for completeness but we don't need to know about:
- Transaction Control Language (TCL) : used to start/stop and delimit transactions.
- Data Control Language (DCL) : used to manage DB users, grant permissions, revoke permissions

In SQL / RDBMSs we have schemas that contain tables that contain records, analogous to mongo's databases that contain collections that contain documents.  In SQL we define columns for each table, and each record in that table has all of those columns.  You can have null values in SQL, but you can't have the column be missing.
Some other terms for the above : schema is sometimes called database, table is sometimes called relation, records are somtimes rows.

We identify the sublanguage based on the first keyword, so keywords for sublanguages:
- DML : INSERT, UPDATE, DELETE
- DDL : CREATE, ALTER, DROP
- DQL : SELECT

SELECT "clauses":
- SELECT specifies columns
- FROM specifies the table
- WHERE filters the records
- ORDER BY orders the results
- LIMIT limits the output to some number of records
- OFFSET skips some number of records at the beginning of the output


## FAQ:

- What does "valid state" mean when we talk about Consistency in ACID?  In an RDBMS, we have a lot of structure and a lot of rules for what our data can look like.  Attempting to break those rules in a Transaction will cause the transaction to fail.  This might be using the wrong data types, failing checks on length/null, or it might mean specifying references that don't exist.
- *Primary Key* : A Primary key is a unique identifier for some object.  In Mongo, the _id field is that primary key.  In an RDBMS we create our own primary key fields.
