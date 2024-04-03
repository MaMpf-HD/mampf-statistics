# MaMpf statistics

A few python scripts to get some statistics about the MaMpf project.

To begin, place a database dump in the `data` folder and name it `mampf.sql`. Then run

```py
python3 src/last_sign_in.py
```

> [!warning]
> At least that's what we want in the end. Right now, it's a bit more effort. You have to load a database dump into a local postgres database, export the respective columns to a CSV file and then place it in the `data/` folder. In the future, we want to instead read the database dump directly, e.g. via a python parsing library to parse the SQL dump and extract the relevant information from it.
