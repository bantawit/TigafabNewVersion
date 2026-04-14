import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción", 'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'h1': "Somos un despacho de traductores e interpretes oficiales, jurados, nativos profesionales, encabezados por doña Fatima Benamar, con más de 15 años de experiencia. Ofrecemos a nuestros clientes un servicio rápido, personalizado, puntualidad, máxima calidad, confidencialidad, asesoramiento, trato directo y tarifas ajustadas.",
        'h2': "OFRECEMOS un servicio integral en traducción jurada y asesoramiento para la tramitación de todos sus documentos.",
        'srv_header_main': "Nuestras Especialidades",
        'srv_header_sub': "Servicios de élite en Traducción, Gestión y Asesoramiento Internacional",
        'srv_jurada_title': "Traducciones Juradas",
        'srv_tecnica_title': "Traducciones Técnicas",
        'srv_organismos_title': "Gestión ante Organismos",
        'srv_visados_title': "Gestión de Visados",
        'srv_libia_title': "Asesoramiento Especializado LIBIA",
        'srv_libia_desc': "Introducimos empresas en el mercado LIBIO con apoyo técnico, contactos reales y asesoramiento estratégico.",
        'hero_contact_title': "Contacte con Nosotros",
        'contact_title': "Hablemos de su proyecto",
        'form_name': "Nombre Completo", 'form_btn': "ENVIAR",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada.",
        'legal_title': "Aviso Legal", 'privacy_title': "Política de Privacidad"
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_lang': "Language",
        'hero_title': "Excellence in Translation", 'hero_subtitle': "ARABIC • SPANISH • ENGLISH • GERMAN • FRENCH",
        'home_cta_btn': "GET A QUOTE",
        'h1': "Professional translation and interpretation firm, led by Fatima Benamar, with over 15 years of excellence. We offer speed, quality, and confidentiality.",
        'h2': "Comprehensive sworn translation and administrative management for all your documents.",
        'srv_header_main': "Our Specialties",
        'srv_header_sub': "Professional Services in Legal and Technical Translation",
        'srv_jurada_title': "Sworn Translation",
        'srv_tecnica_title': "Technical Translation",
        'srv_organismos_title': "Official Procedures",
        'srv_visados_title': "Visa Management",
        'srv_libia_title': "Libyan Market Consultant",
        'srv_libia_desc': "We bridge European companies with the LIBYAN market through real field support and technical expertise.",
        'form_name': "Full Name", 'form_btn': "SUBMIT",
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Experts.",
        'legal_title': "Legal Notice", 'privacy_title': "Privacy Policy"
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "خدماتنا", 'nav_contact': "اتصل بنا", 'nav_lang': "اللغة",
        'hero_title': "خبراء في الترجمة المعتمدة", 'hero_subtitle': "العربية • الإسبانية • الإنجليزية • الألمانية • الفرنسية",
        'home_cta_btn': "اطلب عرض سعر الآن",
        'h1': "نحن مكتب ترجمة ومترجمين شفويين محلفين ومعتمدين رسمياً، تحت إدارة السيدة فاطمة بن عمار، بخبرة تمتد لأكثر من 15 عاماً. نضمن لعملائنا السرعة، والدقة، والسرية التامة، مع تقديم استشارات مباشرة وأسعار تنافسية.",
        'h2': "نقدم خدمات شاملة في الترجمة المحلفة وإدارة المعاملات لجميع أنواع المستندات الدولية.",
        'srv_header_main': "تخصصاتنا المهنية",
        'srv_header_sub': "خدمات راقية في الترجمة الدولية، الإدارة والتمثيل التجاري",
        'srv_jurada_title': "الترجمة المحلفة والمعتمدة",
        'srv_tecnica_list': ["ترجمة الكتالوجات والكتب التقنية", "خطط الأعمال والمشاريع", "كتيبات الهندسة", "ترجمة المواقع الإلكترونية", "قوائم الأسعار والمراسلات التجارية"],
        'srv_tecnica_title': "الترجمة التقنية والتجارية",
        'srv_organismos_title': "إدارة المعاملات الرسمية",
        'srv_visados_title': "إصدار التأشيرات",
        'srv_libia_title': "مستشار متخصص في السوق الليبي",
        'srv_libia_desc': "نعمل على إدخال الشركات الإسبانية والأوروبية إلى السوق الليبي من خلال توفير الدعم الفني، وشبكة علاقات حقيقية، وتمثيل مهني في الاجتماعات الاستراتيجية.",
        'hero_contact_title': "تواصل معنا",
        'contact_title': "تحدث إلينا عن مشروعك",
        'form_name': "الاسم الكامل", 'form_btn': "إرسال الطلب",
        'footer_rights': "© 2026 تيجافاب (TIGAFAB). مكتب ترجمة دولي معتمد.",
        'legal_title': "إشعار قانوني", 'privacy_title': "سياسة الخصوصية"
    }
}

