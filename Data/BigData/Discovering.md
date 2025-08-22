# Big Data Discovery Exercise

In this exercise we want you to work as a team to pull together a presentation on specific topics in **Big Data**.

The term **Big Data** relates to data that is too big to be stored on a single server.  Most big data systems can be ran as a single standalone system for learning, but in the real world the amount of data, in modern terms, is in excess of **Petabytes**.  For this to be sustainable and useable we need many computers to provide access to it.

Beyond **[Petabytes](https://www.idtech.com/blog/orders-of-magnitude-digital-data)**

* Exabyte - 10<sup>18</sup>
* Zettabyte - 10<sup>21</sup>
* Yottabyte - 10<sup>24</sup>

Systems such as;

* MongoDB
* HBase
* CouchDB
* RIAK
* DynamoDB

The choice of database is governed by the CAP theorem;

* C = Consistency
* A = Availability
* P = Partition tolerance

The choice is normally based on 2 of the above.

---

![CAP Theorem](images/scalability-cap-theorem1.webp)

> CAP Theorem diagram

---

Agents run on the servers to perform actions requested by users.  These agents communicate with each other to gather the required data for queries so that it can be compiled into a valid dataset to be returned to the user quickly.

The splitting of data across servers and disks is known as **sharding** (a form of partitioning of the data, but across servers, rather than just disk).  This splitting of data also allows for speed of data insert as well as reading and the resilience of the data is performed by ensuring that we always have 1 server that can become redundant.

---

![Sharding vs Partitioning](images/sharding_vs_partitioning.png)

> Partitioning vs Sharding diagram

---

![Sharding in action](images/DB-Shard-Pic-1-e1513014455288.png)

> Sharding in action

---

In the **Sharding diagram** we see that the **Tracking Table** is the virtual view of the data, but in reality that data is spread across different machines, and the agents on those systems will provide the complete view to the **requesting** agent.

There are many systems now available to store large amounts of data, starting with the Mother of all systems [Apache Hadoop](https://hadoop.apache.org).  All other systems came after.

Systems are now categorised into;

* Data Warehouse
* Data Lake
* Data Lakehouse

Increasing in size as we go down the list.

## A typical big data architecture

Large data systems require a structured architecture to manage disk and servers, and provide an interfaces to enable different data users to access the data in the way they need.

<center>

![Azure Synapse Analytics](images/cdmutilv2.webp)
Azure Synapse Analytics Architecture Diagram

---

![Spark Architecture](images/sparkArch.png)
Spark Architecture Diagram

---

![pySpark Architecture](images/pySparkArch.png)
PySpark Architecture Diagram
</center>

## Making data quickly available

The engineering process of making data available, mean we need a product pipeline.  This automates our manual process.  So you might have been thinking that Python isn't for me, but we need to automate the process of;

* Cleaning
* Transforming
* Providing

To produce a data product that can be consumed by our clients;

* Business Analysts
* Data Scientists
* Developers

Data is now a commodity that can be sold.  The better our product the more people are prepared to pay.

Map reduce is one task that allows us to divide tasks and divide into smaller parallel tasks.  Map reduce example can be found [here](../DataEng/README.md).

An ETL process can be found [here](../DataEng/DataEngTask2-ETL.md).

# The task

You will divide into teams, and be given a subject area relating to big data to research and present back.

The subject areas are;

* Big data - speed and performance: the need for big data
    * In this topic you need to cover the 4 Vs, telling us what they are and how different databases handle these.
* Processing big data
    * Tools and platforms used to manage and work with big data
    * Who are the big players in the data services and what are their products
    * What tools allow us to interact with them
* Data pipelines, ETL and map reduce
* Data Warehouse
    * What is it, what systems are there to store the data, and what software can be used to work with the data
    * What are Data warehouses being used for.  Who is using them and what for?
* Data Lakes
    * What is it, what systems are there to store the data, and what software can be used to work with the data
    * What are Data Lakes being used for.  Who is using them and what for?
* Data Lake House
    * What is it, what systems are there to store the data, and what software can be used to work with the data
    * What are Data Lake houses being used for.  Who is using them and what for?