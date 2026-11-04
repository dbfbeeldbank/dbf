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
- **Auteursrechtregel aangevuld (24 oktober 2026).** Aanleiding: een HTML (Cotap, 23 oktober) kwam zonder auteursrechtregel. De gids op GitHub en in de zip was op dat moment wel actueel (22 oktober), maar het referentievoorbeeld `DBF_voorbeeld_html.html` (13 oktober) had de regel nog niet; de HTML volgt dat voorbeeld verder precies. Ook de projectkopie van de gids liep achter (10 oktober). Daarnaast stond in de gids de verkeerde rechtspersoon ("De Betekenisfabriek B.V."); dat is nu "De Betekenisfabriek Groep B.V.". De regel staat nu ook op de achterkant van het rapport, onder een gouden lijn (besluit 22 oktober, toen niet in de gids verwerkt). Het voorbeeld heeft de regel nu ook. Les: na elke gidswijziging ook het referentievoorbeeld en de projectkopie bijwerken.
- **Twee optionele HTML-bouwstenen (24 oktober 2026, besluit Paul).** (1) Vertrouwelijkheidsregel: niet standaard, alleen bij echt vertrouwelijke stukken; eenzijdige disclaimers hebben weinig juridische kracht en verwateren als ze overal staan. (2) Co-brandingbalk: witte balk met DBF-logo links en klantlogo rechts, in plaats van de bovenste laag van het titelblok. Claude vraagt bij elke HTML naar beide (§0).
- **Tabellen binnen de tekstkolom (26 oktober 2026, besluit Paul).** Aanleiding: een HTML (ZSM, Deel je leven) had tabellen die links buiten de tekstkolom uitstaken en rechts verder liepen dan de koppen; Paul: "niet acceptabel". De gids gaf voor tabellen alleen kleuren, geen regel voor breedte, en het voorbeeld had geen tabel. Nu: tabel altijd binnen de kolom, in een eigen scrollkader; nooit uitbreken. Beide voorbeeld-HTML's hebben nu een tabel.
- **Zand in plaats van lichtblauw (27 oktober 2026, besluit Paul).** Aanleiding: de Aveleijn-leergang (HTML) gebruikte lichtblauw voor een blok en labels, terwijl het HTML-palet die kleur niet kende; §1.1 noemde lichtblauw nog als kaartkleur, het PowerPoint-deel niet meer. Vergeleken: lichtblauw of zand. Gekozen: zand ("rechts voor mij"). Lichtblauw blijft alleen voor de heatmap; `--zand` staat nu in het HTML-palet.
- **Label als band (27 oktober 2026, besluit Paul).** Aanleiding: kleine massieve datumblokjes oogden hard, en door hun wisselende breedte stonden de moduletitels niet onder elkaar. Bekeken: lichter blok, gouden streep, omlijnd; daarna banden in lichte kleuren, in goud of grijs, en in koningsblauw met een donkerdere tweede kleur. Gekozen: koningsblauw met middenblauw (geen zebrapad), plus een gouden lijn van 2px langs de band voor warmte. Merriweather voor de datums bekeken en afgewezen: het zijn labels, dus Open Sans.

## 28 oktober 2026 — signaalkleuren en beeldschermachtergronden

