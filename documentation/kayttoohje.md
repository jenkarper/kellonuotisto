## ASENNUS JA KÄYTTÖ

### Sovelluksen asentaminen paikallisesti

Voit asentaa sovelluksen omalle koneellesi kloonaamalla sen tästä GitHub-repositoriosta. Avaa ensin komentorivi ja vaihda työhakemistoksi se, johon haluat sovelluksen asentaa. Kirjoita tämän jälkeen komento `git clone https://github.com/jenkarper/kellonuotisto.git`: kloonauskomentoa seuraava URL on repositorion osoite. Komennolla kopioit repositoriosta kaiken projektin senhetkisen datan omalle koneellesi. Kun kloonaus on valmis, siirry komentorivillä projektin juurikansioon Kellonuotisto.

Tämän jälkeen luo projektille Python-virtuaaliympäristö komennolla `python3 -m venv venv` ja aktivoi se komennolla `source venv/bin/activate`. Lisää virtuaaliumpäristöön vielä projektin riippuvuudet komennolla `pip install -r requirements.txt`. Nyt sovellus on käytössä paikallisesti! Voit käynnistää sovelluksen komentoriviltä, kun olet aktivoinut virtuaaliympäristön. Mene ensin projektin juurikansioon, aktivoi virtuaaliympäristö yllä mainitulla komennolla ja käynnistä sovellus komennolla `python run.py`. Pääset käyttämään sovellusta selaimessa osoitteessa http://localhost:5000/.

Kun käynnistät sovelluksen ensimmäistä kertaa, SQLAlchemy luo automaattisesti paikallisen tietokantatiedoston (application/sheetmusic.db). Pääset luomaan ensimmäisen pääkäyttäjätunnuksen tietokantaan komentorivillä: Mene ensin sovelluksen juurihakemistoon ja kirjoita sen jälkeen komento `sqlite3 application/sheetmusic.db`. Syötä sen jälkeen haluamasi käyttäjätiedot komennolla

```sql
INSERT INTO account (name, username, password_hash, role)
VALUES ('Käyttäjän nimi', 'käyttäjätunnus', 'salasana', 'ADMIN');
```
Tämän jälkeen voit luoda uusia käyttäjiä sovelluksessa. Pääset kuitenkin käsiksi tietokantaan aina myös komentoriviltä ylläolevan komennon avulla.

### Sovelluksen asentaminen Herokuun

Käyttääksesi sovellusta Herokussa tarvitset Heroku-tunnusten lisäksi Herokun työvälineet komentoriville ([Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)). Kun olet asentanut sovelluksen paikallisesti ja aktivoinut virutaaliympäristön, mene komentorivillä projektin juurikansioon ja aja seuraavat komennot:

- `heroku create kellonuotisto` (luo sovellukselle paikan Herokussa)
- `heroku config:set HEROKU=1` (luo HEROKU-ympäristömuuttujan)
- `heroku addons:add heroku-postgresql:hobby-dev` (lisää sovellukseen tietokannan)
- `git push heroku master` (lähettää koodin paikallisesta repositoriosta Herokuun)

