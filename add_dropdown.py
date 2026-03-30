import os
import glob
import re

html_files = glob.glob('c:/Users/ADMIN/OneDrive/Desktop/SkyRise Builders/*.html')

dropdown_html = """<li class="dropdown">
                        <a href="services.html" class="nav-link {active_class} dropbtn">Services <i class="fas fa-chevron-down" style="font-size: 0.8rem;"></i></a>
                        <div class="dropdown-content">
                            <a href="service-residential.html">Residential Construction</a>
                            <a href="service-commercial.html">Commercial Construction</a>
                            <a href="service-renovation.html">Building Renovation</a>
                            <a href="service-interior.html">Interior</a>
                            <a href="service-planning.html">Building Planning</a>
                            <a href="service-maintenance.html">Maintenance Services</a>
                            <a href="service-work.html">Work</a>
                        </div>
                    </li>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace matching <li>...Services...</li>
    # Pattern to match: <li><a href="services.html" class="nav-link">Services</a></li>
    # Or with "nav-link active"
    
    # Let's find if it has 'active' class
    has_active = 'href="services.html" class="nav-link active"' in content
    
    # Create the replacement text
    replacement = dropdown_html.replace('{active_class}', 'active' if has_active else '')
    
    # Use re.sub to find the existing services li wrapper
    # We should match: <li>\s*<a href="services.html"[^>]*>Services</a>\s*</li>
    # Wait, some lines might have <li><a href="services.html" class="nav-link">Services</a></li>
    pattern = r'<li>\s*<a\s+href="services\.html"\s+class="nav-link(?:\s+active)?"[^>]*>Services</a>\s*</li>'
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, replacement, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}")
    else:
        print(f"No match found in {os.path.basename(file_path)} (maybe already updated?)")
