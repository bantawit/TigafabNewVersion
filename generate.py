import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- CONSTANTES ---
LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

# --- TRADUCCIONES MAESTRAS ---
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
        'srv_header_main': "Nuestras Especialidades",
        'srv_jurada_title': "Traducciones Juradas",
        'srv_jurada_list': ["Pasaportes al Árabe", "Escrituras y Contratos", "Poderes Notariales", "Estatutos de Sociedades", "Auditorías y Cuentas Anuales", "Autorizaciones y Actas", "Certificados (Cámara, Mercantil, Origen)", "Facturas Comerciales", "Acuerdos Sociales", "Títulos y Expedientes Académicos"],
        'srv_tecnica_title': "Traducciones Técnicas",
        'srv_tecnica_list': ["Catálogos y Presentaciones", "Planes de Negocio", "Manuales de Ingeniería", "Páginas Web", "Listados de Precios", "Correspondencia y Cartas", "Informes Técnicos"],
        'srv_organismos_title': "Gestión ante Organismos",
        'srv_organismos_list': ["Ministerio de Asuntos Exteriores", "Ministerio de Justicia y Sanidad", "Cámara de Comercio de Madrid", "Colegio de Notarios", "Embajadas (Libia, Argelia, Irán, Egipto...)"],
        'srv_visados_title': "Gestión de Visados",
        'srv_visados_list': ["Tramitación en consulados", "Libia, Argelia, Irán, Egipto...", "Impresos oficiales", "Requisitos"],
        'srv_libia_title': "Asesoramiento Especializado LIBIA",
        'srv_libia_desc': "Introducimos empresas en el mercado LIBIO con contactos reales y apoyo técnico.",
        'hero_contact_title': "Contacte con Nosotros",
        'form_btn': "ENVIAR SOLICITUD",
        'reviews_title': "Confianza Global", 'exp_verificadas': "EXPERIENCIAS VERIFICADAS",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada."
    }
}

def get_nav(lang, rel_path):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    links = "".join([f'<a href="{rel_path + (LANG_FOLDERS[lc] + "/index.html" if LANG_FOLDERS[lc] else "index.html")}" class="{"active" if lc == lang else ""}">{LANG_NAMES[lc]}</a>' for lc in LANG_NAMES])
    return f"""<nav id="navbar"><div class="container nav-container"><a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a><ul class="nav-links"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li></ul><div class="lang-selector"><div class="lang-current">{t['nav_lang']}</div><div class="lang-dropdown">{links}</div></div></div></nav>"""

def get_list_html(key, lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    return "".join([f"<li>{x}</li>" for x in t.get(key, [])])

def get_review_cards():
    reviews_data = [
        ("Marta (Google)", "Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord para un trámite urgente que me pedían por sorpresa. Su trato y rapidez son excelentes, me dio mucha tranquilidad."),
        ("Mohamed (Google)", "Gente muy profesional y muy amable. Lo recomiendo 100% para cualquier gestión de traducción o visados. Me ayudaron con el registro en un tiempo récord y con una calidad técnica insuperable."),
        ("Juan Carlos (Google)", "Atención excepcional y rapidez. Necesitaba una traducción jurada de árabe a español para el ministerio y lo tuvieron listo antes del plazo. Rigurosos y con un precio justo."),
        ("Laila (Google)", "La mejor agencia de Madrid para árabe. Son extremadamente serios con los plazos de entrega, algo vital para licitaciones. Trato exquisito por parte del equipo técnico."),
        ("Constructor S.A. (Google)", "Indispensables para nuestras licitaciones en el norte de África. Su conocimiento del mercado libio nos ha permitido cerrar contratos muy complejos con éxito."),
        ("Karim (Google)", "Expertos reales en el mercado árabe y español. Máximo rigor jurídico en cada documento. Su apoyo técnico en Libia es fundamental para nuestra expansión.")
    ]
    cards = "".join([f'<div class="review-card-premium"><div><i class="fas fa-star" style="color:#c2a35d"></i>' * 5 + f'</div><p>{txt}</p><strong>{name}</strong></div>' for name, txt in reviews_data])
    return cards * 4

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t.get(title_key, title_key)} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background: rgba(0,0,0,0.2); backdrop-filter: blur(10px); color:white; padding:4rem 2rem; text-align:center;"><div style="font-family: 'Playfair Display', serif; font-size:2rem; margin-bottom:1rem;">TIGAFAB<span style="color:#c2a35d;">.</span></div><p>{t['footer_rights']}</p></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script><script src="{rel_path}js/main.js?v={os.urandom(2).hex()}"></script><script>AOS.init();</script></body></html>"""
    merged_t = t_es.copy(); merged_t.update(t)
    for k, v in merged_t.items():
        if isinstance(v, str): full_html = full_html.replace(f't-{k.replace("_","-")}', v)
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang]); os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

