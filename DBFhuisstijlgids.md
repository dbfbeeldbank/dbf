# DBF Huisstijlgids — één bron voor HTML, PDF, PowerPoint en Word

> Eén gids voor HTML, PDF, PowerPoint en Word. Stand: 10 oktober 2026 — **concept, bevroren voor toetsing in de praktijk.** Niet definitief zolang de open visuele keuzes (§6) niet getoetst zijn.
>
> Drie documenten, elk met een eigen functie; ze herhalen elkaars inhoud niet:
> - **Deze huisstijlgids:** de geldende regels en ontwerpprincipes. De normatieve bron.
> - **`DBF_ontwikkellogboek.md`:** hoe keuzes tot stand kwamen, afgewezen varianten, open ontwikkelpunten. Wordt bijgewerkt als de huisstijl zelf verandert. Niet nodig om een uiting te maken.
> - **Kwaliteitsrapportage (§5):** per oplevering, over die ene uiting. Geen ontwikkelgeschiedenis.
>
> **Alle bestanden** (logo's, chevrons, patronen, sjablonen, sjabloonfoto's, beeldbank) staan in de openbare GitHub-repository `dbfbeeldbank/dbf`, met een volledige lijst in `DBF_assets_manifest.csv` (Bijlage A). **Lukt downloaden niet**, bijvoorbeeld in een AI-omgeving zonder internet, vraag de gebruiker dan om `DBF_huisstijl_assets.zip`: daarin zit alles, inclusief deze gids en het manifest.

## Wegwijzer — wat lees je voor welk formaat?

Lees altijd de leidende principes, §0 en §1.1–§1.5, en §5 (kwaliteitsrapportage, bij elke oplevering). Lees daarna alleen wat bij je opdracht hoort; de rest kun je overslaan.

| Je maakt | Lees | Alleen als het speelt |
|---|---|---|
| **HTML-pagina** | §2, Bijlage A | Beeld: §1.7 + Bijlage C · Patroonstrook: §1.6 + B.3 (HTML) |
| **PowerPoint** | §3, Bijlage A, §1.7 (openingsdia heeft altijd een beeld), B.3 (PowerPoint) | Historische foto of sessiebeeld: Bijlage C |
| **Word of PDF** | §4, Bijlage A | Beeld: §1.7 + Bijlage C · Achterkant met patroon: §1.6 + B.3 (Word/PDF) |

Open punten die nog niet beslist zijn: §6. Doe daar geen aannames over; vraag het na.

---

## Leidende principes

### De inhoud bepaalt de vorm, niet andersom

Een uiting moet allereerst helder, overtuigend, betekenisvol en prettig leesbaar zijn. De huisstijl ondersteunt de inhoud en mag nooit de aandacht van het verhaal afleiden.

- Een goede compositie gaat boven het mechanisch toepassen van huisstijlelementen.
- Witruimte is een volwaardig ontwerpmiddel.
- Foto's, patronen, kleurvlakken en andere grafische elementen alleen als ze daadwerkelijk iets toevoegen.
- Typografie, inhoudelijke hiërarchie en leesbaarheid gaan voor decoratie.
- Verschillende media mogen een verschillende visuele uitwerking krijgen.
- Technische voorschriften mogen niet leiden tot een geforceerde indeling of een onnodig druk ontwerp.

**Bij twijfel: weglaten is beter dan toevoegen.**

### Hiërarchie van de huisstijlelementen

1. **Inhoud en verhaal** — wat willen we overbrengen?
2. **Logo en typografie** — wat maakt ons direct herkenbaar?
3. **Kleur en witruimte** — wat geeft karakter en rust?
4. **Fotografie** — wat voegt betekenis en menselijke zeggingskracht toe?
5. **Grafische elementen** (chevron, patroon) — wat ondersteunt het geheel?

Dit is een ontwerpprincipe, geen stappenplan. Een uiting zonder patroon kan volledig in huisstijl zijn; een uiting waarin het patroon te nadrukkelijk aanwezig is, past juist minder goed. Het patroon is geen tweede logo.

### Vaste regels en ontwerpvrijheid

| Soort | Wat | Hoe ermee omgaan |
|---|---|---|
| **Vaste identiteitsregels** | Logo, identiteitskleuren (§1.1 A), lettertypen, beeldtaal, essentiële herkenbaarheid | Altijd respecteren |
| **Mediumspecifieke standaarden** | Bijv. openingsdia PowerPoint, Word-offertesjabloon, HTML-typografie | Respecteren; afwijken alleen gemotiveerd (en melden in de kwaliteitsrapportage) |
| **Ontwerpvrijheid** | Compositie, witruimte, beeldgebruik, informatiedichtheid, bewust weglaten van decoratie | Professioneel ontwerpen, vanuit de inhoud |

Het doel is consistentie, niet uniformiteit.

---

## 0. Werkafspraak: eerst het formaat vaststellen

**Voordat er iets gebouwd wordt, ligt het uitvoerformaat vast.** Noemt de opdracht niet expliciet HTML, PDF, PowerPoint (pptx) of Word (docx)? Dan vraagt Claude eerst, in één korte vraag, welk formaat bedoeld is. Niet zelf kiezen, ook niet als het voor de hand lijkt te liggen.

- Signaalwoorden als "document", "rapport", "stuk", "presentatie", "notitie" of "lesbrief" zijn **geen** formaatkeuze. Ook dan eerst vragen.
- Wordt PDF gekozen: vraag direct mee of de PDF moet uitgaan van de **Word-opmaak** (drukwerk, offerte/rapport) of van een **HTML-export**. Er is nog geen aparte PDF-gids (zie §6, open punten).
- Een aangeleverd bronbestand (.dotx, .potx, .docx) dat bewerkt moet worden, bepaalt zelf het formaat. Dan niet vragen.
- Na de keuze geldt: §1 (gedeeld fundament) **plus** het hoofdstuk van het gekozen formaat (§2 HTML, §3 PowerPoint, §4 Word).

**Werkwijze bij elk nieuw documenttype:** eerst het aangeleverde bronbestand technisch valideren, dan de stijlwaarden er exact uit halen, pas dan bouwen. Nooit waarden verzinnen op gevoel. **Een bronbestand (template, .potx, .dotx) gaat voor op deze gids** als waarden botsen. Wordt een fout gevonden en hersteld, dan wordt de oorzaak en de regel in dezelfde handeling in deze gids vastgelegd.

---

## 1. Gedeeld fundament (geldt voor elk formaat)

### 1.1 Kleur: drie niveaus

De kleurwaarden komen uit `kleurenpalet.png`, aangevuld met de afgeleide tinten hieronder. Dit hoofdstuk legt vast welke **rol** een kleur heeft. Het is het enige kleurvoorschrift; de mediumhoofdstukken verwijzen hiernaar. Drie niveaus betekent niet: meer kleuren gebruiken. **Een afzonderlijke uiting bevat zo weinig mogelijk verschillende kleuren.**

**A. Identiteitskleuren** — dragen de merkidentiteit.

| Kleur | Hex | Pantone | Functie |
|---|---|---|---|
| **Koningsblauw** | `#27275B` | 2758 C | Primaire identiteitskleur, dominant. Eén donkerblauw in elk formaat (besluit Paul, 10 oktober 2026). |
| **DBF-goud** | `#DDB85E` | 7408 C | Secundaire identiteitskleur, terughoudend: lijn, rand, chevron, nummer of tekst op donker. |
| **Wit** | `#FFFFFF` | — | Rust, helderheid en contrast. |

**B. Ondersteunende huisstijlkleuren** — vastgelegd voor specifieke toepassingen; geen gelijkwaardige alternatieven voor A.

| Kleur | Hex | Functie |
|---|---|---|
| Zwart | `#000000` | Lopende tekst (Word, PowerPoint) |
| Lichtblauw | `#E3E4ED` | Lichte kaartvlakken en panelen |
| Zand | `#ECE4D7` | Warme kaarten en vlakken voor nadruk (palet-Goud `#C1A57B` op 30%) |
| Warm gebroken wit | `#F5F3EE` | Achtergrond van digitale uitingen (HTML) |
| Donker marine | `#222831` | Alleen als bewust gemotiveerde uitzondering |
| Crème | `#FFFCF2` | Uitsluitend de PowerPoint-instructiedia "Plaatjes" |

**C. Functionele toepassingskleuren** — afgeleid, alleen als ze functioneel nodig zijn (tabellen, heatmaps, datavisualisatie, secundaire tekst, subtiel contrast). Ze vormen geen eigen palet.

| Hex | Toepassing |
|---|---|
| `#4E4E79`, `#66668A`, `#BEBECE` | HTML-tinten van koningsblauw (§2.3) |
| `#C7AD79`, `#F1E7D0` | HTML-tinten van goud (§2.3) |
| `#DCD8CE` | Dunne lijnen en scheiders in HTML (§2.3) |
| `#AEB0C9` | Middelste waarde tabel-heatmap (§3.1) |
| `#ECECEC` | Tabelkopregel PowerPoint |
| `#464646` | Secundaire tekst, bijschriften |
| `#C1A57B`, `#30475E` | Paletkleuren zonder eigen rol; alleen functioneel |

Het eerdere HTML/Word-blauw `#15284B` vervalt. Waar in deze gids "donkerblauw" of "navy" staat zonder hexcode, is koningsblauw bedoeld.

**Goud (DBF) `#DDB85E`:** goud is nooit een tekstkleur op een licht vlak. Contrast goud-op-wit is ca. 1,8:1, ruim onder de WCAG-norm van 4,5:1. Goud alleen als lijn, rand, stip, of als tekstkleur op donkerblauw. Vlakken met witte tekst (labels, chips, badges) staan op donkerblauw, nooit op goud.

### 1.2 Logo en beeldmerk

- Altijd het officiële logobestand. Nooit een zelfgetekende benadering.
- Gebruik alleen de logo's en beeldmerken uit **Bijlage A**. De witte bestanden in de oude assetbibliotheek (`Logo_..._wit_....png`, `Beeldmerk_wit_....png`) zijn beschadigd (wit op wit, zonder transparantie): niet gebruiken.
- **Het hexagon is uitsluitend de vorm van het beeldmerk zelf.** Het is geen decoratief motief, geen kopmarkering en geen bullet; daarvoor is de chevron (§1.3).
- Gebruik nooit het losse beeldmerk náást het logo: het logo bevat het beeldmerk al.

**Tagline "IDENTITY MARKETING":**
- **Standaardregel (HTML, PowerPoint):** alleen bij grote, eenmalige plaatsingen (cover, titelslide). Bij kleine of herhalende plaatsingen (documentkopje, footer) de wordmark **zonder** tagline. Op kleine hoogte wordt de tagline onleesbaar; de fix is de tagline weglaten, niet het logo opblazen.
- **Uitzondering Word-offerte (besluit Paul, op basis van het offertesjabloon):** horizontaal logo **mét** tagline, zwart, herhalend op elke pagina. Het bronbestand overrulet hier de standaardregel. Of dit ook voor brief/rapport/memo geldt, is nog niet vastgesteld.

### 1.3 Chevron (`›`) als kopmarkering

Bron: `Schermafbeelding_20260910_om_16_01_39.png`. Een gestileerde, dikke "›" — geen tekstkarakter maar een los vlak met scherpe punten. Komt ook terug in de Word-sjablonen als opsommingsteken bij ingesprongen tekst (`DB_brief_sjabloon.pdf`, `DBF_rapport_sjabloon.pdf`).

Vectorpunten (viewBox `0 0 924 1316`): `191,118 452,653 191,1188 273,1188 763,653 273,118`.

- **Gebruik:** markering bij korte, betekenisvolle koppen (bijv. **"› Vandaag"**). Niet bij lange, doorlopende bullet-lijsten: daar blijft een gewone bullet passender.
- **Kleur kiezen op basis van de achtergrond** (voldoende contrast): navy/koningsblauw op licht, goud of wit op donker.
- **Verboden:** een herhalende rij chevrons als lijnaccent of breker, ook niet "subtiel" of "één keer per titelblok".
- **Uitlijning:** de y-positie nooit via een geschatte offset. Centreer op de rij: `chevron-y = rij-y + rijhoogte/2 − chevron-hoogte/2`. Geldt voor elke chevron.
- Bestanden: `DBF_chevron.svg` (schaalbaar, `fill="currentColor"`) en de PNG-bibliotheek in §3.7. In HTML: inline `<svg><polygon>` met een CSS-variabele als `fill`.

### 1.4 Typografie per formaat

| Formaat | Koppen | Lopende tekst | Labels/tabellen |
|---|---|---|---|
| HTML | Merriweather 400/700, cursief 400 | Merriweather | Open Sans 400/600/700 |
| PowerPoint | Merriweather | Open Sans | Open Sans |
| Word (offerte) | Calibri Light vet 10,5pt | Calibri Light 10,5pt | Calibri Light 9pt |

**Regel:** gebruik altijd de voorgeschreven lettertypen. Sluit ze in waar dat technisch mogelijk en licentierechtelijk toegestaan is. **De visuele uitkomst is leidend:** controleer bij exporteren of delen of de typografie goed wordt weergegeven.

| Medium | Uitwerking |
|---|---|
| HTML | Fonts als base64 `@font-face` in het bestand (§2.2). Dat is hier altijd mogelijk en de enige manier waarop een losse of gepubliceerde pagina overal goed toont. Geen Calibri (niet vrij op het web). |
| PowerPoint | Merriweather en Open Sans insluiten (§3.6) en controleren in echte PowerPoint, liefst op een andere computer. Zonder Merriweather valt de uitstraling weg. |
| Word | Calibri Light staat op elke Office-installatie; insluiten is geen eis. Gebruik de sjablooninstellingen (§4). |
| PDF | Fonts ingesloten in het PDF-bestand en de weergave gecontroleerd. |

