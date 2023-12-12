# XML PARSZOLÁS
import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")
root = tree.getroot()

# címek
for movie in root.iterfind("./movie/title"):
    print(movie.text)

#címek keresése, 1linerként
movie_title = [title.text for title in root.iterfind("./movie/title")]
print(movie_title)