def get_nav(lang, rel_path):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    links = "".join([f'<a href="{rel_path + (LANG_FOLDERS[lc] + "/index.html" if LANG_FOLDERS[lc] else "index.html")}">{LANG_NAMES[lc]}</a>' for lc in LANG_NAMES])
    return f"""<nav id="navbar" dir="ltr"><div class="container nav-container"><a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a><ul class="nav-links"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li></ul><div class="lang-selector" id="langSelector"><div class="lang-current">{t['nav_lang']} <i class="fas fa-chevron-down"></i></div><div class="lang-dropdown" id="langDropdown">{links}</div></div></div></nav>"""

def get_list_html(key, lang):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    items = t.get(key, ["Traducción Premium", "Gestión Pro", "Asesoría Internacional"])
    return "".join([f"<li>{x}</li>" for x in items])

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t.get(title_key, title_key)} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&family=Cairo:wght@400;700&display=swap" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background: rgba(15,23,42,0.95); backdrop-filter: blur(20px); border-top: 1px solid var(--glass-border); color:white; padding:5rem 2rem; text-align:center;"><div class="container"><div style="font-family:'Playfair Display'; font-size:2.5rem; margin-bottom:1.5rem;">TIGAFAB<span style="color:var(--primary);">.</span></div><div style="margin-bottom:2.5rem; display:flex; gap:2rem; justify-content:center; opacity:0.7;"><a href="index.html" style="color:white; text-decoration:none;">{t['nav_home']}</a><a href="servicios.html" style="color:white; text-decoration:none;">{t['nav_services']}</a><a href="contacto.html" style="color:white; text-decoration:none;">{t['nav_contact']}</a><a href="aviso-legal.html" style="color:white; text-decoration:none;">{t['legal_title']}</a></div><p>{t['footer_rights']}</p></div></footer><script src="{rel_path}js/main.js?v={os.urandom(2).hex()}"></script></body></html>"""
    merged_t = t_es.copy(); merged_t.update(t)
    for k in sorted(merged_t.keys(), key=len, reverse=True):
        if isinstance(merged_t[k], str): full_html = full_html.replace(f't-{k.replace("_","-")}', str(merged_t[k]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang]); os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

for lang in LANG_FOLDERS:
    home = f"""<section class="hero"><div class="container"><h1>t-hero-title</h1><p>t-hero-subtitle</p><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>
    <section style="padding:10rem 0;"><div class="container"><h2 style="font-size:3rem; margin-bottom:2.5rem;">t-h2</h2><p style="font-size:1.4rem; line-height:1.8; opacity:0.9;">t-h1</p></div></section>"""
    generate_page(lang, "index.html", 'nav_home', home)
    srv = f"""<section class="hero" style="min-height:50vh; padding:120px 0;"><div class="container"><h1>t-srv-header-main</h1><p>t-srv-header-sub</p></div></section>
    <section style="padding: 8rem 0; background: var(--bg-dark);"><div class="container"><div class="services-creative-grid">
    <div class="service-premium-box"><i class="fas fa-stamp"></i><h3>t-srv-jurada-title</h3></div>
    <div class="service-premium-box"><i class="fas fa-file-invoice"></i><h3>t-srv-tecnica-title</h3></div>
    <div class="service-premium-box featured-libia" style="grid-column: 1 / -1;"><i class="fas fa-globe-africa"></i><h3>t-srv-libia-title</h3><p>t-srv-libia-desc</p></div>
    </div></div></section>"""
    generate_page(lang, "servicios.html", 'nav_services', srv)
    cont = f"""<section class="hero" style="min-height:45vh; padding:100px 0;"><div class="container"><h1>t-hero-contact-title</h1></div></section>
    <section style="padding:8rem 0;"><div class="container"><div class="contact-grid">
    <div class="contact-info-box"><h2>t-contact-title</h2><div class="contact-item"><i class="fas fa-envelope"></i><div><h4>Email</h4><p>info@tigafab.com</p></div></div><div class="contact-item"><i class="fas fa-phone-alt"></i><div><h4>Teléfono</h4><p>+34 91 606 20 20</p></div></div></div>
    <div class="contact-form-premium"><form action="#" method="POST"><button type="submit" class="btn-premium" style="width:100%">t-form-btn</button></form></div>
    </div></div></section>"""
    generate_page(lang, "contacto.html", 'nav_contact', cont)
    legal = """<section class="hero" style="min-height:40vh; padding:100px 0;"><div class="container"><h1>t-legal-title</h1></div></section><section style="padding:8rem 0;"><div class="container"><h3>Legal Information</h3><p>Tigafab S.L.</p></div></section>"""
    generate_page(lang, "aviso-legal.html", 'legal_title', legal)

print("🚀 WEB ARABIC FIX: Cairo font added, logical properties applied, and refined Arabic translations.")
