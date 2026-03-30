import os
import re

pexels_bgs = [
    "https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=1920",
    "https://images.pexels.com/photos/157811/pexels-photo-157811.jpeg?auto=compress&cs=tinysrgb&w=1920",
    "https://images.pexels.com/photos/1105766/pexels-photo-1105766.jpeg?auto=compress&cs=tinysrgb&w=1920"
]

pexels_projects = [
    "https://images.pexels.com/photos/1336067/pexels-photo-1336067.jpeg?auto=compress&cs=tinysrgb&w=800",
    "https://images.pexels.com/photos/2724749/pexels-photo-2724749.jpeg?auto=compress&cs=tinysrgb&w=800",
    "https://images.pexels.com/photos/209296/pexels-photo-209296.jpeg?auto=compress&cs=tinysrgb&w=800",
    "https://images.pexels.com/photos/1029599/pexels-photo-1029599.jpeg?auto=compress&cs=tinysrgb&w=800",
    "https://images.pexels.com/photos/305833/pexels-photo-305833.jpeg?auto=compress&cs=tinysrgb&w=800",
    "https://images.pexels.com/photos/259588/pexels-photo-259588.jpeg?auto=compress&cs=tinysrgb&w=800"
]

engineer_img = "https://images.pexels.com/photos/585418/pexels-photo-585418.jpeg?auto=compress&cs=tinysrgb&w=800"

files = ["index.html", "about.html", "services.html", "projects.html", "contact.html"]

for filename in files:
    if not os.path.exists(filename): continue
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Generic Unsplash background (page-header)
    content = re.sub(r"url\('.*?unsplash.*?'\)", f"url('{pexels_bgs[0]}')", content)
    
    # Hero slider Unsplash images in index.html
    if filename == "index.html":
        content = re.sub(r"url\('https://images\.unsplash\.com/photo-1541881451967.*?'\)", f"url('{pexels_bgs[0]}')", content)
        content = re.sub(r"url\('https://images\.unsplash\.com/photo-1503387762.*?'\)", f"url('{pexels_bgs[1]}')", content)
        content = re.sub(r"url\('https://images\.unsplash\.com/photo-1486406146926.*?'\)", f"url('{pexels_bgs[2]}')", content)
        
        # Why Choose us image
        content = re.sub(r"https://images.unsplash.com/photo-1541881512677-548edddf61de\?[^\"]*", engineer_img, content)
        content = re.sub(r"https://images.unsplash.com/photo-1541881512677-548edddf61de", engineer_img, content)

    # About image replace
    if filename == "about.html":
        content = re.sub(r"https://images.unsplash.com/photo-1541881512677-548edddf61de\?[^\"]*", engineer_img, content)
        content = re.sub(r"https://images.unsplash.com/photo-1504307651254-35680f356fce\?[^\"]*", engineer_img, content)
        content = re.sub(r"https://images.unsplash.com/photo-[a-zA-Z0-9\-]+\?[^\"]*", engineer_img, content) # Catch all remaining unsplash on about.html just in case

    # Projects images replace
    if filename == "projects.html":
        content = re.sub(r"https://images.unsplash.com/photo-1600596542815[^\"]*", pexels_projects[0], content)
        content = re.sub(r"https://images.unsplash.com/photo-1486406146926[^\"]*", pexels_projects[1], content)
        content = re.sub(r"https://images.unsplash.com/photo-1497366216548[^\"]*", pexels_projects[2], content)
        content = re.sub(r"https://images.unsplash.com/photo-1512917774080[^\"]*", pexels_projects[3], content)
        content = re.sub(r"https://images.unsplash.com/photo-1503387762[^\"]*", pexels_projects[4], content)
        content = re.sub(r"https://images.unsplash.com/photo-1524758631624[^\"]*", pexels_projects[5], content)
        
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("SUCCESS")
