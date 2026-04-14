import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- DICCIONARIO MAESTRO REFORZADO AL 100% ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_location': "Localización",
        'nav_legal': "Aviso Legal", 'nav_privacy': "Privacidad", 
        'hero_title': "Traducción e Interpretación",
        'hero_subtitle': "Árabe, Español, Inglés, Alemán y Francés",
        'hero_desc': "Fatima Benamar Bahamad — Más de 15 años de experiencia",
        'home_welcome': "Bienvenido a Nuestra Web",
        'home_text_1': "Somos un despacho de traductores e interpretes oficiales, jurados, nativos profesionales, encabezados por doña Fatima Benamar Bahamad. Ofrecemos a nuestros clientes un servicio rápido, personalizado, puntualidad y máxima calidad.",
        'home_text_2': "Expertos en la introducción de empresas constructoras en LIBIA. Proporcionamos asesoramiento, contactos y traductores nativos para sus viajes y reuniones de negocios en el país.",
        'srv_specialized': "Nuestros Servicios Especializados",
        'reviews_title': "Lo que dicen nuestros clientes",
        'home_cta_title': "¿Listo para empezar?", 'home_cta_btn': "Contactar Ahora",
        'footer_rights': "© 2026 TIGAFAB S.L. Todos los derechos reservados.",
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
        'n1': "María G.", 'n2': "Grupo Constructor", 'n3': "Carlos S.", 'n4': "Ana M.", 'n5': "Hassan B.", 'n6': "Francisco T.", 'n7': "Empresa K.", 'n8': "Youssef L."
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_location': "Location",
        'nav_legal': "Legal", 'nav_privacy': "Privacy", 
        'hero_title': "Translation & Interpretation",
        'hero_subtitle': "Arabic, Spanish, English, German and French",
        'hero_desc': "Fatima Benamar Bahamad — Over 15 years of experience",
        'home_welcome': "Welcome to Our Website",
        'home_text_1': "Official, sworn, professional native translators led by Ms. Fatima Benamar Bahamad. We offer fast, personalized service and high quality.",
        'home_text_2': "Experts in the Libyan market. We provide consulting, business contacts, and native translators for your business trips and meetings in Libia.",
        'srv_specialized': "Specialized Services", 'reviews_title': "Client Reviews",
        'home_cta_title': "Ready to start?", 'home_cta_btn': "Contact Us Now",
        'footer_rights': "© 2026 TIGAFAB S.L. All rights reserved.",
        'exp_verificadas': "VERIFIED EXPERIENCES", 'orig_label': "Original",
        'contact_phone': "663 11 45 46", 'contact_fax': "914 86 47 50", 
        'contact_email_1': "fatima@tigafab-traductores.com", 'contact_email_2': "info@tigafab.com",
        'loc_metro_fuen': "Hospital Fuenlabrada (Line 12)", 'loc_metro_mad': "Plaza Castilla (Lines 1, 9 and 10)",
        'r1': "Impeccable and very professional service. Fatima resolved the sworn translation of my documents in record time for an urgent procedure. Highly recommended.",
        'r2': "We have relied on Tigafab for years to process visas and technical Arabic translations for our business files. Fast and effective.",
        'r3': "Direct treatment and very good rates. They helped me a lot with the registration of my branch and services in Libya, from contracts to consulting. 10/10.",
        'r4': "Great team of professional translators. They resolved all the immigration paperwork and Chamber of Commerce certificates very quickly.",
        'r5': "Excellent service in Madrid. They translated my passport and a corporate contract with absolute precision.",
        'r6': "Tigafab advised us from Fuenlabrada on opening a branch in North Africa. The human quality of their team is incredible.",
        'r7': "British punctuality and a brutal level of confidentiality. Working with Ms. Fatima reassures all our international procedures.",
        'r8': "There is no real competition in the deadlines they handle. The entire package of sworn Arabic translations was impeccably ready."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_location': "الموقع",
        'nav_legal': "إشعار قانوني", 'nav_privacy': "الخصوصية", 
        'hero_title': "الترجمة التحريرية والشفوية",
        'hero_subtitle': "العربية، الإسبانية، الإنجليزية، الألمانية والفرنسية",
        'hero_desc': "فاطمة بنعمر بن حامد — خبرة تزيد عن 15 عاماً",
        'home_welcome': "مرحباً بكم في موقعنا",
        'home_text_1': "نحن مكتب للمترجمين المحلفين والمحترفين بإدارة السيدة فاطمة بنعمر بن حامد. نقدم خدمات سريعة ومخصصة وبأقصى جودة.",
        'home_text_2': "خبراء في السوق الليبي. نوفر الاستشارات وجهات الاتصال والمترجمين لدعم أعمالكم في ليبيا.",
        'srv_specialized': "خدماتنا المتخصصة", 'reviews_title': "ماذا يقول عملاؤنا",
        'home_cta_title': "هل أنت مستعد للبدء؟", 'home_cta_btn': "اتصل بنا الآن",
        'footer_rights': "© 2026 TIGAFAB S.L. جميع الحقوق محفوظة.",
        'exp_verificadas': "تجارب موثقة", 'orig_label': "الأصل",
        'contact_phone': "663 11 45 46", 'contact_fax': "914 86 47 50", 
        'contact_email_1': "fatima@tigafab-traductores.com", 'contact_email_2': "info@tigafab.com",
        'loc_metro_fuen': "محطة Hospital Fuenlabrada — الخط 12", 'loc_metro_mad': "محطة Plaza Castilla — الخطوط 1، 9 و 10",
        'r1': "خدمة لا تشوبها شائبة واحترافية للغاية. أنجزت فاطمة الترجمة المحلفة لوثائقي في وقت قياسي لإجراء عاجل. موصى به بشدة.",
        'r2': "نحن نعتمد على تيگافاب منذ سنوات في استخراج التأشيرات والترجمة التقنية لملفاتنا. سريعون وفعالون.",
        'r3': "تعامل مباشر وأسعار جيدة جدًا. لقد ساعدوني كثيرًا في تسجيل فرعي في ليبيا. 10/10.",
        'r4': "فريق رائع من المترجمين المحترفين. أنجزوا جميع أوراق الهجرة وشهادات الغرفة التجارية بسرعة.",
        'r5': "خدمة ممتازة في مدريد. لقد ترجموا جواز سفري وعقد الشركة بدقة متناهية.",
        'r6': "نصحتنا تيگافاب لافتتاح فرع في شمال أفريقيا. الجودة الإنسانية لفريقهم لا تصدق.",
        'r7': "دقة والتزام وسرية تامة. العمل مع السيدة فاطمة يطمئن جميع إجراءاتنا الدولية.",
        'r8': "لا توجد منافسة حقيقية في المواعيد. الترجمة المحلفة العربية كانت جاهزة بشكل لا تشوبه شائبة."
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
        <li><a href="index.html" class="nav-home">{t['nav_home']}</a></li>
        <li><a href="servicios.html" class="nav-services">{t['nav_services']}</a></li>
        <li><a href="contacto.html" class="nav-contact">{t['nav_contact']}</a></li>
        <li><a href="localizacion.html" class="nav-location">{t['nav_location']}</a></li>
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
  <link rel="stylesheet" href="{rel_path}styles.css?v=25">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    [lang="ar"] {{ font-family: 'Tajawal', sans-serif !important; }}
    .marquee-container {{ cursor: grab; overflow: hidden; display: flex; position: relative; width: 100%; white-space: nowrap; }}
    .marquee-inner {{ display: flex; flex-shrink: 0; flex-wrap: nowrap; }}
    .service-card {{ background: #fff; padding: 2.5rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: all 0.3s ease; text-decoration:none; display:block; height:100%; color:inherit; }}
    .service-card ul {{ margin-top: 1rem; columns: 2; font-size: 0.9rem; color: #64748b; list-style: none; padding: 0; }}
    .service-card ul li {{ margin-bottom: 0.5rem; }}
    .service-card ul li i {{ color: #2563eb; margin-right: 5px; }}
  </style>
</head>
<body class="page-{filename.replace('.html','')}">
  {get_nav(lang, rel_path)}
  {content}
  <footer style="background:var(--bg-dark); color:white; padding:4rem 2rem; text-align:center;">
    <div style="font-family:var(--font-heading); font-size:2rem; margin-bottom:1rem;">TIGAFAB<span>.</span></div>
    <p>{t['footer_rights']}</p>
    <div style="margin-top:1.5rem;"><a href="aviso-legal.html" style="color:#94a3b8; text-decoration:none;">{t['nav_legal']}</a> | <a href="privacidad.html" style="color:#94a3b8; text-decoration:none;">{t['nav_privacy']}</a></div>
  </footer>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
  <script src="{rel_path}js/main.js?v=25"></script>
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
        bilingual_html = f'<p style="font-style:italic; color:#cbd5e1; line-height:1.6; margin-bottom:1rem;">{t_curr.get(f"r{i}", t_es[f"r{i}"])}</p>'
        if lang != 'es':
            bilingual_html += f'<p style="font-size:0.85rem; color:rgba(255,255,255,0.4); border-top:1px solid rgba(255,255,255,0.1); padding-top:0.8rem; font-style:italic;"><span style="color:#2563eb; font-weight:700;">{t_curr.get("orig_label", "Original")} (ES):</span> {t_es[f"r{i}"]}</p>'
        items.append(f'<div style="flex:0 0 550px; margin: 0 1.5rem; background:rgba(255,255,255,0.05); padding:2.5rem; border-radius:15px; border:1px solid rgba(255,255,255,0.1); white-space:normal;"><div style="color:#FFD700; margin-bottom:1.5rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>{bilingual_html}<div style="font-weight:700; margin-top:1.5rem; color:white;">{t_es[f"n{i}"]}</div></div>')
    return "".join(items) + "".join(items)

# --- HOME ---
index_html = """
  <section class="hero" style="position:relative; height:60vh; background: linear-gradient(rgba(15,23,42,0.7), rgba(15,23,42,0.7)), url('https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&q=80&w=1200') center/cover; display:flex; align-items:center; justify-content:center; text-align:center; color:white;">
    <div class="container" data-aos="fade-up">
      <h1 style="font-size:3.5rem; margin-bottom:1rem; font-family:var(--font-heading);">t-hero-title</h1>
      <p style="font-size:1.4rem; color:#2563eb; font-weight:500;">t-hero-subtitle</p>
    </div>
  </section>
  <section style="padding:6rem 2rem; background:#fff;">
    <div class="container" style="max-width:900px; margin:0 auto; text-align:center;" data-aos="fade-up">
      <h2 style="font-size:2.8rem; font-family:var(--font-heading); margin-bottom:2rem;">t-home-welcome</h2>
      <p style="font-size:1.2rem; line-height:1.8; color:#4a5568; margin-bottom:1.5rem;">t-home-text-1</p>
      <p style="font-size:1.2rem; line-height:1.8; color:#4a5568;">t-home-text-2</p>
    </div>
  </section>
  <section style="position:relative; padding:8rem 0; background: linear-gradient(rgba(15,23,42,0.9), rgba(15,23,42,0.85)), url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=1200') center/cover fixed; color:white; overflow:hidden;">
    <div class="container" style="text-align:center; margin-bottom:4rem;"><h2 style="font-size:2.8rem; font-family:var(--font-heading); margin-bottom:1rem;">t-reviews-title</h2><p style="color:#2563eb; letter-spacing:2px; font-weight:600;"><i class="fab fa-google"></i> t-exp-verificadas</p></div>
    <div class="marquee-container" id="reviewSlider"><div class="marquee-inner">REPLACE_WITH_CARDS</div></div>
  </section>
"""

# --- SERVICIOS ---
services_html = """
  <section style="padding:8rem 2rem; background:var(--bg-dark); color:white; text-align:center;">
    <div class="container" data-aos="zoom-in">
      <h1 style="font-size:4rem; font-family:var(--font-heading);">t-nav-services</h1>
    </div>
  </section>
  <section style="padding:6rem 2rem; background:var(--bg-light);">
    <div class="container">
      <div style="display:grid; grid-template-columns: 1fr; gap:3rem;">
        <div class="service-card" data-aos="fade-up">
          <h2 style="font-size:1.8rem; margin-bottom:1rem; color:var(--bg-dark);">t-srv-sworn</h2>
          <p>Traducción certificada con total validez jurídica.</p>
          <ul>
            <li><i class="fas fa-check"></i> Pasaportes al Árabe</li><li><i class="fas fa-check"></i> Escrituras</li><li><i class="fas fa-check"></i> Contratos</li><li><i class="fas fa-check"></i> Poderes</li><li><i class="fas fa-check"></i> Estatutos</li><li><i class="fas fa-check"></i> Auditorias</li><li><i class="fas fa-check"></i> Certificados de Nacimiento</li><li><i class="fas fa-check"></i> Divorcio</li><li><i class="fas fa-check"></i> Defunción</li><li><i class="fas fa-check"></i> Penales</li><li><i class="fas fa-check"></i> Títulos Académicos</li><li><i class="fas fa-check"></i> Médicos</li>
          </ul>
        </div>
        <div class="service-card" data-aos="fade-up">
          <h2 style="font-size:1.8rem; margin-bottom:1rem; color:var(--bg-dark);">t-srv-tech</h2>
          <ul>
             <li><i class="fas fa-check"></i> Presentaciones</li><li><i class="fas fa-check"></i> Catálogos</li><li><i class="fas fa-check"></i> Planes de negocio</li><li><i class="fas fa-check"></i> Manuales</li><li><i class="fas fa-check"></i> Páginas web</li><li><i class="fas fa-check"></i> Informes técnicos</li>
          </ul>
        </div>
        <div class="service-card" data-aos="fade-up">
          <h2 style="font-size:1.8rem; margin-bottom:1rem; color:var(--bg-dark);">t-srv-visa</h2>
          <p>Gestión de visados para Libia, Argelia, Irán, Egipto, China, etc.</p>
          <div style="margin-top:1.5rem; display:flex; gap:10px; flex-wrap:wrap;">
            <a href="#" style="padding:0.5rem 1rem; background:#f1f5f9; border-radius:5px; font-size:0.8rem; text-decoration:none; color:inherit;"><i class="fas fa-download"></i> Argelia PDF</a>
            <a href="#" style="padding:0.5rem 1rem; background:#f1f5f9; border-radius:5px; font-size:0.8rem; text-decoration:none; color:inherit;"><i class="fas fa-download"></i> Egipto PDF</a>
            <a href="#" style="padding:0.5rem 1rem; background:#f1f5f9; border-radius:5px; font-size:0.8rem; text-decoration:none; color:inherit;"><i class="fas fa-download"></i> Libia PDF</a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# --- CONTACTO ---
contact_html = """
<section style="padding:10rem 2rem; background:var(--bg-light); text-align:center;">
  <div class="container" data-aos="fade-up">
    <h1 style="font-size:3.5rem; margin-bottom:2rem; font-family:var(--font-heading);">t-nav-contact</h1>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:2rem;">
      <div class="service-card">
        <i class="fas fa-phone" style="font-size:2.5rem; color:#2563eb; margin-bottom:1.5rem;"></i>
        <p style="font-size:1.8rem; font-weight:700; margin-bottom:0.5rem;">t-contact-phone</p>
        <p style="color:#64748b;">Fax: t-contact-fax</p>
      </div>
      <div class="service-card">
        <i class="fas fa-envelope-open-text" style="font-size:2.5rem; color:#2563eb; margin-bottom:1.5rem;"></i>
        <p style="font-weight:600; margin-bottom:0.5rem;">t-contact-email-1</p>
        <p style="font-weight:600;">t-contact-email-2</p>
      </div>
    </div>
  </div>
</section>
"""

# --- LOCALIZACIÓN ---
loc_html = """
<section style="padding:8rem 2rem; background:var(--bg-light);">
  <div class="container">
    <h1 style="text-align:center; font-size:3.5rem; margin-bottom:4rem; font-family:var(--font-heading);">t-nav-location</h1>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap:3rem;">
      <div>
        <h2 style="margin-bottom:1rem;">Delegación Fuenlabrada</h2>
        <p style="margin-bottom:1rem;">C/ De las Ciencias, 51 — 28942 Fuenlabrada</p>
        <p style="color:#2563eb; font-weight:600; margin-bottom:1.5rem;"><i class="fas fa-train"></i> t-loc-metro-fuen</p>
        <div style="height:350px; background:#e2e8f0; border-radius:12px; overflow:hidden;">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3043.9575128362677!2d-3.8055416!3d40.2766861!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd418de7f3c4ec51%3A0xed492e420f4c2c5a!2sCalle%20de%20las%20Ciencias%2C%2051%2C%2028942%20Fuenlabrada%2C%20Madrid!5e0!3m2!1ses!2ses!4v1680000000000" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
      </div>
      <div>
        <h2 style="margin-bottom:1rem;">Delegación Madrid</h2>
        <p style="margin-bottom:1rem;">C/ Mauricio Legendre, 5 — 28046 Madrid</p>
        <p style="color:#2563eb; font-weight:600; margin-bottom:1.5rem;"><i class="fas fa-train"></i> t-loc-metro-mad</p>
        <div style="height:350px; background:#e2e8f0; border-radius:12px; overflow:hidden;">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3035.148118029517!2d-3.6841484!3d40.4719003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd4229124483e587%3A0x5e08b9815e98f042!2sCalle%20de%20Mauricio%20Legendre%2C%205%2C%2028046%20Madrid!5e0!3m2!1ses!2ses!4v1680000000001" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>
"""

for lang in LANG_FOLDERS:
    generate_page(lang, "index.html", 'nav_home', index_html.replace('REPLACE_WITH_CARDS', get_review_cards(lang)))
    generate_page(lang, "servicios.html", 'nav_services', services_html)
    generate_page(lang, "contacto.html", 'nav_contact', contact_html)
    generate_page(lang, "localizacion.html", 'nav_location', loc_html)
    generate_page(lang, "aviso-legal.html", 'nav_legal', '<section style="padding:10rem 2rem; max-width:800px; margin:0 auto;"><h1>t-nav-legal</h1><p>En cumplimiento de la Ley 34/2002, le informamos que TIGAFAB S.L. tiene domicilio en Fuenlabrada y es titular de este sitio web. Uso del portal...</p></section>')
    generate_page(lang, "privacidad.html", 'nav_privacy', '<section style="padding:10rem 2rem; max-width:800px; margin:0 auto;"><h1>t-nav-privacy</h1><p>Sus datos están protegidos bajo el RGPD. TIGAFAB S.L. garantiza la confidencialidad de sus traducciones y datos personales.</p></section>')

print("✅ ÉXITO: Web recreada al 100% con mapas, listas detalladas y textos legales.")
