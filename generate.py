import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- CONSTANTES ---
LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

# --- DICCIONARIO MAESTRO COMPLETO ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción",
        'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        # TEXTO ORIGINAL CLIENTE
        'h1': "Somos un despacho de traductores e interpretes oficiales, jurados, nativos profesionales, encabezados por doña Fatima Benamar, con más de 15 años de experiencia. Ofrecemos a nuestros clientes un servicio rápido, personalizado, puntualidad, máxima calidad, confidencialidad, asesoramiento, trato directo y tarifas ajustadas.",
        'h2': "OFRECEMOS un servicio integral en traducción jurada y asesoramiento para la tramitación de todos sus documentos.",
        'h3': "A través de nuestro asesoramiento y atención personalizada le garantizamos una tramitación correcta. De esta forma se ahorrará mucho tiempo, dinero y disgustos.",
        'h4': "Siempre satisfacemos a nuestros clientes. Y nos comprometemos a entregar el trabajo en el plazo acordado.",
        'h5': "Cada vez son más las empresas españolas que se proyectan al exterior que cuentan con nuestros servicios de traducción, gestión y asesoramiento para su expansión en el mercado internacional, ofrecemos servicio de introducción de empresas constructoras en el país LIBIA, por ello contamos con agentes y empresarios en Libia, con proyectos adjudicados, proporcionamos todo el asesoramiento, consejos y traductores en Libia, para asistir a sus reuniones en sus viajes en este país.",
        'h6': "Nuestras tarifas de precios sin competencia y nuestro equipo técnico especializado hacen de nosotros un punto de referencia en el sector. Hemos realizado proyectos para diferentes empresas. Estamos avalados por muchas grandes empresas españolas e internacionales.",
        # SERVICIOS
        'srv_header': "Servicios Boutique",
        'srv_sworn_title': "Traducción Jurada",
        'srv_sworn_desc': "Traducciones oficiales con validez legal ante organismos públicos y embajadas.",
        'srv_tech_title': "Traducción Técnica",
        'srv_tech_desc': "Manuales de ingeniería y expedientes técnicos para licitaciones.",
        'srv_visa_title': "Gestión de Visados",
        'srv_visa_desc': "Asesoramiento y tramitación completa para Libia y países árabes.",
        'srv_legal_title': "Asesoramiento Legal",
        'srv_legal_desc': "Registro de filiales y contratos en mercados emergentes como Libia.",
        # CONTACTO
        'hero_contact_title': "Contacte con Nosotros",
        'contact_title': "Hablemos de su proyecto",
        'info_address_title': "Ubicación",
        'info_address_text': "Calle de la Constitución, Fuenlabrada, 28944 Madrid, España",
        'info_email_title': "Correo Electrónico",
        'info_phone_title': "Teléfono Directo",
        'form_name': "Nombre Completo",
        'form_email': "Correo Electrónico",
        'form_phone': "Teléfono",
        'form_message': "Su Mensaje",
        'form_btn': "ENVIAR SOLICITUD",
        'reviews_title': "Confianza Global",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada."
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_lang': "Language",
        'hero_title': "Translation Excellence",
        'home_cta_btn': "REQUEST A QUOTATION",
        'h1': "We are an office of official, sworn, native professional translators and interpreters, led by Ms. Fatima Benamar, with more than 15 years of experience.",
        'h2': "WE OFFER an integral service in sworn translation and advice for the processing of all your documents.",
        'srv_header': "Boutique Services",
        'hero_contact_title': "Get in Touch",
        'contact_title': "Let's talk about your project",
        'form_btn': "SEND REQUEST",
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Boutique."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_lang': "اللغة",
        'home_cta_btn': "طلب عرض سعر",
        'hero_contact_title': "اتصل بنا",
        'form_btn': "إرسال الطلب",
        'footer_rights': "© 2026 TIGAFAB S.L. بيت الترجمة المحلفة."
    }
}

