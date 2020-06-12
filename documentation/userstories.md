# Käyttötapaukset

## Vieras

- Vieras voi selata kappaleiden, säveltäjien ja sovittajien listausnäkymää.

**SQL-kyselyt:**

```sql
SELECT * FROM Piece ORDER BY Piece.name

SELECT * FROM Composer ORDER BY Composer.name

SELECT * FROM Arranger ORDER BY Arranger.name
```

## Käyttäjä

### Ennen kirjautumista:

- Käyttäjä voi selata kappaleiden, säveltäjien ja sovittajien listausnäkymää.
- Käyttäjä voi kirjautua palveluun.

### Kirjautuneena:

- Käyttäjä voi selata konserttien listausnäkymää.
- Käyttäjä voi lisätä rivejä tietokantatauluihin Piece, Composer, Arranger, Style ja Technique.
- Käyttäjä voi hakea tietoa tietokannasta hakusanalla.
- Käyttäjä voi tarkastella omia kirjautumistietojaan sekä vaihtaa salasanansa.

**SQL-kyselyt:**
- Pääavaimen hakeminen viiteavaimen lisäämistä varten:

   ```sql
   SELECT id FROM Composer WHERE name = 'nimi';
   ```
   
- Rivin lisääminen:

  ```sql
  INSERT INTO Piece (name, octaves, length, composer_id, arranger_id, style_id)
  VALUES ('nimi', 'oktaavit', 3, 3, 7, 1);
  ```
   
- Erikoistekniikan lisääminen kappaleeseen:

   ```sql
   INSERT INTO PieceTechnique (piece_id, technique_id)
   VALUES (3, 5);
   ```
- Tyylilajien kappalemäärät ja raakaminuutit:

   ```sql
   SELECT Style.name, COUNT(*), SUM(length)
   FROM Piece
   LEFT JOIN Style ON Style.id = Piece.style_id
   GROUP BY Style.name
   ORDER BY Style.name
   ```

## Pääkäyttäjä

- Pääkäyttäjällä on kaikki Käyttäjän oikeudet.

### Ainoastaan Pääkäyttäjällä olevat oikeudet:

- Pääkäyttäjä voi luoda uusia Käyttäjiä.

   ```sql
   INSERT INTO Account (name, username, password_hash, role)
   VALUES ('Uusi nimi', 'käyttäjänimi', 'salasana', 'REGULAR');
   ```
   
- Pääkäyttäjä voi tarkastella listaa sovelluksen Käyttäjistä (nimiä ja käyttäjänimiä) (SQL kuten muissakin listauksissa).
- Pääkäyttäjä voi poistaa rivejä kaikista tietokantatauluista.

   ```sql
   DELETE FROM Piece WHERE id = 3;
   ```
   
- Pääkäyttäjä voi lisätä uuden konsertin ja liittää sen kappaleeseen (SQL kuten erikoistekniikan lisäämisessä). *(konsertin liittäminen kappaleeseen ei tällä hetkellä toimi!)*
- Pääkäyttäjä voi lisätä uuden muistiinpanon ja liittää sen kappaleeseen.

   ```sql
   INSERT INTO Note (comment, user_id, piece_id, piece_name)
   VALUES ('muistiinpano', 3, 5, 'Kappaleen nimi');
   ```
   
- Pääkäyttäjä voi tarkastella omia muistiinpanojaan.
   
   ```sql
   SELECT * FROM Note
   WHERE user_id = current_user.id;
   ```
