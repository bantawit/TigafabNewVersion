/**
 * TIGAFAB Main Engine
 * Maneja el selector de idiomas, menú móvil y el carrusel de reseñas
 */
window.onload = function() {

    const applyTheme = function(theme) {
        const resolvedTheme = theme === 'light' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', resolvedTheme);
        const themeToggle = document.getElementById('themeToggle');
        if (themeToggle) {
            const icon = themeToggle.querySelector('i');
            themeToggle.setAttribute('aria-label', resolvedTheme === 'light' ? 'Cambiar a modo oscuro' : 'Cambiar a modo claro');
            themeToggle.setAttribute('title', resolvedTheme === 'light' ? 'Modo oscuro' : 'Modo claro');
            if (icon) {
                icon.className = resolvedTheme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
            }
        }
    };

    const getPreferredTheme = function() {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'light' || savedTheme === 'dark') {
            return savedTheme;
        }
        return window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
    };

    applyTheme(getPreferredTheme());

    // 1. Menú Móvil (Hamburguesa)
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');
    const navbar = document.getElementById('navbar');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            navToggle.classList.toggle('open');
            navLinks.classList.toggle('show');
            document.body.classList.toggle('menu-open', navLinks.classList.contains('show'));
            document.body.style.overflow = navLinks.classList.contains('show') ? 'hidden' : '';
        });

        // Cerrar menú al hacer clic en un enlace
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                navToggle.classList.remove('open');
                navLinks.classList.remove('show');
                document.body.classList.remove('menu-open');
                document.body.style.overflow = '';
            });
        });

        // Cerrar menú al hacer clic fuera
        document.addEventListener('click', function(e) {
            if (navLinks.classList.contains('show') && !navbar.contains(e.target)) {
                navToggle.classList.remove('open');
                navLinks.classList.remove('show');
                document.body.classList.remove('menu-open');
                document.body.style.overflow = '';
            }
        });
    }

    // 2. Lógica del Selector de Idiomas
    const langSelector = document.getElementById('langSelector');
    const langDropdown = document.getElementById('langDropdown');

    if (langSelector && langDropdown) {
        langSelector.addEventListener('click', function(e) {
            e.stopPropagation();
            langDropdown.classList.toggle('show');
        });
    }

    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            const currentTheme = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
            const nextTheme = currentTheme === 'light' ? 'dark' : 'light';
            localStorage.setItem('theme', nextTheme);
            applyTheme(nextTheme);
            if (navbar) {
                navbar.style.background = window.scrollY > 50 ? 'var(--bg-navbar-scrolled)' : 'var(--bg-navbar)';
            }
        });
    }

    // Cerrar el menú de idioma si se hace clic en cualquier otro sitio
    document.addEventListener('click', function(e) {
        if (langDropdown && langDropdown.classList.contains('show')) {
            if (!langSelector.contains(e.target)) {
                langDropdown.classList.remove('show');
            }
        }
    });

    // 3. Motor de las Reseñas (Infinite Marquee)
    const marquee = document.querySelector('.marquee-inner');
    if (marquee) {
        marquee.addEventListener('mouseenter', () => {
            marquee.style.animationPlayState = 'paused';
        });
        marquee.addEventListener('mouseleave', () => {
            marquee.style.animationPlayState = 'running';
        });
        // Touch support para móviles
        marquee.addEventListener('touchstart', () => {
            marquee.style.animationPlayState = 'paused';
        }, { passive: true });
        marquee.addEventListener('touchend', () => {
            setTimeout(() => {
                marquee.style.animationPlayState = 'running';
            }, 2000);
        }, { passive: true });
    }

    // 4. Navbar scroll effect
    const navbarEl = document.getElementById('navbar');
    if (navbarEl) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbarEl.style.background = 'var(--bg-navbar-scrolled)';
                navbarEl.style.boxShadow = '0 4px 30px var(--shadow-main)';
            } else {
                navbarEl.style.background = 'var(--bg-navbar)';
                navbarEl.style.boxShadow = 'none';
            }
        }, { passive: true });
    }

    // 5. Dynamic Years of Experience Calculator
    // Founded: 2001 — updates automatically every year without any manual change
    const FOUNDED_YEAR = 2001;
    const currentYear = new Date().getFullYear();
    const yearsExp = currentYear - FOUNDED_YEAR;

    document.querySelectorAll('.dyn-years').forEach(el => {
        el.textContent = yearsExp;
    });

    // File upload name display and validation
    const fileInput = document.getElementById('fileInput');
    const fileNameDisplay = document.getElementById('fileName');
    const contactForm = document.querySelector('form[action="send-email.php"]');
    
    if (fileInput && fileNameDisplay) {
        fileInput.addEventListener('change', function(e) {
            const files = e.target.files;
            if (files.length > 0) {
                const names = Array.from(files).map(f => f.name).join(', ');
                fileNameDisplay.textContent = names.length > 50 ? names.substring(0, 50) + '...' : names;
                
                // Validate files
                const allowedExtensions = ['pdf', 'doc', 'docx', 'zip'];
                const maxSize = 10 * 1024 * 1024; // 10MB
                let invalidFiles = [];
                let oversizedFiles = [];
                
                for (let i = 0; i < files.length; i++) {
                    const file = files[i];
                    const ext = file.name.split('.').pop().toLowerCase();
                    
                    if (!allowedExtensions.includes(ext)) {
                        invalidFiles.push(file.name);
                    }
                    if (file.size > maxSize) {
                        oversizedFiles.push(file.name);
                    }
                }
                
                if (invalidFiles.length > 0) {
                    showNotification('Formato no permitido. Solo se aceptan: PDF, DOC, DOCX, ZIP', 'error');
                    fileInput.value = '';
                    fileNameDisplay.textContent = '';
                    return;
                }
                
                if (oversizedFiles.length > 0) {
                    showNotification('El archivo excede el tamaño máximo de 10MB', 'error');
                    fileInput.value = '';
                    fileNameDisplay.textContent = '';
                    return;
                }
                
                if (files.length > 5) {
                    showNotification('Máximo 5 archivos permitidos', 'error');
                    fileInput.value = '';
                    fileNameDisplay.textContent = '';
                    return;
                }
            } else {
                fileNameDisplay.textContent = '';
            }
        });
    }
    
    // Form submission with elegant error handling
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(contactForm);
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.disabled = true;
            submitBtn.textContent = 'Enviando...';
            
            fetch('send-email.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.ok) {
                    window.location.href = 'gracias.html';
                } else {
                    return response.json().then(data => {
                        throw new Error(data.message || 'Error al enviar el formulario');
                    });
                }
            })
            .catch(error => {
                showNotification(error.message, 'error');
                submitBtn.disabled = false;
                submitBtn.textContent = originalText;
            });
        });
    }
    
    // Elegant notification system
    function showNotification(message, type = 'info') {
        // Remove existing notification
        const existing = document.querySelector('.notification-toast');
        if (existing) existing.remove();
        
        const notification = document.createElement('div');
        notification.className = `notification-toast notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas fa-${type === 'error' ? 'exclamation-circle' : 'check-circle'}"></i>
                <span>${message}</span>
            </div>
        `;
        
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => notification.classList.add('show'), 10);
        
        // Auto remove
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, 4000);
    }

    // WhatsApp disabled tooltip translation and click prevention
    const whatsappBtn = document.querySelector('.whatsapp-float[data-tooltip]');
    if (whatsappBtn) {
        const tooltipText = whatsappBtn.getAttribute('data-tooltip');
        if (tooltipText && tooltipText.startsWith('t-')) {
            const translationKey = tooltipText.replace('t-', '').replace('-', '_');
            if (window.translations && window.translations[lang] && window.translations[lang][translationKey]) {
                whatsappBtn.setAttribute('data-tooltip', window.translations[lang][translationKey]);
            }
        }
        
        // Prevent click if disabled
        if (whatsappBtn.classList.contains('whatsapp-disabled')) {
            whatsappBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                return false;
            });
        }
    }

    // Language selector: maintain current page when switching language (DISABLED)
    // The links are already correctly generated by generate.py
    /*
    if (langDropdown) {
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        const currentPath = window.location.pathname;
        const langLinks = langDropdown.querySelectorAll('a');
        
        // Determine current language from path
        let currentLang = 'es';
        if (currentPath.match(/\/en\//)) currentLang = 'en';
        else if (currentPath.match(/\/fr\//)) currentLang = 'fr';
        else if (currentPath.match(/\/ar\//)) currentLang = 'ar';
        
        langLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href) {
                // Determine target language from the original href
                let targetLang = 'es';
                if (href.match(/\/en\//)) targetLang = 'en';
                else if (href.match(/\/fr\//)) targetLang = 'fr';
                else if (href.match(/\/ar\//)) targetLang = 'ar';
                
                // Build correct path based on current and target language
                if (currentLang === 'es') {
                    // Currently in Spanish (root)
                    if (targetLang === 'es') {
                        link.setAttribute('href', currentPage);
                    } else {
                        link.setAttribute('href', `${targetLang}/${currentPage}`);
                    }
                } else {
                    // Currently in a language folder
                    if (targetLang === 'es') {
                        link.setAttribute('href', `../${currentPage}`);
                    } else if (targetLang === currentLang) {
                        link.setAttribute('href', currentPage);
                    } else {
                        link.setAttribute('href', `../${targetLang}/${currentPage}`);
                    }
                }
            }
        });
    }
    */

    console.log(`Tigafab Engine Ready ✓ | ${yearsExp} años de experiencia`);
};
