# KELLONUOTISTO

## CREATE TABLE -lauseet

### Tietokantataulut:

```sql
CREATE TABLE Arranger (
id INTEGER,
name VARCHAR(50),
PRIMARY KEY (id)
);

CREATE TABLE Composer (
id INTEGER,
name VARCHAR(50),
PRIMARY KEY (id)
);

CREATE TABLE Style (
id INTEGER,
name VARCHAR(50),
PRIMARY KEY (id)
);

CREATE TABLE Technique (
id INTEGER,
name VARCHAR(50),
PRIMARY KEY (id)
);

CREATE TABLE Concert (
id INTEGER,
name VARCHAR(50),
venue VARCHAR(50),
date VARCHAR(50),
PRIMARY KEY (id)
);

CREATE TABLE Account (
id INTEGER,
name VARCHAR(50),
username VARCHAR(50),
password_hash VARCHAR(50),
role VARCHAR(10),
PRIMARY KEY (id)
);

CREATE TABLE Piece (
id INTEGER,
name VARCHAR(50),
octaves VARCHAR(20),
length INTEGER,
FOREIGN KEY (composer_id) REFERENCES Composer(id),
FOREIGN KEY (arranger_id) REFERENCES Arranger(id),
FOREIGN KEY (style_id) REFERENCES Style(id),
PRIMARY KEY (id)
);

CREATE TABLE Note (
id INTEGER,
comment TEXT,
piece_name VARCHAR(50),
FOREIGN KEY (user_id) REFERENCES User(id),
FOREIGN KEY (piece_id) REFERENCES Piece(id),
PRIMARY KEY (id)
);
```
### Liitostaulut:

```sql
CREATE TABLE PieceTechnique (
id INTEGER,
FOREIGN KEY (piece_id) REFERENCES Piece(id),
FOREIGN KEY (technique_id) REFERENCES Technique(id),
PRIMARY KEY (id)
);

CREATE TABLE PieceConcert (
id INTEGER,
FOREIGN KEY (pieceid) REFERENCES Piece(id),
FOREIGN KEY (concert_id) REFERENCES Concert(id),
PRIMARY KEY (id)
);
```
