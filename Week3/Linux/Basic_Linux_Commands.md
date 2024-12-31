# Commands

## pwd
    - print absolute path of present working directory
    - Absolute Path
        - Path to directory or file starting from the root directory
    - Relative path
        - Path to directory or file starting from the pwd
    - Home directory
        - Denoted with ~
    - Root directory
        - Uppermost parennt directory in fs
        - Denoted with /

## ls
    - list files/directories in pwd
    - commonly used with -al

## cd
    - change directory
    - followed by path to wanted directory
        - Can use absolute path or relative path

## mkdir [directory name]
    - Create new directory

## echo [text ]
    - prints text to console
    - Output can be redirected with > or >>

## cat [file name]
    - Concatenate file
    - Prints file contents to console

## cp [file name] [new location]
    - copy a file

## mv [file name] [location/new file name]
    - move a file
    - can be used to rename a file

## rm [file name]
    - remove file
    - can be used with -r to recursively delete a directory

## grep [pattern ] [file name]
    - Search a file for a pattern and return the matching lines
    - -i
        - Case insensitive
    - -c
        - Count of lines that match

## chmod
    - Changing permissions on a file