# How to activate virtual environment

Open a new terminal. This should open within the 'coding' folder. If not, find your way to it using `cd FOLDER_NAME` and `ls` to see what is in each folder. 

Once in the coding folder type:
```
.venv\Scripts\activate
```

This should make the folder path change from: 

```
PS C:\Users\rmacdonald\OneDrive - Blyth & Blyth Consulting Engineers\Desktop\Work\Work 2\coding>
```

to 
```
(.venv) PS C:\Users\rmacdonald\OneDrive - Blyth & Blyth Consulting Engineers\Desktop\Work\Work 2\coding>
```

Notice the brackets showing the (.venv) is activated. 

## Using pip - the python package manager

In windows we need to access pip more or less always using `python -m pip {command}`. 

So to see the already installed packages in the `.venv` we use:

```
python -m pip list
```

To add new packages we use: 

```
python -m pip install {package name}
```

etc.



# How to view this document with nicer formatting

Use `ctrl-shift-P` to open up the command bar. Then start typing 'markdown'. 

Click 'Markdown: Open Preview'