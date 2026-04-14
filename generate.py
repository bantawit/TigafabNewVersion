import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- CONSTANTES ---
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}
LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}

TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción",
        'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        # HOME TEXT
        'h1': "Somos un despacho de traductores e interpretes oficiales, jurados, nativos profesionales, encabezados por doña Fatima Benamar, con más de 15 años de experiencia.",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada.",
        # SECCIÓN SERVICIOS CREATIVA
        'srv_jurada_title': "Traducciones Juradas",
        'srv_jurada_list': ["Pasaportes al Árabe", "Escrituras y Contratos", "Poderes Notariales", "Estatutos de Sociedades", "Auditorías y Cuentas Anuales", "Autorizaciones y Actas", "Certificados (Cámara, Mercantil, Origen)", "Facturas Comerciales", "Acuerdos Sociales", "Títulos y Expedientes Académicos"],
        'srv_tecnica_title': "Traducciones Técnicas",
        'srv_tecnica_list': ["Catálogos y Presentaciones", "Planes de Negocio", "Manuales de Ingeniería", "Páginas Web", "Listados de Precios", "Correspondencia y Cartas", "Informes Técnicos", "Cualquier otro documento"],
        'srv_organismos_title': "Gestión ante Organismos",
        'srv_organismos_list': ["Ministerio de Asuntos Exteriores", "Ministerio de Justicia y Sanidad", "Cámara de Comercio de Madrid", "Colegio de Notarios", "Todas las Embajadas (Libia, Argelia, Irán, Egipto, China...)"],
        'srv_visados_title': "Gestión de Visados",
        'srv_visados_list': ["Tramitación en consulados extranjeros", "Libia, Argelia, Irán, Egipto...", "Gestión de impresos oficiales", "Asesoramiento en requisitos"],
        'srv_libia_title': "Asesoramiento Especializado LIBIA",
        'srv_libia_desc': "Introducimos y asesoramos a las empresas españolas y extranjeras que desean trabajar o abrir filial, delegación o sucursal o instalarse como sede central en LIBIA. Proporcionamos contactos reales, apoyo técnico en todos los asuntos de registro y acompañamiento en viajes de negocios."
    }
}

def get_nav(lang, rel_path):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    links = ""
    for l_code in ['es', 'en', 'fr', 'de', 'ar']:
        l_folder = LANG_FOLDERS[l_code]
        links += f'<a href="{rel_path + (l_folder + "/index.html" if l_folder else "index.html")}" class="{"active" if l_code == lang else ""}">{LANG_NAMES[l_code]}</a>'
    return f"""<nav id="navbar" dir="ltr"><div class="container nav-container"><a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a><ul class="nav-links"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li></ul><div class="lang-selector" id="langSelector"><div class="lang-current">{t['nav_lang']} <i class="fas fa-chevron-down"></i></div><div class="lang-dropdown" id="langDropdown">{links}</div></div></div></nav>"""

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t.get(title_key, title_key)} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background: rgba(0,0,0,0.2); backdrop-filter: blur(10px); color:white; padding:4rem 2rem; text-align:center;"><div style="font-family: 'Playfair Display', serif; font-size:2rem; margin-bottom:1rem;">TIGAFAB<span style="color:#c2a35d;">.</span></div><p>{t['footer_rights']}</p></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script><script src="{rel_path}js/main.js?v={os.urandom(2).hex()}"></script><script>AOS.init();</script></body></html>"""
    merged_t = t_es.copy(); merged_t.update(t)
    for k in sorted(merged_t.keys(), key=len, reverse=True): 
        if isinstance(merged_t[k], str):
            full_html = full_html.replace(f't-{k.replace("_","-")}', str(merged_t[k]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang])
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

def get_list_html(key, lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    items = t.get(key, [])
    return "".join([f"<li>{item}</li>" for item in items])

for lang in LANG_FOLDERS:
    # 1. HOME (Se mantiene)
    index_content = f"""<section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>"""
    generate_page(lang, "index.html", 'nav_home', index_content)
    
    # 2. SERVICIOS CREATIVOS
    srv_content = f"""
    <section class="hero" style="min-height:40vh; height:auto; padding: 120px 0;">
        <div class="container" data-aos="fade-up">
            <h1 style="font-size:3.5rem;">Nuestras Especialidades</h1>
            <p style="font-size:1.2rem; opacity:0.8;">Servicios de élite en Traducción, Gestión y Asesoramiento Internacional</p>
        </div>
    </section>
    
    <section style="padding: 8rem 0; background: var(--bg-dark);">
        <div class="container">
            <div class="services-creative-grid">
                <!-- Jurada -->
                <div class="service-premium-box" data-aos="fade-up">
                    <i class="fas fa-stamp"></i>
                    <h3>t-srv-jurada-title</h3>
                    <ul class="service-list-detailed">{get_list_html('srv_jurada_list', lang)}</ul>
                </div>
                <!-- Técnica -->
                <div class="service-premium-box" data-aos="fade-up" data-aos-delay="100">
                    <i class="fas fa-file-invoice"></i>
                    <h3>t-srv-tecnica-title</h3>
                    <ul class="service-list-detailed">{get_list_html('srv_tecnica_list', lang)}</ul>
                </div>
                <!-- Organismos -->
                <div class="service-premium-box" data-aos="fade-up" data-aos-delay="200">
                    <i class="fas fa-landmark"></i>
                    <h3>t-srv-organismos-title</h3>
                    <ul class="service-list-detailed">{get_list_html('srv_organismos_list', lang)}</ul>
                </div>
                <!-- Visados -->
                <div class="service-premium-box" data-aos="fade-up">
                    <i class="fas fa-passport"></i>
                    <h3>t-srv-visados-title</h3>
                    <ul class="service-list-detailed">{get_list_html('srv_visados_list', lang)}</ul>
                </div>
                <!-- LIBIA ESPECIAL -->
                <div class="service-premium-box featured-libia" data-aos="zoom-in">
                    <div style="display:grid; grid-template-columns: 80px 1fr; gap:2rem; align-items:center;">
                        <i class="fas fa-globe-africa" style="margin:0;"></i>
                        <div>
                            <h3>t-srv-libia-title</h3>
                            <p style="font-size:1.2rem; color:#f8fafc; line-height:1.8; margin-top:1rem;">t-srv-libia-desc</p>
                            <a href="contacto.html" class="btn-premium" style="margin-top:2rem;">Solicitar Información Mercado Libio</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    generate_page(lang, "servicios.html", 'nav_services', srv_content)
    
    # 3. CONTACTO (Se mantiene)
    generate_page(lang, "contacto.html", 'nav_contact', '<section class="hero"><h1>CONTACTO</h1></section>')

print("✅ ÉXITO: Página de Servicios Creativos generada con todos los detalles.")
