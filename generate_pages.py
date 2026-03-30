import os
import re

template_file = 'c:/Users/ADMIN/OneDrive/Desktop/SkyRise Builders/service-commercial.html'

with open(template_file, 'r', encoding='utf-8') as f:
    template_content = f.read()

pages_data = {
    'service-planning.html': {
        'title': 'Building Planning | SkyRise Builders',
        'bg_img': 'https://images.pexels.com/photos/1109541/pexels-photo-1109541.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'page_title': 'Building Planning',
        'page_subtitle': 'Expert architectural planning and structural blueprinting',
        'h2': 'Precision Planning for Your Structure',
        'p1': 'Comprehensive building planning ensures your project starts on the right foundation. We handle architectural CAD, 3D modeling, and strict compliance checking.',
        'features': [
            '<li><i class="fas fa-check-circle"></i> 3D Architecture Modeling</li>',
            '<li><i class="fas fa-check-circle"></i> Structural Blueprinting</li>',
            '<li><i class="fas fa-check-circle"></i> Zoning Approvals</li>',
            '<li><i class="fas fa-check-circle"></i> Cost Estimation</li>'
        ],
        'about_img': 'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=800',
        'work_desc': 'Our work in building planning combines innovative design with structural integrity. We collaborate closely with our clients and utilize advanced software to create detailed blueprints that minimize construction errors and optimize material usage.'
    },
    'service-maintenance.html': {
        'title': 'Maintenance Services | SkyRise Builders',
        'bg_img': 'https://images.pexels.com/photos/2219024/pexels-photo-2219024.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'page_title': 'Maintenance Services',
        'page_subtitle': 'Reliable building maintenance for long-lasting durability',
        'h2': 'Keep Your Property in Top Condition',
        'p1': 'Our routine and emergency maintenance services cover structural, electrical, and plumbing upkeep to preserve property value and safety.',
        'features': [
            '<li><i class="fas fa-check-circle"></i> Preventive Maintenance</li>',
            '<li><i class="fas fa-check-circle"></i> Immediate Repairs</li>',
            '<li><i class="fas fa-check-circle"></i> Safety Inspections</li>',
            '<li><i class="fas fa-check-circle"></i> Modern Upgrades</li>'
        ],
        'about_img': 'https://images.pexels.com/photos/1249611/pexels-photo-1249611.jpeg?auto=compress&cs=tinysrgb&w=800',
        'work_desc': 'Our work revolves around proactive inspections and swift resolutions. Teams of highly trained professionals are dispatched to diagnose issues, repair structural damages, and apply preventive measures ensuring every building we maintain functions seamlessly.'
    },
    'service-work.html': {
        'title': 'Our Work | SkyRise Builders',
        'bg_img': 'https://images.pexels.com/photos/585418/pexels-photo-585418.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'page_title': 'Our Work',
        'page_subtitle': 'Delivering excellence across all forms of construction',
        'h2': 'Comprehensive Construction Work',
        'p1': 'Beyond specialized niches, we handle diverse general construction, contracting, and civil works with an unwavering focus on quality.',
        'features': [
            '<li><i class="fas fa-check-circle"></i> Site Preparation</li>',
            '<li><i class="fas fa-check-circle"></i> Earthworks & Foundations</li>',
            '<li><i class="fas fa-check-circle"></i> Concrete Solutions</li>',
            '<li><i class="fas fa-check-circle"></i> Project Management</li>'
        ],
        'about_img': 'https://images.pexels.com/photos/1216589/pexels-photo-1216589.jpeg?auto=compress&cs=tinysrgb&w=800',
        'work_desc': 'Our work spans the entire lifecycle of civil engineering and construction. We oversee on-site coordination, adhere to rigid safety protocols, and employ cutting-edge machinery to execute structural foundations and earthworks precisely as engineered.'
    }
}

for filename, data in pages_data.items():
    content = template_content
    content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', content)
    content = re.sub(r'background: linear-gradient[^;]+;', f"background: linear-gradient(rgba(15,23,42,0.8), rgba(15,23,42,0.8)), url('{data['bg_img']}') center/cover;", content)
    content = re.sub(r'<h1 class="page-title">.*?</h1>', f'<h1 class="page-title">{data["page_title"]}</h1>', content)
    content = re.sub(r'<h1 class="page-title">.*?</h1>\s*<p>.*?</p>', f'<h1 class="page-title">{data["page_title"]}</h1>\n            <p>{data["page_subtitle"]}</p>', content)
    content = re.sub(r'<h2>.*?</h2>', f'<h2>{data["h2"]}</h2>', content)
    
    # Replace the P paragraph
    content = re.sub(r'<h2>.*?</h2>\s*<p>.*?</p>', f'<h2>{data["h2"]}</h2>\n                <p>{data["p1"]}</p>\n                <p class="work-desc" style="margin-top: 15px; color: var(--text-dark); font-weight: 500;"><strong>About Our Work:</strong> {data["work_desc"]}</p>', content)
    
    # Replace features
    features_html = '\n                    '.join(data["features"])
    content = re.sub(r'<ul class="features-list"[^>]*>.*?</ul>', f'<ul class="features-list" style="margin-top: 20px;">\n                    {features_html}\n                </ul>', content, flags=re.DOTALL)
    
    # Replace about image
    content = re.sub(r'<img src="https://images.pexels.com/photos/[0-9]+/pexels-photo-[0-9]+\.jpeg\?auto=compress&cs=tinysrgb&w=800"[^>]*>', f'<img src="{data["about_img"]}" alt="{data["page_title"]}" style="border-radius: 8px; box-shadow: var(--shadow-lg);">', content)

    with open(f'c:/Users/ADMIN/OneDrive/Desktop/SkyRise Builders/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Created {filename}")

# Now inject work_desc into existing pages if not already there
existing_pages = {
    'service-residential.html': 'Our work in residential projects is focused on bringing customized visions to life. We utilize sustainable materials and collaborate with skilled artisans to craft unique living spaces that are structurally sound and aesthetically warm.',
    'service-commercial.html': 'Our work in commercial construction involves rigorous planning, state-of-the-art technological implementation, and comprehensive project management to ensure minimal disruption to your timeline, setting a gold standard in the industry.',
    'service-renovation.html': 'Our work revamps outdated structures by reinforcing their core while modernizing their exteriors and interiors. We deploy specialized demolition and retrofitting teams to seamlessly transition old properties into brilliant modern commodities.',
    'service-interior.html': 'Our work in interior design blends functionality with bespoke elegance. From custom carpentry to advanced lighting installations, our team manages every detail of the fit-out to deliver exceptional, ready-to-use spaces.'
}

for filename, work_desc in existing_pages.items():
    filepath = f'c:/Users/ADMIN/OneDrive/Desktop/SkyRise Builders/{filename}'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'class="work-desc"' not in content:
        # Inject after the first paragraph in about-content
        # We find: <h2>.*?</h2>\s*<p>.*?</p>
        replacement = r'\g<0>\n                <p class="work-desc" style="margin-top: 15px; color: var(--text-dark); font-weight: 500;"><strong>About Our Work:</strong> ' + work_desc + r'</p>'
        new_content = re.sub(r'(<h2>.*?</h2>\s*<p>.*?</p>)', replacement, content, count=1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
