Simple datafile controller with simple syntax.

Simple datafile parsing example.

dat.df
```
Name = DataFile
Version = 1.0
License = Mit
```

main.py
```python
from datafile import newparser, delparser

parser = newparser('dat.df')

print(f'Name is {parser.getvalue('Name')}')
print(f'Version is {parser.getvalue('Version')}')
print(f'License is {parser.getvalue('License')}')

parser = delparser()
```

And output is.
```
Name is DataFile
Version is 1.0
License is Mit
```

Commentaries.
```
It's a commentary!
x = 1
```

You can see how simple is this parser.
But, parser and df is very raw, so, it's maybe early to use in seriously project, but for fast and simple project, it's can be usable.
