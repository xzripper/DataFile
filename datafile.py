"""
Simple parser for data file,
syntax in data file like in ini,
but a bit changed,
based on regular expressions,
and some mechanics.
Extension of datafile is "df".\n
Author - Ivan Perzhinsky.\n
License - MIT License.\n
Version - 1,0.\n
"""

# Simple datafile parser based on regular expressions.
# And with syntax like in ini.
# But a bit changed.
# Author: Ivan Perzhinsky.
# License: MIT License.
# Version: 1.0.

from re import findall
from os.path import exists
from os import remove
from typing import Union


class DataFile:
    def __init__(self, df: str) -> None:
        """Constructor of parser. Work of constructor is remembering file, and handling some work."""
        self.pattern = '.*?=.*'

        if exists(df):
            self.df = df

        elif df.endswith('.df'):
            self.df = 1

            raise Exception('unknown extension of datafile')

        else:
            self.df = 1

            raise FileNotFoundError('datafile not found')

    def parse(self) -> Union[None, list]:
        """Parse data from datafile, if self.df == 1, returning None."""
        if self.df == 1:
            return None

        else:
            with open(self.df, 'r') as df_io:
                content = df_io.read()

            parsed = findall(self.pattern, content)

            if parsed == []:
                return {}

            else:
                nh_keys = {}
                keys = {}

                for val in parsed:
                    nh_keys[val.split('=')[0]] = val.split('=')[1]

                for key in nh_keys:
                    if key.endswith(' '):
                        keys[key[:-1]] = nh_keys[key]

                    else:
                        keys[key] = nh_keys[key]

                for val in keys:
                    if keys[val].startswith(' '):
                        keys[val] = keys[val][1:]

                    else:
                        keys[val] = keys[val]

                return keys

    def getvalue(self, key: str) -> Union[None, str]:
        """Get value from key in datafile. If key not exists or error happened while parsing file, returning None."""
        try:
            parsed = self.parse()

            if parsed == 1:
                return None

            else:
                return parsed[key]
        except KeyError:
            return None

    def keyexists(self, key: str) -> Union[None, bool]:
        """Is key exists in datafile. If error happened while parsing, returning None."""
        parsed = self.parse()

        if parsed == 1:
            return None

        else:
            return key in parsed

    def delkey(self, parsed: dict, key: str) -> int:
        """Delete key in parsed dict, if all success returning 0, else if error, returning 1."""
        if parsed == 1:
            return parsed

        else:
            try:
                parsed.pop(key)

                return parsed
            except KeyError:
                return 1

    def keyscount(self, parsed: dict) -> Union[None, int]:
        """Count keys in parsed datafile, if error returning None, else count."""
        if parsed == 1:
            return None

        else:
            return len(list(parsed.keys()))

    def updatefile(self, newfile: str):
        """Update file, using class constructor in function."""
        self.__init__(newfile)

    def getfile(self) -> Union[None, str]:
        """Get file name, if self.df is error code, returning None, else returning data file."""
        if self.df == 1:
            return None

        else:
            return self.df

    def delfile(self) -> int:
        """Delete data file, if self.df equals 1, returning 1, else deleting file and returning 0."""
        if self.df == 1:
            return 1

        else:
            remove(self.df)

            return 0

newparser = lambda df: DataFile(df)
delparser = lambda: None
