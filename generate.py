import os
import re
import json

# Directorio base
BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# Idiomas y carpetas
LANGUAGES = {
    'es': '',
    'en': 'en',
    'fr': 'fr',
    'de': 'de',
    'ar': 'ar'
}

# --- EXTRACTOR DE TRADUCCIONES ---
def load_translations():
    with open(os.path.join(BASE_DIR, "js/i18n.js"), "r", encoding="utf-8") as f:
        js_content = f.read()
    
    # Extraer el objeto JSON del archivo JS mediante regex
    match = re.search(r"window\.translations\s*=\s*(\{.*?\});", js_content, re.DOTALL)
    if not match:
        raise Exception("No se pudo encontrar el objeto de traducciones en i18n.js")
    
    # Limpiar el JS para que sea JSON válido (quitar comas finales, ajustar strings)
    # Nota: Este es un parser simple, si i18n.js es muy complejo fallará. 
    # Para ser robustos, usamos el diccionario directamente en Python si el JS es complejo.
    return {
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
            'footer_rights': "© 2026 TIGAFAB S.L. Todos los derechos reservados."
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
            'footer_rights': "© 2026 TIGAFAB S.L. All rights reserved."
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
            'srv_tech': "Traducciones Técnicas", 'srv_tech_short': "Spécialistes des manuels et textes d'entreprise.",
            'srv_visa': "Gestion des Visas", 'srv_visa_short': "Démarches consulaires et légalisations.",
            'footer_rights': "© 2026 TIGAFAB S.L. Tous droits réservés."
        },
        'de': {
            'nav_home': "Startseite", 'nav_services': "Dienstleistungen", 'nav_contact': "Kontakt", 'nav_location': "Standort",
            'nav_legal': "Impressum", 'nav_privacy': "Datenschutz", 'hero_title': "Übersetzung & Dolmetschen",
            'hero_subtitle': "Arabisch, Spanisch, Englisch, Deutsch und Französisch", 'home_welcome': "Willkommen auf unserer Website",
            'home_welcome_sub': "Übersetzungen, Dolmetschen, Management und Beratung",
            'srv_specialized:': "Unsere Fachdienstleistungen", 'reviews_title': "Was unsere Kunden sagen",
            'home_cta_title': "Bereit zu starten?", 'home_cta_sub': "Holen Sie sich noch heute Ihr unverbindliches Angebot.",
            'home_cta_btn': "Fatima kontaktieren", 'srv_more': "Mehr erfahren", 'srv_view_all': "Alle Dienste anzeigen",
            'srv_sworn': "Beglaubigte Übersetzungen", 'srv_sworn_short': "Zertifizierte Dokumentation mit voller Rechtsgültigkeit.",
            'srv_tech': "Technische Übersetzungen", 'srv_tech_short': "Spezialisten für Handbücher und Firmentexte.",
            'srv_visa': "Visum-Management", 'srv_visa_short': "Konsularische Verfahrung und Beglaubigungen.",
            'footer_rights': "© 2026 TIGAFAB S.L. Alle Rechte vorbehalten."
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
            'footer_rights': "© 2026 TIGAFAB S.L. جميع الحقوق محفوظة."
        }
    }

TRANSLATIONS = load_translations()

def get_nav(lang, rel_path):
    t = TRANSLATIONS[lang]
    # Determinar prefijos para los enlaces de idioma
    lang_links = ""
    for l_code, l_folder in LANGUAGES.items():
        active_class = "active" if l_code == lang else ""
        # Si estoy en raíz y voy a raíz: index.html
        # Si estoy en carpeta y voy a raíz: ../index.html
        # Si estoy en raíz y voy a carpeta: carpeta/index.html
        # Si estoy en carpeta y voy a carpeta: ../carpeta/index.html
        
        target_path = "index.html"
        if l_code == 'es':
            href = rel_path + target_path
        else:
            href = rel_path + l_folder + "/" + target_path
            
        lang_links += f'<a href="{href}" class="lang-btn {active_class}">{l_code.upper()}</a>'

    return f"""
  <nav id="navbar">
    <div class="nav-container">
      <a href="{rel_path}index.html" class="logo">TIGAFAB<span>.</span></a>
      <ul class="nav-links" id="navMenu">
        <li><a href="index.html" class="nav-home">{t.get('nav_home')}</a></li>
        <li><a href="servicios.html" class="nav-services">{t.get('nav_services')}</a></li>
        <li><a href="contacto.html" class="nav-contact">{t.get('nav_contact')}</a></li>
        <li><a href="localizacion.html" class="nav-location">{t.get('nav_location')}</a></li>
      </ul>
      <div class="lang-selector">
        {lang_links}
      </div>
    </div>
  </nav>
"""

