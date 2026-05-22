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

    console.log(`Tigafab Engine Ready ✓ | ${yearsExp} años de experiencia`);
};
