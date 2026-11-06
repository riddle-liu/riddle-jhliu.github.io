# Regenerate talkmap/org-locations.js from the `location` field of each talk.
#
# Run from the repository root:   python talkmap.py
# Requires: geopy   (pip install geopy)
#
# Only the data file is rewritten. The map page itself (talkmap/map.html) and
# its self-hosted Leaflet files are maintained by hand.

import glob
import json
import re
import time

from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent="academic-site-talkmap")
points = {}

for path in sorted(glob.glob("_talks/*.md")):
    with open(path, encoding="utf-8") as f:
        match = re.search(r'^location:\s*"([^"]+)"', f.read(), re.M)
    if not match or match.group(1) in points:
        continue
    place = match.group(1)
    result = geocoder.geocode(place)
    time.sleep(1)  # Nominatim allows at most one request per second
    if result is None:
        print(f"Could not geocode: {place} ({path})")
        continue
    points[place] = [place, result.latitude, result.longitude]
    print(place, "->", result.latitude, result.longitude)

with open("talkmap/org-locations.js", "w", encoding="utf-8") as f:
    f.write("var addressPoints = " + json.dumps(list(points.values()), indent=2, ensure_ascii=False) + ";\n")

print(f"Wrote {len(points)} locations to talkmap/org-locations.js")
