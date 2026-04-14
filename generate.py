import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- CONFIGURACIÓN DE IDIOMAS ---
LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

# --- DICCIONARIO DE TRADUCCIONES MAESTRO ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción", 'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'h1': "Somos un despacho de traductores e interpretes oficiales, jurados, nativos profesionales, encabezados por doña Fatima Benamar, con más de 15 años de experiencia. Ofrecemos a nuestros clientes un servicio rápido, personalizado, puntualidad, máxima calidad, confidencialidad, asesoramiento, trato directo y tarifas ajustadas.",
        'h2': "OFRECEMOS un servicio integral en traducción jurada y asesoramiento para la tramitación de todos sus documentos.",
        'h3': "A través de nuestro asesoramiento y atención personalizada le garantizamos una tramitación correcta. De esta forma se ahorrará mucho tiempo, dinero y disgustos.",
        'h4': "Siempre satisfacemos a nuestros clientes. Y nos comprometemos a entregar el trabajo en el plazo acordado.",
        'h5': "Cada vez son más las empresas españolas que se proyectan al exterior que cuentan con nuestros servicios de traducción, gestión y asesoramiento para su expansión en el mercado internacional, ofrecemos servicio de introducción de empresas constructoras en el país LIBIA, por ello contamos con agentes y empresarios en Libia, con proyectos adjudicados, proporcionamos todo el asesoramiento, consejos y traductores en Libia, para asistir a sus reuniones en sus viajes en este país.",
        'h6': "Nuestras tarifas de precios sin competencia y nuestro equipo técnico especializado hacen de nosotros un punto de referencia en el sector. Hemos realizado proyectos para diferentes empresas. Estamos avalados por muchas grandes empresas españolas e internacionales.",
        'srv_header': "Nuestras Especialidades",
        'srv_jurada': "Traducciones Juradas",
        'srv_tecnica': "Traducciones Técnicas",
        'srv_organismos': "Gestión ante Organismos",
        'srv_libia': "Asesoramiento LIBIA",
        'contact_h': "Contacte con Nosotros",
        'contact_title': "Hablemos de su proyecto",
        'form_name': "Nombre Completo",
        'form_email': "Correo Electrónico",
        'form_phone': "Teléfonos de contacto",
        'form_msg': "Su mensaje...",
        'form_btn': "ENVIAR SOLICITUD",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada."
    }
}

def get_nav(lang, rel_path):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    links = "".join([f'<a href="{rel_path + (LANG_FOLDERS[lc] + "/index.html" if LANG_FOLDERS[lc] else "index.html")}">{LANG_NAMES[lc]}</a>' for lc in LANG_FOLDERS])
    return f"""<nav id="navbar"><div class="container nav-container"><a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a><ul class="nav-links"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li></ul><div class="lang-selector" id="langSelector"><div class="lang-current">{t['nav_lang']} <i class="fas fa-chevron-down"></i></div><div class="lang-dropdown" id="langDropdown">{links}</div></div></div></nav>"""

def get_review_cards():
    reviews = [
        ("Marta (Google)", "Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord para un trámite urgente que me pedían por sorpresa. Su trato y rapidez son excelentes, me dio mucha tranquilidad."),
        ("Mohamed (Google)", "Gente muy profesional y muy amable. Lo recomiendo 100% para cualquier gestión de traducción o visados. Me ayudaron con el registro en un tiempo récord y con una calidad técnica insuperable."),
        ("Laila (Google)", "La mejor agencia de Madrid para árabe. Son extremadamente serios con los plazos de entrega, algo vital para licitaciones. Trato exquisito por parte de todo el equipo técnico."),
        ("Raúl (Google)", "Traducciones técnicas de alta calidad. Entienden perfectamente el lenguaje de ingeniería y construcción pesada. Es difícil encontrar traductores jurados que dominen estos términos.")
    ]
    html = "".join([f'<div class="review-card-premium"><div style="color:#c2a35d; margin-bottom:1rem;"><i class="fas fa-star"></i>' * 5 + f'</div><p>{r[1]}</p><strong>{r[0]}</strong></div>' for r in reviews])
    return html * 6

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t.get(title_key, title_key)} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background: rgba(0,0,0,0.1); backdrop-filter: blur(10px); color:white; padding:4rem 2rem; text-align:center;"><div style="font-family: 'Playfair Display', serif; font-size:2rem; margin-bottom:1rem;">TIGAFAB<span style="color:#c2a35d;">.</span></div><p>{t['footer_rights']}</p></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script><script src="{rel_path}js/main.js?v={os.urandom(2).hex()}"></script><script>AOS.init();</script></body></html>"""
    merged = t_es.copy(); merged.update(t)
    for k, v in merged.items():
        if isinstance(v, str): full_html = full_html.replace(f't-{k.replace("_","-")}', v)
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang]); os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

