# XML PARSZOLÁS
import xml.etree.ElementTree as ET
# text wrap importálása
import textwrap
import subprocess

# element tree inicializálása / fájl beolvasás
tree = ET.parse("data.xml")
root = tree.getroot()

# jelenítsük meg a filmek címét, megjelenés dátumát, kategóriáját, játékidőt, és az összefoglalót.
for movie in root.findall("movie"):
    # cím érték kinyerése
    cim = [cim.text for cim in movie.findall("title")][0]
    # megjelenési dátum értéke
    megjelenes = [megjelenes.text for megjelenes in movie.findall("year")][0]
    # kategória érték
    kategoria = movie.get("genre")
    # játékidő / hossz
    hossz = movie.get("runtime")
    # összefoglaló a filmről
    sztori = [sztori.text for sztori in movie.findall("plot")][0]
    # kiíratjuk formázottan
    print(f"{cim}, {megjelenes}, {kategoria}, {hossz} perc ".ljust(72, '.'),\
          f"\n{textwrap.fill(sztori, width=72).strip()}\n{'.'*72}\n")

ping_statisztika = subprocess.check_output("git log --oneline", encoding="UTF-8")
print(ping_statisztika)