Gebruik alleen fontgewichten die beschikbaar of ingesloten zijn; anders bootst de applicatie ze lelijk na.

### 1.5 Afbeeldingen en hergebruik

- **Nooit non-uniform schalen** (aparte factor voor breedte en hoogte). Bereken de crop: `crop_breedte = bronhoogte × doelverhouding`, snijd dat uit, schaal daarna uniform.
- Slides uit een ander klanttraject mogen als figuur, maar **altijd zonder het logo van die andere klant** (pixelvlak wegpoetsen, daarna programmatisch op restpixels controleren). Noem de andere klant ook niet in bijschrift of bronvermelding.
- **Verifieer altijd in of zo dicht mogelijk bij de echte applicatie.** Een preview die er goed uitziet, bewijst niets (LibreOffice ≠ Word/PowerPoint, eigen browser ≠ ontvanger).

### 1.6 Beeld en decoratief patroon

**De kern van de huisstijl is typografie, kleur, witruimte en het officiële logo.** Een uiting moet zonder foto en zonder patroon herkenbaar zijn: Merriweather-koppen, koningsblauw, de korte gouden lijn en het logo.

**Fotografie** brengt mensen en verhalen binnen. Bij voorkeur beelden van betekenisvolle momenten: mensen die samen iets doen, sociale verbanden, informeel kapitaal. Historische documentaire fotografie (zwart-wit) is karakteristiek, maar geen verplichting: een sterke hedendaagse documentaire foto past even goed. Combineer per uiting bij voorkeur ‘toen’ en ‘nu’. Rechten en bronvermelding per foto controleren.

**Het decoratieve patroon** is een aanvulling, geen vast onderdeel. Het is afgeleid van de chevron (§1.3) en wordt als vast bestand geplaatst (Bijlage B), niet nagebouwd of gevarieerd.

- Ondergeschikt aan logo, typografie, kleur en inhoud. Nooit verplicht op een pagina of dia.
- Alleen op afsluitende momenten: achterkant van een rapport, slotdia van een presentatie, smalle strook boven de voet van een webpagina.
- Altijd toon op toon (lijnen op circa 10% verschil met de achtergrond). Nooit in hetzelfde vlak als een foto, nooit achter tekst of knoppen.
- In beginsel maximaal één keer per uiting.
- Donkere variant: koningsblauw is de standaard. Donker marine alleen als gemotiveerde uitzondering.
- Bij bijzondere uitgaven mag het patroon nadrukkelijker aanwezig zijn; dat is een bewuste uitzondering, niet de standaard.

Fotografie volgt het formaat: beelden die in een sjabloon een vaste plek hebben (zoals de titeldia in PowerPoint) worden niet naar andere formaten overgezet. Het logo blijft in elk formaat op zijn vaste plek staan; een foto vervangt nooit het logo.

Technische specificatie en bestanden: **Bijlage B**.

### 1.7 Beeldkeuze uit de beeldbank

Bron: **Bijlage C** (beeldbank). Beeld is een keuze per document, geen vast onderdeel. **Bepaal eerst wat de tekst zegt; kies pas daarna of er een beeld bij hoort.** Twijfel = geen beeld.

**Uitzondering — openingsdia PowerPoint: altijd een beeld.** De binnenkomer van een presentatie krijgt standaard een foto, naast het effen vlak in koningsblauw (§3). Kies in deze volgorde:
1. een historisch beeld uit Bijlage C dat de betekenis van de presentatie raakt;
2. een sessiebeeld (C.23–C.27) als de presentatie over een sessie of samenwerking met het bureau gaat;
3. anders het vaste titeldiabeeld uit het PowerPoint-sjabloon (strandsilhouetten, §3).
Een bijschrift is op de openingsdia niet nodig; de identiteitsvraag mag er klein in, als die bij het onderwerp past. Voor alle andere plekken en formaten geldt de beslisvolgorde hieronder.

**Beslisvolgorde (één keuze per plek, van boven naar beneden):**

1. **Geen beeld — de standaard.** In de meeste documenten (richtwaarde: circa 8 op de 10) raakt geen beeld de inhoud. Dan geen beeld. Een document zonder foto is volledig in huisstijl (§1.6).
2. **Historisch beeld — alleen als het de betekenis raakt.** Kies op betekenis, niet op het letterlijk afgebeelde onderwerp. Voorbeelden: *Mannen aan boord* (C.17) bij een beschrijving van een finish, een mijlpaal of samen op weg gaan; *Het dorpsplein* (C.06) bij ontmoeting en erbij horen; *Voorlezen aan kinderen* (C.10) bij het verhaal dat een organisatie bijeenhoudt. Maximaal één historisch beeld per hoofdstuk, bij voorkeur één per document.
3. **Persoon van het bureau — alleen als die persoon auteur of afzender is.** Portret klein bij de naam, bijvoorbeeld onderaan bij de ondertekening of in een auteursregel. Alleen de personen die in de tekst als auteur voorkomen; nooit als sfeerbeeld.
4. **Sessiebeeld — alleen als de tekst over een sessie, werkvorm of samenwerking met het bureau gaat.** Bijvoorbeeld bij een terugblik op een werksessie of een beschrijving van de aanpak. Gebruik de teamfoto's (C.23–C.27).

De richtwaarden (circa 8 op 10 geen beeld; de rest verdeeld over 2–4) zijn een kompas, geen quotum. Een tekst kan in aanmerking komen voor 3 én 4 (auteur van een sessieverslag); kies dan het sessiebeeld en zet het portret alleen bij de ondertekening.

**Bijschrift bij historische beelden.** Een beschrijving en identiteitsvraag uit Bijlage C mogen erbij, maar alleen als de vraag inhoudelijk aansluit. Twee vormen, kies er één:

- **In het beeld:** klein, onderin over de foto, in wit (Open Sans, 400) op een donkere verloopband van onderen (koningsblauw, 0 → 60% dekking), zodat het contrast altijd minimaal 4,5:1 is. Alleen de identiteitsvraag, maximaal twee regels.
- **Onder het beeld:** als toelichting, cursief en schreefloos (HTML/PowerPoint: Open Sans italic; Word: Calibri Light italic), kleiner dan de lopende tekst, kleur `#464646` of koningsblauw. Eerst de beschrijving, dan de vraag.

Altijd onder of naast het beeld, klein: de bronvermelding (bijv. *Nationaal Archief, fotocollectie Spaarnestad Onderwerpen*). Werkbeschrijvingen uit de beeldbank niet als feit presenteren (geen jaartallen, namen of plaatsen die niet in het archief bevestigd zijn).

**Verwijzing naar *Ken je de foto?*** (https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html), voor historische foto's uit Bijlage C (C.01–C.17 en C.46); niet voor portretten, teamfoto's en gebouwen:
- **Digitaal** (HTML, PowerPoint, digitale PDF): de foto linkt naar de toelichting.
- **Gedrukt:** één korte URL, één QR-code of een vermelding in het colofon voor de hele uiting. Niet per foto een eigen QR-code.

**Per formaat:**

- **HTML:** beeld als figuur in de inhoud, nooit boven of in plaats van het titelblok met logo (§2.4). Beeld als base64 data-URI insluiten (§2.8); de URL in Bijlage C is alleen de bron om het bestand op te halen. Is het bestand niet op te halen, dan geen beeld (niet raden, geen kapotte link). Historische foto: `<img>` in een `<a href="…Ken_je_de_foto.html" target="_blank" rel="noopener">`, met `title="Over deze foto"`.
- **PowerPoint:** openingsdia altijd met beeld (zie uitzondering hierboven); historisch beeld op een scheidingsdia alleen volgens de beslisvolgorde, naast een effen vlak in koningsblauw (§3). Portretten op een team- of contactdia. Bijschrift in het beeld of eronder zoals hierboven. Historische foto: hyperlink op de afbeelding naar *Ken je de foto?*.
- **Word/PDF:** historisch beeld op de omslag of bij een hoofdstukopening; portret bij de ondertekening. Beeld ingebed, niet gekoppeld. Historische foto: digitaal een hyperlink op de afbeelding; gedrukt één verwijzing in het colofon (zie hierboven).

**Niet doen:** meerdere historische beelden als decoratie door een document strooien; een portret zonder dat die persoon auteur is; namen zetten bij groepsfoto's; een foto in hetzelfde vlak als het patroon (§1.6); beelden bijsnijden tot een detail dat de betekenis verandert.

---
## 2. HTML

Geldt voor elk op zichzelf staand HTML-bestand: lesstof, rapport, offerte, voorstel, whitepaper, uitnodiging. Geen vast sjabloon met verplichte secties, maar een consistente set regels en bouwstenen — kies per document wat past, binnen deze visuele taal.

### 2.1 Logo in HTML

- **Nooit een `<img src="bestandsnaam.png">`-verwijzing naar een los logobestand.** Haal het logo op via de URL in Bijlage A en plak het als volledige data-URI in de `<img>`-tag. Een los bestand raakt bij delen of archiveren zoek.
- Geef de logo-`<img>` een expliciete `width` en `height`, anders kan de lay-out inklappen in previews.

### 2.2 Fonts in HTML

**De regel:** fonts worden, net als logo's, als `@font-face` met een base64 data-URI **in het bestand zelf** ingebed — geen `<link>` naar een CDN.

Praktische manier om aan de woff2-bestanden te komen: de npm-pakketten `@fontsource/merriweather` en `@fontsource/open-sans` bevatten de kant-en-klare woff2's per gewicht (`node_modules/@fontsource/merriweather/files/merriweather-latin-400-normal.woff2`, enzovoort). Codeer het gewenste subset (400/700 normal + 400 italic voor Merriweather, 400/600/700 normal voor Open Sans) base64 en bouw daarmee dit blok, vóór de overige `<style>`-regels:

```html
<style>
@font-face{
  font-family:'Merriweather';
  font-style:normal;
  font-weight:400;
  src:url(data:font/woff2;charset=utf-8;base64,....) format('woff2');
}
/* idem voor gewicht 700, cursief 400, en Open Sans 400/600/700 */
</style>
```

Dit voegt ca. 150–250 KB toe — acceptabel, en de enige manier om te garanderen dat het document er bij de ontvanger hetzelfde uitziet, ook offline.

Gebruik alleen fontgewichten die je ook embedt. `font-weight:600` op Merriweather bijvoorbeeld wordt niet meegeleverd — de browser bootst dat dan lelijk na.

### 2.3 Kleuren als CSS-variabelen

Elk bestand definieert zijn palet bovenaan als CSS custom properties:

```css
:root{
  --inkt:#27275B;       /* koningsblauw, §1.1 */
  --inkt-mid:#4E4E79;
  --inkt-zacht:#66668A; /* 4,9:1 op papier — leesbaar voor secundaire tekst */
  --papier:#F5F3EE;
  --wit:#FFFFFF;
  --goud:#DDB85E;
  --goud-mat:#C7AD79;
  --goud-licht:#F1E7D0;
  --lijn:#DCD8CE;
  --wit-zacht:#BEBECE;  /* secundaire tekst op donkerblauw, 7,5:1 */
}
```

Nooit losse hex-codes in de rest van het document — ook niet in SVG's (dus `fill="var(--inkt)"`, niet `fill="#27275B"`). Zo blijft een kleurwijziging één regel werk.

**Dit `:root`-blok staat precies één keer in het bestand, bovenaan en compleet.** Verandert het kleurenschema, herschrijf dan dit ene blok; zet er geen tweede blok achter.


### 2.4 Component-kit

Bouwstenen. Gebruik wat past bij het documenttype, laat weg wat niet nodig is:

- **Titelblok** — donkerblauw, met logo, eyebrow-regel, titel, subtitel, eventueel een dunne effen goudlijn als breker (geen chevron-lijnaccent, zie §1.3)
- **Hoofdstukkop** — donkerblauw blok met chevron-icoon + nummer + titel — dit is de vaste, herkenbare plek voor het chevron-icoon (zie §1.3). Het nummer krijgt **dezelfde kleur en hetzelfde lettertype/gewicht/formaat als de titel ernaast** (beide wit, `Open Sans` bold, `font-size` tussen **1.1rem en 1.3rem**, vergelijkbaar met een h3) — géén apart goud of een ander lettertype voor het cijfer. Nummer en titel horen visueel bij elkaar; laat het cijfer gewoon de kleur van de omringende tekst erven (`color` niet apart overschrijven op `.nummer`), niet weggemoffeld als klein label. Het chevron-icoon ernaast schaalt mee, ongeveer even hoog als het cijfer.
- **"In het kort"-kader** — korte samenvatting bovenaan een sectie
- **Doelenlijst** — gewone bullets. Geen chevron-bullets: dat oogt al snel druk over een hele pagina tekst
- **Zelfcheck/kadertje met badge** — kleine navy "merkje" boven een korte tekst
- **Voorbeeldkader** — zachte goudtint, voor cases en toelichtingen
- **Pull quote** — dikke goud zijrand, opvallende regel
- **Tabellen** — donkerblauw kopregel, witte tekst
- **Figuren/diagrammen** — SVG met bijschrift
- **Klikbare navigatie** — bij een langere tekst (vanaf een stuk of vijf secties/hoofdstukken): een vaste "Inhoud"-knop rechtsonder die een uitschuifpaneel opent, zie §2.5
- **Footer** — donkerblauw, **wit logo zonder tagline** (Bijlage A) + documentregel. Gebruik nooit het losse beeldmerk náást het logo: het logo bevat het beeldmerk al, dus dan staat het hexagon-icoon dubbel. Geef de footer onderaan ca. 88px padding, zodat de vaste "Inhoud"-knop de documentregel niet afdekt (in print terug naar normaal).
- **Bronfragment** — letterlijk citaat uit een klantstuk (bijv. als oefenmateriaal): papiertint-vlak, dunne `--inkt-zacht` zijrand, cursief, iets kleiner dan de lopende tekst. Duidelijk anders dan de pull quote (goud), zodat lezers zien: dit is brontekst, geen eigen kernboodschap.
- **Hergebruikte slides als figuur** — slides uit een ander klanttraject mogen als figuur worden ingebed, maar **altijd zonder het logo van die andere klant** (pixelvlak wegpoetsen naar de achtergrondkleur vóór het inbedden, daarna programmatisch controleren dat er geen restpixels over zijn). Het DBF-logo mag blijven staan. Noem de andere klant ook niet in bijschrift of bronvermelding.


