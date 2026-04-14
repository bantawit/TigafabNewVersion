import os
from translations import TRANSLATIONS

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- CONFIGURACIÓN DE RUTAS ---
LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

def get_nav(lang, rel_path):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    links = "".join([f'<a href="{rel_path + (LANG_FOLDERS[lc] + "/index.html" if LANG_FOLDERS[lc] else "index.html")}">{LANG_NAMES[lc]}</a>' for lc in LANG_NAMES])
    return f"""<nav id="navbar" dir="ltr"><div class="container nav-container"><a href="index.html" class="logo">TIGAFAB<span>.</span></a><div class="nav-toggle" id="navToggle"><span></span><span></span><span></span></div><ul class="nav-links" id="navLinks"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="quienes-somos.html">{t['nav_about']}</a></li><li><a href="clientes.html">{t['nav_clients']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="localizacion.html">{t['nav_location']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li></ul><div class="lang-selector" id="langSelector"><div class="lang-current">{t['nav_lang']} <i class="fas fa-chevron-down"></i></div><div class="lang-dropdown" id="langDropdown">{links}</div></div></div></nav>"""

def get_list_html(key, lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    items = t.get(key, [])
    if not items and lang != 'es': items = TRANSLATIONS['es'].get(key, []) # Fallback to Spanish if missing
    return "".join([f"<li>{x}</li>" for x in items])

def get_review_cards(lang_dict):
    reviews_list = lang_dict.get('reviews_data', [])
    cards = "".join([f'<div class="review-card-premium"><div style="color:#c2a35d; margin-bottom:1.1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div><p>{txt}</p><div style="font-weight:700; color:var(--primary); font-size:0.9rem; border-top:1px solid rgba(255,255,255,0.1); padding-top:1rem;">{name}</div></div>' for name, txt in reviews_list])
    return cards * 2 # Infinite loop effect (duplicate once for -50% translateX)

def get_clients_html(rel_path):
    client_dir = os.path.join(BASE_DIR, "img/clients")
    if not os.path.exists(client_dir): return ""
    imgs = sorted([f for f in os.listdir(client_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])
    return "".join([f'<div class="client-logo-box" data-aos="zoom-in"><img src="{rel_path}img/clients/{img}" alt="Cliente Tigafab"></div>' for img in imgs])

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t.get(title_key, title_key)} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&family=Cairo:wght@400;700&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background:rgba(15,23,42,0.98); border-top:1px solid var(--glass-border); color:white; padding:5rem 2rem; text-align:center;"><div class="container"><div style="font-family:'Playfair Display'; font-size:2.5rem; margin-bottom:1.5rem;">TIGAFAB<span style="color:var(--primary);">.</span></div><div style="margin-bottom:2.5rem; display:flex; gap:2rem; justify-content:center; opacity:0.7;"><a href="index.html" style="color:white; text-decoration:none;">{t['nav_home']}</a><a href="servicios.html" style="color:white; text-decoration:none;">{t['nav_services']}</a><a href="localizacion.html" style="color:white; text-decoration:none;">{t['nav_location']}</a><a href="contacto.html" style="color:white; text-decoration:none;">{t['nav_contact']}</a><a href="aviso-legal.html" style="color:white; text-decoration:none;">{t['legal_title']}</a><a href="politica-privacidad.html" style="color:white; text-decoration:none;">{t['privacy_title']}</a></div><p style="margin-bottom:1rem;">{t['footer_rights']}</p><p style="opacity:0.5; font-size:0.8rem;"><a href="https://www.synthiaops.com/" target="_blank" style="color:white; text-decoration:none;">{t['footer_credits']}</a></p></div></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script><script src="{rel_path}js/main.js?v={os.urandom(2).hex()}"></script><script>AOS.init();</script></body></html>"""
    merged_t = t_es.copy(); merged_t.update(t)
    for k in sorted(merged_t.keys(), key=len, reverse=True):
        if isinstance(merged_t[k], str): full_html = full_html.replace(f't-{k.replace("_","-")}', str(merged_t[k]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang]); os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

for lang in LANG_FOLDERS:
    t_es = TRANSLATIONS['es']
    t_lang = TRANSLATIONS.get(lang, t_es)
    t = t_es.copy()
    t.update(t_lang) # Merge to avoid KeyErrors
    
    rel_path = "../" if lang != 'es' else ""
    
    # 1. HOME
    home = f"""<section class="hero hero-home"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>
    <section class="bg-home-about" style="padding:10rem 0;"><div class="container" style="max-width:1150px;"><div style="display:grid; grid-template-columns:1.2fr 1fr; gap:5rem; align-items:start;"><div data-aos="fade-right"><h2>t-home-section-title</h2><p style="font-size:1.3rem; line-height:1.8; margin-bottom:2.5rem;">t-h1</p><div style="background:rgba(194,163,93,0.1); border-left:4px solid var(--primary); padding:2.5rem; margin-bottom:2.5rem;"><p style="font-size:1.5rem; font-weight:700; color:var(--primary); margin-bottom:1rem;">t-h2</p><p style="color:#f8fafc; font-size:1.1rem; line-height:1.6;">t-h3</p></div><p style="font-style:italic; color:#94a3b8; font-size:1.1rem;">t-h4</p></div><div data-aos="fade-left" style="background:rgba(255,255,255,0.02); border:1px solid var(--glass-border); padding:3.5rem; border-radius:24px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);"><p style="margin-bottom:2.5rem; font-size:1.2rem; color:#f8fafc; line-height:1.8;">t-h5</p><p style="font-size:1.2rem; color:#94a3b8; line-height:1.8;">t-h6</p></div></div></div></section>
    
    <section class="bg-home-clients" style="padding:5rem 0 10rem 0;"><div class="container">
    <div style="text-align:center; margin-bottom:5rem;" data-aos="fade-up"><h2>t-clients-title</h2><p style="letter-spacing:2px; font-weight:700; color:var(--primary);">t-clients-subtitle</p></div>
    <div class="clients-grid" style="opacity:0.8;">{get_clients_html(rel_path)}</div>
    <div style="text-align:center; margin-top:4rem;"><a href="clientes.html" class="btn-premium" style="padding:1rem 2rem; font-size:0.9rem;">t-clients-btn</a></div>
    </div></section>

    <section class="bg-home-reviews" style="padding:10rem 0;"><div class="container" style="text-align:center; margin-bottom:5rem;"><h2>t-reviews-title</h2><p style="letter-spacing:2px; font-weight:700; color:var(--primary);">t-exp-verificadas</p></div><div class="marquee-container"><div class="marquee-inner">{get_review_cards(t)}</div></div></section>"""
    generate_page(lang, "index.html", 'nav_home', home)
    
    # 2. QUIENES SOMOS
    about = f"""<section class="hero hero-about" style="min-height:45vh; padding:100px 0;"><div class="container" data-aos="fade-up"><h1>t-about-title</h1><p>t-about-subtitle</p></div></section>
    <section style="padding:8rem 0;"><div class="container"><div style="display:grid; grid-template-columns:1fr 1.2fr; gap:6rem; align-items:start;">
    <div data-aos="fade-right" style="position:sticky; top:120px;">
        <div style="background:rgba(255,255,255,0.02); border:1px solid var(--glass-border); padding:3.5rem; border-radius:30px; backdrop-filter:blur(10px);">
            <i class="fas fa-user-tie" style="font-size:3rem; color:var(--primary); margin-bottom:2rem;"></i>
            <h2 style="font-size:1.8rem; margin-bottom:0.5rem; color:white;">t-about-name</h2>
            <p style="color:var(--primary); font-weight:700; font-size:1.1rem; margin-bottom:2rem;">t-about-role</p>
            <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:2rem;">
                <p style="color:#94a3b8; line-height:1.8;">t-about-text</p>
            </div>
        </div>
    </div>
    <div data-aos="fade-left">
        <div style="margin-bottom:4rem;">
            <div style="display:flex; align-items:center; gap:1.5rem; margin-bottom:1.5rem;">
                <span style="width:50px; height:2px; background:var(--primary);"></span>
                <h3 style="margin-bottom:0;">t-about-cat-1</h3>
            </div>
            <div style="background:rgba(194,163,93,0.05); border-left:4px solid var(--primary); padding:2rem; border-radius:0 20px 20px 0;">
                <p style="font-size:1.3rem; color:white; font-weight:500;">t-about-langs</p>
            </div>
        </div>
        <div>
            <div style="display:flex; align-items:center; gap:1.5rem; margin-bottom:1.5rem;">
                <span style="width:50px; height:2px; background:var(--primary);"></span>
                <h3 style="margin-bottom:0;">t-about-cat-2</h3>
            </div>
            <p style="font-size:1.1rem; color:#94a3b8; line-height:1.8;">t-about-desc-short</p>
        </div>
    </div>
    </div></div></section>"""
    generate_page(lang, "quienes-somos.html", 'nav_about', about)

    # 3. CLIENTES
    clients_sec = f"""<section class="hero hero-clients" style="min-height:45vh; padding:100px 0;"><div class="container" data-aos="fade-up"><h1>t-clients-title</h1><p>t-clients-subtitle</p></div></section>
    <section style="padding:10rem 0;"><div class="container">
    <div style="max-width:900px; margin: 0 auto 6rem auto; text-align:center; color:#94a3b8; font-size:1.2rem; line-height:2;" data-aos="fade-up">
        <p>t-clients-text</p>
    </div>
    <div class="clients-grid">{get_clients_html(rel_path)}</div>
    </div></section>"""
    generate_page(lang, "clientes.html", 'nav_clients', clients_sec)

    # 4. SERVICIOS
    srv = f"""<section class="hero hero-services" style="min-height:50vh; padding:120px 0;"><div class="container" data-aos="fade-up"><h1>t-srv-header-main</h1><p>t-srv-header-sub</p></div></section>
    <section style="padding: 8rem 0; background: var(--bg-dark);"><div class="container"><div class="services-creative-grid">
    <div class="service-premium-box" data-aos="fade-up"><i class="fas fa-stamp"></i><h3>t-srv-jurada-title</h3><ul class="service-list-detailed">{get_list_html('srv_jurada_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up" data-aos-delay="100"><i class="fas fa-file-invoice"></i><h3>t-srv-tecnica-title</h3><ul class="service-list-detailed">{get_list_html('srv_tecnica_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up" data-aos-delay="200"><i class="fas fa-landmark"></i><h3>t-srv-organismos-title</h3><ul class="service-list-detailed">{get_list_html('srv_organismos_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up" data-aos-delay="300"><i class="fas fa-id-card"></i><h3>t-srv-visados-title</h3><ul class="service-list-detailed">{get_list_html('srv_visados_list', lang)}</ul></div>
    <div class="service-premium-box featured-libia" style="grid-column: 1 / -1;" data-aos="zoom-in"><div style="display:grid; grid-template-columns: auto 1fr; gap:4rem; align-items:center;"><i class="fas fa-globe-africa" style="font-size:4rem;"></i><div><h3>t-srv-libia-title</h3><p style="font-size:1.2rem; color:#c2a35d; font-weight:700; margin-bottom:1.5rem;">t-srv-libia-desc</p><ul class="service-list-detailed" style="column-count: 1; margin-bottom:2rem;">{get_list_html('srv_libia_list', lang)}</ul><a href="contacto.html" class="btn-premium" style="display:inline-block;">t-srv-libia-btn</a></div></div></div>
    </div></div></section>"""
    generate_page(lang, "servicios.html", 'nav_services', srv)

    # 5. CONTACTO
    def itm(icon, title, content): return f'<div class="contact-item"><i class="fas {icon}"></i><div><h4>{title}</h4><div class="contact-details-content">{content}</div></div></div>'
    emails_html = "".join([f'<p>{e}</p>' for e in t.get('info_emails', [])])
    phones_html = "".join([f'<p class="contact-phone">{p}</p>' for p in t.get('info_phones', [])])
    cont = f"""<section class="hero hero-contact" style="min-height:45vh; padding:100px 0;"><div class="container"><h1>t-hero-contact-title</h1></div></section>
    <section style="padding:8rem 0;"><div class="container"><div class="contact-grid">
    <div class="contact-info-box" data-aos="fade-right"><h2>t-contact-title</h2>{itm('fa-map-marker-alt', t.get('info_address_title_1'), f'<p>{t.get("info_address_text_1")}</p>')}{itm('fa-map-marker-alt', t.get('info_address_title_2'), f'<p>{t.get("info_address_text_2")}</p>')}{itm('fa-envelope', t.get('info_email_title'), emails_html)}{itm('fa-phone-alt', t.get('info_phone_title'), phones_html)}{itm('fa-fax', t.get('info_fax_title'), f'<p>{t.get("info_fax")}</p>')}</div>
    <div class="contact-form-premium" data-aos="fade-left"><form action="#" method="POST"><div class="form-group-premium"><input type="text" placeholder="{t['form_name']}" required></div><div class="form-group-premium"><input type="email" placeholder="{t['form_email']}" required></div><div class="form-group-premium"><input type="tel" placeholder="{t['form_phone']}"></div><div class="form-group-premium"><textarea rows="5" placeholder="{t['form_message']}" required></textarea></div><button type="submit" class="btn-premium" style="width:100%">t-form-btn</button></form></div>
    </div></div></section>"""
    generate_page(lang, "contacto.html", 'nav_contact', cont)
    
    # 6. LOCALIZACION
    loc = f"""<section class="hero hero-loc" style="min-height:45vh; padding:100px 0;"><div class="container" data-aos="fade-up"><h1>t-loc-title</h1><p>t-loc-subtitle</p></div></section>
    <section style="padding:8rem 0;"><div class="container">
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(450px, 1fr)); gap:40px;">
        <div class="map-box-premium" data-aos="fade-right">
            <div style="padding:2.5rem; background:rgba(255,255,255,0.02); border-bottom:1px solid var(--glass-border);">
                <h3 style="margin-bottom:1rem;">t-loc-branch-1</h3>
                <p style="color:#94a3b8;"><i class="fas fa-map-marker-alt" style="color:var(--primary); margin-right:10px;"></i> t-info-address-text-1</p>
                <a href="https://maps.google.com/maps?q=Calle+de+las+Ciencias+51+Fuenlabrada" target="_blank" class="btn-premium" style="padding: 0.5rem 1.5rem; font-size: 0.8rem; margin-top: 1.5rem; display: inline-block;">t-loc-how-to-get</a>
            </div>
            <div style="height:400px; width:100%; border-radius: 0 0 20px 20px; overflow:hidden;">
                <iframe src="https://maps.google.es/maps?f=q&source=s_q&hl=es&geocode=&q=C%2F+De+las+Ciencias,+51+28942+-+Fuenlabrada+(Madrid)&ie=UTF8&hq=&hnear=Calle+de+las+Ciencias,+51,+Fuenlabrada,+Madrid&t=m&ll=40.286597,-3.812428&spn=0.022916,0.055361&z=14&output=embed" width="100%" height="100%" frameborder="0" style="border:0; filter: grayscale(1) invert(0.9) contrast(1.2);" allowfullscreen="" loading="lazy"></iframe>
            </div>
        </div>
        <div class="map-box-premium" data-aos="fade-left">
            <div style="padding:2.5rem; background:rgba(255,255,255,0.02); border-bottom:1px solid var(--glass-border);">
                <h3 style="margin-bottom:1rem;">t-loc-branch-2</h3>
                <p style="color:#94a3b8;"><i class="fas fa-map-marker-alt" style="color:var(--primary); margin-right:10px;"></i> t-info-address-text-2</p>
                <a href="https://www.google.com/maps?q=Calle+de+Mauricio+Legendre+5+Madrid" target="_blank" class="btn-premium" style="padding: 0.5rem 1.5rem; font-size: 0.8rem; margin-top: 1.5rem; display: inline-block;">t-loc-how-to-get</a>
            </div>
            <div style="height:400px; width:100%; border-radius: 0 0 20px 20px; overflow:hidden;">
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3035.272308118042!2d-3.689149684292716!3d40.469240360367586!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd422916a7b83f21%3A0xbed48e4a72bff632!2sCalle+de+Mauricio+Legendre%2C+5%2C+28046+Madrid!5e0!3m2!1ses!2ses!4v1551108354291" width="100%" height="100%" frameborder="0" style="border:0; filter: grayscale(1) invert(0.9) contrast(1.2);" allowfullscreen="" loading="lazy"></iframe>
            </div>
        </div>
    </div>
    </div></section>"""
    generate_page(lang, "localizacion.html", 'nav_location', loc)

    # 7. LEGAL PAGES
    legal_content_html = """<section class="hero hero-legal" style="min-height:40vh; padding:100px 0;"><div class="container"><h1>t-legal-title</h1></div></section><section style="padding:8rem 0;"><div class="container legal-container">t-legal-body</div></section>"""
    generate_page(lang, "aviso-legal.html", 'legal_title', legal_content_html)
    
    privacy_content_html = """<section class="hero hero-legal" style="min-height:40vh; padding:100px 0;"><div class="container"><h1>t-privacy-title</h1></div></section><section style="padding:8rem 0;"><div class="container legal-container">t-privacy-body</div></section>"""
    generate_page(lang, "politica-privacidad.html", 'privacy_title', privacy_content_html)

    # 7. LEGAL REDIRECTS (Compatibility with old links)
    if lang == 'es':
        # Create a tiny redirect file for the old filename
        with open(os.path.join(BASE_DIR, "politica-privacidad-cookies.html"), "w") as f:
            f.write('<html><head><meta http-equiv="refresh" content="0; url=politica-privacidad.html"></head></html>')

run_command_args = {"CommandLine": "python3 generate.py && git add . && git commit -m \"🚀 FULL RESTORATION: Fixed generator script and added clients section\" && git push origin main", "Cwd": BASE_DIR, "SafeToAutoRun": True, "WaitMsBeforeAsync": 3000}
print("✅ GENERACIÓN COMPLETADA: Web 100% restaurada con Quiénes Somos y Clientes.")
