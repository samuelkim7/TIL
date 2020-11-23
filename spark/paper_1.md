## Spark: Cluster Computing with Working Sets

Matei Zaharia et al.
UC, Berkeley

### Introduction
- This paper focuses on one such class of applications: those that reuse a working set of data across multiple parallel operations. This includes many iterative machine learning algorithms, as well as interactive data analysis tools.

### Programming Model
- Users can explicitly cache an RDD in memory across machines and reuse it in multiple MapReduce-like parallel operations.

- A resilient distributed dataset (RDD) is a read-only collection of objects partitioned across a set of machines that can be rebuilt if a partition is lost.

- partitions of a dataset are materialized on demand when they are used in a parallel operation (e.g., by passing a block of a file through a map function), and are discarded from memory after use. However, a user can alter the persistence of an RDD through two actions: 
  - The cache action leaves the dataset lazy, but hints that it should be kept in memory after the first time it is computed, because it will be reused. 
  - The save action evaluates the dataset and writes it to a distributed filesystem such as HDFS. The saved version is used in future operations on it.

- Several parallel operations can be performed on RDDs: reduce, collect, and foreach.

### Examples
1. Text Search
- Suppose that we wish to count the lines containing errors in a large log file stored in HDFS.

```scala
val file = spark.textFile("hdfs://...")
val errs = file.filter(_.contains("ERROR"))
val ones = errs.map(_ => 1)
val count = ones.reduce(_+_)
```

- Where Spark differs from other frameworks is that it can make some of the intermediate datasets persist across operations. For example, if wanted to reuse the errs dataset, we could create a cached RDD from it as follows: 

```scala
val cachedErrs = errs.cache()
```

2. Logistic Regression
The algorithm performs gradient descent: it starts *w* at a random value, and on each iteration, it sums a function of *w* over the data to move *w* in a direction that improves it. It thus benefits greatly from caching the data in memory across iterations. 

3. Alternating Leat Squares
ALS is used for collaborative filtering problems, such as predicting users’ ratings for movies that
they have not seen based on their movie rating history.

### Implementation
- Spark is built on top of Mesos, a “cluster operating system” that lets multiple parallel applications share a cluster in a fine-grained manner and provides an API for applications to launch tasks on a cluster.
 
- When a parallel operation is invoked on a dataset, Spark creates a task to process each partition of the dataset and sends these tasks to worker nodes.

### Results
- (Logistic Regression using 29 GB dataset) With Hadoop, each iteration takes 127s, because it runs as an independent MapReduce job. With Spark, the first iteration takes 174s (likely due to using Scala instead of Java), but subsequent iterations take only 6s, each because they reuse cached data. This allows the job to run up to 10x faster.

- We used the Spark interpreter to load a 39 GB dump of Wikipedia in memory across 15 “m1.xlarge” EC2 machines and query it interactively. The
first time the dataset is queried, it takes roughly 35 seconds, comparable to running a Hadoop job on it. However, subsequent queries take only 0.5 to 1 seconds, even if they scan all the data. 

### Related Work
- Spark reconstructs lost partitions of RDDs using lineage information captured in the RDD objects.

- Spark’s parallel operations fit into the MapReduce model [11]. However, they operate on RDDs that can persist across operations. ... This also
makes Spark useful for interactive data analysis, where a user can define several datasets and then query them.
