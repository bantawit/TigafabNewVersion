import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- CONSTANTES ---
LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

# --- TRADUCCIONES COMPLETAS (TODO EL CONTENIDO) ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción", 'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'h1': "Somos un despacho de traductores e interpretes oficiales, jurados, nativos profesionales, encabezados por doña Fatima Benamar, con más de 15 años de experiencia.",
        'srv_header_main': "Nuestras Especialidades",
        'srv_header_sub': "Servicios de élite en Traducción, Gestión y Asesoramiento Internacional",
        'srv_jurada_title': "Traducciones Juradas",
        'srv_jurada_list': ["Pasaportes al Árabe", "Escrituras y Contratos", "Poderes Notariales", "Estatutos de Sociedades", "Auditorías y Cuentas Anuales", "Autorizaciones y Actas", "Certificados (Cámara, Mercantil, Origen)", "Facturas Comerciales", "Acuerdos Sociales", "Títulos y Expedientes Académicos"],
        'srv_tecnica_title': "Traducciones Técnicas",
        'srv_tecnica_list': ["Catálogos y Presentaciones", "Planes de Negocio", "Manuales de Ingeniería", "Páginas Web", "Listados de Precios", "Correspondencia y Cartas", "Informes Técnicos", "Cualquier otro documento"],
        'srv_organismos_title': "Gestión ante Organismos",
        'srv_organismos_list': ["Ministerio de Asuntos Exteriores", "Ministerio de Justicia y Sanidad", "Cámara de Comercio de Madrid", "Colegio de Notarios", "Todas las Embajadas (Libia, Argelia, Irán, Egipto, China...)"],
        'srv_visados_title': "Gestión de Visados",
        'srv_visados_list': ["Tramitación en consulados extranjeros", "Libia, Argelia, Irán, Egipto...", "Gestión de impresos oficiales", "Asesoramiento en requisitos"],
        'srv_libia_title': "Asesoramiento Especializado LIBIA",
        'srv_libia_desc': "Introducimos y asesoramos a las empresas españolas y extranjeras que desean trabajar o abrir filial, delegación o sucursal o instalarse como sede central en LIBIA. Proporcionamos contactos reales, apoyo técnico en todos los asuntos de registro y acompañamiento en viajes de negocios.",
        'srv_libia_btn': "Solicitar Información Mercado Libio",
        'reviews_title': "Confianza Global", 'exp_verificadas': "EXPERIENCIAS VERIFICADAS",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada."
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_lang': "Language",
        'hero_title': "Translation Excellence", 'hero_subtitle': "ARABIC • SPANISH • ENGLISH • GERMAN • FRENCH",
        'home_cta_btn': "REQUEST A QUOTATION",
        'h1': "We are an office of official, sworn, native professional translators and interpreters, led by Ms. Fatima Benamar, with more than 15 years of experience.",
        'srv_header_main': "Our Specialties",
        'srv_header_sub': "Elite services in Translation, Management and International Advisory",
        'srv_jurada_title': "Sworn Translations",
        'srv_jurada_list': ["Passports to Arabic", "Deeds and Contracts", "Powers of Attorney", "Articles of Association", "Audits and Annual Accounts", "Authorizations and Minutes", "Certificates (Chamber, Mercantile, Origin)", "Commercial Invoices", "Social Agreements", "Academic Titles and Records"],
        'srv_tecnica_title': "Technical Translations",
        'srv_tecnica_list': ["Catalogs and Presentations", "Business Plans", "Engineering Manuals", "Websites", "Price Lists", "Correspondence and Letters", "Technical Reports", "Any other document"],
        'srv_organismos_title': "Administrative Procedures",
        'srv_organismos_list': ["Ministry of Foreign Affairs", "Ministry of Justice and Health", "Madrid Chamber of Commerce", "Association of Notaries", "All Embassies (Libya, Algeria, Iran, Egypt, China...)"],
        'srv_visados_title': "Visa Management",
        'srv_visados_list': ["Processing in foreign consulates", "Libya, Algeria, Iran, Egypt...", "Management of official forms", "Advice on requirements"],
        'srv_libia_title': "Specialized LIBYA Advisory",
        'srv_libia_desc': "We introduce and advise Spanish and foreign companies wishing to work or open a subsidiary, delegation or branch or set up as headquarters in LIBYA. We provide real contacts, technical support in all registration matters and business travel accompaniment.",
        'srv_libia_btn': "Request Libya Market Information",
        'reviews_title': "Global Trust", 'exp_verificadas': "VERIFIED EXPERIENCES",
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Boutique."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_lang': "اللغة",
        'hero_title': "التميز في الترجمة", 'hero_subtitle': "العربية • الإسبانية • الإنجليزية • الألمانية • الفرنسية",
        'home_cta_btn': "طلب عرض سعر",
        'h1': "نحن مكتب للمترجمين التحريريين والفوريين الرسميين والمحلفين والمواطنين المحترفين، بقيادة السيدة فاطمة بنعمر، ومع أكثر من 15 عاماً من الخبرة.",
        'srv_header_main': "تخصصاتنا",
        'srv_header_sub': "خدمات متميزة في الترجمة والإدارة والاستشارات الدولية",
        'srv_jurada_title': "الترجمة المحلفة",
        'srv_jurada_list': ["جوازات السفر إلى العربية", "العقود والاتفاقيات", "التوكيلات الرسمية", "النظام الأساسي للشركات", "التدقيق والحسابات السنوية", "التفويضات والمحاضر", "شهادات (الغرفة، السجل التجاري، المنشأ)", "الفواتير التجارية", "الاتفاقيات الاجتماعية", "الشهادات والسجلات الأكاديمية"],
        'srv_tecnica_title': "الترجمة التقنية",
        'srv_tecnica_list': ["الكتالوجات والعروض التقديمية", "خطط العمل", "كتيبات الهندسة", "المواقع الإلكترونية", "قوائم الأسعار", "المراسلات والرسائل", "التقارير الفنية", "أي وثيقة أخرى"],
        'srv_organismos_title': "الإجراءات أمام الهيئات الرسمية",
        'srv_organismos_list': ["وزارة الشؤون الخارجية", "وزارة العدل والصحة", "غرفة تجارة مدريد", "نقابة الموثقين", "جميع السفارات (ليبيا، الجزائر، إيران، مصر، الصين...)"],
        'srv_visados_title': "إدارة التأشيرات",
        'srv_visados_list': ["المعالجة في القنصليات الأجنبية", "ليبيا، الجزائر، إيران، مصر...", "إدارة النماذج الرسمية", "نصائح حول المتطلبات"],
        'srv_libia_title': "استشارات متخصصة في السوق الليبي",
        'srv_libia_desc': "نقوم بتقديم المشورة للشركات الإسبانية والأجنبية التي ترغب في العمل أو فتح فرع أو مكتب تمثيلي أو مكتب فرعي أو التأسيس كمقر رئيسي في ليبيا. نحن نوفر اتصالات حقيقية ودعماً فنياً في جميع مسائل التسجيل ومرافقة في رحلات العمل.",
        'srv_libia_btn': "طلب معلومات عن السوق الليبي",
        'reviews_title': "ثقة عالمية", 'exp_verificadas': "تجارب موثقة",
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

