"""
DBF-chevron en DBF-patroon — generator. Huisstijlgids §1.3, §3.7 en Bijlage B.
Vastgesteld 13 oktober 2026 (besluit Paul). Vervangt de versie van 10 oktober 2026.

CHEVRON (§1.3)
  De chevron van 10 oktober, in de pijlrichting samengedrukt tot 63,04 % (= 535 / (490·√3)),
  zodat de armen exact onder 30° staan: buitenhoek 120°, binnenhoek 146°.
  Vectorpunten (viewBox 0 0 924 1316, punt naar rechts, gecentreerd zoals de oude vorm):
  296.7,118 461.2,653 296.7,1188 348.4,1188 657.3,653 348.4,118

PATROON (Bijlage B.5)
  Honingraat met randlengte d (hoekpunten met puntige zeshoeken, verticale randen).
  Op elke rand twee chevrons met de punten naar de hoekpunten, die elkaar aankijken: samen een kleine zeshoek.
  Op elk hoekpunt komen drie chevrons samen tot een Y-ster; de witte Y-voegen wijzen naar het zeshoekmidden.
  Maat van de chevron in het raster: halve breedte a = 0,408·d; afstand punt tot hoekpunt 0,047·d.
  Optionele verbindingsstaaf (alleen bijzondere toepassingen): dwars door een zeshoekmidden, van ster naar ster,
  breedte = eindbreedte van de chevron (0,0966·a), vrij van de chevrons (start op 1,27·a van het hoekpunt).
  Standaard: alleen de chevrons, toon op toon (5 % wit op donker, 5 % koningsblauw op wit). Geen goud, geen verloop.

Gebruik:  python3 patroon.py           -> DBF_chevron.svg, 10 chevron-PNG's, 6 patroon-SVG's
          python3 patroon.py --png     -> ook de dia-afbeeldingen (4000x2250, vereist cairosvg en
                                          DBF-beeldmerk-wit.png in dezelfde map)
  Het raster is gecentreerd: het midden van één verticaal chevronpaar valt op het midden van het vlak.
"""
import math, sys

# ---------- chevron ----------
F = 535 / (490 * math.sqrt(3))               # 0,63036
CHEVRON = [(296.7,118),(461.2,653),(296.7,1188),(348.4,1188),(657.3,653),(348.4,118)]
# genormaliseerd: punt in (0,0), opent naar +y, halve breedte 1
CHV = [(-1, 572*F/535), (0, 311*F/535), (1, 572*F/535), (1, 490*F/535), (0, 0), (-1, 490*F/535)]

PALET_PNG = {  # bestandsnaam: kleur  (§3.7; namen ongewijzigd i.v.m. bouwscripts)
    'DBF_chevron_navy.png': '#27275B', 'DBF_chevron_222831.png': '#222831', 'DBF_chevron_30475E.png': '#30475E',
    'DBF_chevron_C1A57B.png': '#C1A57B', 'DBF_chevron_gold.png': '#DDB85E', 'DBF_chevron_ECECEC.png': '#ECECEC',
    'DBF_chevron_000000.png': '#000000', 'DBF_chevron_white.png': '#FFFFFF', 'DBF_chevron_FFFCF2.png': '#FFFCF2',
    'DBF_chevron_E3E4ED.png': '#E3E4ED'}

def chevron_svg():
    pts = ' '.join(f'{x},{y}' for x, y in CHEVRON)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 924 1316">'
            f'<polygon points="{pts}" fill="currentColor"/></svg>')

def chevron_png(naam, kleur, ss=4):
    from PIL import Image, ImageDraw
    big = Image.new('RGBA', (924*ss, 1316*ss), (0, 0, 0, 0))
    rgb = tuple(int(kleur[i:i+2], 16) for i in (1, 3, 5))
    ImageDraw.Draw(big).polygon([(x*ss, y*ss) for x, y in CHEVRON], fill=rgb + (255,))
    big.resize((924, 1316), Image.LANCZOS).save(naam)

