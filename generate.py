import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- DICCIONARIO MAESTRO FINAL ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción",
        'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_welcome': "Más de 15 años de prestigio internacional",
        'home_text_1': "Somos un despacho boutique de traductores e interpretes oficiales jurados, encabezados por Fatima Benamar Bahamad. Nuestra firma es sinónimo de rigor jurídico, confidencialidad absoluta y calidad de élite.",
        'home_text_2': "Líderes en asesoramiento mercante para el mercado LIBIO. Proporcionamos una estructura completa de apoyo para empresas constructoras, desde el registro legal hasta el apoyo técnico en reuniones estratégicas.",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'srv_header': "Servicios Boutique",
        'srv_sworn_title': "Traducción Jurada",
        'srv_sworn_desc': "Traducciones oficiales con validez legal ante organismos públicos y embajadas.",
        'srv_tech_title': "Traducción Técnica",
        'srv_tech_desc': "Manuales de ingeniería y expedientes técnicos para licitaciones.",
        'srv_visa_title': "Gestión de Visados",
        'srv_visa_desc': "Asesoramiento y tramitación para Libia y países árabes.",
        'srv_legal_title': "Asesoramiento Legal",
        'srv_legal_desc': "Registro de filiales y contratos en mercados emergentes.",
        'reviews_title': "Confianza Global",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS", 
        'r1': "Servicio impecable y profesional. Fátima resolvió mi traducción urgente.",
        'r2': "Confiamos en Tigafab para todos nuestros expedientes internacionales.",
        'n1': "María G.", 'n2': "Constructor S.A.",
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
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada."
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_lang': "Language",
        'hero_title': "Translation Excellence",
        'hero_subtitle': "ARABIC • SPANISH • ENGLISH • GERMAN • FRENCH",
        'home_welcome': "15+ Years of International Prestige",
        'home_text_1': "We are a boutique office of official sworn native translators and interpreters, led by Ms. Fatima Benamar Bahamad. Our firm is synonymous with legal rigor and premium quality.",
        'home_text_2': "Leaders in merchant advisory for the LIBYAN market. Support for construction companies from registration to strategic meetings.",
        'home_cta_btn': "REQUEST A QUOTATION",
        'srv_header': "Boutique Services",
        'srv_sworn_title': "Sworn Translation",
        'srv_sworn_desc': "Official translations with legal validity before public bodies.",
        'srv_tech_title': "Technical Translation",
        'srv_tech_desc': "Engineering manuals and technical files for tenders.",
        'srv_visa_title': "Visa Management",
        'srv_visa_desc': "Full advisory and processing of visas for Arab countries.",
        'srv_legal_title': "Legal Advisory",
        'srv_legal_desc': "Support in company registration in emerging markets.",
        'reviews_title': "Global Trust",
        'exp_verificadas': "VERIFIED EXPERIENCES",
        'hero_contact_title': "Get in Touch",
        'contact_title': "Let's talk about your project",
        'info_address_title': "Location",
        'info_address_text': "Constitución St, Fuenlabrada, 28944 Madrid, Spain",
        'info_email_title': "Email Us",
        'info_phone_title': "Direct Line",
        'form_name': "Full Name",
        'form_email': "Email Address",
        'form_phone': "Phone Number",
        'form_message': "Your Message",
        'form_btn': "SEND REQUEST",
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Boutique."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_lang': "اللغة",
        'hero_title': "التميز في الترجمة",
        'hero_subtitle': "العربية • الإسبانية • الإنجليزية • الألمانية • الفرنسية",
        'home_welcome': "أكثر من 15 عاماً من الخبرة الدولية",
        'home_text_1': "نحن مكتب بوتيك للمترجمين والمترجمين الفوريين الرسميين المحلفين، برئاسة السيدة فاطمة بنعمر بن حامد. شركتنا مرادفة للدقة القانونية والجودة المتميزة.",
        'home_text_2': "رواد في تقديم الاستشارات التجارية للسوق الليبي. نحن نوفر هيكلاً كاملاً من الدعم لشركات المقاولات.",
        'home_cta_btn': "طلب عرض سعر",
        'srv_header': "خدمات حصرية",
        'srv_sworn_title': "الترجمة المحلفة",
        'srv_sworn_desc': "ترجمات رسمية ذات صلاحية قانونية أمام الهيئات العامة والسفارات.",
        'srv_tech_title': "الترجمة التقنية",
        'srv_tech_desc': "كتيبات الهندسة والملفات الفنية للمناقصات الدولية.",
        'srv_visa_title': "إدارة التأشيرات",
        'srv_visa_desc': "الاستشارة والمعالجة الكاملة للتأشيرات للدول العربية.",
        'srv_legal_title': "الاستشارات القانونية",
        'srv_legal_desc': "دعم في تسجيل الشركات في الأسواق الناشئة.",
        'reviews_title': "ثقة عالمية",
        'exp_verificadas': "تجارب موثقة",
        'hero_contact_title': "اتصل بنا",
        'contact_title': "دعنا نتحدث عن مشروعك",
        'info_address_title': "الموقع",
        'info_address_text': "شارع الدستور، فوينلابرادا، 28944 مدريد، إسبانيا",
        'info_email_title': "بريدنا الإلكتروني",
        'info_phone_title': "الخط المباشر",
        'form_name': "الاسم الكامل",
        'form_email': "البريد الإلكتروني",
        'form_phone': "رقم الهاتف",
        'form_message': "رسالتك",
        'form_btn': "إرسال الطلب",
        'footer_rights': "© 2026 TIGAFAB S.L. بيت الترجمة المحلفة."
    }
}

LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

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
        full_html = full_html.replace(f't-{k.replace("_","-")}', str(merged_t[k]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang])
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

def get_review_cards(lang):
    t_curr = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    items = []
    for i in range(1, 3):
        txt = t_curr.get(f'r{i}', t_es.get(f'r{i}', ''))
        name = t_es.get(f'n{i}', 'Cliente')
        items.append(f'<div class="review-card-premium"><div style="color:#c2a35d; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div><p style="font-style:italic; color:#e2e8f0; line-height:1.6; margin-bottom:1rem;">{txt}</p><div style="font-weight:700; color:white;">{name}</div></div>')
    return "".join(items) * 4

for lang in LANG_FOLDERS:
    # 1. INDEX
    index_content = f"""
    <section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>
    <section style="padding:10rem 0;"><div class="container" style="max-width:1000px; text-align:center;" data-aos="fade-up"><h2>t-home-welcome</h2><p style="font-size:1.4rem; color:#94a3b8; line-height:2;">t-home-text-1</p><div style="width:50px; height:2px; background:#c2a35d; margin: 3rem auto;"></div><p style="font-size:1.4rem; color:#94a3b8; line-height:2;">t-home-text-2</p></div></section>
    <section style="padding-bottom: 8rem;"><div class="container" style="text-align:center; margin-bottom:5rem;"><h2 style="font-size:3.5rem; margin-bottom:1rem; color:white;">t-reviews-title</h2><p style="color:#c2a35d; letter-spacing:4px; font-weight:700;">t-exp-verificadas</p></div><div class="marquee-container"><div class="marquee-inner">{get_review_cards(lang)}</div></div></section>"""
    generate_page(lang, "index.html", 'nav_home', index_content)
    
    # 2. SERVICIOS
    srv_content = f"""
    <section class="hero" style="min-height:40vh;"><h1>t-srv-header</h1></section>
    <section style="padding:8rem 0;"><div class="container"><div class="services-grid">
    <div class="service-card" data-aos="fade-up"><h3>t-srv-sworn-title</h3><p>t-srv-sworn-desc</p></div>
    <div class="service-card" data-aos="fade-up"><h3>t-srv-tech-title</h3><p>t-srv-tech-desc</p></div>
    <div class="service-card" data-aos="fade-up"><h3>t-srv-visa-title</h3><p>t-srv-visa-desc</p></div>
    <div class="service-card" data-aos="fade-up"><h3>t-srv-legal-title</h3><p>t-srv-legal-desc</p></div>
    </div></div></section>"""
    generate_page(lang, "servicios.html", 'nav_services', srv_content)
    
    # 3. CONTACTO (Mantenemos la ya creada)
    contact_content = f"""
    <section class="hero" style="height:40vh; min-height:300px;"><div class="container" data-aos="fade-up"><h1>t-hero-contact-title</h1></div></section>
    <section class="contact-section"><div class="container"><div class="contact-grid">
    <div class="contact-info-box" data-aos="fade-right"><h2>t-contact-title</h2><div class="contact-item"><i class="fas fa-map-marker-alt"></i><div><h4>t-info-address-title</h4><p>t-info-address-text</p></div></div><div class="contact-item"><i class="fas fa-envelope"></i><div><h4>t-info-email-title</h4><p>info@tigafab.com</p></div></div><div class="contact-item"><i class="fas fa-phone-alt"></i><div><h4>t-info-phone-title</h4><p>+34 600 000 000</p></div></div></div>
    <div class="contact-form-premium" data-aos="fade-left"><form action="#" method="POST"><div class="form-group"><label>t-form-name</label><input type="text" class="form-control" required></div><div class="form-group"><label>t-form-email</label><input type="email" class="form-control" required></div><div class="form-group"><label>t-form-phone</label><input type="tel" class="form-control"></div><div class="form-group"><label>t-form-message</label><textarea class="form-control" required></textarea></div><button type="submit" class="btn-premium" style="width:100%; border:none;">t-form-btn</button></form></div>
    </div></div></section>"""
    generate_page(lang, "contacto.html", 'nav_contact', contact_content)

print("✅ ÉXITO: Web completa y profesional generada.")
