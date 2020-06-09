# KELLONUOTISTO
## AIHEKUVAUS

Tavoitteena on luoda Käsikelloyhtye Sonukselle nuottiarkisto, josta voi hakea nuotteja kappaleen nimen, säveltäjän, sovittajan tai tyylilajin perusteella. Sovelluksessa voi myös luoda muistiinpanoja yksittäisistä kappaleista. Sovellus toimii työkaluna orkesterin johtajalle ohjelmistojen suunnittelussa ja auttaa hallitsemaan kasvavaa nuotistoa. Tällä hetkellä valtaosa yhtyeen nuoteista on paperimuodossa, mutta tulevaisuudessa sovellusta voisi laajentaa siten, että tietokannassa olisi mahdollisuus myös digitaalisessa muodossa olevan nuotin tallentamiseen.

## TIETOKANNAN RAKENTEESTA

Tietokannassa on tällä hetkellä kahdeksan tietokantataulua:

- Piece
- Composer
- Arranger
- Style
- Technique
- Concert
- User
- Note

Lisäksi tarvitaan kaksi liitostaulua, PieceTechnique ja PieceConcert. Tietokannan säilyttämän datan näkökulmasta keskeisin taulu on Piece, joka kuvaa yksittäistä kappaletta. Sovelluksen tärkeimmät toiminnallisuudet kohdistuvat tähän tauluun. Jokaisella kappaleella on nimi, tieto kappaleessa käytettävistä oktaaveista sekä kappaleen arvioitu pituus. Lisäksi kappaleeseen liittyy yksi säveltäjä, yksi sovittaja ja yksi tyylilaji, jotka ovat tietokannassa omina tauluinaan ja joihin viitataan kappaleessa viiteavaimella. Kappaleeseen voi liittyä myös yksi tai useampi erikoistekniikka: erikoistekniikalla tarkoitetaan käsikellon soittotapaa, joka poikkeaa perustekniikasta. Erikoistekniikat ovat omassa tietokantataulussaan, joka liittyy kappaletauluun liitostaulun kautta.

Tietokannan taulu Concert kuvaa konserttia, jossa käsikelloyhtye on esiintynyt. Konsertilla on nimi, päivämäärä ja pitopaikka. Myös konsertti liittyy kappaletauluun liitostaulun kautta, koska yhdessä konsertissa on monta kappaletta, ja toisaalta samaa kappaletta voidaan esittää useassa eri konsertissa. Konserttitaulun tarkoitus on ensisijassa auttaa orkesterinjohtajaa hahmottamaan, milloin mitäkin kappaletta on soitettu ja millaisin yhdistelmin. Lisksi konserttitaulun päivämäärä-attribuutti toimii viitteenä johtajan omiin, tämän sovelluksen ulkopuolisiin arkistoihin esimerkiksi kellojaoista (eli mitkä kellot ovat kenenkin soittajan vastuulla). Konserttitaulun toissijaisena tarkoituksena on kuvata yhtyeen esityshistoriaa, jota voidaan hyödyntää esimerkiksi toimintakertomuksen laatimisessa.

Sovelluksen käyttäjää kuvaa taulu User, ja käyttäjän luomaa muistiinpanoa kuvaa taulu Note. Muistiinpanon luominen on pääkäyttäjän toiminto, ja muistiinpano liittyy aina tiettyyn kappaleeseen viitteavaimen perusteella.

### Suunnitellut lisäykset

Tietokantaa on tarkoitus kasvattaa vielä yhdellä taululla Instrument, joka sekin liittyisi kappaletauluun liitostaulun kautta samaan tapaan kuin erikoistekniikka. Instrument kuvaa soolo- tai säestävää soitinta, jota kappaleessa voidaan käsikellojen lisäksi käyttää. Lisäksi kappaletauluun lisätään attribuutti, joka kertoo kappaleen vaatiman minimimäärän soittajia. Sovelluksessa voi sitten suodattaa kappaleita sen perusteella, kuinka monta soittajaa on käytettävissä.

Tietokantaan voisi mahdollisesti lisätä vielä avainsanat, joiden perusteella musiikkia voisi hakea. Avainsanalista voisi jopa korvata tyylilajitaulun, niin että myös tyylilaji liitettäisiin kappaleeseen avainsanana.

## TOIMINNALLISUUDET

Ohjelmaan voi kirjautua tavallisena käyttäjänä tai pääkäyttäjänä. Tavallinen käyttäjä voi selata nuotteja sekä lisätä uusia rivejä osaan tauluista. Hän voi myös muokata joitakin tauluja. Pääkäyttäjä voi muokata kaikkia tietokantatauluja, lisätä ja poistaa rivejä sekä liittää yksittäiseen kappaleeseen konsertin tai muistiinpanon. Pääkäyttäjä voi myös luoda uusia käyttäjiä. Toiminnallisuudet on kuvattu tarkemmin dokumentissa [Käyttötapaukset](documentation/userstories.md).

## ASENNUS JA KÄYTTÖ

### Sovelluksen asentaminen paikallisesti

Voit asentaa sovelluksen omalle koneellesi kloonaamalla sen tästä GitHub-repositoriosta. Avaa ensin komentorivi ja vaihda työhakemistoksi se, johon haluat sovelluksen asentaa. Kirjoita tämän jälkeen komento `git clone https://github.com/jenkarper/kellonuotisto.git`: kloonauskomentoa seuraava URL on repositorion osoite. Komennolla kopioit repositoriosta kaiken projektin senhetkisen datan omalle koneellesi. Kun kloonaus on valmis, siirry komentorivillä projektin juurikansioon Kellonuotisto.

Tämän jälkeen luo projektille Python-virtuaaliympäristö komennolla `python3 -m venv venv` ja aktivoi se komennolla `source venv/bin/activate`. Lisää virtuaaliumpäristöön vielä projektin riippuvuudet komennolla `pip install -r requirements.txt`. Nyt sovellus on käytössä paikallisesti! Voit käynnistää sovelluksen komentoriviltä, kun olet aktivoinut virtuaaliympäristön. Mene ensin projektin juurikansioon, aktivoi virtuaaliympäristö yllä mainitulla komennolla ja käynnistä sovellus komennolla `python run.py`. Pääset käyttämään sovellusta selaimessa osoitteessa http://localhost:5000/.

### Sovelluksen käyttö Herokussa

Kellonuotisto on käytettävissä myös Heroku-pilvipalvelussa. Pääset sinne klikkaamalla tämän README-tiedoston lopussa olevaa linkkiä.

### Käyttöohje

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

5. **Tiedon lisääminen tietokantaan.** *Tulossa.*

6. **Tiedon poistaminen tietokannasta.** Vain pääkäyttäjä voi poistaa tietoa tietokannasta. Myös tiedon poistamistoiminnallisuuteen pääset yksittäisen tietueen tiedot näyttävältä sivulta linkistä "Poista koko rivi".

7. **Omien tietojen tarkastelu ja salasanan vaihtaminen.** *Tulossa.*

8. **Uuden käyttäjän luominen ja käyttäjien listaus.** *Tulossa.*

## LINKIT

[Tietokantakaavio](documentation/kellonuotisto_schema_diagram.png)

[Käyttötapaukset](documentation/userstories.md)

[Sovellus Herokussa](https://kellonuotisto.herokuapp.com/) (Sovelluksen testaamiseen tarvitset pääkäyttäjän testitunnukset. Username: 'kellotar', password: 'salainen'.)