### 2.5 Klikbare navigatie bij langere teksten

Vanaf een stuk of vijf hoofdstukken/secties wordt scrollen zonder overzicht vervelend. Voeg dan een vaste navigatie toe — niet als vervanging van een eventuele inhoudsopgave bovenaan (die blijft, ook handig voor print), maar als aanvulling die tijdens het lezen bereikbaar blijft.

**Patroon:**
- Een ronde knop rechtsonder in beeld, donkerblauw met een icoontje (bijv. een klein lijstje of chevron-teken, geen hexagon), `position:fixed`, altijd zichtbaar tijdens scrollen.
- Een uitschuifpaneel (donkerblauw, vanaf de rechterkant) met dezelfde inhoudsopgave-lijst als bovenaan het document, plus een sluitknop en een overlay die het paneel ook sluit bij klikken ernaast.
- De sectie die je op dat moment aan het lezen bent wordt in het paneel gemarkeerd (dikgedrukt + dunne goudlijn links), bijgewerkt via `IntersectionObserver` op elke sectie (`data-nav-section`).
- Onderaan elk hoofdstuk een kleine "↑ Terug naar inhoud"-link (gewoon pijltje, geen hexagon-icoontje — dat is te veel herhaling van hetzelfde motief) die terugspringt naar het anker van de inhoudsopgave.
- Verberg knop, paneel en overlay in de print-mediaquery — op papier is dit zinloos.
- Werkt zonder dependencies: puur CSS (`transform: translateX()` voor de animatie) en vanilla JS.

Kant-en-klare CSS-bouwstenen (vult aan op de tokens uit §3):

```css
.navtoggle{
  position:fixed; right:22px; bottom:22px; z-index:40;
  display:flex; align-items:center; gap:10px;
  background:var(--inkt); color:var(--wit); border:none; border-radius:999px;
  padding:13px 20px 13px 16px; cursor:pointer;
  font-family:'Open Sans',sans-serif; font-weight:700; font-size:.9rem;
  box-shadow:0 6px 20px rgba(39,39,91,.35);
}
.navpanel{
  position:fixed; top:0; right:0; height:100%; width:min(380px, 88vw);
  background:var(--inkt); color:var(--wit); z-index:60;
  transform:translateX(100%); transition:transform .28s ease;
  padding:28px 26px; overflow-y:auto;
}
.navpanel.open{ transform:translateX(0); }
.navpanel-overlay{
  position:fixed; inset:0; background:rgba(39,39,91,.45); z-index:50;
  opacity:0; pointer-events:none; transition:opacity .28s ease;
}
.navpanel-overlay.open{ opacity:1; pointer-events:auto; }
.navtoggle.is-hidden{ opacity:0; visibility:hidden; pointer-events:none; }
.toc-list--panel li.actief::before{
  content:""; position:absolute; left:-26px; top:0; bottom:0; width:3px; background:var(--goud);
}
@media print{ .navtoggle, .navpanel, .navpanel-overlay, .terug-naar-inhoud{ display:none !important; } }
```

Bijbehorende JS (open/sluiten + actieve sectie):

```html
<script>
(function(){
  var toggle = document.getElementById('navtoggle');
  var panel = document.getElementById('navpanel');
  var overlay = document.getElementById('navpanel-overlay');
  function openPanel(){
    panel.classList.add('open'); overlay.classList.add('open');
    toggle.classList.add('is-hidden'); document.body.style.overflow = 'hidden';
  }
  function closePanel(){
    panel.classList.remove('open'); overlay.classList.remove('open');
    toggle.classList.remove('is-hidden'); document.body.style.overflow = '';
  }
  toggle.addEventListener('click', function(){
    panel.classList.contains('open') ? closePanel() : openPanel();
  });
  overlay.addEventListener('click', closePanel);
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closePanel(); });
  panel.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', closePanel); });

  var sections = document.querySelectorAll('[data-nav-section]');
  var panelLinks = {};
  panel.querySelectorAll('.toc-list--panel > li').forEach(function(li){
    var a = li.querySelector('a');
    if(a) panelLinks[a.getAttribute('data-target')] = li;
  });
  var observer = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      var li = panelLinks[entry.target.id];
      if(!li || !entry.isIntersecting) return;
      Object.keys(panelLinks).forEach(function(k){ panelLinks[k].classList.remove('actief'); });
      li.classList.add('actief');
    });
  }, { rootMargin: '-40% 0px -55% 0px', threshold: 0 });
  sections.forEach(function(s){ observer.observe(s); });
})();
</script>
```

Elke sectie krijgt `id="<slug>"` en `data-nav-section`; elke link in het paneel krijgt `data-target="<slug>"` zodat de twee aan elkaar te koppelen zijn.

Drie dingen zitten al in deze code en moeten erin blijven: de knop verdwijnt zolang het paneel open is (`.is-hidden`), een klik op een link sluit het paneel, en de pagina scrollt niet door achter het open paneel.


### 2.6 Titelblok en body horizontaal laten uitlijnen

De tekst in het titelblok moet precies boven de tekst in de body staan.

**De regel:** horizontale padding staat nooit direct op `header.top` of `footer` zelf — die elementen blijven edge-to-edge voor de kleurband. Zet de padding in plaats daarvan op een binnenste wrapper (`.top-inner`, vergelijkbaar met `.wrap`) en gebruik daar **exact dezelfde waarde** als bij `.wrap` (inclusief de waarde in de print-/mobiel-mediaquery). Alleen dan lijnt de tekst in het titelblok uit met de tekst in de body, ongeacht de schermbreedte.

```css
.wrap{max-width:800px;margin:0 auto;padding:0 24px 100px}
.top-inner{max-width:800px;margin:0 auto;padding:0 24px}  /* zelfde 24px, geen padding op header.top zelf */
```


### 2.7 Toegankelijkheid — niet-onderhandelbaar

- Minimale contrastratio: 4,5:1 voor lopende tekst, 3:1 voor grote koppen.
- De regel die uit ons palet volgt: **goud is nooit tekstkleur op een lichte achtergrond.**
- Vlakken met witte tekst erop (labels, chips, badges) staan op donkerblauw — nooit op goud, dat geeft wit-op-licht en is onleesbaar.
- Controleer dit door het bestand daadwerkelijk te renderen, niet door alleen de code te lezen. Fouten hierin zijn met het blote oog in code makkelijk te missen.


### 2.8 Techniek en oplevering

- Eén zelfstandig HTML-bestand: CSS inline in een `<style>`-blok, logo's, beelden **en fonts** als base64 data-URI ingebed (zie §2.2). Geen losse bestanden en geen CDN-`<link>`'s. Dit is een harde eis: een verwijzing naar een los bestand of naar Google Fonts is een gebroken oplevering, ook als het er bij jou goed uitziet.
- Test responsief: smal (mobiel) én breed scherm. Voeg een print-mediaquery toe als het document ook afgedrukt moet kunnen worden.
- Test met de daadwerkelijk geladen fonts vóór oplevering, niet alleen met fallback-fonts. Merriweather en Open Sans zijn beide breder dan een generieke systeemfont — bij vaste-breedte elementen (SVG-labels, badges) kan dat tot overlopende tekst leiden als je dat niet checkt.


### 2.9 Checklist vóór oplevering

- [ ] Kleuren komen exact overeen met het paletblok (§2.3)
- [ ] `:root`-kleurenblok komt precies één keer voor — geen tweede of derde blok dat het eerste overschrijft
- [ ] Logo is het officiële bestand, correct gerenderd (niet wit-op-wit)
- [ ] Logo is ingebed als `data-URI` (`src="data:image/png;base64,..."`), **niet** als verwijzing naar een losse bestandsnaam (`src="logo.png"`)
- [ ] Tagline "IDENTITY MARKETING" alleen bij grote, eenmalige plaatsingen — kleine/herhalende plekken (documentkopje, footer) gebruiken de wordmark zonder tagline (Bijlage A)
- [ ] Fonts (Merriweather + Open Sans) zijn als `@font-face` met base64 data-URI **in het bestand ingebed** — geen `<link>` naar de Google Fonts CDN, alleen embedded gewichten gebruikt
- [ ] Chevron-teken (niet hexagon) is gebruikt als hoofdstuknummer-icoon (§1.3); géén chevron-lijnaccent (verboden) — nergens als bullet voor gewone lijsten of koppen. Het hexagon-vormige beeldmerk (Bijlage A) is de uitzondering: dat is het logo zelf, geen decoratief motief
- [ ] Hoofdstuknummer heeft dezelfde kleur en hetzelfde lettertype/gewicht als de titel ernaast (geen apart goud, geen ander font), en een leesbare maat (1.1–1.3rem, zie §2.4), niet weggemoffeld als klein label
- [ ] Contrast gecontroleerd — geen goud-tekst op licht vlak
- [ ] Getest op mobiele én desktopbreedte
- [ ] Bij een langere tekst (vanaf ~5 secties): klikbare navigatie toegevoegd (§2.5), en getest dat die in print verborgen is
- [ ] Vaste navigatieknop wordt onzichtbaar/onklikbaar zolang het paneel open is (`.is-hidden`-patroon), geen z-index-gok
- [ ] Klikken op een link in het navigatiepaneel sluit het paneel ook (niet alleen navigeren)
- [ ] Titelblok (`header.top`) en body (`.wrap`) gebruiken identieke horizontale padding op de binnenste wrapper (§2.6) — tekst lijnt uit, ook op mobiel
- [ ] Eén zelfstandig bestand, geen gebroken links of ontbrekende assets
- [ ] Daadwerkelijk gerenderd bekeken — geen code-only review

### 2.10 Prompt-ready instructie voor AI-gebruik

Kort blok om mee te geven bij een nieuwe HTML-opdracht aan een AI-tool:

> Gebruik de huisstijl van de Betekenisfabriek: koningsblauw `#27275B` en goud `#DDB85E` als basiskleuren, Merriweather voor koppen en lopende tekst, Open Sans voor labels en tabellen — beide als `@font-face` met base64 ingebed, **geen** `<link>` naar Google Fonts. Gebruik het officiële logo (nooit zelf getekend, ook als base64 ingebed), en zorg dat goud nooit als tekstkleur op een licht vlak wordt gebruikt — alleen als lijn, rand of tekst op donkerblauw. Gebruik het chevron-teken (`›`, §1.3) uitsluitend als enkel hoofdstuknummer-icoon — **geen** herhalend chevron-lijnaccent en **niet** het hexagon-motief, dat is uitsluitend de vorm van het beeldmerk zelf. Het hoofdstuknummer krijgt dezelfde kleur en hetzelfde font als de titel ernaast, geen apart goud. Bouw met de bouwstenen uit §2.4, pas vrij aan naar het documenttype. Is de tekst lang (vanaf ~5 secties/hoofdstukken)? Voeg dan de klikbare navigatie uit §2.5 toe: vaste knop rechtsonder, uitschuifpaneel met inhoudsopgave, actieve sectie gemarkeerd tijdens scrollen.

---

## 3. PowerPoint

Bron: `Powerpoint_sjabloon.potx`. Palet, logo en chevron: zie §1. Opening, scheiding en slot volgen Bijlage B.3.

### 3.1 Kleurgebruik in PowerPoint

- **Koningsblauw `#27275B`** is de donkere kleur (footerbalk, tekstvlak openingsdia, scheidings- en slotdia, headerbalken), zoals in alle formaten (§1.1).
- **Lichte kaartvlakken op witte contentdia's: lichte navy-tint `#E3E4ED`.** Niet crème; crème alleen voor de "Plaatjes"-instructiedia.
- **Zand `#ECE4D7`** (§1.1 B) voor wat nadruk krijgt: citaten, beoogd resultaat, kernkaarten. Houdt warmte in een overwegend blauwe presentatie. Tekst erop in zwart of koningsblauw (contrast 10,9:1). Hooguit twee vlaktinten per dia.
- **Tabel-heatmap** (bijv. scoringsmatrix): sterkste waarde goud, middelste `#AEB0C9`, zwakste `#E3E4ED`. Geen drie losse kleuren zoals sommige klantbestanden doen.

### 3.2 Fonts in PowerPoint

