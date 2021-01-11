# Simple Python SQL Connector

__Basic Python 3 class for connecting to a SQL Database__

This is writen to be used in a project for my education that uses AzureSQL.
I recommend using this as a super class for a custom class, as shown in the quickstart, but can be used without.

### Defaults
- __port:__ _1433_
- __driver:__ _ODBC Driver 17 for SQL Server_

### Quickstart
`pip install -r requirements.txt`

__CODE:__
```python
from SimpleSQLConnector.connector import SQLConnector

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