def get_list_html(key, lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    items = t.get(key, [])
    return "".join([f"<li>{item}</li>" for item in items])

def get_review_cards(lang):
    items = []
    reviews_data = [
        ("Marta (Google)", "Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord para un trámite urgente que me pedían por sorpresa. Su trato y rapidez son excelentes, me dio mucha tranquilidad."),
        ("Mohamed (Google)", "Gente muy profesional y muy amable. Lo recomiendo 100% para cualquier gestión de traducción o visados. Me ayudaron con el registro en un tiempo récord y con una calidad técnica insuperable."),
        ("Juan Carlos (Google)", "Atención excepcional y rapidez. Necesitaba una traducción jurada de árabe a español para el ministerio y estuvo lista en menos de 24 horas. Rigurosos y con un precio muy competitivo."),
        ("Laila (Google)", "La mejor agencia de Madrid para traducción de árabe. Son extremadamente serios con los plazos de entrega, algo vital para licitaciones. Trato exquisito por parte de todo el equipo técnico."),
        ("Constructor S.A. (Google)", "Indispensables para nuestras licitaciones en el norte de África. Su conocimiento del mercado libio y del vocabulario técnico de construcción nos ha permitido cerrar contratos muy complejos con éxito.")
    ]
    for name, txt in reviews_data:
        items.append(f'<div class="review-card-premium"><div style="color:#c2a35d; margin-bottom:1.5rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div><p>{txt}</p><div style="font-weight:700; color:white; border-left: 2px solid var(--primary); padding-left: 1rem;">{name}</div></div>')
    return "".join(items) * 4

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

for lang in LANG_FOLDERS:
    # 1. HOME
    generate_page(lang, "index.html", 'nav_home', f'<section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>')
    # 2. SERVICIOS (TODO TRADUCIDO)
    srv_content = f"""
    <section class="hero" style="min-height:40vh; height:auto; padding: 120px 0;"><div class="container" data-aos="fade-up"><h1>t-srv-header-main</h1><p style="font-size:1.2rem; opacity:0.8;">t-srv-header-sub</p></div></section>
    <section style="padding: 8rem 0; background: var(--bg-dark);"><div class="container"><div class="services-creative-grid">
    <div class="service-premium-box" data-aos="fade-up"><i class="fas fa-stamp"></i><h3>t-srv-jurada-title</h3><ul class="service-list-detailed">{get_list_html('srv_jurada_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up" data-aos-delay="100"><i class="fas fa-file-invoice"></i><h3>t-srv-tecnica-title</h3><ul class="service-list-detailed">{get_list_html('srv_tecnica_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up" data-aos-delay="200"><i class="fas fa-landmark"></i><h3>t-srv-organismos-title</h3><ul class="service-list-detailed">{get_list_html('srv_organismos_list', lang)}</ul></div>
    <div class="service-premium-box" data-aos="fade-up"><i class="fas fa-passport"></i><h3>t-srv-visados-title</h3><ul class="service-list-detailed">{get_list_html('srv_visados_list', lang)}</ul></div>
    <div class="service-premium-box featured-libia" data-aos="zoom-in"><div style="display:grid; grid-template-columns: 80px 1fr; gap:2rem; align-items:center;"><i class="fas fa-globe-africa" style="margin:0;"></i><div><h3>t-srv-libia-title</h3><p style="font-size:1.2rem; color:#f8fafc; line-height:1.8; margin-top:1rem;">t-srv-libia-desc</p><a href="contacto.html" class="btn-premium" style="margin-top:2rem;">t-srv-libia-btn</a></div></div></div>
    </div></div></section>"""
    generate_page(lang, "servicios.html", 'nav_services', srv_content)
    # 3. CONTACTO
    generate_page(lang, "contacto.html", 'nav_contact', '<section class="hero"><h1>CONTACTO</h1></section>')

print("✅ ÉXITO: Todos los servicios traducidos a ES, EN y AR.")
