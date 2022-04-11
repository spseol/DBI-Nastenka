#!/usr/bin/env python3
# Soubor:  cratedb.py
# Datum:   11.04.2022 18:49
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Vytvoří prázdnou DB a příslušné tabulky
############################################################################

import sqlite3

dbfile = "database.sqlite"

SQL = """
CREATE TABLE "uzivatel" (
    "nick"	TEXT,
    "passwd"	TEXT,
    PRIMARY KEY("nick")
);

CREATE TABLE "prispevek" (
    "id"	INTEGER,
    "text"	TEXT NOT NULL,
    "date"	TEXT,
    "nick"	TEXT,

    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("nick") REFERENCES uzivatel(nick)
);

"""

with sqlite3.connect(dbfile) as conn:
    conn.executescript(SQL)
