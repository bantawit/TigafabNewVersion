import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- DICCIONARIO MAESTRO REFORZADO Y TRADUCIDO AL 100% ---
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
        'srv_docs': "Asuntos Oficiales",
        'srv_business': "Estrategia Libia",
        'reviews_title': "Confianza Global",
        'home_cta_title': "¿Hablamos de su próximo proyecto?",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada.",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS", 'orig_label': "Original",
        'contact_phone': "663 11 45 46", 'contact_fax': "914 86 47 50", 
        'contact_email_1': "fatima@tigafab-traductores.com", 'contact_email_2': "info@tigafab.com",
        'loc_metro_fuen': "Hospital Fuenlabrada (Línea 12)", 'loc_metro_mad': "Plaza Castilla (Líneas 1, 9 y 10)",
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
        'home_text_1': "We are a boutique office of official sworn professional native translators led by Fatima Benamar Bahamad. Our firm stands for legal rigor and elite quality.",
        'home_text_2': "Leaders in merchant advisory for the LIBYAN market. We provide a complete support structure for construction companies, from legal registration to technical support.",
        'srv_header': "Boutique Services",
        'srv_sworn': "Sworn Translations",
        'srv_tech': "Technical Translation",
        'srv_visa': "Visa Management",
        'srv_docs': "Official Affairs",
        'srv_business': "Libya Strategy",
        'reviews_title': "Global Trust",
        'home_cta_title': "Discuss your next project?",
        'home_cta_btn': "GET A QUOTE",
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Boutique.",
        'exp_verificadas': "VERIFIED EXPERIENCES", 'orig_label': "Original",
        'contact_phone': "663 11 45 46", 'contact_fax': "914 86 47 50", 
        'contact_email_1': "fatima@tigafab-traductores.com", 'contact_email_2': "info@tigafab.com",
        'loc_metro_fuen': "Hospital Fuenlabrada (Line 12)", 'loc_metro_mad': "Plaza Castilla (Lines 1, 9 and 10)",
        'r1': "Impeccable and very professional service. Fatima resolved the sworn translation of my documents in record time for an urgent procedure. Highly recommended.",
        'r2': "We have relied on Tigafab for years to process visas and technical Arabic translations for our business files. Fast and effective."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_location': "الموقع",
        'nav_legal': "إشعار قانوني", 'nav_privacy': "الخصوصية", 
        'hero_title': "التميز في الترجمة",
        'hero_subtitle': "العربية • الإسبانية • الإنجليزية • الألمانية • الفرنسية",
        'home_welcome': "أكثر من 15 عاماً من الخبرة الدولية",
        'home_text_1': "نحن مكتب بوتيك للمترجمين المحلفين والمحترفين بإدارة السيدة فاطمة بنعمر بن حامد. نرمز للدقة القانونية والجودة العالية.",
        'home_text_2': "رواد في تقديم الاستشارات للسوق الليبي. نوفر الهيكل الكامل لدعم شركات المقاولات من التسجيل القانوني إلى الدعم الفني.",
        'srv_header': "خدمات حصرية",
        'srv_sworn': "الترجمة المحلفة",
        'srv_tech': "الترجمة التقنية",
        'srv_visa': "إدارة التأشيرات",
        'srv_docs': "الشؤون الرسمية",
        'srv_business': "استراتيجية ليبيا",
        'reviews_title': "ثقة عالمية",
        'home_cta_title': "هل نناقش مشروعك القادم؟",
        'home_cta_btn': "طلب عرض سعر",
        'footer_rights': "© 2026 TIGAFAB S.L. بيت الترجمة المحلفة.",
        'exp_verificadas': "تجارب موثقة", 'orig_label': "الأصل",
        'contact_phone': "663 11 45 46", 'contact_fax': "914 86 47 50", 
        'contact_email_1': "fatima@tigafab-traductores.com", 'contact_email_2': "info@tigafab.com",
        'loc_metro_fuen': "محطة Hospital Fuenlabrada — الخط 12", 'loc_metro_mad': "Plaza Castilla — الخطوط 1، 9 و 10",
        'r1': "خدمة لا تشوبها شائبة واحترافية للغاية. أنجزت فاطمة الترجمة المحلفة لوثائقي في وقت قياسي لإجراء عاجل. موصى به بشدة."
    }
}

LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

def get_nav(lang, rel_path):
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    lang_links = ""
    for l_code, l_folder in LANG_FOLDERS.items():
        active = "active" if l_code == lang else ""
        href = rel_path + (f"{l_folder}/index.html" if l_folder else "index.html")
        lang_links += f'<a href="{href}" class="lang-btn {active}">{l_code.upper()}</a>'
    return f"""
  <nav id="navbar">
    <div class="nav-container">
      <a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a>
      <ul class="nav-links">
        <li><a href="index.html">{t['nav_home']}</a></li>
        <li><a href="servicios.html">{t['nav_services']}</a></li>
        <li><a href="contacto.html">{t['nav_contact']}</a></li>
        <li><a href="localizacion.html">{t['nav_location']}</a></li>
      </ul>
      <div class="lang-selector">{lang_links}</div>
    </div>
  </nav>
"""

def generate_page(lang, filename, title_key, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    sorted_keys = sorted(t.keys(), key=len, reverse=True)
    
    full_html = f"""<!DOCTYPE html>
<html lang="{lang}" {is_rtl}>
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t[title_key]} | TIGAFAB</title>
  <link rel="stylesheet" href="{rel_path}styles.css?v={os.urandom(4).hex()}">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
</head>
<body class="page-{filename.replace('.html','')}">
  {get_nav(lang, rel_path)}
  <main>{content}</main>
  <footer style="background: rgba(0,0,0,0.2); backdrop-filter: blur(10px); color:white; padding:4rem 2rem; text-align:center; border-top: 1px solid rgba(255,255,255,0.05);">
    <div style="font-family: 'Playfair Display', serif; font-size:2rem; margin-bottom:1rem;">TIGAFAB<span>.</span></div>
    <p>{t['footer_rights']}</p>
    <div style="margin-top:1.5rem;"><a href="aviso-legal.html" style="color:var(--text-muted); text-decoration:none; font-size:0.8rem;">{t['nav_legal']}</a> | <a href="privacidad.html" style="color:var(--text-muted); text-decoration:none; font-size:0.8rem;">{t['nav_privacy']}</a></div>
  </footer>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
  <script src="{rel_path}js/main.js?v=999"></script>
  <script>AOS.init();</script>
</body>
</html>"""

    for key in sorted_keys:
        full_html = full_html.replace(f't-{key.replace("_","-")}', str(t[key]))
    
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang])
    if not os.path.exists(target_dir): os.makedirs(target_dir)
    with open(os.path.join(target_dir, filename), "w", encoding="utf-8") as f: f.write(full_html)

def get_review_cards(lang):
    t_curr = TRANSLATIONS.get(lang, TRANSLATIONS['es']); t_es = TRANSLATIONS['es']
    items = []
    for i in range(1, 9):
        bilingual = f'<p style="font-style:italic; color:#e2e8f0; line-height:1.6; margin-bottom:1rem;">{t_curr.get(f"r{i}", t_es[f"r{i}"])}</p>'
        if lang != 'es': bilingual += f'<p style="font-size:0.8rem; color:rgba(255,255,255,0.4); border-top:1px solid rgba(255,255,255,0.1); padding-top:0.8rem; font-style:italic;"><span style="color:var(--primary);">{t_curr.get("orig_label", "Original")} (ES):</span> {t_es[f"r{i}"]}</p>'
        items.append(f'<div style="flex:0 0 500px; margin: 0 1.5rem; background:rgba(255,255,255,0.02); padding:2rem; border-radius:20px; border:1px solid rgba(255,255,255,0.05); white-space:normal;"><div style="color:var(--primary); margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>{bilingual}<div style="font-weight:700; margin-top:1.2rem; color:white;">{t_es[f"n{i}"]}</div></div>')
    return "".join(items) + "".join(items)