Herokussa olevaan PostgreSQL-tietokantaan voi kirjautua komennolla `heroku pg:psql -a kellonuotisto`. Saat tietokannassa olevat taulut näkyviin komennolla `\dt, ja voit käsitellä tietueita SQL-kyselyillä.

## Käyttöohje

1. **Käyttö ilman kirjautumista.** Kirjautumatta sovellukseen pääset selaamaan tietokannassa olevaa musiikkia navigointipalkin elementistä "Selaa musiikkia". Klikkaamalla elementtiä saat auki pudotusvalikon, josta voit valita listausnäkymän joko kappaleista, säveltäjistä tai sovittajista. Listausnäkymässä näkyy kappaleen/säveltäjän/sovittajan nimi sekä rajallinen määrä tietoa kyseisestä tietueesta.

2. **Kirjautuminen.** Jos sinulla on jo käyttäjätunnus, voit kirjautua sovellukseen oikean yläkulman Kirjaudu-linkistä. Syötä avautuvaan lomakenäkymään käyttäjätunnuksesi ja salasanasi ja klikkaa `Kirjaudu`. Jos sinulla ei vielä ole käyttäjätunnusta, pyydä sitä sovelluksen admin-käyttäjältä tai hallinnoijalta ja kirjaudu saamillasi tunnuksilla.

3. **Tietokannassa olevan musiikin selaaminen ja hakeminen.** Kirjautuneena käyttäjänä pääset selaamaan tietokannan musiikkia laajemmin. Navigointipalkin Selaa musiikkia avaa nyt laajemman valikon:
   * Kappaleet
   * Säveltäjät
   * Sovittajat
   * Tyylilajit
   * Erikoistekniikat
   * Konsertit
   * Hae musiikkia

   Voit avata listausnäkymän kappaleiden, säveltäjien ja sovittajien lisäksi myös tietokannasta olevista tyylilajeista, erikoistekniikoista ja konerteista. Lisäksi saat käyttöösi hakutoiminnon, jolla voit hakea musiikkia tietokannasta hakusanan perusteella.
   
   Listausnäkymässä näet ensin kaikki valitsemasi kategorian tietokannassa olevat tietueet listana. Kappaleiden, säveltäjien, sovittajien ja konserttien listausnäkymässä kunkin tietueen nimen kohdalla on linkki "Näytä tiedot", jota klikkaamalla saat näkyviin tarkemmat tiedot kyseisesta tietueesta. Hakutoiminnossa voit syöttää tekstikenttään hakusanan. Ohjelma hakee tietokannasta kaikki ne kappaleet, joissa annettu hakusana esiintyy, ja tulostaa näkyviin listan kappaleiden nimistä. Pääset tarkastelemaan yksittäistä kappaletta samanlaisesta "Näytä tiedot" -linkistä kuin listausnäkymässä. Ohjelma myös ilmoittaa, jos tietokannasta ei löydy yhtään musiikkia annetulla hakusanalla.

4. **Tietokannassa olevan tiedon muokkaaminen.** Tavallisena käyttäjänä voit muokata tietokannassa jo olevaa tietoa. Kappaleiden, säveltäjien ja sovittajien tietojen muokkaamiseen pääset yksittäisen tietueen tiedot näyttävältä sivulta "Muokkaa"-linkistä. Muuta haluamasi kohdan tietoja ja paina `Päivitä`.

5. **Tiedon lisääminen tietokantaan.** Tiedon lisääminen tietokantaan vaatii aina kirjautumisen. Joidenkin tietojen lisäämiseen vaaditaan lisäksi pääkäyttäjän oikeudet. Tiedon lisääminen tehdään navigointipalkin kohdasta "Lisää musiikkia". Tavallisena käyttäjänä voit lisätä tästä kohdasta uuden kappaleen klikkaamalla "Lisää kappale". Syötä aukeavaan lomakkeeseen pyydetyt tiedot niille varattuihin kenttiin. Mitään kenttää ei voi jättää tyhjäksi. Voit valita kappaleelle säveltäjän, sovittajan ja tyylilajin lomakkeen valikoista, tai jos oikeaa tietoa ei vielä ole tietokannassa, voit kirjoittaa uuden nimen kunkin valikon alla olevaan tekstikenttään. Paina lopuksi "Lisää". Huom! Säveltäjiä, sovittajia tai tyylilajeja ei voi lisätä tietokantaan erikseen, vaan ne lisätään aina kappaleen lisäyksen yhteydessä.

   Pääkäyttäjänä voit kappaleen lisäämisen ohella lisätä myös konsertteja. Konsertin lisäyslomakkeeseen pääset samasta navigointipalkin kohdasta kuin kappaleen lisäämiseen klikkaamalla "Lisää konsertti". Täytä lomakkeen kentät pyydetyssä muodossa ja paina lopuksi "Lisää". Konsertin liittäminen yksittäiseen kappaleeseen tehdään kyseisen kappaleen näyttösivulla.
   
   YKSITTÄISEEN KAPPALEESEEN LIITTYVÄN LISÄTIEDON LISÄÄMINEN: uuden kappaleen lisäyslomakkeella syötettävien pakollisten tietojen lisäksi kappaleisiin voidaan liittää yksi tai useampi erikoistekniikka, yksi tai useampi konsertti sekä yksi tai useampi muistiinpano. Näistä erikoistekniikan lisääminen on sekä pääkäyttäjän että tavallisen käyttäjän tehtävissä, mutta vain pääkäyttäjä voi liittää kappaleeseen konsertin tai muistiinpanon. Lisätiedot liitetään kappaleeseen sen näyttösivulla luetelluista asianmukaisista linkeistä.
   
6. **Tiedon poistaminen tietokannasta.** Vain pääkäyttäjä voi poistaa tietoa tietokannasta. Myös tiedon poistamistoiminnallisuuteen pääset yksittäisen tietueen tiedot näyttävältä sivulta linkistä "Poista koko rivi".

7. **Omien tietojen tarkastelu ja salasanan vaihtaminen.** Kirjautuneena käyttäjänä voit tarkastella omia tietojasi ja vaihtaa salasanasi navigointipalkin kohdasta "Omat tiedot". Tavallinen käyttäjä näkee nimen ja käyttäjätunnuksen, joilla on rekisteröityneenä palveluun. Pääkäyttäjä näkee lisäksi listan omista muistiinpanoistaan.

8. **Uuden käyttäjän luominen ja käyttäjien listaus.** Pääkäyttäjä voi tarkastella kaikkien tietokannassa olevien käyttäjien nimiä ja käyttäjätunnuksia. Listaus löytyy navigointipalkin kohdasta "Omat tiedot" -> "Listaa käyttäjät". Samasta valikosta löytyy myös linkki uuden käyttäjän luovaan lomakkeeseen ("Luo uusi käyttäjä"). Uudelle käyttäjälle voi antaa joko tavallisen käyttäjän oikeudet tai pääkäyttäjän oikeudet. Syötä pyydetyt tiedot lomakkeeseen ja paina lopuksi "Luo tunnus".
