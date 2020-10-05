# Example

A copy of PyTiny to use with TravisCI

## Set up

```code
from pytiny import PyTiny

db = PyTiny()
```

## Functions

### Set

Set a key and value

```code
db.set("Key")
```

### Get

Get a value from a key

```code
db.get("Key", "Value")
```

### Delete

Delete a value from a key

```code
db.delete("Key")
```

### Reset

Reset the data. All data stored will be delete.

```code
db.reset()
```

### Export

Export the data to a .db file

```code
db.export()
```

### Bring

Import a file. This will be delete all data stored before, and will be restore the new data from the file.

```code
db.bring("file_name")
```
