# OS_Final_Project

### Group Members: Marissa White, Thomas O’Toole, Will Hoppe

This guide will take you through steps that demonstrate the functionality of our final project.

## Using the help command

All commands can utilize the --help flag to give useful information about how to run the command. Here are a few examples:

```bash
python3 cli.py search --help
python3 cli.py read --help
python3 cli.py create --help
```

## Validating a database entry

```bash
python3 cli.py validate '{"title": "newly created movie", "content": "Here is a new content entry", "tags": ["new", "movie", "tags"]}'
```

It will tell you that the data is valid. Here is an example with an invalid database entry:

```bash
python3 cli.py validate '{"invalid": "entry", "keys that are missing": ["title", "content", "tags"]}'
```

## Creating a database entry

```bash
python3 cli.py create '{"title": "newly created movie", "content": "Here is a new content entry", "tags": ["new", "movie", "tags"]}'
```

A new database entry can be created with this command. It will only be added to the database if it is valid against the schema. Here is an example of trying to create an invalid entry.

```bash
python3 cli.py create '{"invalid": "entry", "keys that are missing": ["title", "content", "tags"]}'
```

## Searching for a database entry by keyword

```bash
python3 cli.py search --keyword tags --value 'new'
```

This command searches through only the tags keyword of each entry, and it will show the entry you just created because it contains the tag ‘new’. You could change the value of the search to find new examples. Try searching for database entries with the tag ‘Horror’. Searches are case sensitive.

```bash
python3 cli.py search --keyword tags --value 'Horror'
```

## Searching for a database entry by value

```bash
python3 cli.py search --value 'created'
```

This command searches through all keywords of each entry, searching through every field of the data since a keyword is not specified. It will also show the entry you just created because it contains the ‘created’ in the title.

## Reading all entries

```bash
python3 [cli.py](http://cli.py/) read --all
```

This displays all database entries.

## Reading an entry by ID

```bash
python3 [cli.py](http://cli.py/) read --id 9
```

This shows the entry stored in the database at ID 9.

## Updating an entry by ID

```bash
python3 cli.py search --update 9 --value '{"title": "updated movie", "content": "Here is an updated content entry", "tags": ["updated", "movie", "tags"]}'
```

This command updates the entry with ID 9 with the information entered after --value. It must match the schema for it to be validated and updated.

Try running the read --id 9 command again to check whether it updated.

```bash
python3 [cli.py](http://cli.py/) read --id 9
```

## Deleting an entry by ID

```bash
python3 cli.py delete --id 9
```

This deletes the entry stored with ID 9. Try running the read --id 9 command again to check whether it is deleted. It will say entry not found when deleted properly.

```bash
python3 [cli.py](http://cli.py/) read --id 9
```

## Deleting all entries

```bash
python3 cli.py delete --all
```

This will delete all entries in the database. To see whether all are deleted run the read all command or look in the database file. 

```bash
python3 [cli.py](http://cli.py/) read --all
```

## Creating a new database

If you wish to create a new database to run any tests again, run the database_gen.py file to create a new database full of 10000 entries of randomly generated movies. This is what we used to test our cli.py program.

```bash
python3 database_gen.py
```