# ---------- raster ----------
def honingraat(breed, hoog, d, gecentreerd=True):
    """Gecentreerd: het midden van één verticaal chevronpaar ligt precies in het midden van het vlak
    (daar komt op de slotdia en de achterkant het beeldmerk, B.6)."""
    dx, dy = math.sqrt(3)*d, 1.5*d
    ox, oy = (breed/2 - dx/2, hoog/2) if gecentreerd else (0, 0)
    V = {}; X = []
    for j in range(-int(oy/dy)-3, int((hoog-oy)/dy)+3):
        for i in range(-int(ox/dx)-3, int((breed-ox)/dx)+3):
            c = (ox + i*dx + (dx/2 if j % 2 else 0), oy + j*dy); X.append(c)
            for t in (-90, -30, 30, 90, 150, 210):
                v = (c[0]+d*math.cos(math.radians(t)), c[1]+d*math.sin(math.radians(t)))
                V[(round(v[0], 1), round(v[1], 1))] = v
    V = list(V.values()); E = []
    for i, v in enumerate(V):
        for w in V[i+1:]:
            if abs(math.dist(v, w) - d) < 0.01*d: E.append((v, w))
    return X, V, E

def chevron_op_rand(v, w, d):
    a, eps = 0.408*d, 0.047*d
    ux, uy = (w[0]-v[0])/d, (w[1]-v[1])/d; px, py = -uy, ux
    return [(v[0]+(eps+y*a)*ux+x*a*px, v[1]+(eps+y*a)*uy+x*a*py) for x, y in CHV]

def staaf(c, hoek, d):
    a = 0.408*d; b = 0.0966*a; t0 = 1.27*a
    v = (c[0]+d*math.cos(math.radians(hoek)), c[1]+d*math.sin(math.radians(hoek)))
    ux, uy = (c[0]-v[0])/d, (c[1]-v[1])/d; px, py = -uy*b/2, ux*b/2; s, e = t0, 2*d-t0
    return [(v[0]+ux*s+px, v[1]+uy*s+py), (v[0]+ux*e+px, v[1]+uy*e+py),
            (v[0]+ux*e-px, v[1]+uy*e-py), (v[0]+ux*s-px, v[1]+uy*s-py)]

def _p(pts): return ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)

def svg(breed, hoog, achtergrond, kleur, dekking, d, overslaan=None, extra=''):
    X, V, E = honingraat(breed, hoog, d); vormen = []
    for v, w in E:
        if overslaan and overslaan(v, w): continue
        for p, q in ((v, w), (w, v)):
            pts = chevron_op_rand(p, q, d)
            if all(x < -d or x > breed+d or y < -d or y > hoog+d for x, y in pts): continue
            vormen.append(f'<polygon points="{_p(pts)}"/>')
    bg = f'<rect width="100%" height="100%" fill="{achtergrond}"/>' if achtergrond else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{breed}" height="{hoog}" viewBox="0 0 {breed} {hoog}">'
            f'{bg}<g fill="{kleur}" fill-opacity="{dekking}">{"".join(vormen)}</g>{extra}</svg>')

VARIANTEN = {  # bestand: (breedte, hoogte, achtergrond, kleur, dekking, d)   status volgens Bijlage B.1/B.2
    'DBF_patroon_koningsblauw.svg':    (1920, 1080, '#27275B', '#FFFFFF', 0.05, 180),  # vastgesteld, standaard
    'DBF_patroon_htmlnavy_strook.svg': (1600,   90, '#27275B', '#FFFFFF', 0.06,  40),  # vastgesteld (naam historisch)
    'DBF_patroon_wit.svg':             (1920, 1080, '#FFFFFF', '#27275B', 0.05, 180),  # vastgesteld, bijzondere uitgaven
    'DBF_patroon_navy.svg':            (1240, 1754, '#222831', '#FFFFFF', 0.05, 160),  # alleen gemotiveerde uitzondering
    'DBF_patroon_zand_A_voorstel.svg': (1920, 1080, '#ECE4D7', '#C1A57B', 0.18, 180),  # voorstel
    'DBF_patroon_zand_B_voorstel.svg': (1920, 1080, '#ECE4D7', '#C1A57B', 0.12, 180),  # voorstel
    'DBF_patroon_koningsblauw_A4.svg': (1240, 1754, '#27275B', '#FFFFFF', 0.05, 150),  # vastgesteld: achterkant rapport (staand)
    'DBF_patroon_wit_A4.svg':          (1240, 1754, '#FFFFFF', '#27275B', 0.05, 150),  # vastgesteld: bijzondere uitgaven (staand)
}