# --- FUNCIONES ---
def get_nav(lang, rel_path):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    links = ""
    for l_code in ['es', 'en', 'fr', 'de', 'ar']:
        l_folder = LANG_FOLDERS[l_code]
        links += f'<a href="{rel_path + (l_folder + "/index.html" if l_folder else "index.html")}" class="{"active" if l_code == lang else ""}">{LANG_NAMES[l_code]}</a>'
    return f"""<nav id="navbar" dir="ltr"><div class="container nav-container"><a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a><ul class="nav-links"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li></ul><div class="lang-selector" id="langSelector"><div class="lang-current">{t['nav_lang']} <i class="fas fa-chevron-down"></i></div><div class="lang-dropdown" id="langDropdown">{links}</div></div></div></nav>"""

def get_review_cards(lang):
    items = []
    reviews_data = [
        ("Marta (Google)", "Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord para un trámite urgente que me pedían por sorpresa. Su trato y rapidez son excelentes, me dio mucha tranquilidad."),
        ("Mohamed (Google)", "Gente muy profesional y muy amable. Lo recomiendo 100% para cualquier gestión de traducción o visados. Me ayudaron con el registro en un tiempo récord y con una calidad técnica insuperable."),
        ("Juan Carlos (Google)", "Atención excepcional y rapidez. Necesitaba una traducción jurada de árabe a español para el ministerio y estuvo lista en menos de 24 horas. Rigurosos y con un precio muy competitivo."),
        ("Laila (Google)", "La mejor agencia de Madrid para traducción de árabe. Son extremadamente serios con los plazos de entrega, algo vital para licitaciones. Trato exquisito por parte de todo el equipo técnico."),
        ("Constructor S.A. (Google)", "Indispensables para nuestras licitaciones en el norte de África. Su conocimiento del mercado libio y del vocabulario técnico de construcción nos ha permitido cerrar contratos muy complejos con éxito."),
        ("Irene (Google)", "Fátima es encantadora y una profesional de primer nivel. Hizo que un trámite burocrático difícil fuera sencillo y fluido. Recomiendo Tigafab a cualquiera que busque calidad y rigor."),
        ("Sami (Google)", "Servicio de visados para Libia rápido y sin incidencias. Tienen los contactos y el conocimiento necesario para que no haya retrasos. Altamente eficaces, volveremos a trabajar con ellos seguro."),
        ("Raúl (Google)", "Traducciones técnicas de alta calidad. Entienden perfectamente el lenguaje de ingeniería y construcción pesada. Es difícil encontrar traductores jurados que dominen estos términos tan específicos."),
        ("Elena (Google)", "Me salvaron con una traducción para el día siguiente muy temprano. Un servicio boutique real donde Fátima se involucra personalmente para ayudar al cliente. Profesionalidad de 10."),
        ("Karim (Google)", "Expertos reales en el mercado árabe y español. Máximo rigor jurídico en cada documento. Su apoyo técnico y administrativo en Libia es fundamental para nuestra expansión internacional.")
    ]
    for name, txt in reviews_data:
        items.append(f'<div class="review-card-premium"><div style="color:#c2a35d; margin-bottom:1.5rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div><p>{txt}</p><div style="font-weight:700; color:white; border-left: 2px solid var(--primary); padding-left: 1rem;">{name}</div></div>')
    return "".join(items) * 3

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t.get(title_key, title_key)} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background: rgba(0,0,0,0.2); backdrop-filter: blur(10px); color:white; padding:4rem 2rem; text-align:center;"><div style="font-family: 'Playfair Display', serif; font-size:2rem; margin-bottom:1rem;">TIGAFAB<span style="color:#c2a35d;">.</span></div><p>{t['footer_rights']}</p></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script><script src="{rel_path}js/main.js?v={os.urandom(2).hex()}"></script><script>AOS.init();</script></body></html>"""
    merged_t = t_es.copy(); merged_t.update(t)
    for k in sorted(merged_t.keys(), key=len, reverse=True): 
        full_html = full_html.replace(f't-{k.replace("_","-")}', str(merged_t[k]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang])
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

