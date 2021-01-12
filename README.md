# Simple Python Database Connectors
__Basic Python 3 class for connecting to Databases__

I recommend using this as a super class for a custom class, as shown in the quickstart, but can be used without.

## Main goal
This is something I built for personal (local) projects. I'll expand this repository when I need a new type of database connection for a project. By doing it this way, I have a nice all-in one package for all my different database connections. The goal is to keep the code and package as small and lightweigth as possible.

## Supported Databases
__These databases are tested and working with the current build.__

- AzureSQL
- SQLServer Express 

__These databases should work, but are not (fully) tested__
- MySQL
- SQLite

### Defaults
- __port:__ _1433_
- __driver:__ _ODBC Driver 17 for SQL Server_

## Example Code
```python
from SimpleSQLConnector.Connectors import SQLConnector

class CustomSQLConnector(SQLConnector):
    def __init__(self,
            password,
            server="my-server-endpoint",
            database="my-database-name",
            username="my-db-username",
        ):
        super().__init__(username, password, server, database)

db = CustomSQLConnector(password="my-db-password")

# Get a user by his/her id
id = "00000000-1234-5678-abcd-000000000001" # example uuid4
result = db.get_item_by_id("User", id)

print(result)
```


## Wanted features
- [x] SQL Connector
- [ ] Database Cache
- [ ] MongoDB Connector