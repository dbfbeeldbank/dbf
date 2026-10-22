# DBF Ontwikkellogboek — waarom de huisstijlgids is zoals hij is

> Achtergrond bij `DBF_huisstijlgids.md`. Hier staat wat er tijdens het opbouwen van de huisstijl misging, wat er is besloten en waarom. **Voor het maken van een uiting is dit logboek niet nodig**; de gids bevat alleen de geldende regels.
>
> Werkafspraak: wordt een fout gevonden en hersteld, dan komt de regel in de gids en het verhaal erachter hier.

---

## Herkomst van de gids

- De gids is op 10 oktober 2026 samengevoegd uit drie losse gidsen: de HTML-briefing (v4, gebaseerd op de herstyling van "Module 3 — Framing en adoptie"), de PowerPoint-gids (12 september 2026) en de Office-gids (10 september 2026).
- Dezelfde dag aangevuld met §1.6 (beeld en patroon), §1.7 (beeldkeuze), Bijlage B (patroon) en Bijlage C (beeldbank).
- Daarna opgeschoond: logo's en beelden via GitHub (`dbfbeeldbank/dbf`) in plaats van ingebed of via de website; ontwikkelgeschiedenis naar dit logboek.

## Kleur

- **Twee donkerblauwen.** HTML en Word gebruikten `#15284B` (genoemd als Pantone 2767C), PowerPoint koninklijk blauw `#27275B` (Pantone 2758 C). `#15284B` staat niet in `kleurenpalet.png`, het officiële palet. In de PowerPoint-gids bleek een eerdere navy-waarde een pipetteerfout. In `Powerpoint_sjabloon.potx` is koninklijk blauw gemeten als `#22255A`, binnen de meetmarge.
- **Besluit 10 oktober 2026 (Paul):** één primaire donkere kleur, koninklijk blauw `#27275B`, in alle formaten. HTML-tinten daarop herberekend (`--inkt-mid #4E4E79`, `--inkt-zacht #66668A`, `--wit-zacht #BEBECE`), met gecontroleerd contrast.
- **Nog te doen:** het Word-offertesjabloon heeft in de footer nog `#15284B`.

## Logo's

- De witte logo- en beeldmerkbestanden in de oude assetbibliotheek bleken platgeslagen JPEG's zonder transparantie: wit op wit, onzichtbaar op donker. Ook het sluitdia-logo in `Powerpoint_sjabloon.potx` (`image7.png`) was een leeg wit vlak. Daarom zijn witte versies programmatisch afgeleid uit het zwarte bronlogo.
- De logo's stonden eerst als base64 in de gids zelf. Dat maakte het bestand ruim 600 KB en lastig te openen voor collega's. Nu staan ze op GitHub (Bijlage A).
- **Tagline.** Op kleine hoogte werd de tagline onleesbaar. De reflex om dan het hele logo groter te maken maakte het documentkopje te dominant. Daarom de regel: klein of herhalend = zonder tagline. De Word-offerte is een bewuste uitzondering, omdat het bronbestand het zo doet.

## Hexagon en chevron

- Eerst werd het hexagon uit het beeldmerk gebruikt als hoofdstukmarkering en lijnaccent. Genummerde hexagon-iconen oogden "knullig" en zijn vervangen door de chevron.
- Een "subtiel chevron-lijnaccent" (een rij chevrons als breker) is in meerdere documenten afgewezen en daarna verboden.
- Hoofdstuknummers stonden eerst in goud en een ander lettertype dan de titel. Ze hoorden visueel niet bij elkaar; nu zelfde kleur en font.
- De chevron-PNG's zijn gegenereerd uit de vectorpunten (polygon op een leeg RGBA-canvas, 4× supersampled en verkleind), niet door een bestaande afbeelding op kleur te maskeren. Dat gaf rafelranden.

## HTML

