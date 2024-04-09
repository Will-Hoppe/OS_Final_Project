#!/usr/bin/env python

import os
import typer
import json

app = typer.Typer()


# def read_file(filename: str):
#     """Read the content of a file and print it."""
#     try:
#         with open(filename, 'r') as file:
#             typer.echo(f"Content of '{filename}':\n{file.read()}")
#     except:
#         typer.echo(f"File '{filename}' not found.")

# def update_file(filename: str, new_content: str):
#     """Append new content to an existing file."""
#     try:
#         with open(filename, 'a') as file:
#             file.write(new_content)
#         typer.echo(f"File '{filename}' updated successfully.")
#     except:
#         typer.echo(f"File '{filename}' not found for updating.")

# def delete_file(filename: str):
#     """Delete a file from the disk."""
#     if os.path.exists(filename):
#         os.remove(filename)
#         typer.echo(f"File '{filename}' deleted successfully.")
#     else:
#         typer.echo(f"File '{filename}' not found for deletion.")

# def search_character(filename: str, character: str):
#     """Search for a character in the content of a file."""
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#             found = 0
#             with typer.progressbar(content) as progress:
#                 for char in progress:
#                     if char == character:
#                         found += 1
#             typer.echo(f"Character '{character}' found {found} times in '{filename}'.")
#     except FileNotFoundError:
#         typer.echo(f"File '{filename}' not found.")
        
def validate(json_entry):
    return True

@app.command()
def create(entry: str):
    """Create a new entry with the specified json content."""
    try:
        with open('database.json', 'r') as file:
            database = json.load(file)
    except FileNotFoundError:
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
def update(id: str, entry: str):
    """Update the content of a database entry."""
    with open('database.json', 'r') as file:
        database = json.load(file)
        for i in range(len(database["entries"])):
            if str(database["entries"][i]["id"]) == id:
                if validate(entry):
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
        typer.echo(f"Error: Database entry {id} does exist.")

@app.command()
def delete(filename: str):
    """Delete a file."""
    pass

@app.command()
def search(value: str, update: str, keyword: str):
    """Search for something in database"""
    

if __name__ == "__main__":
    app()