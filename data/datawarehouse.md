### Star Schema 
- is a type of relational modeling technique that separates measures or events (facts) relating to a business process from their context (dimensions).
- more denormalized than relational database schemas (application databases)
- was designed to be efficient for Analytic queries (OLAP workloads).
- We can avoid UPDATEs, locking and the need for ACID compliance in a Data Warehouse by adapting `Star Schema` approach to leverage cheap cloud storage.
  - Foreign keys are hashes instead of integer sequences
  - Dimensions use daily snapshots
  - Facts are partitioned by `extraction date` to support idempotent processing and the potential overwriting of partitions
    - Extraction date: the date when the data was extracted from the source system.
    - Additionally, partitioning by the “event date” is recommended as queries will often use it as a filter (WHERE clauses).
    - Other partitioning keys can be added to additionally increase query speed
      - but we need to make sure they are used in filters, and the resulting files are not too small.
- Extensibility
  - A newly added fact can re-use the existing dimensions.
  - New dimensions can be added to facts by adding more foreign keys to the fact tables.  
    - As a result, new datasets can be integrated without introducing major changes to the schema.
    
### dimension snapshot
- Dimensions should be much smaller than facts. 
- The transactions, orders, and customer reviews (facts) of an e-commerce might be in the millions
- the number of unique customers (dimension) will be much smaller.
- Dimensions also differ from facts due to the “state” they carry. 
  - A record in a dimension will have an `identity` that needs to be preserved as other attributes change.
- Dimension snapshots are simple to manage
  - Every day we could re-write the entire dimension table in a versioned snapshot
    - s3://my_data_warehouse/dim_users/ds=2020-01-01
    - s3://my_data_warehouse/dim_users/ds=2020-01-02

### Late Arriving facts
- A fact row is late arriving if the most current dimensional context for new fact rows does not match the incoming row. 
- This happens when the fact row is delayed. 
- In this case, the relevant dimensions must be searched to ﬁnd the dimension keys that were effective when the late arriving measurement event occurred.

### Resource
- Ralph Kimball

### ETL
- Extract
  - You get the data out of its original source location (E)
- Transform
  - you do something to it (T)
- Load
  - then you load it (L) into a final set of tables for the business users to query.
