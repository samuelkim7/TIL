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

### Examples

- Where Spark differs from other frameworks is that it can make some of the intermediate datasets persist across operations. For example, if wanted to reuse the errs dataset, we could create a cached RDD from it as follows: 

```scala
val cachedErrs = errs.cache()
```

