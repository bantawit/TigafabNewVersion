import os

dir_path = "/Users/mohamedbentaoit/Downloads/ProyectosAnti-gravity/tigafab-web-nueva"

nav = """
  <nav id="navbar">
    <div class="nav-container">
      <a href="index.html" class="logo">TIGAFAB<span>.</span></a>
      <ul class="nav-links" id="navMenu">
        <li><a href="index.html" class="nav-home">Inicio</a></li>
        <li><a href="servicios.html" class="nav-services">Servicios</a></li>
        <li><a href="contacto.html" class="nav-contact">Contacto</a></li>
        <li><a href="localizacion.html" class="nav-location">Localización</a></li>
      </ul>
      <div class="lang-selector">
        <button class="lang-btn active" onclick="window.app.changeLang('es')">ES</button>
        <button class="lang-btn" onclick="window.app.changeLang('en')">EN</button>
        <button class="lang-btn" onclick="window.app.changeLang('fr')">FR</button>
        <button class="lang-btn" onclick="window.app.changeLang('de')">DE</button>
        <button class="lang-btn" onclick="window.app.changeLang('ar')">AR</button>
      </div>
    </div>
  </nav>
"""

footer = """
  <!-- Footer -->
  <footer>    <div class="footer-content">
      <div class="footer-logo">TIGAFAB<span>.</span></div>
      <p class="t-home-welcome-sub" style="font-family: var(--font-heading);">Traducciones, Interpretación, Gestión y Asesoramiento</p>
      <div class="footer-links">
        <a href="aviso-legal.html" class="nav-legal">Aviso Legal</a>
        <a href="privacidad.html" class="nav-privacy">Privacidad</a>
      </div>
    </div>
    <div style="margin-top: 2rem; display: flex; justify-content: center; gap: 1.5rem;">
      <a href="https://www.google.com/maps/place/TIGAFAB+Traductores+Fuenlabrada" target="_blank" rel="noopener noreferrer" style="color: white; font-size: 1.5rem; transition: color 0.3s;"><i class="fas fa-map-marker-alt"></i></a>
      <a href="https://www.linkedin.com/company/tigafab-sl/" target="_blank" rel="noopener noreferrer" style="color: white; font-size: 1.5rem; transition: color 0.3s;"><i class="fab fa-linkedin"></i></a>
    </div>
    <p class="t-footer-rights" style="margin-top:2rem;">© 2026 TIGAFAB S.L. Todos los derechos reservados.</p>
  </footer>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
  <script src="js/i18n.js?v=2"></script>
  <script src="js/main.js?v=2"></script>
</body>
</html>
"""

def getTemplate(title, content):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' https: 'unsafe-inline' 'unsafe-eval'; img-src 'self' data: https:;">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-Frame-Options" content="SAMEORIGIN">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>{title} | TIGAFAB Traductores</title>
  <link rel="stylesheet" href="styles.css?v=2">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
