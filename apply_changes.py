import os
import re

files = ["about.html", "services.html", "projects.html", "contact.html", "index.html"]

favicon_tag = '<link rel="icon" type="image/png" href="https://cdn-icons-png.flaticon.com/512/2942/2942149.png">\n</head>'

logo_html = '''<a href="index.html" class="logo">
                <img src="https://cdn-icons-png.flaticon.com/512/2942/2942149.png" alt="Logo" class="brand-logo"> SkyRise<span>Builders</span>
            </a>'''

footer_logo_html = '''<a href="index.html" class="footer-logo">
                    <img src="https://cdn-icons-png.flaticon.com/512/2942/2942149.png" alt="Logo" class="brand-logo-footer"> SkyRise<span>Builders</span>
                </a>'''

floating_phone = '''<a href="tel:9999988888" class="phone-float" aria-label="Call Us">
        <i class="fas fa-phone fa-flip-horizontal"></i>
    </a>
    <a href="https://wa.me/919999988888" class="whatsapp-float" target="_blank" aria-label="Chat with us on WhatsApp">'''

for filename in files:
    if not os.path.exists(filename): continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Favicon
    if '<link rel="icon"' not in content:
        content = content.replace('</head>', favicon_tag)

    # Flip Phone Icon across all codebase
    content = content.replace('fa-phone-alt', 'fa-phone fa-flip-horizontal')

    # Replace Navbar Logo
    content = re.sub(r'<a href="index\.html" class="logo">.*?</a>', logo_html, content, flags=re.DOTALL)

    # Replace Footer Logo
    content = re.sub(r'<a href="index\.html" class="footer-logo">.*?</a>', footer_logo_html, content, flags=re.DOTALL)

    # Add Floating Phone
    if 'class="phone-float"' not in content:
        content = content.replace('<a href="https://wa.me/919999988888" class="whatsapp-float" target="_blank" aria-label="Chat with us on WhatsApp">', floating_phone)
        content = content.replace('<a href="https://wa.me/919999988888" class="whatsapp-float" target="_blank">', floating_phone)


    # Update Stats
    content = content.replace('data-target="10"', 'data-target="15"')
    content = content.replace('data-target="250"', 'data-target="1500"')
    content = content.replace('data-target="100"', 'data-target="350"')
    
    # Text fallback replacement for stats inside HTML text
    content = content.replace('<span class="years">10+</span>', '<span class="years">15+</span>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Global Replacements Done")