- **Los logobestand.** Een opgeleverd document verwees naar `betekenisfabriek-logo.png`, dat niet werd meegeleverd: kapot logo bij de klant. Sindsdien altijd inbedden.
- **Google Fonts via `<link>`.** Werkte bij het maken, maar zonder (goede) internetverbinding viel de browser terug op een systeemfont, vooral merkbaar op mobiel. Sindsdien fonts altijd inbedden.
- **Meerdere `:root`-blokken.** Tijdens het itereren werden kleurenblokken achter elkaar gezet. Het werkte toevallig, maar was fragiel en onleesbaar. Nu: één blok.
- **Navigatieknop onder de overlay.** De vaste knop had een lagere z-index dan de overlay en werd onklikbaar. Opgelost door de knop te laten verdwijnen zolang het paneel open is (`.is-hidden`), niet door met z-index te schuiven.
- **Paneel bleef open na klikken op een link.** Opgelost met een klik-handler op alle links in het paneel.
- **Titelblok en tekst niet uitgelijnd.** Titelblok en body hadden een verschillende binnenmarge (2rem tegen 24px). Beide even breed, maar de tekst stond niet op dezelfde lijn. Nu staat de marge op een binnenste wrapper met dezelfde waarde.
- **Strandfoto in HTML.** Een keer als kopfoto boven het titelblok gebruikt. Afgewezen: die foto hoort bij de PowerPoint-titeldia, en in HTML blijft het titelblok met logo bovenaan.
- **Patroon nagebouwd.** Bij gebrek aan het SVG-bestand is het patroon een keer uit de maten in B.5 nagebouwd. Niet de bedoeling; de gids zegt nu expliciet: zonder bestand geen patroon.

## PowerPoint

