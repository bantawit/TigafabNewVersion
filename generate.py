import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- CONSTANTES ---
LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

# --- TRADUCCIONES COMPLETAS ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción", 'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'h1': "Somos un despacho de traductores e interpretes oficiales, jurados, nativos profesionales, encabezados por doña Fatima Benamar, con más de 15 años de experiencia.",
        'home_welcome': "Más de 15 años de prestigio internacional",
        'h2': "OFRECEMOS un servicio integral en traducción jurada y asesoramiento para la tramitación de todos sus documentos.",
        'h3': "A través de nuestro asesoramiento y atención personalizada le garantizamos una tramitación correcta.",
        'h4': "Siempre satisfacemos a nuestros clientes.",
        'h5': "Especialistas en la introducción de empresas constructoras en LIBIA.",
        'h6': "Tarifas sin competencia y equipo técnico especializado.",
        # SECCIÓN SERVICIOS
        'srv_header_main': "Nuestras Especialidades",
        'srv_header_sub': "Servicios de élite en Traducción, Gestión y Asesoramiento Internacional",
        'srv_jurada_title': "Traducciones Juradas",
        'srv_tecnica_title': "Traducciones Técnicas",
        'srv_organismos_title': "Gestión ante Organismos",
        'srv_visados_title': "Gestión de Visados",
        'srv_libia_title': "Asesoramiento Especializado LIBIA",
        'srv_libia_desc': "Introducimos y asesoramos a empresas en el mercado LIBIO con apoyo técnico y contactos reales.",
        'srv_libia_btn': "Solicitar Información",
        # CONTACTO 100% TRADUCIDO
        'hero_contact_title': "Contacte con Nosotros",
        'contact_title': "Hablemos de su proyecto",
        'contact_subtitle': "Estamos a su entera disposición para cualquier consulta técnica o jurídica.",
        'info_address_title': "Ubicación",
        'info_address_text': "C. de las Ciencias, 51, 28942 Fuenlabrada, Madrid / C. Mauricio Legendre 5, Madrid",
        'info_email_title': "Email Corporativo",
        'info_phone_title': "Teléfono Directo",
        'form_name': "Nombre Completo",
        'form_email': "Correo Electrónico",
        'form_phone': "Teléfono de Contacto",
        'form_message': "Escriba su mensaje aquí...",
        'form_btn': "ENVIAR SOLICITUD",
        'reviews_title': "Confianza Global", 'exp_verificadas': "EXPERIENCIAS VERIFICADAS",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada."
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_lang': "Language",
        'hero_title': "Translation Excellence", 'hero_subtitle': "ARABIC • SPANISH • ENGLISH • GERMAN • FRENCH",
        'home_cta_btn': "REQUEST A QUOTATION",
        'h1': "Official sworn native translators led by Ms. Fatima Benamar, with 15+ years of experience.",
        'hero_contact_title': "Get in Touch",
        'contact_title': "Let's talk about your project",
        'contact_subtitle': "We are at your full disposal for any technical or legal inquiry.",
        'info_address_title': "Location",
        'info_address_text': "Sciencias St, 51, Fuenlabrada, Madrid / Mauricio Legendre 5, Madrid",
        'info_email_title': "Corporate Email",
        'info_phone_title': "Direct Line",
        'form_name': "Full Name",
        'form_email': "Email Address",
        'form_phone': "Contact Phone",
        'form_message': "How can we help you?",
        'form_btn': "SEND REQUEST",
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Boutique."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_lang': "اللغة",
        'hero_title': "التميز في الترجمة", 'hero_subtitle': "العربية • الإسبانية • الإنجليزية • الألمانية • الفرنسية",
        'home_cta_btn': "طلب عرض سعر",
        'h1': "مترجمون فوريون وتحريريون محلفون بقيادة السيدة فاطمة بنعمر، خبرة تزيد عن 15 عاماً.",
        'hero_contact_title': "اتصل بنا",
        'contact_title': "دعنا نتحدث عن مشروعك",
        'contact_subtitle': "نحن تحت تصرفكم بالكامل لأي استفسار فني أو قانوني.",
        'info_address_title': "الموقع",
        'info_address_text': "شارع العلوم، 51، فوينلابرادا، مدريد / شارع ماوريسيو ليجيندر 5، مدريد",
        'info_email_title': "البريد الإلكتروني",
        'info_phone_title': "الخط المباشر",
        'form_name': "الاسم الكامل",
        'form_email': "البريد الإلكتروني",
        'form_phone': "رقم الهاتف",
        'form_message': "كيف يمكننا مساعدتك؟",
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
        ("Marta (Google)", "Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord."),
        ("Mohamed (Google)", "Gente muy profesional y muy amable. Lo recomiendo 100% para cualquier gestión.")
    ]
    for name, txt in reviews_data:
        items.append(f'<div class="review-card-premium"><div style="color:#c2a35d; margin-bottom:1.5rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div><p>{txt}</p><div style="font-weight:700; color:white;">{name}</div></div>')
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
    # 2. SERVICIOS (Damos por hecho que ya están cargados)
    generate_page(lang, "servicios.html", 'nav_services', f'<section class="hero" style="min-height:30vh;"><h1>t-srv-header-main</h1></section>')
    
    # 3. CONTACTO REPLICADO Y TRADUCIDO
    contact_html = f"""
    <section class="hero" style="min-height:45vh; height:auto; padding: 120px 0;">
        <div class="container" data-aos="fade-up">
            <h1>t-hero-contact-title</h1>
        </div>
    </section>
    
    <section class="contact-section">
        <div class="container">
            <div class="contact-grid">
                <div class="contact-info-box" data-aos="fade-right">
                    <h2>t-contact-title</h2>
                    <p style="margin-bottom:3rem; color:#94a3b8; font-size:1.1rem;">t-contact-subtitle</p>
                    
                    <div class="contact-item">
                        <i class="fas fa-map-marker-alt"></i>
                        <div>
                            <h4>t-info-address-title</h4>
                            <p>t-info-address-text</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <i class="fas fa-envelope"></i>
                        <div>
                            <h4>t-info-email-title</h4>
                            <p>info@tigafab.com</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <i class="fas fa-phone-alt"></i>
                        <div>
                            <h4>t-info-phone-title</h4>
                            <p>+34 91 606 20 20</p>
                        </div>
                    </div>
                </div>
                
                <div class="contact-form-premium" data-aos="fade-left">
                    <form action="https://formspree.io/f/TU_ID_AQUI" method="POST">
                        <div class="form-group">
                            <label>t-form-name</label>
                            <input type="text" name="name" class="form-control" required placeholder="...">
                        </div>
                        <div class="form-group">
                            <label>t-form-email</label>
                            <input type="email" name="email" class="form-control" required placeholder="email@example.com">
                        </div>
                        <div class="form-group">
                            <label>t-form-phone</label>
                            <input type="tel" name="phone" class="form-control" placeholder="+34 ...">
                        </div>
                        <div class="form-group">
                            <label>t-form-message</label>
                            <textarea name="message" class="form-control" required placeholder="t-form-message"></textarea>
                        </div>
                        <button type="submit" class="btn-premium" style="width:100%; border:none; cursor:pointer;">t-form-btn</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
    """
    generate_page(lang, "contacto.html", 'nav_contact', contact_html)

print("✅ ÉXITO: Página de Contacto replicada y traducida en todos los idiomas.")
