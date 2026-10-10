"""
DBF-patroon — vastgesteld 10 oktober 2026 (besluit Paul). Huisstijlgids Bijlage B.5.

Opbouw: de chevron uit §1.3 (vectorpunten 191,118 452,653 191,1188 273,1188 763,653 273,118),
liggend met de punt omhoog, als omlijning met één binnenlijn langs het midden.
Liggend halfsteensverband: rijafstand 86, vormlengte 201,5, tussenruimte 44 (eenheden); hoogte x 0,8.
Alleen de vormen: GEEN diagonale of horizontale verbindingslijnen.

Gebruik:  python3 patroon.py            -> schrijft alle SVG-varianten in de huidige map
          python3 patroon.py --png      -> idem, plus dia-achtergrond PNG (4000x2250, vereist cairosvg)
"""
import sys

S = 201.5 / 1070
def _rot(pts):
    return [((y - 118) * S, (763 - x) * S * 0.8) for x, y in pts]

OMLIJNING = _rot([(191,118),(452,653),(191,1188),(273,1188),(763,653),(273,118)])
BINNENLIJN = _rot([(232,118),(607.5,653),(232,1188)])
PERIODE = 201.5 + 44   # horizontaal
RIJ = 86               # verticaal

def _pts(pts, dx, dy):
    return ' '.join(f'{x+dx:.1f},{y+dy:.1f}' for x, y in pts)

def tegel():
    out = ''
    for dy, offsets in [(0, [0, PERIODE]), (RIJ, [-PERIODE/2, PERIODE/2, PERIODE*1.5])]:
        for dx in offsets:
            out += f'<polygon points="{_pts(OMLIJNING, dx+22, dy)}"/><polyline points="{_pts(BINNENLIJN, dx+22, dy)}"/>'
    return out

def svg(breed, hoog, achtergrond, lijnkleur, dekking=1.0, schaal=0.72, lijndikte=2):
    pw, ph = PERIODE * schaal, 2 * RIJ * schaal
    bg = f'<rect width="100%" height="100%" fill="{achtergrond}"/>' if achtergrond else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{breed}" height="{hoog}" viewBox="0 0 {breed} {hoog}">'
            f'<defs><pattern id="dbf" width="{pw:.3f}" height="{ph:.3f}" patternUnits="userSpaceOnUse">'
            f'<g transform="scale({schaal:.5f})"><g fill="none" stroke="{lijnkleur}" stroke-opacity="{dekking}" stroke-width="{lijndikte}">{tegel()}</g></g>'
            f'</pattern></defs>{bg}<rect width="100%" height="100%" fill="url(#dbf)"/></svg>')

VARIANTEN = {
    # bestand: (breedte, hoogte, achtergrond, lijnkleur, dekking, schaal)   status volgens Bijlage B.1/B.2
    'DBF_patroon_koningsblauw.svg':       (1920, 1080, '#27275B', '#FFFFFF', 0.10, 0.72),  # vastgesteld, standaard
    'DBF_patroon_htmlnavy_strook.svg':    (1600,   90, '#27275B', '#FFFFFF', 0.10, 0.50),  # vastgesteld (naam historisch)
    'DBF_patroon_wit.svg':                (1920, 1080, '#FFFFFF', '#27275B', 0.09, 0.72),  # vastgesteld, bijzondere uitgaven
    'DBF_patroon_navy.svg':               (1240, 1754, '#222831', '#FFFFFF', 0.10, 0.72),  # alleen gemotiveerde uitzondering
    'DBF_patroon_zand_A_voorstel.svg':    (1920, 1080, '#ECE4D7', '#D9CEBB', 1.00, 0.72),  # voorstel
    'DBF_patroon_zand_B_voorstel.svg':    (1920, 1080, '#ECE4D7', '#E2D8C6', 1.00, 0.72),  # voorstel
}

if __name__ == '__main__':
    for naam, (w, h, bg, lc, a, sc) in VARIANTEN.items():
        open(naam, 'w').write(svg(w, h, bg, lc, a, sc))
        print('geschreven:', naam)
    if '--png' in sys.argv:
        import cairosvg   # pip install cairosvg
        # dia 13,333 inch = 4000 px; rijafstand ±0,43 inch = 129 px
        cairosvg.svg2png(bytestring=svg(4000, 2250, '#27275B', '#FFFFFF', 0.10, 129/86, 2.2).encode(),
                         write_to='DBF_patroon_slotdia_koningsblauw.png')
        print('geschreven: DBF_patroon_slotdia_koningsblauw.png')