</head>
<body class="page-{title.lower()}">
{nav}
{content}
{footer}
"""

cards = """
        <div class="review-card">
          <i class="fas fa-quote-left review-quote-icon"></i>
          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p class="review-text t-review-1">"Servicio impecable y muy profesional. Fátima resolvió la traducción jurada de mis documentos en tiempo récord para un trámite urgente. Totalmente recomendados."</p>
          <div class="review-author">
            <div style="width:40px; height:40px; border-radius:50%; background:var(--primary); display:flex; align-items:center; justify-content:center; font-weight:700;">M</div>
            <div>
              <span class="t-rev-name-1">María G.</span>
              <div style="font-size:0.8rem; color:#94A3B8;"><i class="fab fa-google"></i> Madrid</div>
            </div>
          </div>
        </div>

        <div class="review-card">
          <i class="fas fa-quote-left review-quote-icon"></i>
          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p class="review-text t-review-2">"Llevamos años confiando en Tigafab para la tramitación de visados y traducción técnica hacia el árabe de los expedientes de nuestra empresa. Rápidos y eficaces."</p>
          <div class="review-author">
            <div style="width:40px; height:40px; border-radius:50%; background:#475569; display:flex; align-items:center; justify-content:center; font-weight:700;">G</div>
            <div>
              <span class="t-rev-name-2">Grupo Constructor</span>
              <div style="font-size:0.8rem; color:#94A3B8;"><i class="fab fa-google"></i> Fuenlabrada</div>
            </div>
          </div>
        </div>

        <div class="review-card">
          <i class="fas fa-quote-left review-quote-icon"></i>
          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p class="review-text t-review-3">"Trato directo y tarifas muy buenas. Me ayudaron muchísimo con el registro de mi filial y servicios en Libia, desde los contratos hasta el asesoramiento. Un 10."</p>
          <div class="review-author">
            <div style="width:40px; height:40px; border-radius:50%; background:var(--primary); display:flex; align-items:center; justify-content:center; font-weight:700;">C</div>
            <div>
              <span class="t-rev-name-3">Carlos S.</span>
              <div style="font-size:0.8rem; color:#94A3B8;"><i class="fab fa-google"></i> Madrid</div>
            </div>
          </div>
        </div>

        <div class="review-card">
          <i class="fas fa-quote-left review-quote-icon"></i>
          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p class="review-text t-review-4">"Gran equipo de traductores profesionales. Resolvieron toda la papeleta de extranjería y certificados de la Cámara de Comercio rapidísimo."</p>
          <div class="review-author">
            <div style="width:40px; height:40px; border-radius:50%; background:#0ea5e9; display:flex; align-items:center; justify-content:center; font-weight:700;">A</div>
            <div>
              <span class="t-rev-name-4">Ana M.</span>
              <div style="font-size:0.8rem; color:#94A3B8;"><i class="fab fa-google"></i> Fuenlabrada</div>
            </div>
          </div>
        </div>

        <div class="review-card">
          <i class="fas fa-quote-left review-quote-icon"></i>
          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p class="review-text t-review-5">"Excelente servicio en Madrid. Me tradujeron el pasaporte y un contrato societario con un rigor absoluto."</p>
          <div class="review-author">
            <div style="width:40px; height:40px; border-radius:50%; background:#10b981; display:flex; align-items:center; justify-content:center; font-weight:700;">H</div>
            <div>
              <span class="t-rev-name-5">Hassan B.</span>
              <div style="font-size:0.8rem; color:#94A3B8;"><i class="fab fa-google"></i> Madrid</div>
            </div>
          </div>
        </div>

        <div class="review-card">
          <i class="fas fa-quote-left review-quote-icon"></i>
          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p class="review-text t-review-6">"Tigafab nos asesoró desde Fuenlabrada para la apertura de una filial en el norte de África. La calidad humana de su equipo es increíble."</p>
          <div class="review-author">
            <div style="width:40px; height:40px; border-radius:50%; background:#8b5cf6; display:flex; align-items:center; justify-content:center; font-weight:700;">F</div>
            <div>
              <span class="t-rev-name-6">Francisco T.</span>
              <div style="font-size:0.8rem; color:#94A3B8;"><i class="fab fa-google"></i> Fuenlabrada</div>
            </div>
          </div>
        </div>

        <div class="review-card">
          <i class="fas fa-quote-left review-quote-icon"></i>
          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p class="review-text t-review-7">"Puntualidad británica y un nivel de confidencialidad brutal. Trabajar con doña Fátima tranquiliza todas nuestras gestiones internacionales."</p>
          <div class="review-author">
            <div style="width:40px; height:40px; border-radius:50%; background:#475569; display:flex; align-items:center; justify-content:center; font-weight:700;">E</div>
            <div>
              <span class="t-rev-name-7">Empresa K.</span>
              <div style="font-size:0.8rem; color:#94A3B8;"><i class="fab fa-google"></i> Madrid</div>
            </div>
          </div>
        </div>

        <div class="review-card">
          <i class="fas fa-quote-left review-quote-icon"></i>
          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
          <p class="review-text t-review-8">"No hay competencia real en los plazos que manejan. Todo el paquete de traducciones juradas del árabe listo impecablemente."</p>
          <div class="review-author">
            <div style="width:40px; height:40px; border-radius:50%; background:var(--primary); display:flex; align-items:center; justify-content:center; font-weight:700;">Y</div>
            <div>
              <span class="t-rev-name-8">Youssef L.</span>
              <div style="font-size:0.8rem; color:#94A3B8;"><i class="fab fa-google"></i> Madrid</div>
            </div>
          </div>
        </div>