- **Aanleiding.** Bij een blik op het palet (de vraag was of een mocha of cacao ontbrak) bleek het palet geen kleur te missen, maar wel vaste waarden voor goed, let op en stop. De kwaliteitsrapportage (§5), scorematrices en voortgangsoverzichten gebruikten elk hun eigen tinten. Mocha is afgewezen: een tweede donkere kleur naast koningsblauw (contrast onderling 1,2–1,8:1), de warmte zit al in goud en zand, en de kleur lag dicht tegen een trend aan.
- **Signaalkleuren (besluit Paul).** Eerste voorstel: donker en goed leesbaar als tekst (flessengroen, roestoranje, baksteenrood). Te donker bevonden; daarna licht en warm (salie, abrikoos, terracotta). Abrikoos haalde op zijn eigen vlaktint maar 2,4:1, onder de 3:1 voor markeringen; Paul zag het zelf in een schermafbeelding. Bijgesteld tot oker `#B96B29`, groen een tikje dieper `#648C55`, terracotta `#C7553F` ongewijzigd. Alle drie halen nu 3:1 op wit, papier en eigen vlaktint. Gecontroleerd met de WCAG-formule en een simulatie van rood-groenkleurenblindheid (Machado 2009).
- **Gevolg van licht en warm:** de kleuren zijn geen tekstkleur meer, alleen markering. Daarom een vaste vorm per status (rondje, driehoek, vierkant), zodat kleur nooit alleen staat. Oranje en rood blijven bij kleurenblindheid dicht bij elkaar; de vorm vangt dat op.
- **Play-, pauze- en stopiconen bekeken en afgewezen:** ze beschrijven of iets loopt, niet of het goed gaat, en de play-driehoek botst met de let-op-driehoek.
- **Bewust niet gedaan:** lichtere vlaktinten (die lossen op tegen papier, nu al 1,1:1) en een aparte donkere iconkleur (drie extra kleuren).
- **Nieuw referentievoorbeeld:** `DBF_voorbeeld_signaalkleuren.html`. Tijdens het maken bleek een eerste versie nog de chevron van vóór 13 oktober, witte in plaats van zandkleurige kaarten en geen auteursrechtregel te hebben, omdat die versie was gebouwd op de projectkopie van de gids (10 oktober). Rechtgezet met de gids op GitHub (27 oktober). Les uit 24 oktober bevestigd: bouw altijd vanaf de GitHub-versie.
- **Beeldschermachtergronden (B.8, voorstel).** Briefing toegevoegd: eerst vragen naar kleur (koningsblauw of goud), afwerking (toon op toon of glas) en apparaat, daarna de resolutie opzoeken bij de fabrikant en met een tweede bron controleren. Claude kan niet zien op welk apparaat een vraag gesteld wordt. "Glas" is bewust gedefinieerd zonder glans, verloop of onscherpte, zodat het binnen B.2 blijft. Goud als achtergrond mag alleen hier, omdat er geen tekst op staat. Goud en glas staan in proef (§6).
- **Externe review (28 oktober 2026).** Een tweede AI-model beoordeelde gids, logboek, manifest en voorbeelden. De harde bevindingen zijn nagerekend en klopten: (1) het manifest had verouderde controlegetallen voor gids, logboek en `DBF_voorbeeld_html.html` en miste drie bestanden. Oorzaak: het releasescript maakt het manifest niet opnieuw aan, dus elke update maakte het verder verouderd. Nu opnieuw opgebouwd; het manifest staat bewust niet in zichzelf. (2) `DBF_offerte_sjabloon.dotx` had in de stijlen Kop 4 en Kop 5 nog de oude Word-blauw `#2E74B5`; niet zichtbaar in het sjabloon (dat gebruikt alleen Kop 1), wel zodra iemand die koppen gebruikt. Nu zwart, zoals de andere koppen. (3) Bijlage A noemde het logo met tagline voor de slotdia, die geen logo heeft. (4) De kop "Kleur: drie niveaus" telde na de signaalkleuren vier soorten.
- **Voorrangsregel omgedraaid (besluit Paul).** §0 zei dat een bronbestand voorgaat op de gids. Dat kwam uit de bouwfase (geen waarden verzinnen), maar liet een oud sjabloon een nieuw besluit terugdraaien. Nu: de gids gaat voor, een sjabloon is de uitvoering, en bij verschil meldt Claude het in plaats van zelf te kiezen.
- **Overgenomen als richting, nog niet uitgevoerd:** schrijfstijl (af te leiden uit eigen teksten van Paul), afspraken over eigen identiteit tegenover die van de klant, vormgeving van strategische modellen, labels per regel (verplicht, standaard, optioneel, in proef) en de gids opsplitsen in merkregels, productie-instructies en beeldbank. **Niet overgenomen:** versienummers in plaats van datums (weinig winst), sjablonen voor LinkedIn, video en nieuwsbrief (nog geen vraag naar).
- **Schrijfstijl als apart bestand (28 oktober 2026).** Aanleiding: de externe review miste een afspraak over hoe DBF klinkt. Paul leverde een offerte, een memo aan een raad van bestuur, een brief aan managers, een strategieplan waar hij trots op is, een websitetekst en een tegenvoorbeeld (een koersdocument: "inhoud geweldig, taal te wollig, abstract, metaforisch en modelmatig"). Volgens Paul komt dat mede doordat analyses eerst door taalmodellen zijn verwoord en daarna bijgeschaafd. De telling bevestigde dat: in het tegenvoorbeeld meer abstracte woorden en ruim twee keer zoveel "niet X, maar Y"-zinnen. Vastgelegd in `DBF_schrijfstijl.md` (concept, in proef), apart van de gids: de eerste stap in de opsplitsing die de review aanraadde. Geen citaten uit klantstukken; voorbeelden herschreven of geanonimiseerd.

