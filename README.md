## AIHEKUVAUS

Tavoitteena on luoda Käsikelloyhtye Sonukselle nuottiarkisto, josta voi hakea nuotteja kappaleen nimen, säveltäjän, sovittajan tai tyylilajin perusteella. Tietokannassa on yhteensä kahdeksan tietokantataulua:

- Piece
- Composer
- Arranger
- Style
- Technique
- Concert
- User
- Note

Lisäksi tarvitaan kaksi liitostaulua, PieceTechnique ja PieceConcert. Näistä keskeisenä voidaan pitää tauluja Piece ja User. Taulut Composer, Arranger, Style, Technique ja Concert liittyvät Piece-tauluun viiteavaimen tai liitostaulun kautta, ja taulu Note liittyy tauluun User.


## TOIMINNALLISUUDET

Ohjelmaan voi kirjautua tavallisena käyttäjänä tai pääkäyttäjänä. Tavallinen käyttäjä voi selata nuotteja sekä lisätä uusia rivejä osaan tauluista. Hän voi myös muokata joitakin tauluja. Pääkäyttäjä voi muokata kaikkia tietokantatauluja, lisätä ja poistaa rivejä sekä liittää yksittäiseen kappaleeseen konsertin tai muistiinpanon. Pääkäyttäjä voi myös luoda uusia käyttäjiä.

## LINKIT

[Tietokantakaavio](https://github.com/jenkarper/kellonuotisto/blob/master/documentation/kellonuotisto_kaavio_updated.jpg)

[Käyttötapaukset](https://github.com/jenkarper/kellonuotisto/blob/master/documentation/userstories.md)

[Sovellus Herokussa](https://kellonuotisto.herokuapp.com/) (Sovelluksen testaamiseen tarvitset pääkäyttäjän testitunnukset. Username: 'kellotar', password: 'salainen'.)