"""

pages = {
  "index.html": f"""
  <section class="hero view-section active" style="display:flex; padding-top: 5rem;">
    <div class="hero-content" data-aos="fade-up">
      <h2 class="hero-subtitle t-hero-subtitle">Árabe, Español, Inglés, Alemán y Francés</h2>
      <h1 class="hero-title t-hero-title">Traducción e Interpretación</h1>
      <p class="hero-desc t-hero-desc">Traductora, intérprete, gestora de documentos mercantiles, visados y asesora.</p>
      <div style="margin-top:2rem;">
        <a href="servicios.html" class="btn t-btn-services">Nuestros Servicios</a>
        <a href="contacto.html" class="btn btn-outline t-btn-contact">Contactar Ahora</a>
      </div>
    </div>
  </section>

  <section style="padding: 6rem 2rem; background: var(--bg-light);">
    <div class="container" style="padding:0;">
      <div style="max-width:800px; margin:0 auto; text-align:center;">
        <h2 class="t-home-welcome" style="font-size:2.5rem; color:var(--bg-dark); margin-bottom:1rem;">Bienvenido a Nuestra Web</h2>
        <h4 class="t-home-welcome-sub" style="color:var(--primary); margin-bottom:2rem; font-size:1.2rem; font-weight:400;">Traducciones, Interpretación, Gestión y Asesoramiento</h4>
        <p class="t-home-text-1" style="color:#475569; font-size:1.1rem; line-height:1.8; margin-bottom:1.5rem; text-align:justify;"></p>
        <p class="t-home-text-2" style="color:#475569; font-size:1.1rem; line-height:1.8; text-align:justify;"></p>
      </div>
    </div>
  </section>

  <!-- REVIEWS SECTION -->
  <section style="padding: 6rem 0; overflow:hidden; background: var(--bg-dark); color: #fff;">
    <div class="container" style="padding:0 2rem;">
      <div style="text-align:center; margin-bottom: 4rem;" data-aos="fade-up">
        <h2 class="t-reviews-title" style="font-size:2.5rem; margin-bottom:1rem; font-family: var(--font-heading);">Lo que dicen nuestros clientes</h2>
        <div style="width: 60px; height: 3px; background: var(--primary); margin: 0 auto; margin-bottom: 1.5rem;"></div>
        <p class="t-reviews-subtitle" style="color: #94A3B8;">Reseñas verificadas de Google Maps en nuestras localizaciones.</p>
      </div>
    </div>    
    <div class="reviews-marquee" data-aos="fade-up" data-aos-delay="100">
      <div class="reviews-track">
{cards}
{cards}
      </div>
    </div>
  </section>
  """,

  "servicios.html": """
  <section style="padding-top:8rem;">
    <div class="page-header" data-aos="fade-in" style="padding: 3rem 0; text-align:center; background:var(--bg-dark); color:white;">
      <h1 class="page-title t-srv-title" style="font-size:2.5rem;">Nuestros Servicios</h1>
      <p class="page-subtitle t-srv-sub" style="color:var(--primary);">Traducción, Interpretación, Gestión y Asesoramiento</p>
    </div>
    <div class="container">
      <div class="services-grid">
        <!-- Servicio 1 -->
        <a href="servicio-jurada.html" class="service-card" data-aos="fade-up" data-aos-delay="100" style="text-decoration:none;">
          <div class="service-icon"><i class="fas fa-file-signature"></i></div>
          <h3 class="service-title t-srv-sworn">Traducciones Juradas</h3>
          <p class="t-srv-sworn-short" style="color: #64748B; margin-bottom:1.5rem;">Textos y documentación certificada y legalizada con total validez jurídica.</p>
          <div class="btn-sm-details t-btn-details">Saber más <i class="fas fa-arrow-right" style="margin-left: 5px; font-size: 0.8rem;"></i></div>
        </a>

        <!-- Servicio 2 -->
        <a href="servicio-tecnica.html" class="service-card" data-aos="fade-up" data-aos-delay="200" style="text-decoration:none;">
          <div class="service-icon"><i class="fas fa-cogs"></i></div>
          <h3 class="service-title t-srv-tech">Traducciones Técnicas</h3>
          <p class="t-srv-tech-short" style="color: #64748B; margin-bottom:1.5rem;">Documentos especializados corporativos, técnicos y manuales.</p>
          <div class="btn-sm-details t-btn-details">Saber más <i class="fas fa-arrow-right" style="margin-left: 5px; font-size: 0.8rem;"></i></div>
        </a>

        <!-- Servicio 3 -->
        <a href="servicio-visados.html" class="service-card" data-aos="fade-up" data-aos-delay="300" style="text-decoration:none;">
          <div class="service-icon"><i class="fas fa-passport"></i></div>
          <h3 class="service-title t-srv-visa">Gestión de Visados</h3>
          <p class="t-srv-visa-short" style="color: #64748B; margin-bottom:1.5rem;">Resolución ágil de procedimientos consulares.</p>
          <div class="btn-sm-details t-btn-details">Saber más <i class="fas fa-arrow-right" style="margin-left: 5px; font-size: 0.8rem;"></i></div>
        </a>

        <!-- Servicio 4 -->
        <a href="servicio-oficiales.html" class="service-card" data-aos="fade-up" data-aos-delay="400" style="text-decoration:none;">
          <div class="service-icon"><i class="fas fa-landmark"></i></div>
          <h3 class="service-title t-srv-docs">Gestión Documental</h3>
          <p class="t-srv-docs-short" style="color: #64748B; margin-bottom:1.5rem;">Representación en ministerios y organismos.</p>
          <div class="btn-sm-details t-btn-details">Saber más <i class="fas fa-arrow-right" style="margin-left: 5px; font-size: 0.8rem;"></i></div>
        </a>

        <!-- Servicio 5 -->
        <a href="servicio-asesoramiento.html" class="service-card" data-aos="fade-up" data-aos-delay="500" style="text-decoration:none;">
          <div class="service-icon"><i class="fas fa-briefcase"></i></div>
          <h3 class="service-title t-srv-business">Asesoramiento a Empresas</h3>
          <p class="t-srv-business-short" style="color: #64748B; margin-bottom:1.5rem;">Consultoría de expansión internacional comercial.</p>
          <div class="btn-sm-details t-btn-details">Saber más <i class="fas fa-arrow-right" style="margin-left: 5px; font-size: 0.8rem;"></i></div>
        </a>
      </div>
    </div>
  </section>""",

  "servicio-jurada.html": """
  <section style="padding-top: 5rem;">
    <div class="service-detail-hero bg-sworn">
      <div class="service-hero-content" data-aos="zoom-in">
        <h1 class="t-srv-sworn">Traducciones Juradas</h1>
        <p class="t-srv-sworn-tagline">Oficialidad y máxima rigurosidad legal garantizada</p>
      </div>
    </div>
    <div class="service-detail-body" data-aos="fade-up">
      <p class="service-detail-text t-srv-sworn-full"></p>
      <ul class="service-detail-list" id="detail-sworn-list"></ul>
      <a href="servicios.html" class="btn-back t-btn-back" style="text-decoration:none;"><i class="fas fa-arrow-left"></i> Volver a Servicios</a>
    </div>
  </section>""",

  "servicio-tecnica.html": """
  <section style="padding-top: 5rem;">
    <div class="service-detail-hero bg-tech">
      <div class="service-hero-content" data-aos="zoom-in">
        <h1 class="t-srv-tech">Traducciones Técnicas</h1>
        <p class="t-srv-tech-tagline">Soluciones lingüísticas corporativas precisas</p>
      </div>
    </div>
    <div class="service-detail-body" data-aos="fade-up">
      <p class="service-detail-text t-srv-tech-full"></p>
      <ul class="service-detail-list" id="detail-tech-list"></ul>
      <a href="servicios.html" class="btn-back t-btn-back" style="text-decoration:none;"><i class="fas fa-arrow-left"></i> Volver a Servicios</a>
    </div>
  </section>""",

  "servicio-visados.html": """
  <section style="padding-top: 5rem;">
    <div class="service-detail-hero bg-visa">
      <div class="service-hero-content" data-aos="zoom-in">
        <h1 class="t-srv-visa">Gestión de Visados</h1>
        <p class="t-srv-visa-tagline">Aprobación fluida y sin contratiempos</p>
      </div>
    </div>
    <div class="service-detail-body" data-aos="fade-up">
      <p class="service-detail-text t-srv-visa-full"></p>
      <ul class="service-detail-list" id="detail-visa-list"></ul>
      <a href="servicios.html" class="btn-back t-btn-back" style="text-decoration:none;"><i class="fas fa-arrow-left"></i> Volver a Servicios</a>
    </div>
  </section>""",

  "servicio-oficiales.html": """
  <section style="padding-top: 5rem;">
    <div class="service-detail-hero bg-docs">
      <div class="service-hero-content" data-aos="zoom-in">
        <h1 class="t-srv-docs">Gestión Documental</h1>
        <p class="t-srv-docs-tagline">Presentación impecable frente a Organismos Oficiales</p>
      </div>
    </div>
    <div class="service-detail-body" data-aos="fade-up">
      <p class="service-detail-text t-srv-docs-full"></p>
      <ul class="service-detail-list" id="detail-docs-list"></ul>
      <a href="servicios.html" class="btn-back t-btn-back" style="text-decoration:none;"><i class="fas fa-arrow-left"></i> Volver a Servicios</a>
    </div>
  </section>""",

  "servicio-asesoramiento.html": """
  <section style="padding-top: 5rem;">
    <div class="service-detail-hero bg-business">
      <div class="service-hero-content" data-aos="zoom-in">
        <h1 class="t-srv-business">Asesoramiento Empresarial</h1>
        <p class="t-srv-business-tagline">Conquistando el mercado internacional con confianza</p>
      </div>
    </div>
    <div class="service-detail-body" data-aos="fade-up">
      <p class="service-detail-text t-srv-business-full"></p>
      <a href="servicios.html" class="btn-back t-btn-back" style="text-decoration:none;"><i class="fas fa-arrow-left"></i> Volver a Servicios</a>
    </div>
  </section>""",

  "contacto.html": """
  <section style="padding:10rem 0 5rem;">
    <div class="page-header" data-aos="fade-in" style="margin-top:-10rem; padding-top:10rem; padding-bottom: 4rem;">
      <h1 class="page-title t-contact-title">Contacte con Nosotros</h1>
      <p class="page-subtitle t-contact-sub">Estamos a su disposición para cualquier consulta</p>
    </div>
    <div class="container">
      <div class="contact-grid">
        <div data-aos="fade-right">
          <div class="contact-info-box">
            <div class="contact-icon"><i class="fas fa-phone-alt"></i></div>
            <div class="contact-details">
              <h4 class="t-contact-phone">Teléfono</h4>
              <p>+34 663 11 45 46</p>
            </div>
          </div>
          <div class="contact-info-box">
            <div class="contact-icon"><i class="fas fa-fax"></i></div>
            <div class="contact-details">
              <h4 class="t-contact-fax">Fax</h4>
              <p>+34 914 86 47 50</p>
            </div>
          </div>
        </div>
        <div data-aos="fade-left">
          <div class="contact-info-box">
            <div class="contact-icon"><i class="fas fa-envelope"></i></div>
            <div class="contact-details">
              <h4 class="t-contact-email">Correo Electrónico</h4>
              <p>fatima@tigafab-traductores.com</p>
              <p>fatima.benamar@yahoo.es</p>
            </div>
          </div>
          <div class="contact-info-box">
            <div class="contact-icon" style="color: #0a66c2; background: rgba(10, 102, 194, 0.1);"><i class="fab fa-linkedin-in"></i></div>
            <div class="contact-details">
              <h4>LinkedIn</h4>
              <p><a href="https://www.linkedin.com/company/tigafab-sl/" target="_blank" rel="noopener noreferrer" style="color: var(--primary); text-decoration: none;" class="t-contact-linkedin">Seguir Empresa en LinkedIn</a></p>
            </div>
          </div>
          <div class="contact-info-box">
            <div class="contact-icon"><i class="fas fa-map-marker-alt"></i></div>
            <div class="contact-details">
              <h4 class="t-contact-hq">Oficina Principal</h4>
              <p class="t-contact-hq-address">C/ De las Ciencias, 51. 28942 - Fuenlabrada (Madrid)</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>""",

  "localizacion.html": """
  <section style="padding:10rem 0 5rem;">
    <div class="page-header" data-aos="fade-in" style="margin-top:-10rem; padding-top:10rem; padding-bottom: 4rem;">
      <h1 class="page-title t-loc-title">Dónde Localizarnos</h1>
      <p class="page-subtitle t-loc-sub">Visite nuestras delegaciones</p>
    </div>
    <div class="container">
      <div style="margin-bottom: 4rem;" data-aos="fade-up">
        <h3 class="t-loc-fuenlabrada" style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--bg-dark);">Delegación Fuenlabrada</h3>
        <p class="t-contact-hq-address" style="color: #64748B; margin-bottom: 1rem;">C/ De las Ciencias, 51. 28942 Madrid (Metro Hospital Fuenlabrada)</p>
        <div class="map-container">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3042.427771746206!2d-3.8184581!3d40.2831861!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd418c3b7a8a1ab9%3A0xe9ef8abf98af074!2sC.%20de%20las%20Ciencias%2C%2051%2C%2028942%20Fuenlabrada%2C%20Madrid!5e0!3m2!1ses!2ses" allowfullscreen="" loading="lazy"></iframe>
        </div>
      </div>
      <div data-aos="fade-up" data-aos-delay="200">
        <h3 class="t-loc-madrid" style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--bg-dark);">Delegación Madrid Capital</h3>
        <p class="t-loc-madrid-address" style="color: #64748B; margin-bottom: 1rem;">C/ Mauricio Legendre, 5 - Local 11. 28046 (Madrid)</p>
        <div class="map-container">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3034.7865241416715!2d-3.6874457!3d40.4812!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd422967119e8633%3A0xa64b38d3886561f0!2sC.%20de%20Mauricio%20Legendre%2C%205%2C%2028046%20Madrid!5e0!3m2!1ses!2ses" allowfullscreen="" loading="lazy"></iframe>
        </div>
      </div>
    </div>
  </section>""",

  "aviso-legal.html": """
  <section style="padding:10rem 0 5rem;">
    <div class="page-header" data-aos="fade-in" style="margin-top:-10rem; padding-top:10rem; padding-bottom: 4rem;">
      <h1 class="page-title t-legal-title">Aviso Legal</h1>
      <p class="page-subtitle t-legal-sub">Información corporativa y legal</p>
    </div>
    <div class="container" data-aos="fade-up" data-aos-delay="100">
      <div class="legal-wrapper">
        <h3 class="t-legal-heading-1"><i class="fas fa-building"></i> 1. Datos del Responsable</h3>
        <p class="t-legal-text-1">La empresa titular de los dominios web es TIGAFAB, S.L., con domicilio a estos efectos en C/ DE LAS CIENCIAS, 51, 28942. FUENLABRADA, MADRID.</p>
        
        <h3 class="t-legal-heading-2"><i class="fas fa-balance-scale"></i> 2. Condiciones de Uso</h3>
        <p class="t-legal-text-2">El acceso y/o uso de este portal atribuye la condición de USUARIO, que acepta los Términos de Uso reflejados en el presente texto.</p>
      </div>
    </div>
  </section>""",

  "privacidad.html": """
  <section style="padding:10rem 0 5rem;">
    <div class="page-header" data-aos="fade-in" style="margin-top:-10rem; padding-top:4rem; padding-bottom: 3rem;">
      <h1 class="page-title t-privacy-title">Política de Privacidad y Cookies</h1>
      <p class="page-subtitle t-privacy-sub">Protección de sus datos (RGPD)</p>
    </div>
    <div class="container" data-aos="fade-up" data-aos-delay="100">
      <div class="legal-wrapper">
        <h3 class="t-privacy-heading-1"><i class="fas fa-user-shield"></i> 1. Derechos del Usuario (RGPD)</h3>
        <p class="t-privacy-text-1">Usted podrá ejercer los siguientes derechos sobre sus datos personales:</p>
        <div class="legal-rights-grid" id="list-privacy-rights"></div>
        
        <h3 class="t-privacy-heading-2" style="margin-top:1rem;"><i class="fas fa-gavel"></i> 2. Tutela de Derechos</h3>
        <p class="t-privacy-text-2">Puede contactar con la Agencia Española de Protección de Datos (https://www.aepd.es) sita en C/ Jorge Juan, 6, 28001, Madrid o en los teléfonos 901.100.099 y 912.663.517.</p>
        
        <h3 class="t-privacy-heading-3"><i class="fas fa-cookie-bite"></i> 3. Política de Cookies</h3>
        <p class="t-privacy-text-3" style="margin-bottom:0;">Utilizamos Cookies de sesión y persistentes (propias y de terceros) así como Google Analytics para proveer funciones esenciales y recopilar estadísticas anónimas de visitas.</p>
      </div>
    </div>
  </section>"""
}

for filename, content in pages.items():
    finalContent = getTemplate(filename.replace('.html','').upper(), content)
    with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as f:
        f.write(finalContent)

print("¡11 archivos generados perfectamente!")