## 2 november 2026 — HTML: bladspiegel, kaarten met diepte en de hoekregel

- **Aanleiding.** Een HTML voor een gemeenteweekend (werkvormen met keuzekaarten, tijdlijn en draaikaartjes) viel op als "supermooi", terwijl rapportages in dezelfde week flets oogden, met dunne grijze lijntjes. De workshoppagina bleek gebouwd op een tussenversie van de gids en week op drie punten af: een grote chevron in het titelblok, afgeronde hoeken en eigen iconen.
- **Afgewezen: meer kleurcontrast als oplossing.** Eerste diagnose: de lichte tinten liggen te dicht bij elkaar (zand op papier 1,14:1). Voorstel: witte achtergrond, zand voor alle kaarten, drempels voor contrast. Toegepast op een Aveleijn-HTML: "werkelijk vreselijk", verder weg van de workshoppagina dan het origineel. Les: diepte maakt het vlak, niet de kleur. Witte kaarten op papier zijn volgens de meetlat onzichtbaar (1,11:1), maar met een zachte schaduw juist het sterkst.
- **Afgewezen: alles haaks.** Na "deze Claude-hoekjes zijn een no-go" werden alle hoeken recht. Dat was te ruim gelezen: bedoeld was alleen een gekleurde rand die meebuigt met een afgeronde hoek. Rechte kopbalken tussen afgeronde kaarten oogden eerst "verblokt"; later toch gekozen voor haakse titelblokken en kopbalken (besluit Paul), met afgeronde kaarten eromheen.
- **Besluiten (Paul).** Grote chevron rechts in het HTML-titelblok, één laag, `#3F3A5B`. Titelmaat als de workshoppagina. Zwevende kaart over de onderrand van het titelblok ("bladspiegel"). Kaarten wit met schaduw, zonder grijze rand; vlakken zand. Hoekregel: kaarten 14px, zwevende kaart 18px, labels rond, titelblok en koppen haaks, en een gekleurde rand buigt nooit mee. Draaikaartjes met de chevron op gelijke hoogte. Mobiele regel: inhoud in het eerste scherm, keuze bereikbaar, geen zijwaarts scrollen.
- **Mobiel.** De workshoppagina toonde op een telefoon pas na bijna anderhalf scherm inhoud, de tijdlijnbalk verloor zijn namen en wisselen vroeg terugscrollen. Opgelost met een korter titelblok, een uitklapregel voor de aandachtspunten, een vaste keuzebalk en het weglaten van de tijdlijnbalk. In de Aveleijn-HTML bleek de pagina op mobiel 485px breed: keuzelabels zonder spatie ertussen braken niet af.
- **Tijdlijnbalk.** Namen werden afgekapt ("Samen opplak…"). Nu een nummer in elk blok, de naam alleen als hij past, en de volledige naam onder de balk bij aanwijzen.
- **Voorbeelden.** `DBF_voorbeeld_html.html` bijgewerkt (titelblok met chevron, zwevende kaart, kaarten met schaduw). Nieuw: `DBF_voorbeeld_html_interactief.html`, met neutrale inhoud. Co-branding- en signaalkleurenvoorbeeld volgen bij de eerstvolgende bewerking (§6).
- **Let op voor de huisstijlskill:** de valkuil "Geen afgeronde hoeken" klopt niet meer; vervangen door de hoekregel uit §2.4 A.
- **Werkt zonder JavaScript (2 november 2026, later die dag).** Op een telefoon, geopend vanuit de mail, toonde de workshoppagina alleen de kopblokken: de voorvertoning voert geen script uit, en alle panelen stonden verborgen en de stappen werden door het script opgebouwd. Nu staat alle inhoud in de HTML en verbergt het script alleen. Regel in §2.8, controlepunt in §2.9; het interactieve voorbeeld is omgebouwd.
- **Noindex als vaste regel (2 november 2026, besluit Paul).** De workshoppagina bleek vindbaar voor zoekmachines. De noindex-regels waren tot nu toe per document toegevoegd (onder meer de Sensire-lesbrief, 5 oktober), maar stonden nooit in de gids. Nu vast in §2.8 en de checklist, en toegevoegd aan alle vier de HTML-voorbeelden. Met de waarschuwing om zo'n pagina niet in robots.txt te zetten.