| Rol | Font | Grootte en kleur |
|---|---|---|
| Titel openingsdia | Merriweather, bold | ±36–44pt, wit |
| Titel inhoudsdia | Merriweather, bold | 26pt, koningsblauw |
| Lopende tekst | Open Sans | 14–16pt, zwart |
| Ingebedde varianten | Merriweather regular/bold/italic, Open Sans regular/bold/italic | Gebruik geen andere gewichten |

In code de familienamen `Merriweather` en `Open Sans`, precies zoals ze in de ingebedde lettertypebestanden heten (§3.6).

### 3.3 Vormstijl

- Effen vlakken, geen lijn/omlijning (expliciet genoteerd in bronbestand: "Doen we zo: effen vlakken zonder lijn").
- Openings-, scheidings- en slotdia: zie §3.5 en Bijlage B.3.
- Footerbalk op inhoudsdia's blijft ruim binnen de dia-breedte staan, zodat er naast het DBF-logo ook plek is voor een opdrachtgeverslogo (co-branding, zie cover-slide).


### 3.4 Accentgebruik: waar de huisstijl bewust "donker" inzet

Opening, scheidingsdia's en slot hebben hun vaste donkere vormgeving (§3.5). Daarnaast mag **één scharniermoment** in een langere
presentatie — de conclusie of het inzicht waar de rest van het verhaal naartoe werkt — dezelfde
volle, donkere behandeling krijgen in plaats van de lichte inhouds-chrome. Dit is een bewuste
uitzondering, geen vast om-de-zoveel-dia's-ritme: per document beoordelen welke dia het verdient.
Voorbeeld: in een analyse van negen dia's krijgt de dia met het antwoord op de hoofdvraag deze behandeling.


### 3.5 Contentdia-indeling (referentie-implementatie, 16:9 standaard 13,333 × 7,5 inch)

Dit is de werkende maatvoering; nieuwe presentaties bouwen hierop (zie ook §6 over de slidemaster).

**Kleuren/fonts:** zie §3.1 en §3.2.

**Contentdia-chrome (`contentChrome`):**

| Element | Positie (inch) | Toelichting |
|---|---|---|
| Linker fotostrook | x=0, y=0, w=0,80, h=7,18 | `DBF_fotostrook_zw.png`: zwart-wit, zonder kleurfilter |
| Navy footerbalk | x=0, y=7,18, w=9,35, h=0,32 | **Bewust korter dan de dia** — laat ruimte vrij voor een opdrachtgeverslogo naast het DBF-logo |
| DBF-logo | w=1,3, rechts uitgelijnd op x=12,67 (= contentmarge-rand), y=6,64 | Zwart logo, **los boven** de balk in het wit — niet op/in de balk zelf, die is te dun (0,32") voor de logohoogte (0,42") |
| Contentmarge | x=1,62, breedte 11,05 | Geldt voor titel, body en footerbijschriften |
| Footerbijschriften | y=6,9, 9pt Open Sans, grijs `#464646` | Optioneel links/rechts, boven de balk |

**Openingsdia** (volgens Bijlage B.3):
- Links een effen tekstvlak in koningsblauw, rechts een foto. Het vlak beslaat ongeveer de linkerhelft (richtwaarde; vastleggen zodra er een goedgekeurd voorbeeld is).
- Foto altijd aanwezig; keuze volgens §1.7: historisch beeld → sessiebeeld → strandsilhouetten. Foto en tekstvlak raken elkaar, overlappen niet. Geen patroon.
- In het tekstvlak: titel wit, Merriweather bold, ±36–44pt; direct eronder de korte gouden lijn (0,15" afstand); ondertitel wit direct onder de lijn (0,13" afstand). Daaronder twee metaregels: een inhoudelijke regel en de documentdatum.
- Logo: wit, mét tagline (Bijlage A), 0,5 inch hoog, linksonder in het tekstvlak. Niet op de foto.

**Scheidingsdia:** effen koningsblauw, nummer in goud, titel wit. Eventueel een foto ernaast (§1.7). Geen patroon.

**Slotdia:** patroon over de volle dia (`DBF_patroon_slotdia_koningsblauw.png`, Bijlage B), met in het midden het logo wit mét tagline, 0,7 inch hoog. Geen tekst.

**Foto-assets uit het sjabloon** (overgenomen uit `Powerpoint_sjabloon.potx`):

| Bestand | Gebruik | Behandeling |
|---|---|---|
| `DBF_fotostrook_zw.png` (kathedraal-detail, 88 × 790 px) | Linker fotostrook op contentdia's, alleen in PowerPoint | Zwart-wit, **zonder kleurfilter**. Al op maat (verhouding 0,1114); plaatsen op 0,80 × 7,18 inch, niet opnieuw bijsnijden |
| `DBF_titelfoto_strand.jpg` (silhouetten op het strand, 2765 × 1844 px) | Openingsdia, rechterhelft — alleen als laatste keuze (§1.7) | Ongefilterd; per presentatie bijsnijden op hoofd-tot-voeten, niet centreren op de lucht |

URL's: `https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF_fotostrook_zw.png` en `https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF_titelfoto_strand.jpg`. De strook is klein (de foto in het sjabloon heeft niet meer pixels); op een groot scherm is hij iets zacht. Strandsilhouetten nooit in HTML gebruiken (§1.6).

**Crop zonder vervorming:** zie §1.5.

