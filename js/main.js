class App {
  constructor() {
    this.currentLang = localStorage.getItem('tigafab_lang') || 'es';
    this.init();
  }

  init() {
    // Navbar scroll effect
    window.addEventListener('scroll', () => {
      const nav = document.getElementById('navbar');
      const scrollPosition = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;
      if (scrollPosition > 50) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    });

    // Make sure lang buttons reflect currentLang
    this.updateLangUI(this.currentLang);

    // Set Active Nav by URL
    this.setActiveNav();

    // Initialize translations & lists
    this.renderTranslations();
  }

  setActiveNav() {
    const path = window.location.pathname;
    let current = 'home';
    if (path.includes('servicios') || path.includes('servicio-')) current = 'services';
    else if (path.includes('contacto')) current = 'contact';
    else if (path.includes('localizacion')) current = 'location';

    document.querySelectorAll('.nav-links a').forEach(el => el.classList.remove('active'));
    const activeEl = document.querySelector(`.nav-${current}`);
    if (activeEl) activeEl.classList.add('active');
  }

  changeLang(lang) {
    this.currentLang = lang;
    localStorage.setItem('tigafab_lang', lang);
    this.updateLangUI(lang);
    this.renderTranslations();
  }

  updateLangUI(lang) {
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.remove('active');
      if (btn.innerText.toLowerCase() === lang) {
        btn.classList.add('active');
      }
    });

    if (lang === 'ar') {
      document.body.setAttribute('dir', 'rtl');
    } else {
      document.body.setAttribute('dir', 'ltr');
    }
  }

  renderTranslations() {
    const t = (typeof translations !== 'undefined') ? translations[this.currentLang] : null;
    if (!t) return;
    
    // Update Page Title
    const pageClass = Array.from(document.body.classList).find(c => c.startsWith('page-'));
    if (pageClass) {
      const pageMap = {
        'page-index': 'nav_home',
        'page-servicios': 'nav_services',
        'page-contacto': 'nav_contact',
        'page-localizacion': 'nav_location',
        'page-aviso-legal': 'nav_legal',
        'page-privacidad': 'nav_privacy',
        'page-servicio-jurada': 'srv_sworn',
        'page-servicio-tecnica': 'srv_tech',
        'page-servicio-visados': 'srv_visa',
        'page-servicio-oficiales': 'srv_docs',
        'page-servicio-asesoramiento': 'srv_business'
      };
      const tKeyTitle = pageMap[pageClass];
      if (tKeyTitle && t[tKeyTitle]) {
        let titleWord = t[tKeyTitle];
        if (pageClass === 'page-index') titleWord = titleWord.toUpperCase();
        document.title = titleWord + ' | TIGAFAB Traductores';
      }
    }
    
    // Multi-class replacer
    const elements = document.querySelectorAll('.nav-home, .nav-services, .nav-contact, .nav-location, .nav-legal, .nav-privacy, [class*="t-"]');
    
    elements.forEach(el => {
      const classes = Array.from(el.classList);
      let tKey = null;
      
      classes.forEach(c => {
        if (c.startsWith('t-')) {
          tKey = c.substring(2).replace(/-/g, '_');
        } else if (c.startsWith('nav-')) {
          tKey = c.replace(/-/g, '_');
        }
      });

      if (tKey && t[tKey]) {
        if (tKey === 'btn_details') {
          const arrowDir = this.currentLang === 'ar' ? 'left' : 'right';
          el.innerHTML = `${t[tKey]} <i class="fas fa-arrow-${arrowDir}" style="margin-left: 5px; font-size: 0.8rem;"></i>`;
        } else if (tKey === 'btn_back') {
          const arrowDir = this.currentLang === 'ar' ? 'right' : 'left';
          const marginSide = this.currentLang === 'ar' ? 'margin-left' : 'margin-right';
          el.innerHTML = `<i class="fas fa-arrow-${arrowDir}" style="${marginSide}: 8px;"></i> ${t[tKey]}`;
        } else {
          el.innerText = t[tKey];
        }
      }
    });

    // Render lists inside detailed pages
    this.renderList('detail-sworn-list', t.srv_sworn_items);
    this.renderList('detail-tech-list', t.srv_tech_items);
    this.renderList('detail-visa-list', t.srv_visa_items);
    this.renderList('detail-docs-list', t.srv_docs_items);
    this.renderPrivacyRights('list-privacy-rights', t.privacy_rights_items);
  }

  renderPrivacyRights(id, items) {
    const container = document.getElementById(id);
    if (!container || !items) return;
    container.innerHTML = '';
    
    items.forEach((item, index) => {
      const div = document.createElement('div');
      div.className = 'legal-right-item';
      div.setAttribute('data-aos', 'fade-up');
      div.setAttribute('data-aos-delay', \`\${Math.min(index * 50, 400)}\`);
      div.innerHTML = \`<i class="fas fa-check-circle"></i> <span>\${item}</span>\`;
      container.appendChild(div);
    });
  }

  renderList(id, items) {
    const ul = document.getElementById(id);
    if (!ul || !items) return;
    ul.innerHTML = '';
    
    items.forEach((item, index) => {
      const li = document.createElement('li');
      li.innerText = item;
      li.setAttribute('data-aos', 'fade-up');
      li.setAttribute('data-aos-delay', \`\${index * 100}\`);
      ul.appendChild(li);
    });
  }
}

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
  window.app = new App();
});