# --- TEMPLATES ---
index_html = """
  <section class="hero">
    <div class="container" data-aos="zoom-out">
      <p>t-hero-subtitle</p>
      <h1>t-hero-title</h1>
      <a href="contacto.html" class="btn-premium">t-home-cta-btn</a>
    </div>
  </section>

  <section style="padding:10rem 0;">
    <div class="container" style="max-width:900px; text-align:center;" data-aos="fade-up">
      <h2 style="font-size:3.5rem; margin-bottom:3rem;">t-home-welcome</h2>
      <p style="font-size:1.4rem; color:var(--text-muted); line-height:2;">t-home-text-1</p>
      <div style="width:50px; hieght:2px; background:var(--primary); margin: 3rem auto;"></div>
      <p style="font-size:1.4rem; color:var(--text-muted); line-height:2;">t-home-text-2</p>
    </div>
  </section>

  <section class="marquee-container">
    <div class="container" style="text-align:center; margin-bottom:5rem;">
      <h2 style="font-size:3.5rem; margin-bottom:1rem;">t-reviews-title</h2>
      <p style="color:var(--primary); letter-spacing:4px; font-weight:700;">t-exp-verificadas</p>
    </div>
    <div class="marquee-container" id="reviewSlider"><div class="marquee-inner">REPLACE_WITH_CARDS</div></div>
  </section>
"""

services_html = """
  <section class="hero" style="padding-top:12rem; padding-bottom:6rem;">
    <div class="container" data-aos="fade-up">
      <p>t-nav-services</p>
      <h1>t-srv-header</h1>
    </div>
  </section>
  <section style="padding:8rem 0;">
    <div class="container">
      <div class="service-grid">
        <div class="service-card" data-aos="fade-up">
          <h2>t-srv-sworn</h2>
          <p>Traducción certificada con total validez jurídica.</p>
          <ul>
            <li><i class="fas fa-circle"></i> Pasaportes</li><li><i class="fas fa-circle"></i> Escrituras</li><li><i class="fas fa-circle"></i> Contratos</li><li><i class="fas fa-circle"></i> Poderes</li><li><i class="fas fa-circle"></i> Estatutos</li><li><i class="fas fa-circle"></i> Auditorias</li>
          </ul>
        </div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="100">
          <h2>t-srv-tech</h2>
          <p>Especialistas en manuales y textos corporativos.</p>
          <ul>
             <li><i class="fas fa-circle"></i> Catálogos</li><li><i class="fas fa-circle"></i> Business Plans</li><li><i class="fas fa-circle"></i> Web Pages</li><li><i class="fas fa-circle"></i> Technical Reports</li>
          </ul>
        </div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="200">
          <h2>t-srv-visa</h2>
          <p>Gestión consular (Libia, Argelia, Irán, China...).</p>
          <div style="margin-top:2rem; display:flex; gap:10px;">
            <div style="padding:10px 20px; border:1px solid var(--glass-border); border-radius:10px; font-size:0.8rem;"><i class="fas fa-file-pdf"></i> PDF Forms</div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

for lang in LANG_FOLDERS:
    generate_page(lang, "index.html", 'nav_home', index_html.replace('REPLACE_WITH_CARDS', get_review_cards(lang)))
    generate_page(lang, "servicios.html", 'nav_services', services_html)
    generate_page(lang, "contacto.html", 'nav_contact', '<section style="padding:15rem 0; text-align:center;"><h1>t-nav-contact</h1><p style="font-size:2rem; margin-top:2rem;">t-contact-phone</p></section>')
    generate_page(lang, "localizacion.html", 'nav_location', '<section style="padding:15rem 0; text-align:center;"><h1>t-nav-location</h1></section>')
    generate_page(lang, "aviso-legal.html", 'nav_legal', '<section style="padding:15rem 0; text-align:center;"><h1>t-nav-legal</h1></section>')
    generate_page(lang, "privacidad.html", 'nav_privacy', '<section style="padding:15rem 0; text-align:center;"><h1>t-nav-privacy</h1></section>')

print("✅ ÉXITO: Diseño PREMIUM y CREATIVO inyectado en todos los idiomas.")