**Donkere "accent"-dia:** zie §3.4 — koningsblauw, witte kaarten, goud als doorbreker, klein
wit beeldmerk rechtsonder (± 0,4").

**Chevron als kopmarkering:** hoogte ± 0,30–0,32", goud — op licht én op donker. Koningsblauw alleen als variant op lichte kaarten. Geen apart nummer nodig — de chevron zelf is de markering.

**Uitlijning chevron:** zie §1.3.


### 3.6 Fonts embedden — verplichte stap, geen optie

`pptxgenjs` embedt zelf **geen** fonts. Merriweather en Open Sans staan op bijna geen computer standaard;
zonder embedding ziet de presentatie er bij de ontvanger anders uit.

Procedure:
1. Lettertypen: de TTF-versies van Merriweather (regular, bold, italic) en Open Sans (regular, bold, italic). Bron: `@fontsource/merriweather` en `@fontsource/open-sans` (npm), omgezet van woff2 naar ttf met `fontTools`. Beide zijn vrij in te sluiten (OFL, fsType 0).
2. Elk TTF-bestand omzetten naar EOT (versie 0x00020001, ongecomprimeerd, met familie-, stijl-, versie- en volledige naam in de kop) en opslaan als `ppt/fonts/fontN.fntdata`. Het volledige lettertype blijft intact; niet herschrijven of tabellen weglaten.
3. Per familie één `<p:embeddedFont>` met `<p:regular>`, `<p:bold>` en `<p:italic>`, direct na `<p:notesSz/>`; `embedTrueTypeFonts="1"` op `<p:presentation>`; fontrelaties in `ppt/_rels/presentation.xml.rels`; `Default Extension="fntdata"` in `[Content_Types].xml`.
4. **Controleer met een script:** de EOT-kop leesbaar, het lettertype erin te openen, en `validate.py` slaagt. Controleer daarna in echte PowerPoint (niet Keynote of Voorvertoning, die negeren ingesloten lettertypen).

### 3.7 Chevron-bibliotheek — alle paletkleuren (ook bruikbaar in Word)

De chevron is **in elke kleur uit het palet** (§1.1) beschikbaar als transparante PNG (924 × 1316 px), allemaal met dezelfde vorm (§1.3). Ophalen via `https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/<bestandsnaam>`. Een nieuwe kleur nodig? Genereer die uit de vectorpunten, niet door een bestaande PNG te verkleuren.

| Bestand | Hex | Paletnaam | Opmerking |
|---|---|---|---|
| `DBF_chevron_navy.png` | `#27275B` | Koningsblauw | **Bestaande naam, let op:** heet "navy" maar is koningsblauw, níet het palet-"Navy" (`#222831`) hieronder — naam blijft zo omdat bouwscripts ernaar verwijzen. Dit is de standaardvariant op lichte achtergronden. |
| `DBF_chevron_222831.png` | `#222831` | Navy | Los van de koningsblauwe variant hierboven — alleen gebruiken als een dia expliciet het palet-"Navy" nodig heeft, niet als vervanging van `chevron_navy.png`. |
| `DBF_chevron_30475E.png` | `#30475E` | Blauw | — |
| `DBF_chevron_C1A57B.png` | `#C1A57B` | Goud | Te onderscheiden van de DBF-accentgoud hieronder. |
| `DBF_chevron_gold.png` | `#DDB85E` | Goud (DBF) | Bestaande naam. Standaard goud-variant, o.a. op navy achtergrond. |
| `DBF_chevron_ECECEC.png` | `#ECECEC` | Grijs | Laag contrast op wit — alleen bruikbaar op een donkere achtergrond. |
| `DBF_chevron_000000.png` | `#000000` | Zwart | — |
| `DBF_chevron_white.png` | `#FFFFFF` | Wit | Bestaande naam. Standaard witte variant, o.a. op navy achtergrond. |
| `DBF_chevron_FFFCF2.png` | `#FFFCF2` | Crème | Zeer laag contrast op wit; alleen zinvol op een donkere achtergrond, en dan nog subtiel. |
| `DBF_chevron_E3E4ED.png` | `#E3E4ED` | Lichte navy-tint | Zeer laag contrast op wit; alleen zinvol op een donkere achtergrond. |

**Gebruik:** kies de kleur op basis van de achtergrond waarop de chevron staat (voldoende contrast), niet
standaard navy of goud. Grijs, crème en de lichte navy-tint zijn alleen bruikbaar op koningsblauwe vlakken
(openingsvlak, scheidings- en slotdia, donkere accentdia) — op wit vallen ze niet op.


---

## 4. Word

Bron: `DBF_offerte_sjabloon.dotx` (afgeleid van het oorspronkelijke `Offertesjabloon.dotx`), gevalideerd in Word. Logo-tagline: zie de uitzondering in §1.2.

### 4.1 Offerte

#### Pagina & marges (A4)
| Marge | Waarde |
|---|---|
| Boven | 4,92 cm |
| Onder | 3,2 cm |
| Links | 3,2 cm |
| Rechts | 3,05 cm |
| Koptekst-afstand | 0,49 cm |
| Voettekst-afstand | 1,25 cm |

Deze marges gelden voor de offerte; voor brief en rapport zijn ze nog niet vastgesteld.

#### Logo & header
- Logo: **horizontale versie mét ondertitel "IDENTITY MARKETING", zwart** — herhaalt op **elke pagina** (geen aparte eerste-pagina-behandeling).
- Afmeting in header: 6,47 × 2,02 cm, aspect ratio vast.
- Positie: 2,21 cm links van de kolomrand (steekt iets in de marge), 1,10 cm onder de bovenkant van het kopgebied.
- Dit overrulet voor de offerte de standaard tagline-regel (zie §1.2).

#### Footer
- Op elke pagina: bedrijfsgegevens (adres, KVK, BTW, IBAN) + paginanummer rechts uitgelijnd.
- Font: **Calibri Light, 5,5pt**, kleur **koningsblauw `#27275B`** (§1.1).

#### Lopende tekst
- Font: **Calibri Light**
- Grootte: **10,5pt**, standaard en overal consistent (geen 10pt-uitzonderingen meer)
- Regelafstand: **1,15** (proportioneel), niet vast/exact

#### Koppen
- Geïmplementeerd als **echte Word-stijl** (Heading 1, outline-niveau ingesteld — navigeerbaar/TOC-geschikt), niet als losse vet-opmaak.
- Uiterlijk: Calibri Light, vet, 10,5pt, zwart (zelfde grootte als body — geen niveau-hiërarchie in grootte). Vastgelegd in de stijl zelf, zodat een nieuwe kop niet in Word-standaardblauw verschijnt.

#### Tabel (bijv. planning & investering) — geldt voor élke tabel met data
- Randen: **bovenrand + horizontale lijnen tussen rijen** (zwart, dun, ~0,1mm).
- **Geen verticale lijnen. Geen sluitende onderrand** onder de laatste rij of totaalrij.
- **Headerrij is verplicht, ook bij een simpele 2-koloms rijtjes-tabel** (bijv. een label/waarde-lijst zoals percentages): **20%-zwart patroonvulling** (`w:shd val="pct20"`), geen vaste hexkleur zoals `#ECECEC` — dat is dus een lichtgrijs patroon, niet een hex-literal. Kolomkoppen vet.
- Teksten: Calibri Light, 9pt; header vet.
- Bij smalle eerste kolom: check dat het kopwoord op één regel past (bijv. "Waarde" i.p.v. "Richtwaarde") — anders kolombreedte vergroten, niet het woord laten afbreken.

#### Bijlage / algemene voorwaarden (kleine lettertjes)
- "Bijlage"-kop: Calibri Light, vet, **12pt** — enige plek met een écht grotere kop dan de rest.
- Artikel-koppen: vet, **Calibri (niet Light)**, 6pt.
- Body-tekst voorwaarden: **Calibri (niet Light)**, 6pt.
- Bewust gewone Calibri: Calibri Light is op dit kleine corps onleesbaar.
- Regelafstand **1,15**, net als de rest van het document; genummerde leden als echte Word-nummering, per artikel opnieuw vanaf 1.
- **Bron:** `DBF_algemene_voorwaarden.md`, https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF_algemene_voorwaarden.md (gecontroleerd 10 oktober 2026: bereikbaar, juiste inhoud, versie 10 oktober 2026). Geldt voor offertes en elk ander document dat de voorwaarden bevat of ernaar verwijst.
- Haal de tekst bij elk gebruik opnieuw op en controleer de versiedatum. Neem de voorwaarden nooit over uit oudere offertes of andere documenten.
- Wijzig de juridische tekst niet zelf: geen vereenvoudiging, samenvatting of herformulering zonder expliciete opdracht. Is de bron niet bereikbaar, meld dat in de kwaliteitsrapportage in plaats van een oudere tekst te gebruiken.

#### Kleuren die daadwerkelijk voorkomen in dit document
- Zwart `#000000` (lopende tekst)
- Wit `#FFFFFF` (achtergrond)
- Koningsblauw `#27275B` (uitsluitend footer-tekst)
- Geen goud, geen `#30475E`, geen `#ECECEC` als hex — die kwamen in dit document niet voor.

#### Bestand
- `DBF_offerte_sjabloon.dotx` — Word-template met bovenstaande waarden, generieke placeholders (`[Naam klant]`, `[Fase 1: omschrijving]`, etc.), algemene voorwaarden verbatim overgenomen (die zijn al generiek/herbruikbaar). URL: `https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF_offerte_sjabloon.dotx`.

### 4.2 Regels voor álle Word-documenten (ook rapport/boekje en memo)

Opbouwregels, geen smaakkeuzes.

**Alinea-afstand — functioneel onderscheid, nooit één uniforme waarde voor het hele document:**
- **Binnen een alinea** (interlinie): overal 1,15 (`line: 276, lineRule: auto`).
- **Tussen gewone lopende alinea's**: een volledige regel extra erna (`after: 276`).
- **Lijst-items onderling**: geen extra ruimte (`after: 0`).
- **De zin die een lijst inleidt** (eindigt op ":"): geen ruimte erna.
- **Koppen**: ruimte ervóór (`before: 276`), niets erna (`after: 0`).
- **Tabelcellen, footer, voorwaarden-clausules**: tight (`after: 0`).
- Vastgelegd in `PARA_SPACING`/`TIGHT_SPACING`-constanten. Bij twijfel: een echt referentiedocument opvragen en meten, niet raden.

**Stijlen:**
- Bestaande Word-stijlen (Heading1 t/m 6, Title, ListParagraph, etc.) altijd **overschrijven** via de override-mechaniek. Nooit een tweede stijl met dezelfde id toevoegen — dan is onvoorspelbaar welke Word gebruikt.

**Lijsten:**
- Elke lijstdefinitie krijgt expliciet `rFonts` (Calibri Light) op het niveau zelf, anders staat het bullet- of nummerteken in Times New Roman.
- Minimale hangende inspringing (227/454 twips), niet de brede Word-default.
- Alinea's die als losse tekst beginnen met "1. ", "2. " (geen echte Word-numbering) krijgen een hangende inspringing van ±200 twips.
- Rijtjes van parallelle label/waarde-paren (bijv. "30% → betaald werk") horen in een tabel, niet als bullets. Verhalende punten blijven bullets.

**Tabellen:**
- Vaste DXA-breedtes (`columnWidths` op de tabel + `width` in DXA op elke cel) plus `layout: TableLayoutType.FIXED`. Nooit percentage-breedtes.
- Moet de tabel een rand hebben, dan krijgt **geen enkele cel** zelf een randinstelling — cel-niveau wint altijd van tabelniveau.
- Elke tabel met data krijgt de standaard tabelstijl uit §4.1 (headerrij 20%-grijs, bovenrand + rijlijnen). "Rustig" betekent geen verticale lijnen en geen zware opmaak, niet: geen randen of geen headerrij. Headerrij herhaalt bij pagina-afbreking.
- Uitzondering: een onzichtbare lay-outtabel (bijv. ondertekenblok) is geen datatabel.

**Verificatie:**
- Valideer met de OOXML-schemavalidator (`scripts/office/validate.py` uit de docx-skill) op het daadwerkelijk opgeleverde bestand.
- LibreOffice zonder Calibri Light geeft renderartefacten (bijv. tab-uitlijning) die in echte Word niet bestaan, en andersom: fouten die in LibreOffice onzichtbaar zijn, kunnen in Word wél zichtbaar zijn.

### 4.3 Bewust neutrale keuzes (nog geen brondocument)

- **Verhalende bullets/genummerd:** standaard rond bolletje (•) / decimaal cijfer, sub-niveau open bolletje (◦), Calibri Light 10,5pt, geen kleur. **Open vraag:** een DBF-specifieke lijststijl? De brief- en rapportsjablonen tonen de chevron als opsommingsteken met inspringing (§1.3) — dat ligt meer voor de hand dan een hexagon (die is als bullet uitgesloten).
- **Citaat:** cursief, verder ongewijzigd.
- **Inhoudelijke (niet-juridische) bijlage:** gewone body-opmaak, niet het 6pt-corps.
- **Investering:** mag ook een genummerde lijst met rechts-uitgelijnde tab zijn als de brontekst dat al zo aanlevert.

### 4.4 Nog te doen

Rapport/boekje (Word) en memo (Word). Per type: eigen bronbestand aanleveren, technisch valideren, stijlwaarden extraheren, pas dan bouwen. Tot die tijd gelden §1 en §4.2; marges, logo en koppen uit §4.1 zijn alleen voor de offerte geverifieerd.

---

## 5. Kwaliteitsrapportage bij elke oplevering

Bij elke uiting die Claude maakt of inhoudelijk bewerkt (Word, PowerPoint, PDF, HTML en vergelijkbare formaten) hoort een aparte kwaliteitsrapportage in Markdown: `[documentnaam]_kwaliteitsrapportage.md`. Intern, niet voor de opdrachtgever en nooit in het einddocument. Bij een kleine correctie op een eerder opgeleverde uiting volstaat een korte aanvulling op de bestaande rapportage.

Claude heeft daarbij twee rollen: **maker** (zorgvuldig, creatief, trouw aan de huisstijl) en **kritische meelezer** (alert op inhoudelijke zwaktes, inconsistenties, onbedoelde overnames, privacyrisico's). De rapportage is een vast onderdeel van het werk, geen verantwoording achteraf.

**Status bovenaan**, met een korte toelichting eronder:
- 🟢 **GEREED VOOR GEBRUIK** — geen wezenlijke problemen binnen de uitgevoerde controles.
- 🟠 **AANDACHTSPUNTEN** — bruikbaar, maar met punten die beoordeling verdienen.
- 🔴 **NIET VERSPREIDEN VÓÓR CONTROLE** — mogelijk kritieke fouten: vertrouwelijke informatie, gegevens van een andere opdrachtgever, wezenlijke inhoudelijke problemen.

Groen is geen garantie dat een document foutloos, juridisch juist of AVG-proof is. De status rust alleen op controles die echt zijn uitgevoerd.

**Zes verplichte onderdelen:**
1. **Vormkeuzes** — compositie, typografie, kleur, witruimte, hiërarchie, inzet of bewust weglaten van huisstijlelementen. Concreet: hoe heeft de inhoud de vorm bepaald?
2. **Beeldmateriaal** — per beeld: wat, waar, waarom inhoudelijk en visueel, bron en rechten, onzekerheden. Of waarom bewust geen beeld.
3. **Stijl- en spelspanningen** — tussen inhoud, huisstijl, medium en ontwerp. Onderscheid bewuste, gemotiveerde afwijkingen van onbedoelde inconsistenties. Een spanning hoeft niet altijd opgelost; soms moet ze alleen zichtbaar zijn.
4. **Inhoud en opbouw** — logica, centrale boodschap, volgorde, ontbrekende redeneringen, tegenstrijdigheden, herhaling, onduidelijke formuleringen, toon, overtuigingskracht. Concrete verbeterpunten; de bedoeling van de auteur niet eigenmachtig veranderen.
5. **Vreemde of onbedoeld overgenomen inhoud** — namen van andere opdrachtgevers, organisaties, projecten of personen; verkeerde plaatsen en data; achtergebleven kop- en voetteksten; verwijzingen naar andere trajecten; interne opmerkingen. Waar mogelijk ook sprekersnotities, opmerkingen, verborgen tekst en metadata. Aantoonbare fouten binnen de opdracht corrigeren en melden; twijfelgevallen voorleggen, nooit stilzwijgend verwijderen.
6. **Privacy en vertrouwelijkheid** — persoons- en contactgegevens, cliënt-, leerling- of medewerkergegevens, medische en financiële gegevens, interne correspondentie, gegevens van andere opdrachtgevers, metadata. Onderscheid terecht opgenomen van mogelijk onbedoeld. Gevoelige gegevens niet letterlijk in de rapportage: benoem het soort risico en de plek. Bij twijfel markeren en menselijke beoordeling vragen.

**Rapportageregels:** alle zes onderdelen verplicht; niets te melden is "Geen bijzonderheden aangetroffen." Verwijs naar pagina, dia of paragraaf. Onderscheid vastgestelde fouten, vermoedelijke problemen en aanbevelingen; kritieke bevindingen eerst. Vermeld uitgevoerde correcties en technische beperkingen van de controle (bijv. geen echte PowerPoint of Word beschikbaar). Claim geen controles die niet zijn gedaan. Compact, in verhouding tot het document.

---

## 6. Open punten

- **PDF:** geen eigen gids. Openstaande keuze: PDF als export van Word-opmaak, als HTML-export, of een aparte drukopmaak.
- **Tagline in Word buiten de offerte:** geldt de offerte-uitzondering (herhalend mét tagline) ook voor brief, rapport en memo?
- **PowerPoint-sjabloonstructuur:** échte slidemaster/layouts met placeholders vs. huidige opzet (losse vormen per dia) — nog te beslissen.
- **Slidemaat:** `Powerpoint_sjabloon.potx` is custom 22 × 12,375 inch (16:9); de referentie-implementatie gebruikt standaard 13,333 × 7,5 inch. Behouden of standaardiseren?
- **Assetbibliotheek:** schone transparante witte logo's als SVG aanvragen bij de bron (de PNG's in Bijlage A volstaan intussen).
- **Openingsdia PowerPoint:** exacte breedte van het blauwe tekstvlak en de plek van een klantlogo (co-branding) vastleggen aan de hand van een goedgekeurd voorbeeld.
- **Zandvariant van het patroon:** twee voorstellen in proef (B.2). Visuele keuze nog te maken; daarna pas vastleggen.
- **C.22 (`005.jpg`):** staat nog niet op GitHub.
- **Ken je de foto?:** de pagina is vanuit de AI-omgeving niet te controleren (website blokkeert automatische toegang). Werking periodiek zelf nagaan.
- **Praktijktoets:** de gids toetsen met een HTML-lesbrief, een PowerPoint en een Word-offerte, elk met kwaliteitsrapportage. Terugkerende problemen leiden tot een aanpassing van de gids; incidentele niet.

---

## Bijlage A — Assets (via GitHub)

De logo's en beeldmerken staan als echte, transparante PNG's in de openbare GitHub-repository **dbfbeeldbank/dbf**, naast de beeldbank (Bijlage C). De witte versies zijn de gerepareerde varianten (§1.2), gecontroleerd op donkere en lichte achtergrond. Alle zes links getest en bereikbaar op 10 oktober 2026.

**Werkwijze.** Deze gids bevat geen ingebedde afbeeldingen meer, zodat hij licht blijft en voor iedereen te openen is. Bij het maken van een uiting haal je het logo op via de URL hieronder en sluit je het in:

- **HTML:** als base64 data-URI in de `<img>`-tag (§2.1, §2.8). Nooit `src` naar de GitHub-URL laten wijzen: een opgeleverd bestand moet zelfstandig werken.
- **Word en PowerPoint:** de PNG invoegen als ingesloten afbeelding, niet als koppeling.

| Bestand | Afmeting (px) | Gebruik |
|---|---|---|
| `DBF-logo-wit.png` | 1244 × 370 | Footer, documentkopje, navigatie: elke kleine of herhalende plaatsing op donkerblauw. |
| `DBF-logo-zwart.png` | 1244 × 370 | Documentkopje of footer op wit of papiertint. |
| `DBF-logo-wit-tagline.png` | 1244 × 370 | Titelblok (HTML), titel- en slotdia (PowerPoint). |
| `DBF-logo-zwart-tagline.png` | 1244 × 370 | Omslag en, als uitzondering, de koptekst van de Word-offerte (§1.2). |
| `DBF-beeldmerk-wit.png` | 944 × 1083 | Alleen los, nooit naast het logo (§1.2). Bijvoorbeeld klein rechtsonder op een donkere accentdia (§3.5). |
| `DBF-beeldmerk-zwart.png` | 944 × 1083 | Alleen los, nooit naast het logo (§1.2). |

**Overige assets.** Alles staat in de hoofdmap van de repository; URL = `https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/<bestandsnaam>`. De volledige lijst, met afmeting, sha256-controlegetal en status per bestand, staat in **`DBF_assets_manifest.csv`** (https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF_assets_manifest.csv).

| Bestand | Wat | Zie |
|---|---|---|
| `DBF_chevron.svg` + `DBF_chevron_*.png` (10×) | Chevron, vector en in elke paletkleur | §1.3, §3.7 |
| `DBF_patroon_*.svg` (6×), `DBF_patroon_slotdia_koningsblauw.png`, `patroon.py` | Decoratief patroon, dia-afbeelding en generator | Bijlage B |
| `DBF_fotostrook_zw.png`, `DBF_titelfoto_strand.jpg` | Sjabloonfoto's PowerPoint | §3.5 |
| `Powerpoint_sjabloon.potx` | PowerPoint-sjabloon. **Niet in de hoofdmap** (te groot, 28 MiB), maar als bijlage bij de GitHub-release: {R}Powerpoint_sjabloon.potx | §3, §6 |
| `DBF_offerte_sjabloon.dotx`, `dbf_offerte_sjabloon.pdf` | Offertesjabloon en voorbeeld | §4.1 |
| `DB_brief_sjabloon.pdf`, `DBF_rapport_sjabloon.pdf` | Voorbeelden brief en rapport | §1.3, §4.2 |
| `kleurenpalet.png` | Bron van het palet | §1.1 |
| `DBF_algemene_voorwaarden.md` | Algemene voorwaarden | §4.1 |
| `DBF_ontwikkellogboek.md` | Ontwikkelgeschiedenis | — |
| Beeldbank | Historische foto's, portretten, teambeelden | Bijlage C |

**Noodroute:** lukt downloaden niet, vraag dan om `DBF_huisstijl_assets.zip`. Die staat ook als bijlage bij de GitHub-release: {R}DBF_huisstijl_assets.zip


### Logo — wit, zonder tagline, voor donkerblauwe achtergrond (klein / herhalend)

Footer, documentkopje, navigatie: elke kleine of herhalende plaatsing op donkerblauw.

**URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-logo-wit.png

![Logo — wit, zonder tagline, voor donkerblauwe achtergrond (klein / herhalend)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-logo-wit.png)

HTML (na inbedden): `<img src="data:image/png;base64,…" alt="de Betekenisfabriek" width="134" height="40">`

### Logo — zwart, zonder tagline, voor lichte achtergrond (klein / herhalend)

Documentkopje of footer op wit of papiertint.

**URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-logo-zwart.png

![Logo — zwart, zonder tagline, voor lichte achtergrond (klein / herhalend)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-logo-zwart.png)

HTML (na inbedden): `<img src="data:image/png;base64,…" alt="de Betekenisfabriek" width="134" height="40">`

### Logo — wit, met tagline, voor donkerblauwe achtergrond (groot / eenmalig)

Titelblok (HTML), titel- en slotdia (PowerPoint).

**URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-logo-wit-tagline.png

![Logo — wit, met tagline, voor donkerblauwe achtergrond (groot / eenmalig)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-logo-wit-tagline.png)

HTML (na inbedden): `<img src="data:image/png;base64,…" alt="de Betekenisfabriek" width="134" height="40">`

### Logo — zwart, met tagline, voor lichte achtergrond (groot / eenmalig)

Omslag en, als uitzondering, de koptekst van de Word-offerte (§1.2).

**URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-logo-zwart-tagline.png

![Logo — zwart, met tagline, voor lichte achtergrond (groot / eenmalig)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-logo-zwart-tagline.png)

HTML (na inbedden): `<img src="data:image/png;base64,…" alt="de Betekenisfabriek" width="134" height="40">`

### Beeldmerk (los hexagon-icoon) — wit, voor donkerblauwe achtergrond

Alleen los, nooit naast het logo (§1.2). Bijvoorbeeld klein rechtsonder op een donkere accentdia (§3.5).

**URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-beeldmerk-wit.png

![Beeldmerk (los hexagon-icoon) — wit, voor donkerblauwe achtergrond](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-beeldmerk-wit.png)

HTML (na inbedden): `<img src="data:image/png;base64,…" alt="de Betekenisfabriek" width="28" height="32">`

### Beeldmerk (los hexagon-icoon) — zwart, voor lichte achtergrond

Alleen los, nooit naast het logo (§1.2).

**URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-beeldmerk-zwart.png

![Beeldmerk (los hexagon-icoon) — zwart, voor lichte achtergrond](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/DBF-beeldmerk-zwart.png)

HTML (na inbedden): `<img src="data:image/png;base64,…" alt="de Betekenisfabriek" width="28" height="32">`


---

## Bijlage B — Decoratief patroon

### B.1 Bestanden

| Bestand | Status | Gebruik |
|---|---|---|
| `DBF_patroon_koningsblauw.svg` | Vastgesteld | Standaard donkere variant: slotdia PowerPoint, achterkant rapport (Word/PDF) |
| `DBF_patroon_htmlnavy_strook.svg` | Vastgesteld | Strook boven de voet (HTML), op koningsblauw. De naam is historisch; de kleur is koningsblauw |
| `DBF_patroon_wit.svg` | Vastgesteld | Alleen bijzondere uitgaven, op wit |
| `DBF_patroon_navy.svg` | Uitzondering | Alleen als donker marine bewust gemotiveerd is |
| `DBF_patroon_zand_A_voorstel.svg` | Voorstel, in proef | Warme, rustige variant op zand |
| `DBF_patroon_zand_B_voorstel.svg` | Voorstel, in proef | Idem, zachter contrast |
| `DBF_patroon_slotdia_koningsblauw.png` | Vastgesteld | Koningsblauwe variant als volle dia (4000 × 2250 px, 300 dpi, rijafstand 0,43 inch). Voor de slotdia in PowerPoint |
| `patroon.py` | — | Generator van alle bovenstaande bestanden (B.5) |

De SVG-bestanden zijn vector, met dezelfde geometrie (B.5). Het zijn vaste vellen, geen tegels: naast elkaar leggen geeft een naad. Een ander formaat nodig? Genereer het met `patroon.py`. Alle bestanden staan op GitHub: `https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/<bestandsnaam>`. Niet per as schalen; bijsnijden in plaats van vervormen (§1.5). Op een dia plaats je het patroon als afbeelding van de volle dia (bij voorkeur PNG op 300 dpi, rijafstand ±0,43 inch).

### B.2 Kleur

| Variant | Achtergrond | Lijnen | Karakter | Status |
|---|---|---|---|---|
| Koningsblauw | `#27275B` | 10% wit | Krachtig, herkenbaar, uitgesproken | Vastgesteld (standaard) |
| Wit | `#FFFFFF` | 8–10% koningsblauw | Licht, voor bijzondere uitgaven | Vastgesteld |
| Donker marine | `#222831` | 10% wit | — | Alleen gemotiveerde uitzondering |
| Zand A | `#ECE4D7` | `#D9CEBB` | Warm, rustig, verfijnd | Voorstel |
| Zand B | `#ECE4D7` | `#E2D8C6` | Idem, zachter | Voorstel |

Geen goud in het patroon: geen gouden lijnen, geen metallic, verlopen of glans. Goud blijft voor de korte accentlijn en het logo op donker. De zandkleuren in de lijnen zijn proefwaarden, geen vastgestelde huisstijlkleuren.

### B.3 Toepassing per formaat

**Word en PDF (rapport)**
- Omslag: als er een passend beeld is (§1.7) een foto in het bovenste ±56%; anders typografisch. Gouden lijn, titel op wit, logo met tagline rechtsonder. Geen patroon.
- Binnenwerk en hoofdstukopeningen: geen patroon.
- Achterkant: patroon (koningsblauw) over de volle pagina, logo en website gecentreerd. Een achterkant zonder patroon is ook in huisstijl.
- PDF volgt de bronopmaak (§0). Het patroon blijft vector; fijnste lijn minimaal 0,25 pt.

**PowerPoint**
- Openingsdia: koningsblauw tekstvlak links, foto rechts; logo met tagline 0,5 inch hoog, linksonder.
- Scheidingsdia: effen koningsblauw, nummer in goud, titel wit; eventueel een foto. Geen patroon.
- Slotdia: patroon over de volle dia (`DBF_patroon_slotdia_koningsblauw.png`), logo met tagline gecentreerd (0,7 inch hoog). Geen tekst.
- Logomaten gelden voor de standaard dia van 13,333 × 7,5 inch.
- Het patroon verschijnt hooguit één keer per presentatie. Plaatsen als afbeelding, niet als getegelde vulling.

**HTML**
- Het titelblok blijft zoals in §2.4: donkerblauw, **met logo** (wit, uit Bijlage A), eyebrow, titel, subtitel en goudlijn. Deze aanvulling verandert daar niets aan.
- Geen foto boven het titelblok. Een foto is optioneel en staat in de inhoud (als figuur met bijschrift), alleen als die bij het onderwerp van dít document hoort.
- Beeld uit de PowerPoint-bibliotheek (o.a. de strandsilhouetten van de titeldia, §3) wordt niet in HTML gebruikt.
- Geen patroon in het titelblok. Eventueel één smalle patroonstrook (circa 90 px) direct boven de footer, toon op toon. Inline SVG, ingebed. Niet verplicht.

### B.4 Niet doen

- Het patroon als standaardachtergrond of op elke pagina.
- Het patroon combineren met een foto in hetzelfde vlak.
- Het logo in een uitsparing van het patroon plaatsen.
- Eigen kleuren, eigen schaal per as, of het patroon hertekenen.
- Losse chevrons uit het patroon als lijnaccent (§1.3).
- Het patroon als tweede logo: zo groot of zo vaak dat het meer aandacht trekt dan inhoud, logo of typografie.
- Een foto boven of in plaats van het titelblok met logo (HTML).

### B.5 Opbouw (ter verantwoording; gebruik de bestanden uit B.1)

Vastgesteld 10 oktober 2026 (besluit Paul). Generator: `patroon.py`.

- Eén vorm: de chevron uit §1.3, liggend (punt omhoog), als omlijning met één binnenlijn langs het midden.
- Liggend halfsteensverband: rijafstand 86, vormlengte 201,5, tussenruimte 44 (eenheden); hoogte × 0,8.
- Alleen de vormen, **geen diagonale of horizontale verbindingslijnen.**
- Lijnen 10% wit op donker (8–10% koningsblauw op wit).
- Op een dia van 13,333 inch: rijafstand ±0,43 inch.

---

## Bijlage C — Beeldbank (historische foto's, portretten, teambeelden)

> Deze beeldbank bevat 18 historische foto's (C.01–C.17 en C.46), elf eigen beelden met toelichting (C.18–C.28) en 17 aanvullende eigen bestanden (C.29–C.45).
>
> **Ophalen:** altijd via de GitHub-URL (`https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/…`). Stand 10 oktober 2026: alle URL's staan in `DBF_assets_manifest.csv`. Uitzondering: C.22 (`005.jpg`) staat alleen op de website.
>
> **Vindplaats ≠ opslag.** De eigen website en GitHub zijn publicatie- of opslaglocaties, niet de oorspronkelijke archiefvindplaats. Per historische foto staat de oorspronkelijke vindplaats apart vermeld. Een zoekingang (bijv. de fotocollectie van het Nationaal Archief) is géén gecontroleerde, permanente fotoregistratie.
>
> De foto-omschrijvingen bij de Spaarnestad Onderwerpen-beelden zijn grotendeels werkbeschrijvingen op basis van het beeld, geen geverifieerde archiefbijschriften. Datering en rechtenstatus zijn daar nog niet vastgesteld.

### Gebruik door AI en vormgevers

Keuzeregels en bijschriftvorm: zie §1.7. Hieronder de aanvullende regels uit de beeldbank.

- Kies beelden op basis van de betekenis van de tekst, niet alleen op basis van het letterlijk afgebeelde onderwerp.
- Haal een beeld altijd op via de GitHub-afbeeldings-URL en sluit het in het document in (§1.7). Is de URL niet bereikbaar, dan geen beeld.
- Vermeld de identiteitsvraag alleen wanneer die inhoudelijk past; niet automatisch als bijschrift.
- Neem historische details niet als bewezen aan als ze alleen in een werkbeschrijving staan.
- Controleer gebruiksrechten per beeld bij de oorspronkelijke bron.
- Maak elke historische foto klikbaar naar *Ken je de foto?* (https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html), zie §1.7.

### C.01 Heitje voor een karweitje (1952)

**Onderwerp:** Jongeren nemen deel aan Heitje voor een karweitje in Amsterdam (1952).

**Beschrijving:** Jongeren steken de handen uit de mouwen tijdens de maatschappelijke actie Heitje voor een karweitje.

**Identiteitsvraag:** Wat willen jullie in beweging brengen dat zonder jullie niet gebeurt?

**Herkomst:** Nationaal Archief / Wikimedia Commons
**Oorspronkelijke bestandsnaam:** `04-11-1952_10460_Arnold_d%27Ailly,_Damrak,_Heitje_voor_een_Karweitje_(4072259938).jpg`
**Oorspronkelijke vindplaats (Wikimedia Commons):** https://commons.wikimedia.org/wiki/File:04-11-1952_10460_Arnold_d%27Ailly,_Damrak,_Heitje_voor_een_Karweitje_(4072259938).jpg
*Let op:* Commons is de ontsluitingspagina; zie de bestandsbeschrijving voor de archiefinstelling en originele catalogusgegevens.
**Bestand (GitHub):** `04-11-1952_10460_Arnold_dAilly_Damrak_Heitje_voor_een_Karweitje_4072259938.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/04-11-1952_10460_Arnold_dAilly_Damrak_Heitje_voor_een_Karweitje_4072259938.jpg

[![Heitje voor een karweitje (1952)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/04-11-1952_10460_Arnold_dAilly_Damrak_Heitje_voor_een_Karweitje_4072259938.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.02 Bouwvakkers van de Sint-Jan (1925)

**Onderwerp:** Bouwvakkers aan de Sint-Jan in ’s-Hertogenbosch (1925).

**Beschrijving:** Vakmensen werken samen aan een bouwwerk dat hun eigen levens zal overstijgen.

**Identiteitsvraag:** Waaraan bouwen jullie dat groter is dan jullie organisatie?

**Herkomst:** Streekarchief Langstraat Heusden Altena / Wikimedia Commons
**Oorspronkelijke bestandsnaam:** `Bouwvakkers_die_aan_de_St._Jan_werkten._De_man_rechts_met_hoed_is_uitvoerder_G.H._Huiskes,_1925._Archief_SALHA_foto_nr._80272.jpg`
**Oorspronkelijke vindplaats (Wikimedia Commons):** https://commons.wikimedia.org/wiki/File:Bouwvakkers_die_aan_de_St._Jan_werkten._De_man_rechts_met_hoed_is_uitvoerder_G.H._Huiskes,_1925._Archief_SALHA_foto_nr._80272.jpg
*Let op:* Commons is de ontsluitingspagina; zie de bestandsbeschrijving voor de archiefinstelling en originele catalogusgegevens.
**Bestand (GitHub):** `Bouwvakkers_die_aan_de_St._Jan_werkten._De_man_rechts_met_hoed_is_uitvoerder_G.H._Huiskes_1925._Archief_SALHA_foto_nr._80272.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Bouwvakkers_die_aan_de_St._Jan_werkten._De_man_rechts_met_hoed_is_uitvoerder_G.H._Huiskes_1925._Archief_SALHA_foto_nr._80272.jpg

[![Bouwvakkers van de Sint-Jan (1925)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Bouwvakkers_die_aan_de_St._Jan_werkten._De_man_rechts_met_hoed_is_uitvoerder_G.H._Huiskes_1925._Archief_SALHA_foto_nr._80272.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.03 Amsterdamse straatmakers (1953)

**Onderwerp:** Amsterdamse straatmakers helpen bij de wederopbouw in Zeeland (1953).

**Beschrijving:** Amsterdamse straatmakers helpen bij de wederopbouw na de Watersnoodramp.

**Identiteitsvraag:** Waar verbinden jullie je aan, ook als het iets kost?

**Herkomst:** Nationaal Archief / Wikimedia Commons
**Oorspronkelijke bestandsnaam:** `Amsterdamse_straatmakers_helpen_bij_het_herstellen_van_de_schade_van_de_watersno,_Bestanddeelnr_905-6114.jpg`
**Oorspronkelijke vindplaats (Wikimedia Commons):** https://commons.wikimedia.org/wiki/File:Amsterdamse_straatmakers_helpen_bij_het_herstellen_van_de_schade_van_de_watersno,_Bestanddeelnr_905-6114.jpg
*Let op:* Commons is de ontsluitingspagina; zie de bestandsbeschrijving voor de archiefinstelling en originele catalogusgegevens.
**Bestand (GitHub):** `Amsterdamse_straatmakers_helpen_bij_het_herstellen_van_de_schade_van_de_watersno_Bestanddeelnr_905-6114.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Amsterdamse_straatmakers_helpen_bij_het_herstellen_van_de_schade_van_de_watersno_Bestanddeelnr_905-6114.jpg

[![Amsterdamse straatmakers (1953)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Amsterdamse_straatmakers_helpen_bij_het_herstellen_van_de_schade_van_de_watersno_Bestanddeelnr_905-6114.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.04 Oostenrijkse Rode Kruis-ambulance (1953)

**Onderwerp:** Oostenrijkse Rode Kruis-ambulance in Dordrecht (1953).

**Beschrijving:** Een Oostenrijkse ambulance staat klaar om mensen uit het rampgebied te evacueren.

**Identiteitsvraag:** Voor wie zijn jullie er, juist wanneer het moeilijk wordt?

**Herkomst:** Nationaal Archief / Wikimedia Commons
**Oorspronkelijke bestandsnaam:** `Oostenrijkse_Rode_Kruis_Kalonex,_hier_te_Dordrecht_,_zal_worden_ingezet_bij_de_%E2%80%A6,_Bestanddeelnr_905-5501.jpg`
**Oorspronkelijke vindplaats (Wikimedia Commons):** https://commons.wikimedia.org/wiki/File:Oostenrijkse_Rode_Kruis_Kalonex,_hier_te_Dordrecht_,_zal_worden_ingezet_bij_de_%E2%80%A6,_Bestanddeelnr_905-5501.jpg
*Let op:* Commons is de ontsluitingspagina; zie de bestandsbeschrijving voor de archiefinstelling en originele catalogusgegevens.
**Bestand (GitHub):** `Oostenrijkse_Rode_Kruis_Kalonex_Dordrecht_Bestanddeelnr_905-5501.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Oostenrijkse_Rode_Kruis_Kalonex_Dordrecht_Bestanddeelnr_905-5501.jpg

[![Oostenrijkse Rode Kruis-ambulance (1953)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Oostenrijkse_Rode_Kruis_Kalonex_Dordrecht_Bestanddeelnr_905-5501.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.05 Vrijwilligers in Nieuwerkerk (1955)

**Onderwerp:** Vrijwilligers helpen bij de wederopbouw van Nieuwerkerk (1955).

**Beschrijving:** Nederlandse en buitenlandse jongeren werken samen aan de wederopbouw.

**Identiteitsvraag:** Welke overtuiging brengt bij jullie mensen in beweging?

**Herkomst:** Nationaal Archief / Wikimedia Commons
**Oorspronkelijke bestandsnaam:** `Vrijwilligers_waaronder_buitenlandse_jongelui_helpen_bouw_in_Zeeland,_op_Nieuwer,_Bestanddeelnr_907-3011.jpg`
**Oorspronkelijke vindplaats (Wikimedia Commons):** https://commons.wikimedia.org/wiki/File:Vrijwilligers_waaronder_buitenlandse_jongelui_helpen_bouw_in_Zeeland,_op_Nieuwer,_Bestanddeelnr_907-3011.jpg
*Let op:* Commons is de ontsluitingspagina; zie de bestandsbeschrijving voor de archiefinstelling en originele catalogusgegevens.
**Bestand (GitHub):** `Vrijwilligers_waaronder_buitenlandse_jongelui_helpen_bouw_in_Zeeland_op_Nieuwer_Bestanddeelnr_907-3011.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Vrijwilligers_waaronder_buitenlandse_jongelui_helpen_bouw_in_Zeeland_op_Nieuwer_Bestanddeelnr_907-3011.jpg

[![Vrijwilligers in Nieuwerkerk (1955)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Vrijwilligers_waaronder_buitenlandse_jongelui_helpen_bouw_in_Zeeland_op_Nieuwer_Bestanddeelnr_907-3011.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.06 Het dorpsplein

**Beschrijving:** Op een dorpsplein kruisen de levens van kinderen, boeren en andere inwoners elkaar.

**Identiteitsvraag:** Wat maakt dat mensen zich bij jullie ergens onderdeel van voelen?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 482027 / 004 (`482027_004`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_482027_004-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_482027_004-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 482027 / 004)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![Het dorpsplein](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_482027_004-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.07 Samen muziek maken

**Beschrijving:** Jonge vrouwen maken samen muziek in een gemeenschappelijke ruimte.

**Identiteitsvraag:** Wat verbindt jullie mensen, voorbij hun functie of rol?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 2007 / 004 (`2007_004`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_2007_004-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_2007_004-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 2007 / 004)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![Samen muziek maken](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_2007_004-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.08 De eerste vrouwelijke inwoners van Lelystad

**Beschrijving:** De eerste vrouwelijke inwoners van Lelystad staan samen aan de rand van het nieuwe land.

**Identiteitsvraag:** Welke gemeenschap willen jullie helpen ontstaan?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 481200 / 040 (`481200_040`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_481200_040-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_481200_040-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 481200 / 040)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![De eerste vrouwelijke inwoners van Lelystad](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_481200_040-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.09 Kinderen krijgen drinken

**Beschrijving:** Een groep kinderen verzamelt zich rond een vrouw die drinken uitdeelt.

**Identiteitsvraag:** Waaraan merken mensen dat ze bij jullie welkom zijn?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 132169 / 019 (`132169_019`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_132169_019-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_132169_019-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 132169 / 019)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![Kinderen krijgen drinken](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_132169_019-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.10 Voorlezen aan kinderen

**Beschrijving:** Kinderen verzamelen zich rond een vrouw die een verhaal voorleest.

**Identiteitsvraag:** Welk verhaal houdt jullie organisatie bij elkaar?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 363001 / 066 (`363001_066`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_363001_066-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_363001_066-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 363001 / 066)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![Voorlezen aan kinderen](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_363001_066-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.11 Spelen in het park

**Beschrijving:** Kinderen trekken samen met een bolderwagen door een park.

**Identiteitsvraag:** Hoeveel ruimte krijgen mensen bij jullie om zelf iets te ontdekken?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 482067 / 007 (`482067_007`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_482067_007-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_482067_007-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 482067 / 007)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![Spelen in het park](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_482067_007-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.12 De dorpspomp

**Beschrijving:** Kinderen ontmoeten elkaar bij een dorpspomp.

**Identiteitsvraag:** Waar ontstaat bij jullie de ontmoeting die er werkelijk toe doet?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 478052 / 002 (`478052_002`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_478052_002-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_478052_002-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 478052 / 002)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![De dorpspomp](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_478052_002-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.13 De muziekvereniging

**Beschrijving:** Een plaatselijke muziekvereniging speelt voor dorpsbewoners.

**Identiteitsvraag:** Wat kunnen jullie samen wat niemand afzonderlijk kan?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 482084 / 033 (`482084_033`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_482084_033-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_482084_033-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 482084 / 033)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![De muziekvereniging](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_482084_033-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.14 De biljartvereniging

**Beschrijving:** Een groep mannen verzamelt zich rond een biljarttafel.

**Identiteitsvraag:** Wat maakt jullie tot een gemeenschap en niet alleen tot een verzameling mensen?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 481200 / 035 (`481200_035`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_481200_035-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_481200_035-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 481200 / 035)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![De biljartvereniging](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_481200_035-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.15 Het hooien

**Beschrijving:** Boeren zijn aan het werk terwijl het dorp om hen heen zijn dagelijkse gang gaat.

**Identiteitsvraag:** Wat vinden jullie zo belangrijk dat het elke dag opnieuw inzet verdient?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 482038 / 008 (`482038_008`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_482038_008-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_482038_008-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 482038 / 008)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![Het hooien](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_482038_008-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.16 Muziekkorps op het station

> **Niet gebruiken tot de herkomst is vastgesteld.** Op de foto lijkt een militair muziekkorps in Duits uniform te spelen, vermoedelijk tijdens de bezetting. De werkbeschrijving hieronder vermeldt dat niet. Eerst het originele archiefbijschrift controleren.

**Beschrijving:** Een muziekkorps speelt op een druk station, tussen reizigers en omstanders.

**Identiteitsvraag:** Welke momenten verdienen het om als organisatie samen bij stil te staan?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 30073 / 014 (`30073_014`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_30073_014-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_30073_014-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 30073 / 014)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![Muziekkorps op het station](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_30073_014-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### C.17 Mannen aan boord

**Beschrijving:** Vier mannen zwaaien enthousiast met hun petten vanaf een schip.

**Identiteitsvraag:** Welke toekomst maakt dat jullie samen op weg gaan?

**Herkomst:** Nationaal Archief, fotocollectie Spaarnestad Onderwerpen (7.000SPAond)
**Archiefbestandsaanduiding:** 481200 / 012 (`481200_012`)
**Bestand (GitHub):** `NL-HaNA_7.000SPAond_481200_012-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_481200_012-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Onderwerpen, toegang 7.000SPAond.
**Zoekingang:** https://www.nationaalarchief.nl/onderzoeken/fotocollectie (zoek op bestandsaanduiding 481200 / 012)
**Permanente registratie-URL en oorspronkelijke datering:** nog niet vastgesteld.

[![Mannen aan boord](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/NL-HaNA_7.000SPAond_481200_012-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")


### C.46 Samen sjoelen in het buurthuis (1953)

**Onderwerp:** Samen sjoelen in het buurthuis (1953).

**Beschrijving:** Op 12 mei 1953 spelen ouderen ter ontspanning een sjoelspel in een buurthuis of opvang voor ouderen in Amsterdam.

**Identiteitsvraag:** Waar maken jullie ruimte voor ontmoeting die anders niet vanzelf ontstaat?

**Herkomst:** Nationaal Archief / Spaarnestad Photo, toegang 7.000SPABB, bestanddeel 50572. Fotograaf: J.J.M. (Jan) de Jong. Rechtenstatus volgens archief: rechtenvrij.
**Bestand (GitHub):** `50572-groot.jpg`
**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/50572-groot.jpg
**Oorspronkelijke vindplaats:** Nationaal Archief, Spaarnestad Photo, toegang 7.000SPABB, bestanddeel 50572.
**Permanente registratie:** http://hdl.handle.net/10648/35429da6-58d1-a382-e063-6df0900a6686
**Datering:** 12 mei 1953, Amsterdam.

*Nummering:* C.46 in plaats van 18, omdat C.18–C.28 al de eigen beelden zijn. Hoort inhoudelijk bij de historische foto's.

[![Samen sjoelen in het buurthuis (1953)](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/50572-groot.jpg)](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html "Over deze foto")

### Aanvullende beeldbank — medewerkers, team en gebouw

**Herkomst.** De elf beelden C.18–C.28 komen uit de eigen WordPress-mediabibliotheek van De Betekenisfabriek. Fotograaf, opnamedatum en eerste publicatieplaats zijn niet vastgelegd in de aangeleverde gegevens. De websitelinks hieronder zijn daarom opslaglocaties, geen onafhankelijke bronvermeldingen. Ophalen gaat via GitHub.

Eigen beelden voor portretten, teamintroducties en beeldmateriaal over De Betekenisfabriek. De namen bij individuele portretten komen uit de aangeleverde schermafbeeldingen. Bij groepsbeelden zijn individuele personen niet met zekerheid te benoemen: laat een opmaker geen namen raden.

**Opmaakregel:** Bij individuele portretten mag de genoemde persoonsnaam als bijschrift of naamlabel worden gebruikt. Bij groepsfoto's uitsluitend namen tonen nadat de afgebeelde personen zijn bevestigd. Historische identiteitsvragen horen niet automatisch bij deze portretten.

### C.18 Wouter — portret

**Beschrijving:** Portret van Wouter.

**Naam voor opmaak:** Wouter

**Bestandsnaam:** `wouter-De-Betekenisfabriek-5462.jpg`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/wouter-De-Betekenisfabriek-5462.jpg

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/wouter-De-Betekenisfabriek-5462.jpg

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Wouter — portret](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/wouter-De-Betekenisfabriek-5462.jpg)

### C.19 Gert — portret

**Beschrijving:** Portret van Gert.

**Naam voor opmaak:** Gert

**Bestandsnaam:** `gert-De-Betekenisfabriek-5445.jpg`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/gert-De-Betekenisfabriek-5445.jpg

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/gert-De-Betekenisfabriek-5445.jpg

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Gert — portret](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/gert-De-Betekenisfabriek-5445.jpg)

### C.20 Karin — portret

**Beschrijving:** Portret van Karin.

**Naam voor opmaak:** Karin

**Bestandsnaam:** `Karinn_MG_5397.jpg`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Karinn_MG_5397.jpg

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Karinn_MG_5397.jpg

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Karin — portret](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Karinn_MG_5397.jpg)

### C.21 Paul — portret

**Beschrijving:** Portret van Paul.

**Naam voor opmaak:** Paul

**Bestandsnaam:** `paul-De-Betekenisfabriek-5409.jpg`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/paul-De-Betekenisfabriek-5409.jpg

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/paul-De-Betekenisfabriek-5409.jpg

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Paul — portret](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/paul-De-Betekenisfabriek-5409.jpg)

### C.22 Het gebouw — 005

**Beschrijving:** Historische zwart-witfoto van een gebouw. De precieze locatie en herkomst zijn niet bevestigd.

**Naam voor opmaak:** Niet van toepassing

**Bestandsnaam:** `005.jpg`

**Herkomst:** Bestaande mediabibliotheek De Betekenisfabriek (door gebruiker aangeleverd)

**Websitelocatie (opslag, enige locatie):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/005.jpg

**URL-status:** Staat nog niet op GitHub. De websitelink is niet geverifieerd; niet gebruiken tot het bestand op GitHub staat.

![Het gebouw — 005](https://debetekenisfabriek.nl/wp-content/uploads/2026/10/005.jpg)

### C.23 Teamfoto — 5549

**Beschrijving:** Mensen van De Betekenisfabriek in gesprek rond een tafel.

**Naam voor opmaak:** Nog vast te stellen

**Bestandsnaam:** `De-Betekenisfabriek-web-5549.jpg`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5549.jpg

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/De-Betekenisfabriek-web-5549.jpg

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Teamfoto — 5549](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5549.jpg)

### C.24 Teamfoto — 5500

**Beschrijving:** Werkmoment met twee personen, van wie één op de voorgrond.

**Naam voor opmaak:** Nog vast te stellen

**Bestandsnaam:** `De-Betekenisfabriek-web-5500.jpg`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5500.jpg

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/De-Betekenisfabriek-web-5500.jpg

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Teamfoto — 5500](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5500.jpg)

### C.25 Teamfoto — 5504

**Beschrijving:** Informeel werkmoment met een zittende persoon en een gedeeltelijk zichtbare ander.

**Naam voor opmaak:** Nog vast te stellen

**Bestandsnaam:** `De-Betekenisfabriek-web-5504.jpg`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5504.jpg

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/De-Betekenisfabriek-web-5504.jpg

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Teamfoto — 5504](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5504.jpg)

### C.26 Teamfoto — 5508

**Beschrijving:** Twee personen in gesprek of tijdens een werkmoment.

**Naam voor opmaak:** Nog vast te stellen

**Bestandsnaam:** `De-Betekenisfabriek-web-5508.jpg`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5508.jpg

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/De-Betekenisfabriek-web-5508.jpg

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Teamfoto — 5508](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5508.jpg)