def generate_page(lang, filename, title, content):
    rel_path = "../" if lang != 'es' else ""
    t = TRANSLATIONS[lang]
    is_rtl = 'dir="rtl"' if lang == 'ar' else 'dir="ltr"'
    
    # Reemplazar marcadores t- en el contenido
    for key, val in t.items():
        marker = f't-{key.replace("_","-")}'
        content = content.replace(marker, val)

    full_html = f"""<!DOCTYPE html>
<html lang="{lang}" {is_rtl}>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | TIGAFAB</title>
  <link rel="stylesheet" href="{rel_path}styles.css?v=10">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    [lang="ar"] {{ font-family: 'Tajawal', sans-serif !important; }}
  </style>
</head>
<body class="page-{filename.replace('.html','')}">
  {get_nav(lang, rel_path)}
  {content}
  <footer style="background:var(--bg-dark); color:white; padding:4rem 2rem; text-align:center;">
    <div class="footer-logo" style="font-family:var(--font-heading); font-size:2rem; margin-bottom:1rem;">TIGAFAB<span>.</span></div>
    <p>{t.get('footer_rights')}</p>
    <div style="margin-top:2rem; display:flex; justify-content:center; gap:1.5rem;">
      <a href="aviso-legal.html" style="color:white; text-decoration:none;">{t.get('nav_legal')}</a>
      <a href="privacidad.html" style="color:white; text-decoration:none;">{t.get('nav_privacy')}</a>
    </div>
  </footer>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
  <script src="{rel_path}js/main.js?v=10"></script>
  <script>AOS.init();</script>
</body>
</html>"""

    # Guardar archivo
    target_dir = os.path.join(BASE_DIR, LANGUAGES[lang])
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    with open(os.path.join(target_dir, filename), "w", encoding="utf-8") as f:
        f.write(full_html)

# --- GENERACIÓN DE PÁGINAS ---
index_content = """
  <section class="hero" style="position:relative; height:80vh; background: url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=1200') center/cover; display:flex; align-items:center; justify-content:center; text-align:center; color:white;">
    <div style="position:absolute; inset:0; background:rgba(15,23,42,0.6);"></div>
    <div class="container" style="position:relative; z-index:1;" data-aos="fade-up">
      <h1 style="font-size:4rem; margin-bottom:1rem;">t-hero-title</h1>
      <p style="font-size:1.5rem; color:var(--primary);">t-hero-subtitle</p>
    </div>
  </section>

  <section style="padding:6rem 2rem;">
    <div class="container" style="text-align:center;">
      <h2 style="font-size:3rem; margin-bottom:2rem;">t-home-welcome</h2>
      <p style="max-width:800px; margin:0 auto; font-size:1.2rem; color:#475569;">t-home-welcome-sub</p>
    </div>
  </section>

  <section style="padding:4rem 2rem; background:var(--bg-light);">
    <div class="container">
      <h2 style="text-align:center; margin-bottom:4rem;">t-srv-specialized</h2>
      <div class="services-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:2rem;">
        <div class="service-card" data-aos="fade-up">
          <h3>t-srv-sworn</h3>
          <p>t-srv-sworn-short</p>
        </div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="100">
          <h3>t-srv-tech</h3>
          <p>t-srv-tech-short</p>
        </div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="200">
          <h3>t-srv-visa</h3>
          <p>t-srv-visa-short</p>
        </div>
      </div>
    </div>
  </section>

  <section style="padding:6rem 2rem; text-align:center; background:var(--primary); color:white;">
    <h2 style="font-size:2.5rem; margin-bottom:1.5rem;">t-home-cta-title</h2>
    <p style="margin-bottom:2rem;">t-home-cta-sub</p>
    <a href="contacto.html" class="btn" style="background:white; color:var(--primary); padding:1rem 3rem; border-radius:50px; text-decoration:none; font-weight:700;">t-home-cta-btn</a>
  </section>
"""

for lang in LANGUAGES:
    print(f"Generando {lang}...")
    generate_page(lang, "index.html", TRANSLATIONS[lang]['nav_home'], index_content)
    # Aquí puedes añadir el resto de páginas (servicios, contacto, etc.)
    generate_page(lang, "servicios.html", TRANSLATIONS[lang]['nav_services'], "<h1>t-nav-services</h1>")
    generate_page(lang, "contacto.html", TRANSLATIONS[lang]['nav_contact'], "<h1>t-nav-contact</h1>")
    generate_page(lang, "localizacion.html", TRANSLATIONS[lang]['nav_location'], "<h1>t-nav-location</h1>")
    generate_page(lang, "aviso-legal.html", TRANSLATIONS[lang]['nav_legal'], "<h1>t-nav-legal</h1>")
    generate_page(lang, "privacidad.html", TRANSLATIONS[lang]['nav_privacy'], "<h1>t-nav_privacy</h1>")

print("¡Hecho! Sitio multi-ruta generado.")