for lang in LANG_FOLDERS:
    # 1. HOME CON VUESTRO TEXTO
    index_content = f"""
    <section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>
    <section style="padding:10rem 0;"><div class="container" style="max-width:1100px;"><div style="display:grid; grid-template-columns: 1.2fr 1fr; gap:5rem; align-items:start;"><div data-aos="fade-right"><h2 style="font-size:2.8rem; line-height:1.2; margin-bottom:3rem;">Tradición y Rigor Juris</h2><p style="font-size:1.25rem; color:#f8fafc; line-height:1.8; margin-bottom:2rem;">t-h1</p><div style="background:rgba(194,163,93,0.1); border-left:4px solid var(--primary); padding:2rem; margin-bottom:2.5rem;"><p style="font-size:1.4rem; font-weight:700; color:var(--primary); margin-bottom:1rem;">t-h2</p><p style="color:#94a3b8; font-size:1.1rem;">t-h3</p></div><p style="font-size:1.1rem; color:#94a3b8; font-style:italic;">t-h4</p></div><div data-aos="fade-left" style="background:rgba(255,255,255,0.02); border:1px solid var(--glass-border); padding:3rem; border-radius:20px;"><p style="font-size:1.2rem; color:#f8fafc; line-height:1.8; margin-bottom:2rem;">t-h5</p><p style="font-size:1.2rem; color:#94a3b8; line-height:1.8;">t-h6</p></div></div></div></section>
    <section style="padding-bottom: 8rem;"><div class="container" style="text-align:center; margin-bottom:5rem;"><h2 style="font-size:3.5rem; margin-bottom:1rem; color:white;">t-reviews-title</h2><p style="color:#c2a35d; letter-spacing:4px; font-weight:700;">t-exp-verificadas</p></div><div class="marquee-container"><div class="marquee-inner">{get_review_cards(lang)}</div></div></section>"""
    generate_page(lang, "index.html", 'nav_home', index_content)
    
    # 2. SERVICIOS (RESTAURADOS)
    srv_content = f"""
    <section class="hero" style="min-height:40vh;"><h1>t-srv-header</h1></section>
    <section style="padding:8rem 0;"><div class="container"><div class="services-grid">
    <div class="service-card" data-aos="fade-up"><h3>t-srv-sworn-title</h3><p>t-srv-sworn-desc</p></div>
    <div class="service-card" data-aos="fade-up"><h3>t-srv-tech-title</h3><p>t-srv-tech-desc</p></div>
    <div class="service-card" data-aos="fade-up"><h3>t-srv-visa-title</h3><p>t-srv-visa-desc</p></div>
    <div class="service-card" data-aos="fade-up"><h3>t-srv-legal-title</h3><p>t-srv-legal-desc</p></div>
    </div></div></section>"""
    generate_page(lang, "servicios.html", 'nav_services', srv_content)
    
    # 3. CONTACTO (RESTAURADO)
    contact_content = f"""
    <section class="hero" style="min-height:40vh; height:auto; padding: 100px 0;"><div class="container" data-aos="fade-up"><h1>t-hero-contact-title</h1></div></section>
    <section class="contact-section"><div class="container"><div class="contact-grid">
    <div class="contact-info-box" data-aos="fade-right"><h2>t-contact-title</h2><div class="contact-item"><i class="fas fa-map-marker-alt"></i><div><h4>t-info-address-title</h4><p>t-info-address-text</p></div></div><div class="contact-item"><i class="fas fa-envelope"></i><div><h4>t-info-email-title</h4><p>info@tigafab.com</p></div></div><div class="contact-item"><i class="fas fa-phone-alt"></i><div><h4>t-info-phone-title</h4><p>+34 000 000 000</p></div></div></div>
    <div class="contact-form-premium" data-aos="fade-left"><form action="#" method="POST"><div class="form-group"><label>t-form-name</label><input type="text" class="form-control" required></div><div class="form-group"><label>t-form-email</label><input type="email" class="form-control" required></div><div class="form-group"><label>t-form-phone</label><input type="tel" class="form-control"></div><div class="form-group"><label>t-form-message</label><textarea class="form-control" required></textarea></div><button type="submit" class="btn-premium" style="width:100%; border:none; cursor:pointer;">t-form-btn</button></form></div>
    </div></div></section>"""
    generate_page(lang, "contacto.html", 'nav_contact', contact_content)

print("✅ ÉXITO: TODO restaurado (Servicios, Contacto y vuestro Texto Original).")