### C.27 Teamfoto — 5528

**Beschrijving:** Informeel portret met een lachende persoon en een tweede persoon op de voorgrond.

**Naam voor opmaak:** Nog vast te stellen

**Bestandsnaam:** `De-Betekenisfabriek-web-5528.jpg`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5528.jpg

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/De-Betekenisfabriek-web-5528.jpg

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Teamfoto — 5528](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5528.jpg)

### C.28 Paul — bestaand PNG-portret

**Beschrijving:** Bestaand portretbestand van Paul.

**Naam voor opmaak:** Paul

**Bestandsnaam:** `Paul.png`

**Herkomst:** Eigen beeld De Betekenisfabriek (door gebruiker aangeleverd)

**Afbeeldings-URL:** https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Paul.png

**Websitelocatie (opslag):** https://debetekenisfabriek.nl/wp-content/uploads/2022/03/Paul.png

**URL-status:** Op GitHub geplaatst en bereikbaarheid getest (10 oktober 2026).

![Paul — bestaand PNG-portret](https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Paul.png)

### C.29–C.45 Aanvullende bestanden (zonder toelichting)

Extra eigen beelden en varianten, zonder beschrijving of identiteitsvraag. Kies ze alleen volgens §1.7: portret alleen bij de auteur, werkmoment alleen als de tekst over een sessie of samenwerking gaat. Geen namen bij groepsfoto's.

