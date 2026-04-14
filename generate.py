import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- DICCIONARIO MAESTRO AMPLIADO CON RESEÑAS ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_location': "Localización",
        'nav_legal': "Aviso Legal", 'nav_privacy': "Privacidad", 'hero_title': "Traducción e Interpretación",
        'hero_subtitle': "Árabe, Español, Inglés, Alemán y Francés", 'home_welcome': "Bienvenido a Nuestra Web",
        'home_welcome_sub': "Traducciones, Interpretación, Gestión y Asesoramiento",
        'srv_specialized': "Nuestros Servicios Especializados", 'reviews_title': "Lo que dicen nuestros clientes",
        'home_cta_title': "¿Listo para empezar?", 'home_cta_sub': "Obtenga su presupuesto sin compromiso hoy mismo.",
        'home_cta_btn': "Contactar con Fátima", 'srv_more': "Saber más", 'srv_view_all': "Ver todos los servicios",
        'srv_sworn': "Traducciones Juradas", 'srv_sworn_short': "Documentación certificada con total validez jurídica.",
        'srv_tech': "Traducciones Técnicas", 'srv_tech_short': "Especialistas en manuales y textos corporativos.",
        'srv_visa': "Gestión de Visados", 'srv_visa_short': "Trámites consulares y legalizaciones.",
        'footer_rights': "© 2026 TIGAFAB S.L. Todos los derechos reservados.",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS",
        'review_1': "Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord.",
        'review_2': "Llevamos años confiando en Tigafab para la tramitación de visados y traducción técnica hacia el árabe.",
        'review_3': "Trato directo y tarifas muy buenas. Me ayudaron muchísimo con el registro de mi filial en Libia.",
        'review_4': "Gran equipo de traductores profesionales. Resolvieron toda la papeleta de extranjería rapidísimo."
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_location': "Location",
        'nav_legal': "Legal Notice", 'nav_privacy': "Privacy", 'hero_title': "Translation & Interpretation",
        'hero_subtitle': "Arabic, Spanish, English, German and French", 'home_welcome': "Welcome to Our Website",
        'home_welcome_sub': "Translations, Interpretation, Management and Consulting",
        'srv_specialized': "Our Specialized Services", 'reviews_title': "What our clients say",
        'home_cta_title': "Ready to start?", 'home_cta_sub': "Get your no-obligation quote today.",
        'home_cta_btn': "Contact Fatima", 'srv_more': "Learn more", 'srv_view_all': "View all services",
        'srv_sworn': "Sworn Translations", 'srv_sworn_short': "Certified texts and documentation with legal validity.",
        'srv_tech': "Technical Translations", 'srv_tech_short': "Specialists in manuals and corporate texts.",
        'srv_visa': "Visa Management", 'srv_visa_short': "Consular procedures and legalizations.",
        'footer_rights': "© 2026 TIGAFAB S.L. All rights reserved.",
        'exp_verificadas': "VERIFIED EXPERIENCES",
        'review_1': "Impeccable and very professional service. Fatima resolved the sworn translation of my documents in record time.",
        'review_2': "We have relied on Tigafab for years for visa processing and technical Arabic translation.",
        'review_3': "Direct treatment and very good rates. They helped me a lot with the registration of my branch in Libya.",
        'review_4': "Great team of professional translators. They resolved all the immigration paperwork very quickly."
    },
    'fr': {
        'nav_home': "Accueil", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_location': "Localisation",
        'nav_legal': "Mentions Légales", 'nav_privacy': "Confidentialité", 'hero_title': "Traduction & Interprétation",
        'hero_subtitle': "Arabe, Espagnol, Anglais, Allemand et Français", 'home_welcome': "Bienvenue sur notre site",
        'home_welcome_sub': "Traductions, Interprétation, Gestion et Conseil",
        'srv_specialized': "Nos services spécialisés", 'reviews_title': "Ce que disent nos clients",
        'home_cta_title': "Prêt à commencer ?", 'home_cta_sub': "Obtenez votre devis sans engagement dès aujourd'hui.",
        'home_cta_btn': "Contacter Fatima", 'srv_more': "En savoir plus", 'srv_view_all': "Voir tous les services",
        'srv_sworn': "Traductions Assermentées", 'srv_sworn_short': "Documents certifiés avec validité juridique totale.",
        'srv_tech': "Traductions Techniques", 'srv_tech_short': "Spécialistes des manuels et textes d'entreprise.",
        'srv_visa': "Gestion des Visas", 'srv_visa_short': "Démarches consulaires et légalisations.",
        'footer_rights': "© 2026 TIGAFAB S.L. Tous droits réservés.",
        'exp_verificadas': "EXPÉRIENCES VÉRIFIÉES",
        'review_1': "Service impeccable et très professionnel. Fatima a résolu la traduction assermentée en un temps record.",
        'review_2': "Nous faisons confiance à Tigafab depuis des années pour les visas et la traduction technique vers l'arabe.",
        'review_3': "Excellent accueil et très bons tarifs. Ils m'ont beaucoup aidé pour l'enregistrement de ma filiale en Libye.",
        'review_4': "Grande équipe de traductores professionnels. Ils ont résolu mes dossiers d'immigration très rapidement."
    },
    'de': {
        'nav_home': "Startseite", 'nav_services': "Dienstleistungen", 'nav_contact': "Kontakt", 'nav_location': "Standort",
        'nav_legal': "Impressum", 'nav_privacy': "Datenschutz", 'hero_title': "Übersetzung & Dolmetschen",
        'hero_subtitle': "Arabisch, Spanisch, Englisch, Deutsch und Französisch", 'home_welcome': "Willkommen auf unserer Website",
        'home_welcome_sub': "Übersetzungen, Dolmetschen, Management und Beratung",
        'srv_specialized': "Unsere Fachdienstleistungen", 'reviews_title': "Was unsere Kunden sagen",
        'home_cta_title': "Bereit zu starten?", 'home_cta_sub': "Holen Sie sich noch heute Ihr unverbindliches Angebot.",
        'home_cta_btn': "Fatima kontaktieren", 'srv_more': "Mehr erfahren", 'srv_view_all': "Alle Dienste anzeigen",
        'srv_sworn': "Beglaubigte Übersetzungen", 'srv_sworn_short': "Zertifizierte Dokumentation mit voller Rechtsgültigkeit.",
        'srv_tech': "Technische Übersetzungen", 'srv_tech_short': "Spezialisten für Handbücher und Firmentexte.",
        'srv_visa': "Visum-Management", 'srv_visa_short': "Konsularische Verfahrung und Beglaubigungen.",
        'footer_rights': "© 2026 TIGAFAB S.L. Alle Rechte vorbehalten.",
        'exp_verificadas': "VERIFIZIERTE ERFAHRUNGEN",
        'review_1': "Tadelloser und sehr professioneller Service. Fatima hat die Übersetzung in Rekordzeit erledigt.",
        'review_2': "Wir verlassen uns seit Jahren auf Tigafab für Visa und technische Arabisch-Übersetzungen.",
        'review_3': "Direkter Kontakt und sehr gute Preise. Sehr hilfreich bei der Gründung meiner Niederlassung in Libyen.",
        'review_4': "Großartiges Team von professionellen Übersetzern. Immigrationsthemen wurden sehr schnell gelöst."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_location': "الموقع",
        'nav_legal': "إشعار قانوني", 'nav_privacy': "الخصوصية", 'hero_title': "الترجمة التحريرية والشفوية",
        'hero_subtitle': "العربية، الإسبانية، الإنجليزية، الألمانية والفرنسية", 'home_welcome': "مرحباً بكم في موقعنا",
        'home_welcome_sub': "الترجمة، الإدارة والاستشارات",
        'srv_specialized': "خدماتنا المتخصصة", 'reviews_title': "ماذا يقول عملاؤنا",
        'home_cta_title': "هل أنت مستعد للبدء؟", 'home_cta_sub': "احصل على عرض سعر بدون التزام اليوم.",
        'home_cta_btn': "اتصل بفاطمة", 'srv_more': "معرفة المزيد", 'srv_view_all': "عرض جميع الخدمات",
        'srv_sworn': "الترجمة المحلفة", 'srv_sworn_short': "النصوص والوثائق المعتمدة ذات الصلاحية القانونية.",
        'srv_tech': "الترجمة المتخصصة", 'srv_tech_short': "وثائق تقنية للشركات والدلائل عالية الدقة.",
        'srv_visa': "إدارة التأشيرات", 'srv_visa_short': "إجراءات قنصلية سريعة للموظفين الأجانب.",
        'footer_rights': "© 2026 TIGAFAB S.L. جميع الحقوق محفوظة.",
        'exp_verificadas': "تجارب موثقة",
        'review_1': "خدمة مثالية واحترافية للغاية. أنجزت فاطمة الترجمة المحلفة لوثائقي في وقت قياسي.",
        'review_2': "نعتمد على تيگافاب منذ سنوات في استخراج التأشيرات والترجمة التقنية للغة العربية.",
        'review_3': "تعامل مباشر وأسعار ممتازة. ساعدوني كثيراً في تسجيل فرع شركتي في ليبيا.",
        'review_4': "فريق رائع من المترجمين المحترفين. أنجزوا جميع أوراق الهجرة بسرعة كبيرة."
    }
}

LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

def get_nav(lang, rel_path):
    t = TRANSLATIONS[lang]
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
    t = TRANSLATIONS[lang]
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    for key, val in t.items():
        content = content.replace(f't-{key.replace("_","-")}', str(val))
    full_html = f"""<!DOCTYPE html>
<html lang="{lang}" {is_rtl}>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t[title_key]} | TIGAFAB</title>
  <link rel="stylesheet" href="{rel_path}styles.css?v=12">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    [lang="ar"] {{ font-family: 'Tajawal', sans-serif !important; }}
    .marquee-container {{ cursor: grab; overflow: hidden; display: flex; position: relative; width: 100%; white-space: nowrap; }}
    .marquee-container:active {{ cursor: grabbing; }}
    .marquee-inner {{ display: flex; flex-shrink: 0; }}
  </style>
</head>
<body class="page-{filename.replace('.html','')}">
  {get_nav(lang, rel_path)}
  {content}
  <footer style="background:var(--bg-dark); color:white; padding:4rem 2rem; text-align:center;">
    <div style="font-family:var(--font-heading); font-size:2rem; margin-bottom:1rem;">TIGAFAB<span>.</span></div>
    <p>{t['footer_rights']}</p>
    <div style="margin-top:2rem; display:flex; justify-content:center; gap:1.5rem;">
      <a href="aviso-legal.html" style="color:white; text-decoration:none; font-size:0.9rem;">{t['nav_legal']}</a>
      <a href="privacidad.html" style="color:white; text-decoration:none; font-size:0.9rem;">{t['nav_privacy']}</a>
    </div>
  </footer>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
  <script src="{rel_path}js/main.js?v=12"></script>
  <script>AOS.init();</script>
</body>
</html>"""
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang])
    if not os.path.exists(target_dir): os.makedirs(target_dir)
    with open(os.path.join(target_dir, filename), "w", encoding="utf-8") as f: f.write(full_html)

