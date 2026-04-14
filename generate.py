import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- DICCIONARIO MAESTRO ---
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
        'srv_sworn': "Traducciones Juradas", 
        'srv_tech': "Traducción Técnica",
        'srv_visa': "Gestión de Visados",
        'reviews_title': "Confianza Global",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada.",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS", 'orig_label': "Original",
        'r1': "Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord para un trámite urgente. Totalmente recomendados.",
        'r2': "Llevamos años confiando en Tigafab para la tramitación de visados y traducción técnica hacia el árabe de los expedientes de nuestra empresa. Rápidos y eficaces.",
        'r3': "Trato directo y tarifas muy buenas. Me ayudaron muchísimo con el registro de mi filial y servicios en Libia, desde los contratos hasta el asesoramiento. Un 10.",
        'r4': "Gran equipo de traductores profesionales. Resolvieron toda la papeleta de extranjería y certificados de la Cámara de Comercio rapidísimo.",
        'r5': "Excelente servicio en Madrid. Me tradujeron el pasaporte y un contrato societario con un rigor absoluto.",
        'r6': "Tigafab nos asesoró desde Fuenlabrada para la apertura de una filial en el norte de África. La calidad humana de su equipo es increíble.",
        'r7': "Puntualidad británica y un nivel de confidencialidad brutal. Trabajar con doña Fátima tranquiliza todas nuestras gestiones internacionales.",
        'r8': "No hay competencia real en los plazos que manejan. Todo el paquete de traducciones juradas del árabe listo impecablemente.",
        'n1': "María G.", 'n2': "Constructor S.A.", 'n3': "Dr. Carlos S.", 'n4': "Ana M.", 'n5': "Hassan B.", 'n6': "Francisco T.", 'n7': "Empresa K.", 'n8': "Youssef L."
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_location': "Location",
        'nav_legal': "Legal", 'nav_privacy': "Privacy", 
        'hero_title': "Translation Excellence",
        'hero_subtitle': "ARABIC • SPANISH • ENGLISH • GERMAN • FRENCH",
        'home_welcome': "15+ Years of International Prestige",
        'home_text_1': "We are a boutique office of official sworn native translators and interpreters, led by Ms. Fatima Benamar Bahamad. Our firm is synonymous with legal rigor, absolute confidentiality, and elite quality.",
        'home_text_2': "Leaders in merchant advisory for the LIBYAN market. We provide a complete support structure for construction companies, from legal registration to technical support in strategic meetings.",
        'srv_header': "Boutique Services",
        'srv_sworn': "Sworn Translations",
        'srv_tech': "Technical Translation",
        'srv_visa': "Visa Management",
        'reviews_title': "Global Trust",
        'home_cta_btn': "GET A QUOTE",
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
        'srv_sworn': "الترجمة المحلفة",
        'srv_tech': "الترجمة التقنية",
        'srv_visa': "إدارة التأشيرات",
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
    # Mantenemos el orden ES, EN, FR, DE, AR siempre
    for l_code in ['es', 'en', 'fr', 'de', 'ar']:
        l_folder = LANG_FOLDERS[l_code]
        links += f'<a href="{rel_path + (l_folder + "/index.html" if l_folder else "index.html")}" class="lang-btn {"active" if l_code == lang else ""}">{l_code.upper()}</a>'
    
    # Forzamos dir="ltr" en el navbar para que no se invierta el logo
    return f"""<nav id="navbar" dir="ltr"><div class="container nav-container"><a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a><ul class="nav-links"><li><a href="index.html">{t['nav_home']}</a></li><li><a href="servicios.html">{t['nav_services']}</a></li><li><a href="contacto.html">{t['nav_contact']}</a></li><li><a href="localizacion.html">{t['nav_location']}</a></li><li><div class="lang-selector">{links}</div></li></ul></div></nav>"""

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    t_es = TRANSLATIONS['es']
    # Solo el cuerpo de la página será RTL para árabe, el encabezado será LTR fijo
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    full_html = f"""<!DOCTYPE html><html lang="{lang}" {is_rtl}><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{t[title_key]} | TIGAFAB</title><link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(2).hex()}"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&display=swap" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet"></head><body>{get_nav(lang, rel_path)}<main>{content}</main><footer style="background: rgba(0,0,0,0.2); backdrop-filter: blur(10px); color:white; padding:4rem 2rem; text-align:center; border-top: 1px solid rgba(255,255,255,0.05);"><div style="font-family: 'Playfair Display', serif; font-size:2rem; margin-bottom:1rem;">TIGAFAB<span style="color:#c2a35d;">.</span></div><p>{t['footer_rights']}</p></footer><script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script><script src="{rel_path}js/main.js?v=999"></script><script>AOS.init();</script></body></html>"""
    merged_t = t_es.copy(); merged_t.update(t)
    for k in sorted(merged_t.keys(), key=len, reverse=True): 
        full_html = full_html.replace(f't-{k.replace("_","-")}', str(merged_t[k]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang])
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, filename), "w") as f: f.write(full_html)

def get_review_cards(lang):
    t_curr = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    items = []
    for i in range(1, 9):
        bilingual = f'<p style="font-style:italic; color:#e2e8f0; line-height:1.6; margin-bottom:1rem;">{t_curr.get(f"r{i}", t_es.get(f"r{i}", "" ))}</p>'
        if lang != 'es': bilingual += f'<p style="font-size:0.8rem; color:rgba(255,255,255,0.4); border-top:1px solid rgba(255,255,255,0.1); padding-top:0.8rem; font-style:italic;"><span style="color:#c2a35d;">{t_curr.get("orig_label", "Original")} (ES):</span> {t_es.get(f"r{i}", "")}</p>'
        items.append(f'<div class="review-card-premium"><div style="color:#c2a35d; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>{bilingual}<div style="font-weight:700; margin-top:12rem; color:white;">{t_es.get(f"n{i}", "Cliente")}</div></div>')
    return "".join(items) + "".join(items)

for lang in LANG_FOLDERS:
    index_html = f"""<section class="hero"><div class="container" data-aos="fade-up"><p>t-hero-subtitle</p><h1>t-hero-title</h1><a href="contacto.html" class="btn-premium">t-home-cta-btn</a></div></section><section style="padding:10rem 0;"><div class="container" style="max-width:1000px; text-align:center;" data-aos="fade-up"><h2>t-home-welcome</h2><p style="font-size:1.4rem; color:#94a3b8; line-height:2;">t-home-text-1</p><div style="width:50px; height:2px; background:#c2a35d; margin: 3rem auto;"></div><p style="font-size:1.4rem; color:#94a3b8; line-height:2;">t-home-text-2</p></div></section><section style="padding-bottom: 8rem;"><div class="container" style="text-align:center; margin-bottom:5rem;"><h2 style="font-size:3.5rem; margin-bottom:1rem; color:white;">t-reviews-title</h2><p style="color:#c2a35d; letter-spacing:4px; font-weight:700;">t-exp-verificadas</p></div><div class="marquee-container" id="reviewSlider"><div class="marquee-inner">{get_review_cards(lang)}</div></div></section>"""
    generate_page(lang, "index.html", 'nav_home', index_html)
    generate_page(lang, "servicios.html", 'nav_services', '<section class="hero"><h1>t-srv-header</h1></section>')
    for p in ["contacto.html", "localizacion.html", "aviso-legal.html", "privacidad.html"]: generate_page(lang, p, 'nav_home', f'<section class="hero"><h1>{p}</h1></section>')

print("✅ ÉXITO: Encabezado fijado LTR. Logo a la izquierda siempre, incluso en Árabe.")
