# Basics
- The contract between two micro-services is the data itself. That contract is enforced by schemas

## Schema Registry
- Confluent Schema Registry provides a serving layer for your metadata. 
- It provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and Protobuf schemas. 
- It stores a versioned history of all schemas based on a specified subject name strategy, provides multiple compatibility settings and allows evolution of schemas according to the configured compatibility settings and expanded support for these schema types.
```
 {"namespace": "example.avro",
 "type": "record",
 "name": "user",
 "fields": [
     {"name": "name", "type": "string"},
     {"name": "favorite_number",  "type": "int"}
 ]
}
```
