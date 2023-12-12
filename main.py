# XML PARSZOLÁS
import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")
root = tree.getroot()

for movie in root.iter():
    print(movie.text)