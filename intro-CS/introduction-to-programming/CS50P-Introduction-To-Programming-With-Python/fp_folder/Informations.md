# Informacion recopilada

### Tabulate - para tabular las tabla en python
#### Intalacion
Via pip
pip install tabulate

Via poetry
poetry install tabulate

Use example:

```console
>>> from tabulate import tabulate

>>> table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
...          ["Moon",1737,73.5],["Mars",3390,641.85]]
>>> print(tabulate(table))
-----  ------  -------------
Sun    696000     1.9891e+09
Earth    6371  5973.6
Moon     1737    73.5
Mars     3390   641.85
-----  ------  -------------
```
