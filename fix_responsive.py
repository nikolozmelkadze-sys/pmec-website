import re

def fix():
    # 1. Fix guide.html
    with open('guide.html', 'r', encoding='utf-8') as f:
        guide = f.read()
    
    # Remove chapter mentions
    guide = re.sub(r' He is an active member of the PMI.*?project management\.', '', guide)
    guide = guide.replace('; PMI® Tbilisi Chapter Member', '')
    
    with open('guide.html', 'w', encoding='utf-8') as f:
        f.write(guide)
        
    # 2. Fix report.md
    with open('report.md', 'r', encoding='utf-8') as f:
        report = f.read()
    
    report = re.sub(r' He is an active member of the PMI.*?project management\.', '', report)
    report = report.replace('; PMI® Tbilisi Chapter Member', '')
    
    with open('report.md', 'w', encoding='utf-8') as f:
        f.write(report)
        
    # 3. Enhance mobile responsiveness in index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    css_enhancement = """
    /* ─── MOBILE ENHANCEMENTS ───────────────────────────── */
    html, body { overflow-x: hidden; width: 100%; }
    img { max-width: 100%; height: auto; }
    @media (max-width: 480px) {
      .form-iframe-wrap { padding: 16px !important; }
      .hero { padding-top: 32px !important; }
      .nav-logo-wrap img { height: 60px !important; }
      .lang-switcher { margin-left: 10px; }
    }
    """
    
    if "/* ─── MOBILE ENHANCEMENTS ───────────────────────────── */" not in html:
        html = html.replace('/* ─── BILINGUAL SWITCHER UI ───────────────────────────── */', css_enhancement + '\n    /* ─── BILINGUAL SWITCHER UI ───────────────────────────── */')
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
            
    print("Fixes applied successfully.")

if __name__ == "__main__":
    fix()
