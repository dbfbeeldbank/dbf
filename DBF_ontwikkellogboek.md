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
