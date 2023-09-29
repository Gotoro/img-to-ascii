# img-to-ascii
![PNG](wiki/w.png)
Convert any image to ASCII representation. 

Uses the apparent "brightness" or "fill" of certain ascii symbols to generate the illusion of different shades of color, e.g. the dot (".") would appear as the brighter color than the hashtag symbol ("#"). 

It all depends on the background color of the text editor you're viewing it in, as the resulting image would appear inverted when viewed in dark backgrounds as opposed to light ones.

# Usage
```python
python main.py <NAME>.png
```

You can change the symbol table used by editing the `symtable = [x for x in " .:-=+#%&@" + "_"]` line. The ascii characters are sorted in the order of fill.
