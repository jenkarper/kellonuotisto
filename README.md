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

Sovelluksen voi asentaa paikallisesti omalle koneelle tai Heroku-pilvipalveluun ([ohjeet](documentation/kayttoohje.md) asennukseen ja käyttöön).

## LINKIT

[Tietokantakaavio](documentation/kellonuotisto_schema_diagram.png)

[Käyttötapaukset](documentation/userstories.md)

[Asennus- ja käyttöohjeet](documentation/kayttoohje.md)

[Sovellus Herokussa](https://kellonuotisto.herokuapp.com/) (Sovelluksen testaamiseen tarvitset pääkäyttäjän testitunnukset. Username: 'kellotar', password: 'salainen'.)
