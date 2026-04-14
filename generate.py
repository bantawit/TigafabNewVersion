import os

BASE_DIR = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

# --- CONSTANTES DE ESTRUCTURA ---
LANG_NAMES = {'es': 'Español', 'en': 'English', 'fr': 'Français', 'de': 'Deutsch', 'ar': 'العربية'}
LANG_FOLDERS = {'es': '', 'en': 'en', 'fr': 'fr', 'de': 'de', 'ar': 'ar'}

# --- DICCIONARIO MAESTRO CON TEXTO ORIGINAL CLIENTE ---
TRANSLATIONS = {
    'es': {
        'nav_home': "Inicio", 'nav_services': "Servicios", 'nav_contact': "Contacto", 'nav_lang': "Idioma",
        'hero_title': "Excelencia en Traducción",
        'hero_subtitle': "ÁRABE • ESPAÑOL • INGLÉS • ALEMÁN • FRANCÉS",
        'home_cta_btn': "SOLICITAR PRESUPUESTO",
        'h1': "Somos un despacho de traductores e interpretes oficiales, jurados, nativos profesionales, encabezados por doña Fatima Benamar, con más de 15 años de experiencia. Ofrecemos a nuestros clientes un servicio rápido, personalizado, puntualidad, máxima calidad, confidencialidad, asesoramiento, trato directo y tarifas ajustadas.",
        'h2': "OFRECEMOS un servicio integral en traducción jurada y asesoramiento para la tramitación de todos sus documentos.",
        'h3': "A través de nuestro asesoramiento y atención personalizada le garantizamos una tramitación correcta. De esta forma se ahorrará mucho tiempo, dinero y disgustos.",
        'h4': "Siempre satisfacemos a nuestros clientes. Y nos comprometemos a entregar el trabajo en el plazo acordado.",
        'h5': "Cada vez son más las empresas españolas que se proyectan al exterior que cuentan con nuestros servicios de traducción, gestión y asesoramiento para su expansión en el mercado internacional, ofrecemos servicio de introducción de empresas constructoras en el país LIBIA, por ello contamos con agentes y empresarios en Libia, con proyectos adjudicados, proporcionamos todo el asesoramiento, consejos y traductores en Libia, para asistir a sus reuniones en sus viajes en este país.",
        'h6': "Nuestras tarifas de precios sin competencia y nuestro equipo técnico especializado hacen de nosotros un punto de referencia en el sector. Hemos realizado proyectos para diferentes empresas. Estamos avalados por muchas grandes empresas españolas e internacionales.",
        'reviews_title': "Confianza Global",
        'exp_verificadas': "EXPERIENCIAS VERIFICADAS",
        'footer_rights': "© 2026 TIGAFAB S.L. Boutique de Traducción Jurada."
    },
    'en': {
        'nav_home': "Home", 'nav_services': "Services", 'nav_contact': "Contact", 'nav_lang': "Language",
        'hero_title': "Translation Excellence",
        'home_cta_btn': "REQUEST A QUOTATION",
        'h1': "We are an office of official, sworn, native professional translators and interpreters, led by Ms. Fatima Benamar, with more than 15 years of experience. We offer our clients a fast, personalized service, punctuality, maximum quality, confidentiality, advice, direct contact and adjusted rates.",
        'h2': "WE OFFER an integral service in sworn translation and advice for the processing of all your documents.",
        'h3': "Through our advice and personalized attention we guarantee correct processing. In this way you will save a lot of time, money and trouble.",
        'h4': "We always satisfy our clients. And we commit to delivering the work within the agreed period.",
        'h5': "More and more Spanish companies projecting abroad rely on our translation, management and consulting services for their expansion in the international market. We offer a service for introducing construction companies in LIBYA, which is why we have agents and businessmen in Libya, with awarded projects, we provide all the advice, tips and translators in Libya, to attend your meetings on your trips in this country.",
        'h6': "Our unbeatable price rates and our specialized technical team make us a reference point in the sector. We have carried out projects for various companies. We are endorsed by many large Spanish and international companies.",
        'reviews_title': "Global Trust",
        'exp_verificadas': "VERIFIED EXPERIENCES",
        'footer_rights': "© 2026 TIGAFAB S.L. Sworn Translation Boutique."
    },
    'ar': {
        'nav_home': "الرئيسية", 'nav_services': "الخدمات", 'nav_contact': "اتصل بنا", 'nav_lang': "اللغة",
        'h1': "نحن مكتب للمترجمين التحريريين والفوريين الرسميين والمحلفين والمواطنين المحترفين، بقيادة السيدة فاطمة بنعمر، ومع أكثر من 15 عامًا من الخبرة. نحن نقدم لعملائنا خدمة سريعة وشخصية، ودقة في المواعيد، وأعلى جودة، وسرية، واستشارات، وتعامل مباشر وأسعار معدلة.",
        'h2': "نقدم خدمة شاملة في الترجمة المعتمدة والاستشارات لمعالجة جميع وثائقك.",
        'h3': "من خلال استشاراتنا واهتمامنا الشخصي نضمن لك المعالجة الصحيحة. وبهذه الطريقة ستوفر الكثير من الوقت والمال والمشاكل.",
        'h4': "نحن دائماً نرضي عملائنا. ونحن نلتزم بتسليم العمل في غضون الفترة المتفق عليها.",
        'h5': "تعتمد المزيد والمزيد من الشركات الإسبانية التي تتوسع في الخارج على خدمات الترجمة والإدارة والاستشارات للتوسع في السوق الدولية، ونقدم خدمة تقديم شركات البناء في بلد ليبيا، ولهذا السبب لدينا وكلاء ورجال أعمال في ليبيا، مع مشاريع مرساة، ونحن نقدم جميع الاستشارات والنصائح والمترجمين في ليبيا، لحضور اجتماعاتك في رحلاتك في هذا البلد.",
        'h6': "إن أسعارنا التي لا تقبل المنافسة وفريقنا الفني المتخصص يجعل منا نقطة مرجعية في هذا القطاع. لقد نفذنا مشاريع لشركات مختلفة. نحن مدعومون من قبل العديد من الشركات الإسبانية والدولية الكبرى.",
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
        ("Marta (Google)", "Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord para un trámite urgente que me pedían por sorpresa. Su trato y rapidez son excelentes, me dio mucha tranquilidad."),
        ("Mohamed (Google)", "Gente muy profesional y muy amable. Lo recomiendo 100% para cualquier gestión de traducción o visados. Me ayudaron con el registro en un tiempo récord y con una calidad técnica insuperable."),
        ("Juan Carlos (Google)", "Atención excepcional y rapidez. Necesitaba una traducción jurada de árabe a español para el ministerio y estuvo lista en menos de 24 horas. Rigurosos y con un precio muy competitivo."),
        ("Laila (Google)", "La mejor agencia de Madrid para traducción de árabe. Son extremadamente serios con los plazos de entrega, algo vital para licitaciones. Trato exquisito por parte de todo el equipo técnico."),
        ("Constructor S.A. (Google)", "Indispensables para nuestras licitaciones en el norte de África. Su conocimiento del mercado libio y del vocabulario técnico de construcción nos ha permitido cerrar contratos muy complejos con éxito."),
        ("Irene (Google)", "Fátima es encantadora y una profesional de primer nivel. Hizo que un trámite burocrático difícil fuera sencillo y fluido. Recomiendo Tigafab a cualquiera que busque calidad y rigor."),
        ("Sami (Google)", "Servicio de visados para Libia rápido y sin incidencias. Tienen los contactos y el conocimiento necesario para que no haya retrasos. Altamente eficaces, volveremos a trabajar con ellos seguro."),
        ("Raúl (Google)", "Traducciones técnicas de alta calidad. Entienden perfectamente el lenguaje de ingeniería y construcción pesada. Es difícil encontrar traductores jurados que dominen estos términos tan específicos."),
        ("Elena (Google)", "Me salvaron con una traducción para el día siguiente muy temprano. Un servicio boutique real donde Fátima se involucra personalmente para ayudar al cliente. Profesionalidad de 10."),
        ("Karim (Google)", "Expertos reales en el mercado árabe y español. Máximo rigor jurídico en cada documento. Su apoyo técnico y administrativo en Libia es fundamental para nuestra expansión internacional.")
    ]
    for name, txt in reviews_data:
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
    <section style="padding:10rem 0;"><div class="container" style="max-width:1100px;">
        <div style="display:grid; grid-template-columns: 1.2fr 1fr; gap:5rem; align-items:start;">
            <div data-aos="fade-right">
                <h2 style="font-size:2.8rem; line-height:1.2; margin-bottom:3rem;">Tradición y Rigor Juris</h2>
                <p style="font-size:1.25rem; color:#f8fafc; line-height:1.8; margin-bottom:2rem;">t-h1</p>
                <div style="background:rgba(194,163,93,0.1); border-left:4px solid var(--primary); padding:2rem; margin-bottom:2.5rem;">
                    <p style="font-size:1.4rem; font-weight:700; color:var(--primary); margin-bottom:1rem;">t-h2</p>
                    <p style="color:#94a3b8; font-size:1.1rem;">t-h3</p>
                </div>
                <p style="font-size:1.1rem; color:#94a3b8; font-style:italic;">t-h4</p>
            </div>
            <div data-aos="fade-left" style="background:rgba(255,255,255,0.02); border:1px solid var(--glass-border); padding:3rem; border-radius:20px;">
                <p style="font-size:1.2rem; color:#f8fafc; line-height:1.8; margin-bottom:2rem;">t-h5</p>
                <p style="font-size:1.2rem; color:#94a3b8; line-height:1.8;">t-h6</p>
            </div>
        </div>
    </div></section>
    <section style="padding-bottom: 8rem;"><div class="container" style="text-align:center; margin-bottom:5rem;"><h2 style="font-size:3.5rem; margin-bottom:1rem; color:white;">t-reviews-title</h2><p style="color:#c2a35d; letter-spacing:4px; font-weight:700;">t-exp-verificadas</p></div><div class="marquee-container"><div class="marquee-inner">{get_review_cards(lang)}</div></div></section>"""
    generate_page(lang, "index.html", 'nav_home', index_content)
    generate_page(lang, "servicios.html", 'nav_services', '<section class="hero" style="min-height:30vh;"><h1>SERVICIOS</h1></section>')
    generate_page(lang, "contacto.html", 'nav_contact', '<section class="hero" style="min-height:30vh;"><h1>CONTACTO</h1></section>')

print("✅ ÉXITO: Texto original íntegro aplicado sin errores.")
