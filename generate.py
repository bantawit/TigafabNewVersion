import os
from translations import TRANSLATIONS, REVIEWS_DATA

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- CONFIGURACIÓN DE RUTAS ---
LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

def get_nav(lang, rel_path):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    links = "".join([f'<a href="{rel_path + (LANG_FOLDERS[lc] + "/index.html" if LANG_FOLDERS[lc] else "index.html")}">{LANG_NAMES[lc]}</a>' for lc in LANG_NAMES])
    return f"""<nav id="navbar" dir="ltr"><div class="container nav-container"><a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a><ul class="nav-links"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li></ul><div class="lang-selector" id="langSelector"><div class="lang-current">{t['nav_lang']} <i class="fas fa-chevron-down"></i></div><div class="lang-dropdown" id="langDropdown">{links}</div></div></div></nav>"""

def get_list_html(key, lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    items = t.get(key, [])
    if not items and lang != 'es': items = TRANSLATIONS['es'].get(key, []) # Fallback to Spanish if missing
    return "".join([f"<li>{x}</li>" for x in items])

def get_review_cards():
    cards = "".join([f'<div class="review-card-premium"><div style="color:#c2a35d; margin-bottom:1.1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div><p style="margin-bottom:1.5rem;">{txt}</p><div style="font-weight:700; color:var(--primary); font-size:0.9rem; border-top:1px solid rgba(255,255,255,0.1); padding-top:1rem;">{name}</div></div>' for name, txt in REVIEWS_DATA])
    return cards * 4 # Infinite loop effect

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t.get(title_key, title_key)} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&family=Cairo:wght@400;700&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background:rgba(15,23,42,0.98); border-top:1px solid var(--glass-border); color:white; padding:5rem 2rem; text-align:center;"><div class="container"><div style="font-family:'Playfair Display'; font-size:2.5rem; margin-bottom:1.5rem;">TIGAFAB<span style="color:var(--primary);">.</span></div><div style="margin-bottom:2.5rem; display:flex; gap:2rem; justify-content:center; opacity:0.7;"><a href="index.html" style="color:white; text-decoration:none;">{t['nav_home']}</a><a href="servicios.html" style="color:white; text-decoration:none;">{t['nav_services']}</a><a href="contacto.html" style="color:white; text-decoration:none;">{t['nav_contact']}</a><a href="aviso-legal.html" style="color:white; text-decoration:none;">{t['legal_title']}</a></div><p>{t['footer_rights']}</p></div></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script><script src="{rel_path}js/main.js?v={os.urandom(2).hex()}"></script><script>AOS.init();</script></body></html>"""
    merged_t = t_es.copy(); merged_t.update(t)
    for k in sorted(merged_t.keys(), key=len, reverse=True):
        if isinstance(merged_t[k], str): full_html = full_html.replace(f't-{k.replace("_","-")}', str(merged_t[k]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang]); os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

