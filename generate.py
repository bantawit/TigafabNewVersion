import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- DICCIONARIO MAESTRO ---
# He mejorado la traducción al Inglés para que sea más formal y profesional (Boutique Style)
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_location': "Localización",
        'nav_legal': "Aviso Legal", 'nav_privacy': "Privacidad", 
        'hero_title': "Excelencia en Traducción",
        'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_welcome': "Más de 15 años de prestigio internacional",
        'home_text_1': "Somos un despacho boutique de traductores e interpretes oficiales jurados, encabezados por Fatima Benamar Bahamad. Nuestra firma es sinónimo de rigor jurídico, confidencialidad absoluta y calidad de élite.",
        'home_text_2': "Líderes en asesoramiento mercante para el mercado LIBIO. Proporcionamos una estructura completa de apoyo para empresas constructoras, desde el registro legal hasta el apoyo técnico en reuniones estratégicas.",
        'srv_header': "Servicios Boutique",
        'srv_sworn_title': "Traducción Jurada",
        'srv_sworn_desc': "Traducciones oficiales con validez legal ante organismos públicos, ministerios y embajadas. Especialistas en árabe, español y francés.",
        'srv_tech_title': "Traducción Técnica",
        'srv_tech_desc': "Manuales de ingeniería, contratos de obra y expedientes técnicos para licitaciones internacionales en el norte de África.",
        'srv_visa_title': "Gestión de Visados",
        'srv_visa_desc': "Asesoramiento y tramitación completa de visados para Libia y otros países árabes para empresas y personal técnico.",
        'srv_legal_title': "Asesoramiento Legal",
        'srv_legal_desc': "Apoyo en el registro de filiales, contratos societarios y cumplimiento normativo en mercados emergentes.",
        'contact_title': "Contacto Directo",
        'contact_address': "Calle de la Constitución, Fuenlabrada, Madrid",
        'reviews_title': "Confianza Global",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada.",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS", 'orig_label': "Original"
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_location': "Location",
        'nav_legal': "Legal", 'nav_privacy': "Privacy", 
        'hero_title': "Translation Excellence",
        'hero_subtitle': "ARABIC • SPANISH • ENGLISH • GERMAN • FRENCH",
        'home_welcome': "15+ Years of International Prestige",
        'home_text_1': "We are a boutique office of official sworn translators and interpreters, led by Fatima Benamar Bahamad. Our firm is synonymous with legal rigor, absolute confidentiality, and premium quality.",
        'home_text_2': "Leaders in professional advisory for the LIBYAN market. We provide comprehensive support for construction companies, from legal registration to technical assistance in strategic meetings.",
        'srv_header': "Boutique Services",
        'srv_sworn_title': "Sworn Translation",
        'srv_sworn_desc': "Official translations with full legal validity before public bodies, ministries, and embassies.",
        'srv_tech_title': "Technical Translation",
        'srv_tech_desc': "Engineering manuals, work contracts, and technical dossiers for international tenders.",
        'srv_visa_title': "Visa Management",
        'srv_visa_desc': "Full advisory and processing of visas for Libya and other Arab countries for corporate teams.",
        'srv_legal_title': "Legal Advisory",
        'srv_legal_desc': "Support in company registration and corporate contracts in emerging markets.",
        'contact_title': "Direct Contact",
        'contact_address': "Constitución St, Fuenlabrada, Madrid",
        'reviews_title': "Global Trust",
        'home_cta_btn': "REQUEST A QUOTE", # Mejorado de "Get a Quote" a "Request a Quote"
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Boutique.",
        'exp_verificadas': "VERIFIED EXPERIENCES", 'orig_label': "Original"
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_location': "الموقع",
        'nav_legal': "إشعار قانوني", 'nav_privacy': "الخصوصية", 
        'hero_title': "التميز في الترجمة",
        'hero_subtitle': "العربية • الإسبانية • الإنجليزية • الألمانية • الفرنسية",
        'home_welcome': "أكثر من 15 عاماً من الخبرة الدولية",
        'home_text_1': "نحن مكتب بوتيك للمترجمين والمترجمين الفوريين الرسميين المحلفين، برئاسة السيدة فاطمة بنعمر بن حامد. شركتنا مرادفة للدقة القانونية والسرية المطلقة والجودة المتميزة.",
        'home_text_2': "رواد في تقديم الاستشارات التجارية للسوق الليبي. نحن نوفر هيكلاً كاملاً من الدعم لشركات المقاولات، بدءاً من التسجيل القانوني وحتى الدعم الفني في الاجتماعات الاستراتيجية.",
        'srv_header': "خدمات حصرية",
        'srv_sworn_title': "الترجمة المحلفة",
        'srv_sworn_desc': "ترجمات رسمية ذات صلاحية قانونية أمام الهيئات العامة والوزارات والسفارات.",
        'srv_tech_title': "الترجمة التقنية",
        'srv_tech_desc': "كتيبات الهندسة، عقود العمل، والملفات الفنية للمناقصات الدولية في شمال أفريقيا.",
        'srv_visa_title': "إدارة التأشيرات",
        'srv_visa_desc': "الاستشارة والمعالجة الكاملة للتأشيرات لليبيا والدول العربية الأخرى.",
        'srv_legal_title': "الاستشارات القانونية",
        'srv_legal_desc': "دعم في تسجيل الفروع والعقود التجارية في الأسواق الناشئة.",
        'contact_title': "اتصال مباشر",
        'contact_address': "شارع الدستور، فوينلابرادا، مدريد",
        'reviews_title': "ثقة عالمية",
        'home_cta_btn': "طلب عرض سعر",
        'footer_rights': "© 2026 TIGAFAB S.L. بيت الترجمة المحلفة.",
        'exp_verificadas': "تجارب موثقة", 'orig_label': "الأصل"
    }
}

LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

def get_nav(lang, rel_path):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    links = ""
    for l_code in ['es', 'en', 'fr', 'de', 'ar']:
        l_folder = LANG_FOLDERS[l_code]
        links += f'<a href="{rel_path + (l_folder + "/index.html" if l_folder else "index.html")}" class="lang-btn {"active" if l_code == lang else ""}">{l_code.upper()}</a>'
    return f"""<nav id="navbar" dir="ltr"><div class="container nav-container"><a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a><ul class="nav-links"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li><li><a href="localizacion.html">{t['nav_location']}</a></li><li><div class="lang-selector">{links}</div></li></ul></div></nav>"""

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    t_es = TRANSLATIONS['es']
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t.get(title_key, title_key)} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background: rgba(0,0,0,0.2); backdrop-filter: blur(10px); color:white; padding:4rem 2rem; text-align:center; border-top: 1px solid rgba(255,255,255,0.05);"><div style="font-family: 'Playfair Display', serif; font-size:2rem; margin-bottom:1rem;">TIGAFAB<span style="color:#c2a35d;">.</span></div><p>{t['footer_rights']}</p></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script><script src="{rel_path}js/main.js?v=999"></script><script>AOS.init();</script></body></html>"""
    merged_t = t_es.copy(); merged_t.update(t)
    for k in sorted(merged_t.keys(), key=len, reverse=True): 
        full_html = full_html.replace(f't-{k.replace("_","-")}', str(merged_t[k]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang])
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

for lang in LANG_FOLDERS:
    index_html = f"""<section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section><section style="padding:10rem 0;"><div class="container" style="max-width:1000px; text-align:center;" data-aos="fade-up"><h2>t-home-welcome</h2><p style="font-size:1.4rem; color:#94a3b8; line-height:2;">t-home-text-1</p><div style="width:50px; height:2px; background:#c2a35d; margin: 3rem auto;"></div><p style="font-size:1.4rem; color:#94a3b8; line-height:2;">t-home-text-2</p></div></section>"""
    generate_page(lang, "index.html", 'nav_home', index_html)
    # Re-generar servicios y contacto
    srv_html = f"""<section class="hero" style="min-height:40vh;"><h1>t-srv-header</h1></section><section style="padding:8rem 0;"><div class="container"><div class="services-grid"><div class="service-card" data-aos="fade-up"><h3>t-srv-sworn-title</h3><p>t-srv-sworn-desc</p></div><div class="service-card" data-aos="fade-up"><h3>t-srv-tech-title</h3><p>t-srv-tech-desc</p></div><div class="service-card" data-aos="fade-up"><h3>t-srv-visa-title</h3><p>t-srv-visa-desc</p></div><div class="service-card" data-aos="fade-up"><h3>t-srv-legal-title</h3><p>t-srv-legal-desc</p></div></div></div></section>"""
    generate_page(lang, "servicios.html", 'nav_services', srv_html)
    generate_page(lang, "contacto.html", 'nav_contact', f'<section class="hero" style="min-height:40vh;"><h1>t-contact-title</h1></section>')

print("✅ ÉXITO: Terminología en inglés mejorada a 'REQUEST A QUOTE'.")