## 4 november 2026 — tegels voor uitspraken en zilveren fotolijstjes (§1.8)

- **Aanleiding.** Paul kwam op het idee door zijn eigen aantekeningen: blauwe inkt, met een lichtblauwe markeerstift over wat telt. Eerste gedachte: Delftsblauwe tegeltjes voor citaten, om de huisstijl meer lucht te geven.
- **Afgewezen: Delfts blauw.** Kobaltblauw naast koningsblauw `#27275B` oogt als een drukfout. Ook leest een citaat op een tegel snel als tegeltjeswijsheid. Wel behouden: het huiselijke van de tegel.
- **Afgewezen: Merriweather in de tegel.** Een uitspraak van een mens moet er handgeschreven uitzien. Zo ontstaat het verschil tussen onze conclusie (pull quote) en iemands stem (tegel).
- **Afgewezen: afgeronde witte kaart.** Zonder haakse hoeken, ornament, harde schaduw en draaiing was er geen tegelgevoel.
- **Hoekmotieven in drie rondes.** Losse chevrons in de hoeken: "niet goed genoeg". Daarna zes varianten; spinnetje, chevronbloem en lelie vielen af. Toen lijnvarianten zoals het kader. Vaste set: A, D, F, G, H, I, J, K.
- **Handschrift.** Eerst Caveat en Kalam; Kalam te rond. Caveat bleek "iets te informeel"; gezocht naar kroontjespengevoel. Playwrite NL (Nederlands schoolschrift) werd de standaard. Daarna het inzicht van Paul dat meerdere handen het waarachtiger maken: elke stem een eigen hand. Brittany Signature valt af op licentie (alleen persoonlijk gebruik). Homemade Apple mag, maar is het minst leesbaar.
- **Wand of losse tegels.** Een strakke tegelwand (hoeken die samen een motief vormen) werkte technisch, maar voelde als systeem. Gekozen: losse tegels, elk met een eigen hand en hoekje, licht gedraaid. Het concept heet nostalgie.
- **Afgewezen: slijtage.** Een afgebroken hoek en een vergeelde tint zijn bekeken en geschrapt: de tegels blijven wit.
- **Op wit.** In Word, PowerPoint en PDF valt een witte tegel weg. Opgelost met een dunne binnenrand; papiertint is ook bekeken, maar daarop valt de markering weg.
- **Fotolijstje.** Paul vroeg een smal, strak zilveren lijstje (mid-century), eerder donker dan licht, even scheef als de tegels. De witte rand van een oude afdruk werkte binnen het lijstje als passe-partout en gaat er daarom af. Kleurenfoto's werken ook; eigen foto's licht gedempt zodat ze bij de zwart-witbeelden passen.
- **Regels (besluit Paul).** Een naam bij een tegel alleen bij een persona of als we bewust voor- en achternaam vermelden; in onderzoeksuitkomsten niet voor de hand liggend. Verzonnen of samengevatte uitspraken alleen als de waarachtigheid op orde is, en dan altijd als aandachtspunt in de kwaliteitsrapportage. Tegels mogen ook in titelblok, openingsdia en tussendia. Meerdere foto's per pagina mag, bijvoorbeeld indrukken van een sessie. Dezelfde spreker dezelfde hand gaat voor de regel dat twee tegels naast elkaar een andere hand hebben.
- **Nieuwe voorbeelden:** `DBF_voorbeeld_nostalgie.html` en `DBF_voorbeeld_nostalgie_op_wit.pdf`. Word en PowerPoint zijn nog niet getoetst (§6).
- **Grijze blokken in PDF (4 november 2026, later die dag).** Op een iPhone, geopend vanuit Mail, stonden achter de tegels en het fotolijstje in `DBF_voorbeeld_nostalgie_op_wit.pdf` grijze rechthoeken. Hetzelfde gebeurde bij een afgedrukte HTML met kaarten (Sensire, observaties per gesprek). Oorzaak: Chrome zet een vervaagde schaduw om in een grijze afbeelding met een masker; Apple-weergave negeert dat masker. Dit is een bekend probleem met Voorvertoning op de Mac. Oplossing: in print en PDF alleen schaduwen zonder vervaging. Regel in §2.8, controlepunt in §2.9. De printregel toegevoegd aan `DBF_voorbeeld_html.html`, `DBF_voorbeeld_html_interactief.html` en `DBF_voorbeeld_nostalgie.html`; de nostalgie-PDF opnieuw gemaakt. Gecontroleerd met `pdfimages`: geen schaduwafbeeldingen meer. Eerste poging met `html{…}` werkte niet: `:root` weegt zwaarder dan `html`, dus `html:root`.