for lang in LANG_FOLDERS:
    # 1. HOME
    home = f"""<section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>
    <section style="padding:10rem 0;"><div class="container" style="max-width:1150px;"><div style="display:grid; grid-template-columns:1.2fr 1fr; gap:5rem; align-items:start;"><div data-aos="fade-right"><h2>Tradición y Rigor</h2><p style="font-size:1.3rem; line-height:1.8; margin-bottom:2.5rem;">t-h1</p><div style="background:rgba(194,163,93,0.1); border-left:4px solid var(--primary); padding:2.5rem; margin-bottom:2.5rem;"><p style="font-size:1.5rem; font-weight:700; color:var(--primary); margin-bottom:1rem;">t-h2</p><p style="color:#f8fafc; font-size:1.1rem; line-height:1.6;">t-h3</p></div><p style="font-style:italic; color:#94a3b8; font-size:1.1rem;">t-h4</p></div><div data-aos="fade-left" style="background:rgba(255,255,255,0.02); border:1px solid var(--glass-border); padding:3.5rem; border-radius:24px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);"><p style="margin-bottom:2.5rem; font-size:1.2rem; color:#f8fafc; line-height:1.8;">t-h5</p><p style="font-size:1.2rem; color:#94a3b8; line-height:1.8;">t-h6</p></div></div></div></section>
    <section style="padding-bottom:10rem;"><div class="container" style="text-align:center; margin-bottom:5rem;"><h2>t-reviews-title</h2><p style="letter-spacing:2px; font-weight:700; color:var(--primary);">t-exp-verificadas</p></div><div class="marquee-container"><div class="marquee-inner">{get_review_cards()}</div></div></section>"""
    generate_page(lang, "index.html", 'nav_home', home)
    
    # 2. SERVICIOS (TODOS LOS BLOQUES ACTIVOS)
    srv = f"""<section class="hero" style="min-height:50vh; padding:120px 0;"><div class="container" data-aos="fade-up"><h1>t-srv-header-main</h1><p>t-srv-header-sub</p></div></section>
    <section style="padding: 8rem 0; background: var(--bg-dark);"><div class="container"><div class="services-creative-grid">
    <div class="service-premium-box" data-aos="fade-up"><i class="fas fa-stamp"></i><h3>t-srv-jurada-title</h3><ul class="service-list-detailed">{get_list_html('srv_jurada_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up" data-aos-delay="100"><i class="fas fa-file-invoice"></i><h3>t-srv-tecnica-title</h3><ul class="service-list-detailed">{get_list_html('srv_tecnica_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up" data-aos-delay="200"><i class="fas fa-landmark"></i><h3>t-srv-organismos-title</h3><ul class="service-list-detailed">{get_list_html('srv_organismos_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up" data-aos-delay="300"><i class="fas fa-id-card"></i><h3>t-srv-visados-title</h3><ul class="service-list-detailed">{get_list_html('srv_visados_list', lang)}</ul></div>
    <div class="service-premium-box featured-libia" style="grid-column: 1 / -1;" data-aos="zoom-in"><div style="display:grid; grid-template-columns: auto 1fr; gap:4rem; align-items:center;"><i class="fas fa-globe-africa" style="font-size:4rem;"></i><div><h3>t-srv-libia-title</h3><p style="font-size:1.2rem; color:#f8fafc; line-height:1.8;">t-srv-libia-desc</p><a href="contacto.html" class="btn-premium" style="display:inline-block; margin-top:2rem;">t-srv-libia-btn</a></div></div></div>
    </div></div></section>"""
    generate_page(lang, "servicios.html", 'nav_services', srv)
    
    # 3. CONTACTO
    cont = f"""<section class="hero" style="min-height:45vh; padding:100px 0;"><div class="container"><h1>t-hero-contact-title</h1></div></section>
    <section style="padding:8rem 0;"><div class="container"><div class="contact-grid" dir="ltr">
    <div class="contact-info-box" data-aos="fade-right"><h2>t-contact-title</h2><div class="contact-item"><i class="fas fa-map-marker-alt"></i><div><h4>t-info-address-title</h4><p>t-info-address-text</p></div></div><div class="contact-item"><i class="fas fa-envelope"></i><div><h4>t-info-email-title</h4><p>info@tigafab.com</p></div></div><div class="contact-item"><i class="fas fa-phone-alt"></i><div><h4>t-info-phone-title</h4><p class="contact-phone">+34 91 606 20 20</p></div></div></div>
    <div class="contact-form-premium" data-aos="fade-left"><form action="#" method="POST"><button type="submit" class="btn-premium" style="width:100%">t-form-btn</button></form></div>
    </div></div></section>"""
    generate_page(lang, "contacto.html", 'nav_contact', cont)
    
    # 4. LEGAL
    legal = """<section class="hero" style="min-height:40vh; padding:100px 0;"><div class="container"><h1>t-legal-title</h1></div></section><section style="padding:8rem 0;"><div class="container" style="max-width:800px;"><p>t-privacy-title</p><p>Documentación legal completa de Tigafab S.L.</p></div></section>"""
    generate_page(lang, "aviso-legal.html", 'legal_title', legal)

print("✅ GENERACIÓN COMPLETADA: Contenido separado de la lógica. Web 100% restaurada.")
