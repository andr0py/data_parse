# XML PARSZOLÁS
import xml.etree.ElementTree as ET
import textwrap

tree = ET.parse("data.xml")
root = tree.getroot()

# jelenítsük meg a filmek címét, megjelenés dátumát, játékidőt, és az összefoglalót.
for movie in root.findall("movie"):
    cim = [cim.text for cim in movie.findall("title")][0]
    megjelenes = [megjelenes.text for megjelenes in movie.findall("year")][0]
    kategoria = movie.get("genre")
    hossz = movie.get("runtime")
    sztori = [sztori.text for sztori in movie.findall("plot")][0]
    print(f"{cim}, {megjelenes}, {kategoria}, {hossz} perc ".ljust(72, '.'),\
          f"\n{textwrap.fill(sztori, width=72).strip()}\n{'.'*72}\n")