# --- CONTENIDO DE LA HOME ---
index_html = """
  <section class="hero" style="position:relative; height:70vh; background: linear-gradient(rgba(15,23,42,0.5), rgba(15,23,42,0.5)), url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=1200') center/cover; display:flex; align-items:center; justify-content:center; text-align:center; color:white;">
    <div class="container" data-aos="fade-up">
      <h1 style="font-size:3.5rem; margin-bottom:1rem; font-family:var(--font-heading);">t-hero-title</h1>
      <p style="font-size:1.4rem; color:var(--primary); font-weight:500;">t-hero-subtitle</p>
    </div>
  </section>

  <section style="padding:6rem 2rem; background:#fff;">
    <div class="container" style="text-align:center; max-width:900px; margin:0 auto;">
      <h2 style="font-size:2.8rem; margin-bottom:1.5rem; font-family:var(--font-heading); color:var(--bg-dark);">t-home-welcome</h2>
      <div style="width:60px; height:3px; background:var(--primary); margin:0 auto 2rem;"></div>
      <p style="font-size:1.2rem; color:#475569; line-height:1.8;">t-home-welcome-sub</p>
    </div>
  </section>

  <section style="padding:6rem 2rem; background:var(--bg-light);">
    <div class="container">
      <div style="text-align:center; margin-bottom:4rem;">
        <h2 style="font-size:2.5rem; font-family:var(--font-heading); color:var(--bg-dark);">t-srv-specialized</h2>
        <p style="color:var(--primary); margin-top:0.5rem;">t-srv-view-all</p>
      </div>
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:2.5rem;">
        <div class="service-card" data-aos="fade-up">
          <div style="font-size:2rem; color:var(--primary); margin-bottom:1.5rem;"><i class="fas fa-file-signature"></i></div>
          <h3 style="margin-bottom:1rem; font-family:var(--font-heading);">t-srv-sworn</h3>
          <p style="color:#64748B; margin-bottom:1.5rem;">t-srv-sworn-short</p>
          <a href="servicios.html" style="color:var(--primary); font-weight:700; text-decoration:none;">t-srv-more <i class="fas fa-arrow-right"></i></a>
        </div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="100">
          <div style="font-size:2rem; color:var(--primary); margin-bottom:1.5rem;"><i class="fas fa-microchip"></i></div>
          <h3 style="margin-bottom:1rem; font-family:var(--font-heading);">t-srv-tech</h3>
          <p style="color:#64748B; margin-bottom:1.5rem;">t-srv-tech-short</p>
          <a href="servicios.html" style="color:var(--primary); font-weight:700; text-decoration:none;">t-srv-more <i class="fas fa-arrow-right"></i></a>
        </div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="200">
          <div style="font-size:2rem; color:var(--primary); margin-bottom:1.5rem;"><i class="fas fa-passport"></i></div>
          <h3 style="margin-bottom:1rem; font-family:var(--font-heading);">t-srv-visa</h3>
          <p style="color:#64748B; margin-bottom:1.5rem;">t-srv-visa-short</p>
          <a href="servicios.html" style="color:var(--primary); font-weight:700; text-decoration:none;">t-srv-more <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
    </div>
  </section>

  <!-- SECCIÓN RESEÑAS DINÁMICAS -->
  <section style="position:relative; padding:8rem 0; background: linear-gradient(rgba(15,23,42,0.85), rgba(15,23,42,0.85)), url('https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&q=80&w=1200') center/cover fixed; color:white; overflow:hidden;">
    <div class="container" style="text-align:center; margin-bottom:4rem;" data-aos="fade-up">
      <h2 style="font-size:2.8rem; font-family:var(--font-heading); margin-bottom:1rem;">t-reviews-title</h2>
      <p style="color:var(--primary); letter-spacing:2px; font-weight:600;"><i class="fab fa-google"></i> t-exp-verificadas</p>
    </div>
    
    <div class="marquee-container" id="reviewSlider" style="display: flex; overflow-x: hidden; white-space:nowrap; overflow:hidden; position:relative;">
      <div class="marquee-inner" style="display:inline-block; animation: marquee 35s linear infinite;">
        <!-- Card 1 -->
        <div style="display:inline-block; width:400px; margin: 0 1rem; background:rgba(255,255,255,0.05); padding:2rem; border-radius:12px; border:1px solid rgba(255,255,255,0.1); white-space:normal; vertical-align:top;">
          <div style="color:#FFD700; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p style="font-style:italic; color:#cbd5e1; margin-bottom:1rem;">"t-review-1"</p>
          <div style="font-weight:700;">María G.</div>
        </div>
        <!-- Card 2 -->
        <div style="display:inline-block; width:400px; margin: 0 1rem; background:rgba(255,255,255,0.05); padding:2rem; border-radius:12px; border:1px solid rgba(255,255,255,0.1); white-space:normal; vertical-align:top;">
          <div style="color:#FFD700; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p style="font-style:italic; color:#cbd5e1; margin-bottom:1rem;">"t-review-2"</p>
          <div style="font-weight:700;">Construction Group</div>
        </div>
        <!-- Card 3 -->
        <div style="display:inline-block; width:400px; margin: 0 1rem; background:rgba(255,255,255,0.05); padding:2rem; border-radius:12px; border:1px solid rgba(255,255,255,0.1); white-space:normal; vertical-align:top;">
          <div style="color:#FFD700; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p style="font-style:italic; color:#cbd5e1; margin-bottom:1rem;">"t-review-3"</p>
          <div style="font-weight:700;">Carlos S.</div>
        </div>
        <!-- Card 4 -->
        <div style="display:inline-block; width:400px; margin: 0 1rem; background:rgba(255,255,255,0.05); padding:2rem; border-radius:12px; border:1px solid rgba(255,255,255,0.1); white-space:normal; vertical-align:top;">
          <div style="color:#FFD700; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p style="font-style:italic; color:#cbd5e1; margin-bottom:1rem;">"t-review-4"</p>
          <div style="font-weight:700;">Ana M.</div>
        </div>
      </div>
      <!-- Clon para efecto infinito -->
      <div class="marquee-inner" style="display:inline-block; animation: marquee 35s linear infinite;">
        <div style="display:inline-block; width:400px; margin: 0 1rem; background:rgba(255,255,255,0.05); padding:2rem; border-radius:12px; border:1px solid rgba(255,255,255,0.1); white-space:normal; vertical-align:top;">
          <div style="color:#FFD700; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p style="font-style:italic; color:#cbd5e1; margin-bottom:1rem;">"t-review-1"</p>
          <div style="font-weight:700;">María G.</div>
        </div>
        <div style="display:inline-block; width:400px; margin: 0 1rem; background:rgba(255,255,255,0.05); padding:2rem; border-radius:12px; border:1px solid rgba(255,255,255,0.1); white-space:normal; vertical-align:top;">
          <div style="color:#FFD700; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p style="font-style:italic; color:#cbd5e1; margin-bottom:1rem;">"t-review-2"</p>
          <div style="font-weight:700;">Construction Group</div>
        </div>
        <div style="display:inline-block; width:400px; margin: 0 1rem; background:rgba(255,255,255,0.05); padding:2rem; border-radius:12px; border:1px solid rgba(255,255,255,0.1); white-space:normal; vertical-align:top;">
          <div style="color:#FFD700; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p style="font-style:italic; color:#cbd5e1; margin-bottom:1rem;">"t-review-3"</p>
          <div style="font-weight:700;">Carlos S.</div>
        </div>
        <div style="display:inline-block; width:400px; margin: 0 1rem; background:rgba(255,255,255,0.05); padding:2rem; border-radius:12px; border:1px solid rgba(255,255,255,0.1); white-space:normal; vertical-align:top;">
          <div style="color:#FFD700; margin-bottom:1rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p style="font-style:italic; color:#cbd5e1; margin-bottom:1rem;">"t-review-4"</p>
          <div style="font-weight:700;">Ana M.</div>
        </div>
      </div>
    </div>
  </section>

  <section style="padding:6rem 2rem; text-align:center; background:#fff;">
    <div style="max-width:700px; margin:0 auto;">
      <h2 style="font-size:2.8rem; font-family:var(--font-heading); margin-bottom:1.5rem;">t-home-cta-title</h2>
      <p style="color:#64748B; margin-bottom:3rem; font-size:1.1rem;">t-home-cta-sub</p>
      <a href="contacto.html" class="btn" style="background:var(--bg-dark); color:white; text-decoration:none; padding:1.2rem 3.5rem; font-size:1.1rem; box-shadow:0 10px 20px rgba(0,0,0,0.15);">t-home-cta-btn <i class="fas fa-paper-plane" style="margin-left:10px;"></i></a>
    </div>
  </section>
"""

for lang in LANG_FOLDERS:
    # Generamos todas las páginas para cada idioma
    generate_page(lang, "index.html", 'nav_home', index_html)
    generate_page(lang, "servicios.html", 'nav_services', '<section style="padding:10rem 2rem; text-align:center;"><h1 style="font-size:3rem;">t-nav-services</h1></section>')
    generate_page(lang, "contacto.html", 'nav_contact', '<section style="padding:10rem 2rem; text-align:center;"><h1 style="font-size:3rem;">t-nav-contact</h1></section>')
    generate_page(lang, "localizacion.html", 'nav_location', '<section style="padding:10rem 2rem; text-align:center;"><h1 style="font-size:3rem;">t-nav-location</h1></section>')
    generate_page(lang, "aviso-legal.html", 'nav_legal', '<section style="padding:10rem 2rem; text-align:center;"><h1 style="font-size:3rem;">t-nav-legal</h1></section>')
    generate_page(lang, "privacidad.html", 'nav_privacy', '<section style="padding:10rem 2rem; text-align:center;"><h1 style="font-size:3rem;">t-nav-privacy</h1></section>')

print("✅ ÉXITO: Sitio multi-idioma (incluyendo reseñas traducidas) generado.")
