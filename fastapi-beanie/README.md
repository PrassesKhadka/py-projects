# FastAPI + MongoDB + Beanie + Docker

- Lifespan Events in FastAPI

- Async Context Manager in Python -> To manage resources asynchronously
  such as connecting to databases,opening files, or acquiring locks

```
from contextlib import asynccontextmanager

@asynccontextmanager -> Converts the function into something called and "async context manager"

- A context manager in Python is something that you can use in a `with` statement. For Example open() can be used as a context manager

with open("file.txt) as f:
    // code

async with lifespan(app):
    await do_stuff()

When you create a context manager or an async context manager like above, what it does is that, before entering the with block, it will execute the code before the yield, and after exiting the with block, it will execute the code after the yield.
```

Example code:

```
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_resource_manager():
    # Asynchronous setup code
    print("Acquiring resource")
    await asyncio.sleep(1)  # Simulate an async operation, e.g., connecting to a database
    resource = "my_resource"  # Replace with actual resource
    try:
        # The yield statement allows the function to temporarily return the
        # resource to the caller (the block of code that uses the context
        # manager). The code execution will pause here until the block completes.
        # Yield: The yield statement provides the resource to the block of code inside the async with statement.
        # After yield: cleanup code.

        yield resource  # This is where the resource is made available
    finally:
        # Asynchronous teardown code
        print("Releasing resource")
        await asyncio.sleep(1)  # Simulate an async operation, e.g., closing the database connection

async def main():
    <!-- resource from yield in async_resource_manager received here -->
    async with async_resource_manager() as resource:
        print(f"Using resource: {resource}")
        <!-- after this gets complete, finally in async_resource_manager() gets executed -->
        await asyncio.sleep(1)  # Simulate work with the resource

# Run the main function
asyncio.run(main())

```

## Working with beanie + Pydantic models

```
chocolate = Category(name="Chocolate", description="A preparation of roasted and ground cacao seeds.")

# Beanie documents work just like pydantic models
tonybar = Product(name="Tony's", price=5.95, category=chocolate)

# And can be inserted into the database
await tonybar.insert()

# You can find documents with pythonic syntax
product = await Product.find_one(Product.price < 10)

# And update them
await product.set({Product.name:"Gold bar"})
```

## MongoDB Shell (mongosh) cheat sheet

1. Connecting to MongoDB

```
Basic Connection:
mongosh "mongodb://localhost:27017"

Connect to a Specific Database:
mongosh "mongodb://localhost:27017/<database_name>"
```

2. Database Operations

```
Show All Databases:
show dbs

Switch to a Database:
use <database_name>

Show Current Database:
db

Database Statistics:
db.stats()
```

3. Collection Operations

```
List All Collections:
show collections

Create a Collection:
db.createCollection("<collection_name>")

Drop a Collection:
db.<collection_name>.drop()

Collection Statistics:
db.<collection_name>.stats()
```

4. CRUD Operations (Documents)

- Insert Documents

```
Insert a Single Document:
db.<collection_name>.insertOne({ key: "value" })

Insert Multiple Documents:
db.<collection_name>.insertMany([{ key: "value1" }, { key: "value2" }])
```

- Find Documents

```
Find All Documents:
db.<collection_name>.find()

Find with a Condition:
db.<collection_name>.find({ key: "value" })

Find One Document:
db.<collection_name>.findOne({ key: "value" })
```

- Update Documents

```
Update a Single Document:
db.<collection_name>.updateOne({ key: "value" }, { $set: { key2: "new_value" } })

Update Multiple Documents:
db.<collection_name>.updateMany({ key: "value" }, { $set: { key2: "new_value" } })
```

- Delete Documents

```
Delete a Single Document:
db.<collection_name>.deleteOne({ key: "value" })

Delete Multiple Documents:
db.<collection_name>.deleteMany({ key: "value" })
```

5. Indexing:

```
Create Index
db.<collection_name>.createIndex({ key: 1 })

List All Indexes:
db.<collection_name>.getIndexes()
```

6. Administrative Commands

```
Server Status
db.serverStatus()

Current Operations:
db.currentOp()

Kill an Operation:
db.killOp(<op_id>)
```

## Docker

- `docker-compose down` -> removes all containers,networks, and volumes
- `docker-compose stop` -> stops running containers without removing them.
- `docker-compose up --build`-> builds images before starting containers, regardless of whether the images already exist, usseful when you have updated code or dependencies in the Dockerfile(latest changes included)
- `docker-compose logs service_name -f / --tail=100`