- **Fonts.** `pptxgenjs` embedt geen fonts. In een praktijkcase viel PowerPoint daardoor terug op een generieke bold sans. De embedprocedure in §3.6 is herleid uit `Powerpoint_sjabloon.potx`, dat het wel goed doet. LibreOffice toont ingebedde fonts niet betrouwbaar; daarom altijd met een script controleren.
- **Tegenstrijdige titeldia.** De gids beschreef drie versies: volledig navy (§3.4), wit met strandfoto onderaan (§3.5) en blauw tekstvlak links met foto rechts (Bijlage B.3). Ook de sluitdia stond er twee keer in. **Besluit 10 oktober 2026 (Paul):** B.3 is de standaard.
- **Contentdia-maatvoering** is vastgesteld aan de hand van `Doorbraakinitiatieven_DBF.pptx` (8 dia's). Ook gebruikt: de ZSM-adoptie-oefening.
- **Crème op wit** als kaartkleur oogde slap ("geen gezicht"); vervangen door de lichte navy-tint.

## Word

- **Bron:** `Offertesjabloon.dotx`, gevalideerd in echte Word-export door Paul (10 september 2026), getest met de Empatec/Groeituin-offerte en gemeten tegen het origineel.
- **Marges.** Eerder aangenomen: boven 2,6 cm, onder 2,2 cm. Het bronbestand gaf andere waarden en is leidend.
- **Onderrand onder de tabel.** Zat fout in het bronbestand, is in het sjabloon verwijderd.
- **Headerrij vergeten** bij een "rustige" tabel met twee kolommen. Een tabel zonder headerrij oogt niet als tabel; nu altijd verplicht.
- **Eén vaste alinea-afstand voor alles** gaf 11 in plaats van 9 pagina's bij dezelfde inhoud. Vervangen door functionele afstanden (§4.2). De regels in §4.2 komen uit vijf correctierondes.
- **Tab-uitlijning** leek fout, maar bleek een weergavefout van de testomgeving (geen Calibri Light geïnstalleerd).

## Beeldbank

- Beelden stonden eerst als links naar de eigen website. Die bleek niet bereikbaar vanuit Claude, en het moest werken voor collega's vanuit hun eigen Claude-omgeving. Daarom een openbare GitHub-repository (`dbfbeeldbank/dbf`). Websitelinks zijn nu alleen nog opslaglocatie.
- Bestandsnamen op de website (met "-scaled") weken af van de originelen; op GitHub staan de originele archiefnamen.
- Het sjoelbeeld kreeg nummer C.46 in plaats van 18, omdat C.18–C.28 al in gebruik waren.

## 10 oktober 2026 — assetpakket en gids bijgewerkt

- **Assetpakket compleet.** Alle bestanden waar de gids naar verwijst staan op GitHub, met `DBF_assets_manifest.csv` als volledige lijst en `DBF_huisstijl_assets.zip` als noodroute voor AI-omgevingen zonder internet (ChatGPT kon GitHub niet bereiken).
- **Fotostrook zwart-wit, zonder koningsblauw filter** (besluit Paul; vervangt de tint van 62%). Uitsnede overgenomen uit `Powerpoint_sjabloon.potx`. Hogere resolutie bestaat niet: het sjabloon zelf heeft 88 × 791 px.
- **Titelfoto** uit het sjabloon gehaald in de oorspronkelijke resolutie (2765 × 1844) in plaats van de schermafbeelding.
- **Slotdia zonder tekst** (besluit Paul): alleen patroon en logo.
- **Sluitdia-logo in het `.potx` bleek niet beschadigd** (wit, echte transparantie, gecontroleerd op koningsblauw). Waarschuwing uit §1.2 geschrapt.
- **Offertesjabloon aangepast:** footer `#15284B` → `#27275B`; Heading 1/2 stonden in Word-standaardblauw `#2E74B5` en zonder outline-niveau. Nu zwart, Calibri Light, vet, 10,5 pt, navigeerbaar.
- **C.04 hernoemd:** het "…"-teken in de bestandsnaam brak andere AI-omgevingen. Regel voor alle bestandsnamen: alleen `A–Z a–z 0–9 _ - .`.
- **Chevron-PNG's** opnieuw uit de vectorpunten gemaakt; de oude PNG's in de projectmap waren niet transparant en goud week 1 punt af (`#DDB85F`).

## 13 oktober 2026 — nieuwe chevron en nieuw patroon

- **Aanleiding.** Studies voor bureaubladen en seizoensbeelden. Het patroon van 10 oktober (liggende chevrons in halfsteensverband) bleek weinig ruimte te bieden voor variatie.
- **Afgewezen richtingen.** Een algemeen Japans hennepbladraster (asanoha) en een Chinees maliënpatroon: mooi, maar te weinig DBF. Het beeldmerk als tegel herhalen: "vreselijk". Tweekleurige, metallic-achtige vlakken: afgewezen; elke vorm één vlakke kleur. Vormen die uit het raster vallen (herfstbladeren): onrustig; het seizoen moet binnen het raster blijven.
- **Doorbraak uit eigen schetsen van Paul.** Eerst: twee chevrons die samen een zeshoek vormen, met een staafje ertussen. Daarna: drie chevrons rond één punt als Y-ster. Correcte lezing van de tweede schets: op elke rand van een honingraat liggen twee chevrons die elkaar aankijken; de ster ontstaat op de knooppunten. Beide schetsen gebruikten onafhankelijk van elkaar dezelfde samengedrukte chevron (armen onder 30°).
- **Fout hersteld.** In een tussenstap werd de punthoek van de oude chevron als 52° opgegeven. Nagerekend uit de vectorpunten is die 95° (buiten) en 128° (binnen).
- **Second opinion (ChatGPT).** Voorkeur voor het nieuwe raster, standaard volledig toon op toon, één chevron in plaats van twee varianten, beeldmerkintegratie als sterkste argument. Getoetst: het beeldmerk past op 96% van de celbreedte in één verticale cel, zonder vervorming. De bewering dat de chevronvorm nog niet vastlag, klopte niet met de gids (§1.3 was vastgelegd); het vervangen is daarom een bewust besluit met gevolgen voor alle chevronbestanden.
- **Besluiten (Paul).** Nieuwe chevron (63%, buitenhoek 120°) als enige vorm. Nieuw patroon (B.5). Titel- en scheidingsdia 'chevrondiepte' ("echt geweldig"). Dekking van het patroon 5% in plaats van 10%, omdat vlakken zwaarder ogen dan lijnen.
- **Nog in proef.** Slotdia met beeldmerk in één cel (B.6); zandvarianten.
- **Gevonden fout in de gids.** In Bijlage A stonden twee keer de onopgeloste plaatshouder `{R}` in plaats van de release-URL. Hersteld.
- **Fotostrook terug in kleur** (besluit Paul): zwart-wit maakte de contentdia te streng. `DBF_fotostrook.png` is dezelfde uitsnede als in het sjabloon, met de blauwe lucht; `DBF_fotostrook_zw.png` vervalt.
- **PowerPoint-sjabloon was de verkeerde basis.** Aanpassingen in `Powerpoint_sjabloon.potx` (indelingen voor chevrondiepte en slot) gaven een resultaat dat schril afstak bij de gewone DBF-presentaties ("een ramp"). Oorzaak: dat bestand is het oude bronbestand van september; de echte DBF-vormgeving is de referentie-implementatie uit §3.5, waarmee o.a. de Aveleijn-presentatie is gebouwd. De aanpassingen zijn teruggedraaid; het `.potx` blijft ongewijzigd in de release. Nieuw referentievoorbeeld: `DBF_voorbeeldpresentatie.pptx`.
- **Slotdia met beeldmerk vastgesteld** (B.6): het beeldmerk in de middelste cel van een gecentreerd raster, zonder logo of tekst. Zelfde principe voor de achterkant van een rapport, met alleen het webadres. Staande A4-varianten van het patroon toegevoegd.
- **HTML-kop en -voet:** een reeks alternatieven (licht, zand, foto, lichtblauw, zwarte logoband met crème logo) is bekeken en afgewezen: "saai en massief", "babyblauw en een ander font is een no go", "veel te heftig". Het origineel blijft, met twee lijnen: een witte haarlijn onder het logo en een gouden lijn tussen patroonstrook en voet. Les: koningsblauw bovenin is het herkenbaarst; het chevrondieptepaar mag nooit uit elkaar vallen.
- **Fotobeschrijvingen uitgebreid** met 'Wat je ziet' (C.01–C.17, C.46). Bij het bekijken bleken drie toeschrijvingen te stellig: C.02 (welke Sint-Jan), C.03 (plaats niet in de titel) en C.16, dat vrijwel zeker een Duits militair muziekkorps tijdens de bezetting toont.
- **C.16 verwijderd uit de beeldbank** (besluit Paul): de foto toonde vrijwel zeker een Duits militair muziekkorps tijdens de bezetting en was beschreven als neutraal beeld van samen muziek maken. Het nummer C.16 wordt niet opnieuw gebruikt.

## 20–22 oktober 2026 — eigen PowerPoint-sjabloon

- **Nieuwe basis.** `Powerpoint_sjabloon.potx` is opnieuw opgebouwd vanuit de Aveleijn-presentatie (13,333 × 7,5 inch, maten en rand van de inhoudsdia, ingesloten lettertypen), niet vanuit het oude bronbestand van september (22 inch, met klantinhoud). Alle 31 inhoudsdia's en alle klantinhoud zijn weggelaten. Resultaat: een echte slidemaster met tijdelijke aanduidingen, 0,7 MB in plaats van 28 MiB, dus in de hoofdmap in plaats van in de release.
- **Warmer, minder blauw.** Twee varianten bekeken: zand met koningsblauw voor nadruk, of crème met een gouden bovenlijn en zand voor nadruk. Gekozen: zand (besluit Paul). Crème op wit bleek nauwelijks zichtbaar (contrast ongeveer 1:1). Lichtblauw `#E3E4ED` niet meer voor kaarten.
- **Slankere titels.** Merriweather Regular (400) en Light (300) naast elkaar bekeken; gekozen: Regular. Light vroeg een extra ingesloten lettertype voor een klein verschil. Bold blijft voor kleine kaartkoppen.
- **Geen foto op de openingsdia.** Eerst bleef de foto-opening als tweede indeling beschikbaar; daarna geschrapt (besluit Paul: "die foto's zijn leuk voor html's maar niet voor ppt's, we framen teveel"). De chevrondiepte is de enige opening. `DBF_titelfoto_strand.jpg` vervalt.
- **Scheidingsdia.** Het grote gouden nummer boven de titel leek een doorgeschoven titelregel. Nu een klein label (‘01’, Open Sans Bold, goud) boven een korte gouden lijn. Dat wijkt bewust af van de HTML-regel (nummer in dezelfde kleur en letter als de titel): hier staat het nummer niet naast de titel, maar als aparte regel erboven.
- **Titels lager.** Op inhouds- en accentdia stond de titel op 0,42 inch "errug hoog". Nu op 1,05 inch, tekstvak vanaf 2,15 inch. Het tekstvak is daardoor ruim vier regels korter; dat dwingt tot één boodschap per dia.
- **Slotdia zonder titelvak.** De afspraak "elke indeling een titelvak" botst met B.6 (geen tekst op de slotdia). B.6 gaat voor; PowerPoint meldt bij de toegankelijkheidscontrole daardoor een ontbrekende titel.
- **Controle.** `validate.py` geslaagd; ingesloten lettertypen per script gecontroleerd (EOT-kop, lettertype te openen, fsType 0), omdat LibreOffice ingesloten lettertypen niet toont. De chevrondiepte als vrije vorm is vergeleken met `DBF_titeldia_chevrondiepte_koningsblauw.png`: gelijk.
- **Voorbeeldpresentatie** opnieuw gemaakt met het sjabloon, nu wel met ingesloten lettertypen. Dianummers in de gids aangepast (chevrondiepte is dia 1).
- **HTML: vaste auteursrechtregel** onder de documentregel in de footer (besluit Paul, 22 oktober 2026); tekst in §2.4.
