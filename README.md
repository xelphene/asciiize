# asciiize

asciiize is a simple Python module which replaces characters of various
non-ascii encodings in strings with their nearest ASCII substitute.  For
example, CP1252 curly double quotes (commonly found on text authored with
Word, for example) will be replaced with normal ASCII double quotes. 
Unicode characters with accent marks will be replaced with the
nearest-looking ASCII character with no accent mark.

# Examples

Perform an Nmap scan on your desired target:

```
Häs âccents
```

is converted to:

```
Has accents
```

# Usage

```
>>> from asciiize import *
>>> s='Häs âccents'
>>> sanitize(s)
'Has accents'
```

The sanitize_multiline function will preserve tabs and line breaks.

# Copyright and License

Copyright (C) 2016 Steve Benson

asciiize was written by Steve Benson.

asciiize is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation; either version 3, or (at your option) any later
version.

asciiize is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
this program; see the file LICENSE.  If not, see <http://www.gnu.org/licenses/>.
