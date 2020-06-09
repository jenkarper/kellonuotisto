# KELLONUOTISTO

## CREATE TABLE -lauseet

### Tietokantataulut:

CREATE TABLE Arranger (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;name VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);

CREATE TABLE Composer (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;name VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);

CREATE TABLE Style (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;name VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);

CREATE TABLE Technique (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;name VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);

CREATE TABLE Concert (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;name VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;venue VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;date VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);

CREATE TABLE Account (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;name VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;username VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;password_hash VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;role VARCHAR(10),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);

CREATE TABLE Piece (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;name VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;octaves VARCHAR(20),\
&nbsp;&nbsp;&nbsp;&nbsp;length INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY (composer_id) REFERENCES Composer(id),\
&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY (arranger_id) REFERENCES Arranger(id),\
&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY (style_id) REFERENCES Style(id),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);

CREATE TABLE Note (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;comment TEXT,\
&nbsp;&nbsp;&nbsp;&nbsp;piece_name VARCHAR(50),\
&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY (user_id) REFERENCES User(id),\
&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY (piece_id) REFERENCES Piece(id),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);

### Liitostaulut:

CREATE TABLE PieceTechnique (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY (piece_id) REFERENCES Piece(id),\
&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY (technique_id) REFERENCES Technique(id),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);

CREATE TABLE PieceConcert (\
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER,\
&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY (pieceid) REFERENCES Piece(id),\
&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY (concert_id) REFERENCES Concert(id),\
&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY (id)\
);
