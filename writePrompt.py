#!/usr/bin/env python3

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
        file.close()
        return True