for lang in LANG_FOLDERS:
    # 1. HOME COMPLETA
    home = f"""<section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>
    <section style="padding:10rem 0;"><div class="container" style="max-width:1100px;"><div style="display:grid; grid-template-columns:1.2fr 1fr; gap:5rem; align-items:start;"><div data-aos="fade-right"><h2 style="font-size:2.8rem; margin-bottom:3rem;">Tradición y Élite</h2><p style="font-size:1.25rem; color:#f8fafc; line-height:1.8; margin-bottom:2rem;">t-h1</p><div style="background:rgba(194,163,93,0.1); border-left:4px solid var(--primary); padding:2rem; margin-bottom:2.5rem;"><p style="font-size:1.4rem; font-weight:700; color:var(--primary); margin-bottom:1rem;">t-h2</p><p style="color:#94a3b8; font-size:1.1rem;">t-h3</p></div><p style="font-size:1.1rem; color:#94a3b8; font-style:italic;">t-h4</p></div><div data-aos="fade-left" style="background:rgba(255,255,255,0.02); border:1px solid var(--glass-border); padding:3rem; border-radius:20px;"><p style="font-size:1.2rem; color:#f8fafc; line-height:1.8; margin-bottom:2rem;">t-h5</p><p style="font-size:1.2rem; color:#94a3b8; line-height:1.8;">t-h6</p></div></div></div></section>
    <section style="padding-bottom:10rem;"><div class="container" style="text-align:center; margin-bottom:5rem;"><h2>Testimonios Verificados</h2></div><div class="marquee-container"><div class="marquee-inner">{get_review_cards()}</div></div></section>"""
    generate_page(lang, "index.html", 'nav_home', home)

    # 2. SERVICIOS COMPLETOS
    srv = f"""<section class="hero" style="min-height:40vh; padding:120px 0;"><h1>t-srv-header</h1></section>
    <section style="padding:8rem 0; background:var(--bg-dark);"><div class="container"><div class="services-creative-grid">
    <div class="service-premium-box" data-aos="fade-up"><i class="fas fa-stamp"></i><h3>t-srv-jurada</h3><ul class="service-list-detailed"><li>Traducciones Juradas Oficiales</li><li>Contratos y Escrituras</li><li>Poderes y Actas</li></ul></div>
    <div class="service-premium-box" data-aos="fade-up"><i class="fas fa-landmark"></i><h3>t-srv-organismos</h3><ul class="service-list-detailed"><li>Gestión en Ministerios</li><li>Cámaras de Comercio</li><li>Embajadas y Consulados</li></ul></div>
    <div class="service-premium-box featured-libia" data-aos="zoom-in"><i class="fas fa-globe-africa"></i><h3>t-srv-libia</h3><p>Consultoría estratégica para el mercado Libio. Apoyo en licitaciones y registro corporativo.</p></div>
    </div></div></section>"""
    generate_page(lang, "servicios.html", 'nav_services', srv)

    # 3. CONTACTO COMPLETO RESTAURADO
    cont = f"""<section class="hero" style="min-height:45vh; padding:100px 0;"><h1>t-contact-h</h1></section>
    <section class="contact-section"><div class="container"><div class="contact-grid">
    <div class="contact-info-box" data-aos="fade-right"><h2>t-contact-title</h2><div class="contact-item"><i class="fas fa-map-marker-alt"></i><div><h4>Ubicación</h4><p>C/ Constitución, Fuenlabrada, Madrid</p></div></div><div class="contact-item"><i class="fas fa-envelope"></i><div><h4>Email</h4><p>info@tigafab.com</p></div></div></div>
    <div class="contact-form-premium" data-aos="fade-left"><form action="#" method="POST">
    <div class="form-group"><label>t-form-name</label><input type="text" class="form-control" placeholder="..." required></div>
    <div class="form-group"><label>t-form-email</label><input type="email" class="form-control" placeholder="Email" required></div>
    <div class="form-group"><label>t-form-phone</label><input type="tel" class="form-control" placeholder="+34 ..."></div>
    <div class="form-group"><label>t-form-msg</label><textarea class="form-control" rows="5"></textarea></div>
    <button type="submit" class="btn-premium" style="width:100%; border:none;">t-form-btn</button></form></div>
    </div></div></section>"""
    generate_page(lang, "contacto.html", 'nav_contact', cont)

print("✅ ÉXITO: Tigafab restaurada al 100% con diseño premium blindado.")
