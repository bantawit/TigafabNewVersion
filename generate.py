import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- DICCIONARIO MAESTRO ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_location': "Localización",
        'nav_legal': "Aviso Legal", 'nav_privacy': "Privacidad", 'hero_title': "Traducción e Interpretación",
        'hero_subtitle': "Árabe, Español, Inglés, Alemán y Francés", 'home_welcome': "Bienvenido a Nuestra Web",
        'home_welcome_sub': "Traducciones, Interpretación, Gestión y Asesoramiento",
        'srv_specialized': "Nuestros Servicios Especializados", 'reviews_title': "Lo que dicen nuestros clientes",
        'home_cta_title': "¿Listo para empezar?", 'home_cta_sub': "Obtenga su presupuesto sin compromiso hoy mismo.",
        'home_cta_btn': "Contactar con Fátima", 'srv_more': "Saber más", 'srv_view_all': "Ver todos los servicios",
        'srv_sworn_short': "Documentación certificada con total validez jurídica.",
        'srv_sworn': "Traducciones Juradas", 
        'srv_tech_short': "Especialistas en manuales y textos corporativos.",
        'srv_tech': "Traducciones Técnicas",
        'srv_visa_short': "Trámites consulares y legalizaciones.",
        'srv_visa': "Gestión de Visados",
        'srv_docs': "Gestión Documental",
        'srv_docs_short': "Burocracia directa con ministerios y embajadas.",
        'srv_business': "Asesoría Libia",
        'srv_business_short': "Expertos en la apertura de empresas en el mercado Libio.",
        'footer_rights': "© 2026 TIGAFAB S.L. Todos los derechos reservados.",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS",
        'orig_label': "Original",
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
        'nav_legal': "Legal Notice", 'nav_privacy': "Privacy", 'hero_title': "Translation & Interpretation",
        'hero_subtitle': "Arabic, Spanish, English, German and French", 'home_welcome': "Welcome to Our Website",
        'home_welcome_sub': "Translations, Interpretation, Management and Consulting",
        'srv_specialized': "Our Specialized Services", 'reviews_title': "What our clients say",
        'home_cta_title': "Ready to start?", 'home_cta_sub': "Get your no-obligation quote today.",
        'home_cta_btn': "Contact Fatima", 'srv_more': "Learn more", 'srv_view_all': "View all services",
        'srv_sworn_short': "Certified texts and documentation with legal validity.",
        'srv_sworn': "Sworn Translations",
        'srv_tech_short': "Specialists in manuals and corporate texts.",
        'srv_tech': "Technical Translations",
        'srv_visa_short': "Consular procedures and legalizations.",
        'srv_visa': "Visa Management",
        'srv_docs': "Document Management",
        'srv_docs_short': "Direct bureaucracy with ministries and embassies.",
        'srv_business': "Libya Consulting",
        'srv_business_short': "Experts in business setup for the Libyan market.",
        'footer_rights': "© 2026 TIGAFAB S.L. All rights reserved.",
        'exp_verificadas': "VERIFIED EXPERIENCES",
        'orig_label': "Original",
        'r1': "Impeccable and very professional service. Fatima resolved the sworn translation of my documents in record time for an urgent procedure. Highly recommended.",
        'r2': "We have relied on Tigafab for years to process visas and technical Arabic translations for our business files. Fast and effective.",
        'r3': "Direct treatment and very good rates. They helped me a lot with the registration of my branch and services in Libya, from contracts to consulting. 10/10.",
        'r4': "Great team of professional translators. They resolved all the immigration paperwork and Chamber of Commerce certificates very quickly.",
        'r5': "Excellent service in Madrid. They translated my passport and a corporate contract with absolute precision.",
        'r6': "Tigafab advised us from Fuenlabrada on opening a branch in North Africa. The human quality of their team is incredible.",
        'r7': "British punctuality and a brutal level of confidentiality. Working with Ms. Fatima reassures all our international procedures.",
        'r8': "There is no real competition in the deadlines they handle. The entire package of sworn Arabic translations was impeccably ready."
    },
    'fr': {
        'nav_home': "Accueil", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_location': "Localisation",
        'nav_legal': "Mentions Légales", 'nav_privacy': "Confidentialité", 'hero_title': "Traduction & Interprétation",
        'hero_subtitle': "Arabe, Espagnol, Anglais, Allemand et Français", 'home_welcome': "Bienvenue sur notre site",
        'home_welcome_sub': "Traductions, Interprétation, Gestion et Conseil",
        'srv_specialized': "Nos services spécialisés", 'reviews_title': "Ce que disent nos clients",
        'home_cta_title': "Prêt à commencer ?", 'home_cta_sub': "Obtenez votre devis sans engagement dès aujourd'hui.",
        'home_cta_btn': "Contacter Fatima", 'srv_more': "En savoir plus", 'srv_view_all': "Voir tous les servicios",
        'srv_sworn_short': "Documents certifiés avec validité juridique totale.",
        'srv_sworn': "Traductions Assermentées",
        'srv_tech_short': "Spécialistes des manuels et textes d'entreprise.",
        'srv_tech': "Traductions Techniques",
        'srv_visa_short': "Démarches consulaires et légalisations.",
        'srv_visa': "Gestion des Visas",
        'srv_docs': "Gestion Documentaire",
        'srv_docs_short': "Bureaucratie directe avec ministères et ambassades.",
        'srv_business': "Conseil Libye",
        'srv_business_short': "Experts en création d'entreprise sur le marché libyen.",
        'footer_rights': "© 2026 TIGAFAB S.L. Tous droits réservés.",
        'exp_verificadas': "EXPÉRIENCES VÉRIFIÉES",
        'orig_label': "Original",
        'r1': "Service impeccable et profesional. Fatima a résolu la traduction assermentée de mes documents en un temps record pour une procédure urgente. Hautement recommandé.",
        'r2': "Nous faisons confiance à Tigafab depuis des années pour nos visas et traductions techniques vers l'arabe. Rapides et efficaces.",
        'r3': "Excellents tarifs et contact direct. Ils m'ont beaucoup aidé pour l'enregistrement de ma succursale en Libye. 10/10.",
        'r4': "Excellente équipe de professionnels. Ils ont résolu toutes mes procédures d'immigration très rápidamente.",
        'r5': "Excellent service à Madrid. Ils ont traduit mon passeport et un contrat d'entreprise de manière impeccable.",
        'r6': "Tigafab nous a conseillés desde Fuenlabrada pour l'ouverture d'une succursale en Afrique du Nord. L'équipe est incroyable.",
        'r7': "Ponctualité britannique et une grande confidentialité. Travailler avec Madame Fatima est rassurant.",
        'r8': "Il n'y a pas de concurrence concernant leur rapidité. Le paquet entier de traductions vers l'arabe était parfait."
    },
    'de': {
        'nav_home': "Startseite", 'nav_services': "Dienstleistungen", 'nav_contact': "Kontakt", 'nav_location': "Standort",
        'nav_legal': "Impressum", 'nav_privacy': "Datenschutz", 'hero_title': "Übersetzung & Dolmetschen",
        'hero_subtitle': "Arabisch, Spanisch, Englisch, Deutsch und Französisch", 'home_welcome': "Willkommen auf unserer Website",
        'home_welcome_sub': "Übersetzungen, Dolmetschen, Management und Beratung",
        'srv_specialized': "Unsere Fachdienstleistungen", 'reviews_title': "Was unsere Kunden sagen",
        'home_cta_title': "Bereit zu starten?", 'home_cta_sub': "Holen Sie sich noch heute Ihr unverbindliches Angebot.",
        'home_cta_btn': "Fatima kontaktieren", 'srv_more': "Mehr erfahren", 'srv_view_all': "Alle Dienste anzeigen",
        'srv_sworn_short': "Zertifizierte Dokumentation mit voller Rechtsgültigkeit.",
        'srv_sworn': "Beglaubigte Übersetzungen",
        'srv_tech_short': "Spezialisten für Handbücher und Firmentexte.",
        'srv_tech': "Technische Übersetzungen",
        'srv_visa_short': "Konsularische Verfahrung und Beglaubigungen.",
        'srv_visa': "Visum-Management",
        'srv_docs': "Dokumentenmanagement",
        'srv_docs_short': "Direkte Bürokratie mit Ministerien und Botschaften.",
        'srv_business': "Libyen-Beratung",
        'srv_business_short': "Experten für Geschäftsaufbau im libyschen Markt.",
        'footer_rights': "© 2026 TIGAFAB S.L. Alle Rechte vorbehalten.",
        'exp_verificadas': "VERIFIZIERTE ERFAHRUNGEN",
        'orig_label': "Original",
        'r1': "Tadelloser und sehr professioneller Service. Fatima hat die beglaubigte Übersetzung meiner Dokumente in Rekordzeit erledigt. Sehr zu empfehlen.",
        'r2': "Wir verlassen uns seit Jahren auf Tigafab für unsere Visa und technischen Arabisch-Übersetzungen. Schnell und effektiv.",
        'r3': "Sehr gute Preise und direkter Kontakt. Sie haben mir sehr bei der Gründung meiner Niederlassung in Libyen geholfen. 10/10.",
        'r4': "Tolles Team von professionellen Übersetzern. Sie haben alle Einwanderungspapiere sehr schnell erledigt.",
        'r5': "Ausgezeichneter Service in Madrid. Sie haben meinen Pass und einen Vertrag sehr genau übersetzt.",
        'r6': "Tigafab beriet uns bei der Eröffnung einer Niederlassung in Nordafrika. Die menschliche Qualität ist unglaublich.",
        'r7': "Britische Pünktlichkeit und Vertraulichkeit. Die Zusammenarbeit mit Frau Fatima beruhigt unsere Abläufe.",
        'r8': "Es gibt keine wirkliche Konkurrenz bei ihren Fristen. Das gesamte Übersetzungspaket war einwandfrei."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_location': "الموقع",
        'nav_legal': "إشعار قانوني", 'nav_privacy': "الخصوصية", 'hero_title': "الترجمة التحريرية والشفوية",
        'hero_subtitle': "العربية، الإسبانية، الإنجليزية، الألمانية والفرنسية", 'home_welcome': "مرحباً بكم في موقعنا",
        'home_welcome_sub': "الترجمة، الإدارة والاستشارات",
        'srv_specialized': "خدماتنا المتخصصة", 'reviews_title': "ماذا يقول عملاؤنا",
        'home_cta_title': "هل أنت مستعد للبدء؟", 'home_cta_sub': "احصل على عرض سعر بدون التزام اليوم.",
        'home_cta_btn': "اتصل بفاطمة", 'srv_more': "معرفة المزيد", 'srv_view_all': "عرض جميع الخدمات",
        'srv_sworn_short': "النصوص والوثائق المعتمدة ذات الصلاحية القانونية.",
        'srv_sworn': "الترجمة المحلفة", 
        'srv_tech_short': "وثائق تقنية للشركات والدلائل عالية الدقة.",
        'srv_tech': "الترجمة المتخصصة",
        'srv_visa_short': "إجراءات قنصلية سريعة للموظفين الأجانب.",
        'srv_visa': "إدارة التأشيرات",
        'srv_docs': "إدارة الوثائق",
        'srv_docs_short': "إجراءات مباشرة مع الوزارات والسفارات.",
        'srv_business': "استشارات ليبيا",
        'srv_business_short': "خبراء في تأسيس الشركات بالسوق الليبي.",
        'footer_rights': "© 2026 TIGAFAB S.L. جميع الحقوق محفوظة.",
        'exp_verificadas': "تجارب موثقة",
        'orig_label': "الأصل",
        'r1': "خدمة لا تشوبها شائبة واحترافية للغاية. أنجزت فاطمة الترجمة المحلفة لوثائقي في وقت قياسي لإجراء عاجل. موصى به بشدة.",
        'r2': "نعتمد على تيگافاب منذ سنوات في استخراج التأشيرات والترجمة التقنية لملفاتنا. سريعون وفعالون.",
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
    sorted_keys = sorted(t.keys(), key=len, reverse=True)
    full_html = f"""<!DOCTYPE html>
<html lang="{lang}" {is_rtl}>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t[title_key]} | TIGAFAB</title>
  <link rel="stylesheet" href="{rel_path}styles.css?v=22">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap');
    [lang="ar"] {{ font-family: 'Tajawal', sans-serif !important; }}
    .marquee-container {{ cursor: grab; overflow: hidden; display: flex; position: relative; width: 100%; white-space: nowrap; }}
    .marquee-container:active {{ cursor: grabbing; }}
    .marquee-inner {{ display: flex; flex-shrink: 0; flex-wrap: nowrap; }}
    .service-card {{ background: #fff; padding: 2.5rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: all 0.3s ease; text-decoration:none; display:block; height:100%; color:inherit; }}
    .service-card:hover {{ transform: translateY(-10px); color: var(--primary); }}
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
  <script src="{rel_path}js/main.js?v=22"></script>
  <script>AOS.init();</script>
</body>
</html>"""
    for key in sorted_keys:
        full_html = full_html.replace(f't-{key.replace("_","-")}', str(t[key]))
    target_dir = os.path.join(BASE_DIR, LANG_FOLDERS[lang])
    if not os.path.exists(target_dir): os.makedirs(target_dir)
    with open(os.path.join(target_dir, filename), "w", encoding="utf-8") as f: f.write(full_html)

def get_review_cards(lang):
    t_curr = TRANSLATIONS[lang]; t_es = TRANSLATIONS['es']
    items = []
    for i in range(1, 9):
        bilingual_html = f'<p style="font-style:italic; color:#cbd5e1; line-height:1.6; margin-bottom:1rem;">{t_curr[f"r{i}"]}</p>'
        if lang != 'es':
            bilingual_html += f'<p style="font-size:0.85rem; color:rgba(255,255,255,0.4); border-top:1px solid rgba(255,255,255,0.1); padding-top:0.8rem; font-style:italic;"><span style="color:var(--primary); font-weight:700;">{t_curr["orig_label"]} (ES):</span> {t_es[f"r{i}"]}</p>'
        items.append(f'<div style="flex:0 0 550px; margin: 0 1.5rem; background:rgba(255,255,255,0.05); padding:2.5rem; border-radius:15px; border:1px solid rgba(255,255,255,0.1); white-space:normal;"><div style="color:#FFD700; margin-bottom:1.5rem;"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>{bilingual_html}<div style="font-weight:700; margin-top:1.5rem; color:white;">{t_es[f"n{i}"]}</div></div>')
    return "".join(items) + "".join(items)

# --- CONTENIDO DE LAS PÁGINAS ---
index_html = """
  <section class="hero" style="position:relative; height:70vh; background: linear-gradient(rgba(15,23,42,0.5), rgba(15,23,42,0.5)), url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=1200') center/cover; display:flex; align-items:center; justify-content:center; text-align:center; color:white;">
    <div class="container" data-aos="fade-up">
      <h1 style="font-size:3.5rem; margin-bottom:1rem; font-family:var(--font-heading);">t-hero-title</h1>
      <p style="font-size:1.4rem; color:var(--primary); font-weight:500;">t-hero-subtitle</p>
    </div>
  </section>
  <section style="padding:4rem 2rem; background:var(--bg-light);">
    <div class="container">
      <div style="text-align:center; margin-bottom:4rem;"><h2 style="font-size:2.5rem; font-family:var(--font-heading); color:var(--bg-dark);">t-srv-specialized</h2></div>
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:2.5rem;">
        <div class="service-card" data-aos="fade-up"><h3>t-srv-sworn</h3><p>t-srv-sworn-short</p></div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="100"><h3>t-srv-tech</h3><p>t-srv-tech-short</p></div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="200"><h3>t-srv-visa</h3><p>t-srv-visa-short</p></div>
      </div>
    </div>
  </section>
  <section style="position:relative; padding:8rem 0; background: linear-gradient(rgba(15,23,42,0.85), rgba(15,23,42,0.85)), url('https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&q=80&w=1200') center/cover fixed; color:white; overflow:hidden;">
    <div class="container" style="text-align:center; margin-bottom:4rem;"><h2 style="font-size:2.8rem; font-family:var(--font-heading); margin-bottom:1rem;">t-reviews-title</h2><p style="color:var(--primary); letter-spacing:2px; font-weight:600;"><i class="fab fa-google"></i> t-exp-verificadas</p></div>
    <div class="marquee-container" id="reviewSlider"><div class="marquee-inner">REPLACE_WITH_CARDS</div></div>
  </section>
"""

services_html = """
  <section style="padding:10rem 2rem; background:var(--bg-dark); color:white; text-align:center;">
    <div class="container" data-aos="zoom-in">
      <h1 style="font-size:4rem; font-family:var(--font-heading);">t-nav-services</h1>
      <p style="color:var(--primary); font-size:1.2rem;">Soluciones profesionales en 5 idiomas</p>
    </div>
  </section>
  <section style="padding:6rem 2rem; background:var(--bg-light);">
    <div class="container">
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap:3rem;">
        <div class="service-card" data-aos="fade-up">
          <div style="font-size:3rem; color:var(--primary); margin-bottom:1rem;"><i class="fas fa-file-contract"></i></div>
          <h2 style="font-size:1.8rem; margin-bottom:1rem;">t-srv-sworn</h2>
          <p style="margin-bottom:1rem; color:#4a5568;">t-srv-sworn-short</p>
          <ul style="list-style:none; padding:0; line-height:2;">
            <li><i class="fas fa-check" style="color:green; margin-right:10px;"></i> Pasaportes y Títulos</li>
            <li><i class="fas fa-check" style="color:green; margin-right:10px;"></i> Escrituras y Poderes</li>
          </ul>
        </div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="100">
          <div style="font-size:3rem; color:var(--primary); margin-bottom:1rem;"><i class="fas fa-gears"></i></div>
          <h2 style="font-size:1.8rem; margin-bottom:1rem;">t-srv-tech</h2>
          <p style="margin-bottom:1rem; color:#4a5568;">t-srv-tech-short</p>
          <ul style="list-style:none; padding:0; line-height:2;">
            <li><i class="fas fa-check" style="color:green; margin-right:10px;"></i> Manuales Industriales</li>
            <li><i class="fas fa-check" style="color:green; margin-right:10px;"></i> Textos Científicos</li>
          </ul>
        </div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="200">
          <div style="font-size:3rem; color:var(--primary); margin-bottom:1.5rem;"><i class="fas fa-passport"></i></div>
          <h2 style="font-size:1.8rem; margin-bottom:1rem;">t-srv-visa</h2>
          <p style="margin-bottom:1rem; color:#4a5568;">t-srv-visa-short</p>
        </div>
        <div class="service-card" data-aos="fade-up">
          <div style="font-size:3rem; color:var(--primary); margin-bottom:1.5rem;"><i class="fas fa-building-columns"></i></div>
          <h2 style="font-size:1.8rem; margin-bottom:1rem;">t-srv-docs</h2>
          <p style="margin-bottom:1rem; color:#4a5568;">t-srv-docs-short</p>
        </div>
        <div class="service-card" data-aos="fade-up" data-aos-delay="100">
          <div style="font-size:3rem; color:var(--primary); margin-bottom:1.5rem;"><i class="fas fa-briefcase"></i></div>
          <h2 style="font-size:1.8rem; margin-bottom:1rem;">t-srv-business</h2>
          <p style="margin-bottom:1rem; color:#4a5568;">t-srv-business-short</p>
        </div>
      </div>
    </div>
  </section>
"""

for lang in LANG_FOLDERS:
    generate_page(lang, "index.html", 'nav_home', index_html.replace('REPLACE_WITH_CARDS', get_review_cards(lang)))
    generate_page(lang, "servicios.html", 'nav_services', services_html)
    generate_page(lang, "contacto.html", 'nav_contact', '<section style="padding:10rem 2rem; text-align:center;"><h1 style="font-size:3rem;">t-nav-contact</h1></section>')
    generate_page(lang, "localizacion.html", 'nav_location', '<section style="padding:10rem 2rem; text-align:center;"><h1 style="font-size:3rem;">t-nav-location</h1></section>')
    generate_page(lang, "aviso-legal.html", 'nav_legal', '<section style="padding:10rem 2rem; text-align:center;"><h1 style="font-size:3rem;">t-nav-legal</h1></section>')
    generate_page(lang, "privacidad.html", 'nav_privacy', '<section style="padding:10rem 2rem; text-align:center;"><h1 style="font-size:3rem;">t-nav-privacy</h1></section>')

print("✅ ÉXITO: Página de servicios restaurada y completa en todos los idiomas.")