| Nr. | Bestand | Soort | Afbeeldings-URL |
|---|---|---|---|
| C.29 | `004-scaled.jpg` | gebouw, exterieur | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/004-scaled.jpg |
| C.30 | `De-Betekenisfabriek-5409.jpg` | portret | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-5409.jpg |
| C.31 | `De-Betekenisfabriek-5445.jpg` | portret | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-5445.jpg |
| C.32 | `De-Betekenisfabriek-5462.jpg` | portret | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-5462.jpg |
| C.33 | `De-Betekenisfabriek-web-5390.jpg` | portret | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5390.jpg |
| C.34 | `De-Betekenisfabriek-web-5409.jpg` | portret | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5409.jpg |
| C.35 | `De-Betekenisfabriek-web-5442.jpg` | portret | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5442.jpg |
| C.36 | `De-Betekenisfabriek-web-5462.jpg` | portret | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5462.jpg |
| C.37 | `De-Betekenisfabriek-web-5500-2.jpg` | zwart-witversie van `De-Betekenisfabriek-web-5500.jpg` | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5500-2.jpg |
| C.38 | `De-Betekenisfabriek-web-5504-2.jpg` | zwart-witversie van `De-Betekenisfabriek-web-5504.jpg` | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5504-2.jpg |
| C.39 | `De-Betekenisfabriek-web-5508-2.jpg` | zwart-witversie van `De-Betekenisfabriek-web-5508.jpg` | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5508-2.jpg |
| C.40 | `De-Betekenisfabriek-web-5528-2.jpg` | zwart-witversie van `De-Betekenisfabriek-web-5528.jpg` | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5528-2.jpg |
| C.41 | `De-Betekenisfabriek-web-5531.jpg` | werkmoment / sfeerbeeld | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5531.jpg |
| C.42 | `De-Betekenisfabriek-web-5549-2.jpg` | zwart-witversie van `De-Betekenisfabriek-web-5549.jpg` | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5549-2.jpg |
| C.43 | `De-Betekenisfabriek-web-5555.jpg` | werkmoment / sfeerbeeld | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/De-Betekenisfabriek-web-5555.jpg |
| C.44 | `Karinn_MG_5397-2.jpg` | zwart-witversie van `Karinn_MG_5397.jpg` | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Karinn_MG_5397-2.jpg |
| C.45 | `Unknown.jpeg` | gebouw, exterieur — klein bestand (331 × 152 px), alleen als miniatuur bruikbaar | https://raw.githubusercontent.com/dbfbeeldbank/dbf/main/Unknown.jpeg |

