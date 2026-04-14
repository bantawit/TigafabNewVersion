import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- DICCIONARIO MAESTRO ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_location': "Localización",
        'nav_legal': "Aviso Legal", 'nav_privacy': "Privacidad", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción",
        'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_welcome': "Más de 15 años de prestigio internacional",
        'home_text_1': "Somos un despacho boutique de traductores e interpretes oficiales jurados, encabezados por Fatima Benamar Bahamad. Nuestra firma es sinónimo de rigor jurídico, confidencialidad absoluta y calidad de élite.",
        'home_text_2': "Líderes en asesoramiento mercante para el mercado LIBIO. Proporcionamos una estructura completa de apoyo para empresas constructoras, desde el registro legal hasta el apoyo técnico en reuniones estratégicas.",
        'srv_header': "Servicios Boutique",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada.",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS", 'orig_label': "Original"
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_location': "Location",
        'nav_legal': "Legal", 'nav_privacy': "Privacy", 'nav_lang': "Language",
        'hero_title': "Translation Excellence",
        'hero_subtitle': "ARABIC • SPANISH • ENGLISH • GERMAN • FRENCH",
        'home_welcome': "15+ Years of International Prestige",
        'home_text_1': "We are a boutique office of official sworn native translators and interpreters, led by Ms. Fatima Benamar Bahamad. Our firm is synonymous with legal rigor, absolute confidentiality, and premium quality.",
        'home_text_2': "Leaders in merchant advisory for the LIBYAN market. We provide comprehensive support for construction companies, from legal registration to technical assistance in strategic meetings.",
        'srv_header': "Boutique Services",
        'home_cta_btn': "REQUEST A QUOTATION",
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Boutique.",
        'exp_verificadas': "VERIFIED EXPERIENCES", 'orig_label': "Original"
    },
    # ... otras traducciones (simplificadas para el script rápido)
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_location': "الموقع",
        'nav_lang': "اللغة", 'hero_title': "التميز في الترجمة",
        'home_cta_btn': "طلب عرض سعر", 'footer_rights': "© 2026 TIGAFAB S.L. بيت الترجمة المحلفة.",
        'home_text_1': "نحن مكتب بوتيك للمترجمين والمترجمين الفوريين الرسميين المحلفين، برئاسة السيدة فاطمة بنعمر بن حامد. شركتنا مرادفة للدقة القانونية والسرية المطلقة والجودة المتميزة.",
        'home_text_2': "رواد في تقديم الاستشارات التجارية للسوق الليبي. نحن نوفر هيكلاً كاملاً من الدعم لشركات المقاولات، بدءاً من التسجيل القانوني وحتى الدعم الفني في الاجتماعات الاستراتيجية.",
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
    
    return f"""<nav id="navbar" dir="ltr"><div class="container nav-container"><a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a><ul class="nav-links"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li><li><div class="lang-selector" id="langSelector"><div class="lang-current">{t['nav_lang']} <i class="fas fa-chevron-down"></i></div><div class="lang-dropdown" id="langDropdown">{links}</div></div></li></ul></div></nav>"""

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    t_es = TRANSLATIONS['es']
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t.get(title_key, title_key)} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background: rgba(0,0,0,0.2); backdrop-filter: blur(10px); color:white; padding:4rem 2rem; text-align:center;"><div style="font-family: 'Playfair Display', serif; font-size:2rem; margin-bottom:1rem;">TIGAFAB<span style="color:#c2a35d;">.</span></div><p>{t['footer_rights']}</p></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script><script src="{rel_path}js/main.js?v={os.urandom(2).hex()}"></script><script>AOS.init();</script></body></html>"""
    merged_t = t_es.copy(); merged_t.update(t)
    for k in sorted(merged_t.keys(), key=len, reverse=True): 
        full_html = full_html.replace(f't-{k.replace("_","-")}', str(merged_t[k]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang])
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

for lang in LANG_FOLDERS:
    index_html = f"""<section class="hero"><div class="container" data-aos="fade-up"><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section><section style="padding:10rem 0;"><div class="container" style="text-align:center;"><h2>t-home-welcome</h2><p>t-home-text-1</p><p>t-home-text-2</p></div></section>"""
    generate_page(lang, "index.html", 'nav_home', index_html)
    generate_page(lang, "servicios.html", 'nav_services', '<section class="hero"><h1>SERVICIOS</h1></section>')
    generate_page(lang, "contacto.html", 'nav_contact', '<section class="hero"><h1>CONTACTO</h1></section>')

print("✅ EXITO: Nuevo selector desplegable e inglés premium configurado.")