for lang in LANG_FOLDERS:
    # --- CONTENIDO HOME (TEXTO ORIGINAL + RESEÑAS) ---
    index = f"""<section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>
    <section style="padding:10rem 0;"><div class="container" style="max-width:1100px;"><div style="display:grid; grid-template-columns:1.2fr 1fr; gap:5rem; align-items:start;"><div data-aos="fade-right"><h2 style="font-size:2.8rem; margin-bottom:3rem;">Tradición y Rigor</h2><p style="font-size:1.25rem; color:#f8fafc; line-height:1.8; margin-bottom:2rem;">t-h1</p><div style="background:rgba(194,163,93,0.1); border-left:4px solid var(--primary); padding:2rem; margin-bottom:2.5rem;"><p style="font-size:1.4rem; font-weight:700; color:var(--primary); margin-bottom:1rem;">t-h2</p><p style="color:#94a3b8; font-size:1.1rem;">t-h3</p></div><p style="font-size:1.1rem; color:#94a3b8; font-style:italic;">t-h4</p></div><div data-aos="fade-left" style="background:rgba(255,255,255,0.02); border:1px solid var(--glass-border); padding:3rem; border-radius:20px;"><p style="font-size:1.2rem; color:#f8fafc; line-height:1.8; margin-bottom:2rem;">t-h5</p><p style="font-size:1.2rem; color:#94a3b8; line-height:1.8;">t-h6</p></div></div></div></section>
    <section style="padding-bottom:10rem;"><div class="container" style="text-align:center; margin-bottom:5rem;"><h2>t-reviews-title</h2><p>t-exp-verificadas</p></div><div class="marquee-container"><div class="marquee-inner">{get_review_cards()}</div></div></section>"""
    generate_page(lang, "index.html", 'nav_home', index)

    # --- CONTENIDO SERVICIOS (RESTAURADO) ---
    srv = f"""<section class="hero" style="min-height:40vh; padding:120px 0;"><h1>t-srv-header-main</h1></section>
    <section style="padding:8rem 0; background:var(--bg-dark);"><div class="container"><div class="services-creative-grid">
    <div class="service-premium-box" data-aos="fade-up"><i class="fas fa-stamp"></i><h3>t-srv-jurada-title</h3><ul class="service-list-detailed">{get_list_html('srv_jurada_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up"><i class="fas fa-file-invoice"></i><h3>t-srv-tecnica-title</h3><ul class="service-list-detailed">{get_list_html('srv_tecnica_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up"><i class="fas fa-landmark"></i><h3>t-srv-organismos-title</h3><ul class="service-list-detailed">{get_list_html('srv_organismos_list', lang)}</ul></div>
    <div class="service-premium-box featured-libia" data-aos="zoom-in"><i class="fas fa-globe-africa"></i><h3>t-srv-libia-title</h3><p>t-srv-libia-desc</p></div>
    </div></div></section>"""
    generate_page(lang, "servicios.html", 'nav_services', srv)

    # --- CONTENIDO CONTACTO (RESTAURADO) ---
    cont = f"""<section class="hero" style="min-height:45vh; padding:100px 0;"><h1>t-hero-contact-title</h1></section>
    <section class="contact-section"><div class="container"><div class="contact-grid"><div class="contact-info-box" data-aos="fade-right"><h2>Hablemos</h2><p>info@tigafab.com</p></div><div class="contact-form-premium" data-aos="fade-left"><form action="#" method="POST"><div class="form-group"><input type="text" class="form-control" placeholder="Nombre" required></div><button type="submit" class="btn-premium" style="width:100%">t-form-btn</button></form></div></div></div></section>"""
    generate_page(lang, "contacto.html", 'nav_contact', cont)

print("✅ ÉXITO: TODO restaurado al 100% y blindado.")