### Overzicht oorspronkelijke vindplaatsen (historische foto's)

De links verwijzen naar de oorspronkelijke bronpagina of naar een archiefzoekingang. Een zoekingang is géén gecontroleerde, permanente fotoregistratie. Alleen C.46 heeft al een permanente registratie (handle).

| Nr. | Foto | Oorspronkelijke vindplaats | Link |
|---|---|---|---|
| C.01 | Heitje voor een karweitje (1952) | Wikimedia Commons (ontsluitingspagina) | https://commons.wikimedia.org/wiki/File:04-11-1952_10460_Arnold_d%27Ailly,_Damrak,_Heitje_voor_een_Karweitje_(4072259938).jpg |
| C.02 | Bouwvakkers van de Sint-Jan (1925) | Wikimedia Commons (ontsluitingspagina) | https://commons.wikimedia.org/wiki/File:Bouwvakkers_die_aan_de_St._Jan_werkten._De_man_rechts_met_hoed_is_uitvoerder_G.H._Huiskes,_1925._Archief_SALHA_foto_nr._80272.jpg |
| C.03 | Amsterdamse straatmakers (1953) | Wikimedia Commons (ontsluitingspagina) | https://commons.wikimedia.org/wiki/File:Amsterdamse_straatmakers_helpen_bij_het_herstellen_van_de_schade_van_de_watersno,_Bestanddeelnr_905-6114.jpg |
| C.04 | Oostenrijkse Rode Kruis-ambulance (1953) | Wikimedia Commons (ontsluitingspagina) | https://commons.wikimedia.org/wiki/File:Oostenrijkse_Rode_Kruis_Kalonex,_hier_te_Dordrecht_,_zal_worden_ingezet_bij_de_%E2%80%A6,_Bestanddeelnr_905-5501.jpg |
| C.05 | Vrijwilligers in Nieuwerkerk (1955) | Wikimedia Commons (ontsluitingspagina) | https://commons.wikimedia.org/wiki/File:Vrijwilligers_waaronder_buitenlandse_jongelui_helpen_bouw_in_Zeeland,_op_Nieuwer,_Bestanddeelnr_907-3011.jpg |
| C.06 | Het dorpsplein | NA, Spaarnestad Onderwerpen (7.000SPAond), 482027 / 004 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.07 | Samen muziek maken | NA, Spaarnestad Onderwerpen (7.000SPAond), 2007 / 004 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.08 | De eerste vrouwelijke inwoners van Lelystad | NA, Spaarnestad Onderwerpen (7.000SPAond), 481200 / 040 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.09 | Kinderen krijgen drinken | NA, Spaarnestad Onderwerpen (7.000SPAond), 132169 / 019 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.10 | Voorlezen aan kinderen | NA, Spaarnestad Onderwerpen (7.000SPAond), 363001 / 066 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.11 | Spelen in het park | NA, Spaarnestad Onderwerpen (7.000SPAond), 482067 / 007 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.12 | De dorpspomp | NA, Spaarnestad Onderwerpen (7.000SPAond), 478052 / 002 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.13 | De muziekvereniging | NA, Spaarnestad Onderwerpen (7.000SPAond), 482084 / 033 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.14 | De biljartvereniging | NA, Spaarnestad Onderwerpen (7.000SPAond), 481200 / 035 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.15 | Het hooien | NA, Spaarnestad Onderwerpen (7.000SPAond), 482038 / 008 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.16 | Muziekkorps op het station | NA, Spaarnestad Onderwerpen (7.000SPAond), 30073 / 014 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.17 | Mannen aan boord | NA, Spaarnestad Onderwerpen (7.000SPAond), 481200 / 012 | zoekingang: https://www.nationaalarchief.nl/onderzoeken/fotocollectie |
| C.46 | Samen sjoelen in het buurthuis (1953) | NA, Spaarnestad Photo (7.000SPABB), 50572 | http://hdl.handle.net/10648/35429da6-58d1-a382-e063-6df0900a6686 |

**Toelichting bij historische fotografie:** https://debetekenisfabriek.nl/wp-content/uploads/2026/10/Ken_je_de_foto.html — hier linken alle historische foto's naar (§1.7).

---

### Ken je de foto? — herkomst en beeldrechten (tekst voor colofon of website)

De foto's in deze beeldbank komen uit een andere tijd. We vonden ze onder meer in de collecties van het Nationaal Archief. Ze laten zien hoe mensen samen iets tot stand brengen. Hoe ze zich verbinden aan een gedeeld doel, een overtuiging of een ideaal. En hoe daaruit iets ontstaat dat groter is dan henzelf.

Dat is precies wat ons bij De Betekenisfabriek bezighoudt. Want ook vandaag geloven we dat organisaties betekenis krijgen waar mensen zich verbinden aan iets wat ze werkelijk belangrijk vinden.

We hebben ons best gedaan om zorgvuldig na te gaan of we deze foto's mogen gebruiken. Daarbij baseren we ons op de beschikbare informatie over herkomst en gebruiksrechten bij de oorspronkelijke bronnen.

**Herken je jezelf of iemand anders op een foto?** Of heb je vragen over de herkomst of het gebruik ervan? Laat het ons weten. En wil je dat we een foto verwijderen, dan doen we dat. Zonder gedoe.
