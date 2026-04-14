import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- DICCIONARIO MAESTRO CON RESEÑAS 100% COMPLETAS ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción",
        'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_welcome': "Más de 15 años de prestigio internacional",
        'home_text_1': "Somos un despacho boutique de traductores e interpretes oficiales jurados, encabezados por Fatima Benamar Bahamad. Nuestra firma es sinónimo de rigor jurídico, confidencialidad absoluta y calidad de élite.",
        'home_text_2': "Líderes en asesoramiento mercante para el mercado LIBIO. Proporcionamos una estructura completa de apoyo para empresas constructoras, desde el registro legal hasta el apoyo técnico en reuniones estratégicas.",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'reviews_title': "Confianza Global",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS",
        # TEXTOS 100% ÍNTEGROS Y LARGOS
        'r1': "Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord para un trámite urgente que me pedían por sorpresa. Su trato y rapidez son excelentes, me dio mucha tranquilidad.",
        'n1': "Marta (Google)",
        'r2': "Gente muy profesional y muy amable. Lo recomiendo 100% para cualquier gestión de traducción o visados. Me ayudaron con el registro en un tiempo récord y con una calidad técnica insuperable.",
        'n2': "Mohamed (Google)",
        'r3': "Atención excepcional y rapidez. Necesitaba una traducción jurada de árabe a español para el ministerio y estuvo lista en menos de 24 horas. Rigurosos y con un precio muy competitivo.",
        'n3': "Juan Carlos (Google)",
        'r4': "La mejor agencia de Madrid para traducción de árabe. Son extremadamente serios con los plazos de entrega, algo vital para licitaciones. Trato exquisito por parte de todo el equipo técnico.",
        'n4': "Laila (Google)",
        'r5': "Indispensables para nuestras licitaciones en el norte de África. Su conocimiento del mercado libio y del vocabulario técnico de construcción nos ha permitido cerrar contratos muy complejos con éxito.",
        'n5': "Constructor S.A. (Google)",
        'r6': "Fátima es encantadora y una profesional de primer nivel. Hizo que un trámite burocrático difícil fuera sencillo y fluido. Recomiendo Tigafab a cualquiera que busque calidad y rigor.",
        'n6': "Irene (Google)",
        'r7': "Servicio de visados para Libia rápido y sin incidencias. Tienen los contactos y el conocimiento necesario para que no haya retrasos. Altamente eficaces, volveremos a trabajar con ellos seguro.",
        'n7': "Sami (Google)",
        'r8': "Traducciones técnicas de alta calidad. Entienden perfectamente el lenguaje de ingeniería y construcción pesada. Es difícil encontrar traductores jurados que dominen estos términos tan específicos.",
        'n8': "Raúl (Google)",
        'r9': "Me salvaron con una traducción para el día siguiente muy temprano. Un servicio boutique real donde Fátima se involucra personalmente para ayudar al cliente. Profesionalidad de 10.",
        'n9': "Elena (Google)",
        'r10': "Expertos reales en el mercado árabe y español. Máximo rigor jurídico en cada documento. Su apoyo técnico y administrativo en Libia es fundamental para nuestra expansión internacional.",
        'n10': "Karim (Google)",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada."
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_lang': "Language",
        'hero_title': "Translation Excellence",
        'home_cta_btn': "REQUEST A QUOTATION",
        'reviews_title': "Global Trust",
        'exp_verificadas': "VERIFIED EXPERIENCES",
        'r1': "Impeccable and professional service. Fatima handled my sworn translation in record time for an urgent legal procedure. Her speed and kindness are outstanding, giving me total peace of mind.",
        'r2': "Highly professional and friendly staff. 100% recommended for any translation or visa management. They helped us with international registration faster than any other agency.",
        'r5': "Essential for our tenders in North Africa. Their knowledge of the Libyan market and technical construction vocabulary has allowed us to close complex contracts successfully.",
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Boutique."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_lang': "اللغة",
        'home_cta_btn': "طلب عرض سعر",
        'r1': "خدمة مثالية واحترافية للغاية. قامت السيدة فاطمة بحل الترجمة المحلفة لوثائقي في وقت قياسي لإجراء قانوني عاجل. تعاملها وسرعتها ممتازتان.",
        'r2': "موظفون محترفون للغاية وودودون. أوصي به 100٪ لأي ترجمة أو إدارة تأشيرات. لقد ساعدونا في التسجيل الدولي بشكل أسرع من أي وكالة أخرى.",
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

def get_review_cards(lang):
    t_curr = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    items = []
    for i in range(1, 11):
        txt = t_curr.get(f'r{i}', t_es.get(f'r{i}', ''))
        name = t_curr.get(f'n{i}', t_es.get(f'n{i}', 'Cliente'))
        if not txt: continue
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
    index_content = f"""
    <section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section>
    <section style="padding:10rem 0;"><div class="container" style="max-width:1000px; text-align:center;" data-aos="fade-up"><h2>t-home-welcome</h2><p style="font-size:1.4rem; color:#94a3b8; line-height:2;">t-home-text-1</p><div style="width:50px; height:2px; background:#c2a35d; margin: 3rem auto;"></div><p style="font-size:1.4rem; color:#94a3b8; line-height:2;">t-home-text-2</p></div></section>
    <section style="padding-bottom: 8rem;"><div class="container" style="text-align:center; margin-bottom:5rem;"><h2 style="font-size:3.5rem; margin-bottom:1rem; color:white;">t-reviews-title</h2><p style="color:#c2a35d; letter-spacing:4px; font-weight:700;">t-exp-verificadas</p></div><div class="marquee-container"><div class="marquee-inner">{get_review_cards(lang)}</div></div></section>"""
    generate_page(lang, "index.html", 'nav_home', index_content)
    generate_page(lang, "servicios.html", 'nav_services', '<section class="hero" style="min-height:30vh;"><h1>SERVICIOS</h1></section>')
    generate_page(lang, "contacto.html", 'nav_contact', '<section class="hero" style="min-height:30vh;"><h1>CONTACTO</h1></section>')

print("✅ ÉXITO: 10 reseñas restauradas en su versión completa y detallada.")
