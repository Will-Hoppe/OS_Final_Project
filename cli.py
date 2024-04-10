#!/usr/bin/env python

import os
import typer
import json
from jsonschema import validate as validate_json
from jsonschema.exceptions import ValidationError
app = typer.Typer()

@app.command()
def validate(entry: str):
    """Validate data against schema"""
    with open('schema.json', 'r') as schema_file:
        schema = json.load(schema_file)
    try:
        validate_json(instance=json.loads(entry), schema=schema)
        typer.echo('Data is valid against schema')
        return True
    except ValidationError as e:
        typer.echo('Data is not valid against schema')
        return False

@app.command()
def create(entry: str):
    """Create a new entry with the specified json content."""
    try:
        with open('database.json', 'r') as file:
            try:
                database = json.load(file)
            except json.JSONDecodeError:
                typer.echo("Error: database.json contains invalid JSON content.")
                database = {"entries": [], "max_id": 0}
    except FileNotFoundError:
        # If database.json doesn't exist or is empty, create it with default content
        database = {"entries": [], "max_id": 0}
    json_entry = json.loads(entry)
    json_entry["id"] = database["max_id"]
    database["max_id"] += 1
    database["entries"].append(json_entry)
    if validate(entry):
        with open("database.json", 'w') as file:
            json.dump(database, file)
        typer.echo(f"Database entry created successfully.")
    else:
        typer.echo(f"Error: Database entry does not fit schema.")

@app.command()
def delete(filename: str):
    """Delete a file."""
    pass

@app.command()
def search(entry: str = typer.Option(None, "--value", help="Find entered value within data"),
           keyword: str= typer.Option(None, "--keyword", help="Specify part of data to find value"),
           id: str= typer.Option(None, "--update", help="Update record with new data")):
    """Search for something in database"""
    try:
        with open('database.json', 'r') as file:
            database = json.load(file)
            if id is not None:
                idfound=False
                for i in range(len(database["entries"])):
                    if str(database["entries"][i]["id"]) == str(id):
                        idfound=True
                        print(entry)
                        if entry is None:
                            typer.echo("No new data provided to update")
                            return
                        elif validate(entry):
                            json_entry = json.loads(entry)
                            json_entry["id"] = id
                            database["entries"][i] = entry
                            with open("database.json", 'w') as file:
                                typer.echo(f"Database entry updated successfully.")
                                json.dump(database, file)
                                return
                        else:
                            typer.echo(f"Error: Database entry does not fit schema.")
                            return
                if idfound==False:
                    typer.echo(f"Error: Database entry {id} doesn't exist.")
            elif keyword is not None:
                found=False
                if entry is None:
                    typer.echo(f"No value provided to search for")
                    return
                for i in range(len(database["entries"])):
                    option=str(database["entries"][i][keyword])
                    if entry in option:
                        found=True
                        typer.echo("Entry with value {}: {}".format(entry, database["entries"][i]))
                if not found:
                    typer.echo("No entry with value {} found".format(entry, database["entries"][i]))
            elif entry is not None:
                found=False
                for i in range(len(database["entries"])):
                    allparts=database["entries"][i]
                    print(allparts)
            else:
                typer.echo("Provide flags to use search")
    except FileNotFoundError:
        typer.echo("Error: database.json not found.")
    except json.JSONDecodeError:
        typer.echo("Error: database.json contains invalid JSON content.")
    
@app.command()
def read(all: bool = typer.Option(False, "--all", help="Read all entries"),
         id: int = typer.Option(None, "--id", help="Read entry with specified ID")):
    """Search for something in database"""
    try:
        with open('database.json', 'r') as file:
            database = json.load(file)
            if all:
                typer.echo("All entries:")
                for entry in database["entries"]:
                    typer.echo(entry)
            elif id is not None:
                entry_found = False
                for entry in database["entries"]:
                    if entry.get("id") == id:
                        typer.echo("Entry with ID {}: {}".format(id, entry))
                        entry_found = True
                        break
                if not entry_found:
                    typer.echo(f"Entry with ID {id} not found.")
            else:
                typer.echo("Please provide an option: --all or --id.")
    except FileNotFoundError:
        typer.echo("Error: database.json not found.")
    except json.JSONDecodeError:
        typer.echo("Error: database.json contains invalid JSON content.")
    

if __name__ == "__main__":
    app()