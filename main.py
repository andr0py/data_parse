# XML PARSZOLÁS
import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")
root = tree.getroot()

# film cím, és attribútumok
for detail in root.findall("./movie"):
    film_cim = detail.findtext("title")
    film_azonosito = detail.get("id")
    film_kategoria = detail.get("genre")
    film_hossz = detail.get("runtime")
    print(f"id: {film_azonosito} - cím: {film_cim} - kategória: {film_kategoria} - játékidő: {film_hossz} perc")