- **Tegel bleef niet vierkant (4 november 2026, later die dag).** In een Sensire-HTML werd een tegel met een lange uitspraak hoger dan breed. De kaderlijnen, opgebouwd uit vier hoekstukken van een halve tegel, lieten daardoor een gat in de zijlijnen. Oorzaak: `aspect-ratio` is een minimum; de inhoud mag de tegel oprekken. Nu: de tegel is altijd vierkant (`overflow:hidden`, `min-height:0`), de letter schaalt mee met de tegel (`cqi`), en een klein script verkleint de letter als het toch niet past. Getest met vier echte uitspraken, met en zonder script, op 1200 en 390 pixels. Alternatief bekeken en niet gekozen: kaderlijnen in CSS die met elke vorm meerekken, want dan klopt de ingekeepte hoek van F niet meer en is de tegel geen tegel meer.
- **Modelkleuren voor het BSR-model (4 november 2026, besluit Paul).** Aanleiding: in de Sensire-HTML met kaartenuitslagen zette de huisstijl de vier werelden plichtmatig in huiskleuren; Paul moest de rood-geel-blauw-groenindeling met de hand terugzetten. Nu §1.1 E: een model met eigen kleurbetekenis houdt zijn kleuren, de huisstijl zit in vorm en typografie. Waarden overgenomen uit Pauls handmatige versie (gemeten uit de schermafbeelding), niet uit de reader: die gebruikt felle kleuren. Plaatsing nagelopen in de reader (rood linksboven, geel rechtsboven, blauw linksonder, groen rechtsonder). Contrast berekend; "geen" in `--inkt-mid` omdat `--inkt-zacht` op de vlakken 4,3–4,4:1 haalt. Nieuw voorbeeld: `DBF_voorbeeld_bsr.html`.