def beeldmerk_in_cel(breed, hoog, d, bestand='DBF-beeldmerk-wit.png'):
    """<image>-element: het witte beeldmerk precies in de middelste verticale cel (B.6).
    De zeshoek van het beeldmerk wordt 0,906·d hoog; marges in het PNG-bestand worden meegerekend."""
    import base64
    from PIL import Image
    im = Image.open(bestand); bb = im.getbbox(); fw, fh = im.size
    hh = 0.906*d; s = hh/(bb[3]-bb[1]); ww = (bb[2]-bb[0])*s
    x = breed/2 - ww/2 - bb[0]*s; y = hoog/2 - hh/2 - bb[1]*s
    uri = 'data:image/png;base64,' + base64.b64encode(open(bestand, 'rb').read()).decode()
    return f'<image href="{uri}" x="{x:.1f}" y="{y:.1f}" width="{fw*s:.1f}" height="{fh*s:.1f}"/>'

def middelste_cel(breed, hoog, d):
    """Filter voor svg(): laat het chevronpaar in het midden weg."""
    def f(v, w):
        m = ((v[0]+w[0])/2, (v[1]+w[1])/2)
        return abs(v[0]-w[0]) < 1 and math.dist(m, (breed/2, hoog/2)) < 1
    return f

def titeldia_svg(breed=4000, hoog=2250):
    """Titel- en scheidingsdia 'chevrondiepte': twee grote chevrons toon op toon, afgesneden door de rechterrand."""
    def groot(cx, cy, h):  # punt naar rechts, totale hoogte h
        a = h/2; pts = [(-y*a + 0.337*a, x*a) for x, y in CHV]
        return [(cx+x, cy+y) for x, y in pts]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{breed}" height="{hoog}">'
            f'<rect width="100%" height="100%" fill="#27275B"/>'
            f'<polygon points="{_p(groot(0.8875*breed, 0.5*hoog, 1.667*hoog))}" fill="#30306A"/>'
            f'<polygon points="{_p(groot(0.95*breed, 0.5*hoog, 1.222*hoog))}" fill="#34346F"/></svg>')

if __name__ == '__main__':
    open('DBF_chevron.svg', 'w').write(chevron_svg()); print('geschreven: DBF_chevron.svg')
    for naam, kleur in PALET_PNG.items(): chevron_png(naam, kleur); print('geschreven:', naam)
    for naam, (w, h, bg, k, a, d) in VARIANTEN.items():
        open(naam, 'w').write(svg(w, h, bg, k, a, d)); print('geschreven:', naam)
    if '--png' in sys.argv:
        import cairosvg, base64
        d = 375  # 1,25 inch op een dia van 13,333 inch
        cairosvg.svg2png(bytestring=svg(4000, 2250, '#27275B', '#FFFFFF', 0.05, d).encode(),
                         write_to='DBF_patroon_slotdia_koningsblauw.png'); print('geschreven: DBF_patroon_slotdia_koningsblauw.png')
        # slotdia met het beeldmerk in de middelste cel (B.6)
        cairosvg.svg2png(bytestring=svg(4000, 2250, '#27275B', '#FFFFFF', 0.05, d, middelste_cel(4000, 2250, d),
                         beeldmerk_in_cel(4000, 2250, d)).encode(), write_to='DBF_slotdia_beeldmerk_koningsblauw.png')
        print('geschreven: DBF_slotdia_beeldmerk_koningsblauw.png')
        cairosvg.svg2png(bytestring=titeldia_svg().encode(), write_to='DBF_titeldia_chevrondiepte_koningsblauw.png')
        print('geschreven: DBF_titeldia_chevrondiepte_koningsblauw.png')
