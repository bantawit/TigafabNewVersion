/**
 * TIGAFAB Main Engine
 * Maneja el selector de idiomas, menú móvil y el carrusel de reseñas
 */
window.onload = function() {

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
                navbarEl.style.background = 'rgba(15, 23, 42, 0.98)';
                navbarEl.style.boxShadow = '0 4px 30px rgba(0,0,0,0.4)';
            } else {
                navbarEl.style.background = 'rgba(15, 23, 42, 0.9)';
                navbarEl.style.boxShadow = 'none';
            }
        }, { passive: true });
    }

    // 5. Dynamic Years of Experience Calculator
    // Founded: 2011 — updates automatically every year without any manual change
    const FOUNDED_YEAR = 2011;
    const currentYear = new Date().getFullYear();
    const yearsExp = currentYear - FOUNDED_YEAR;

    document.querySelectorAll('.dyn-years').forEach(el => {
        el.textContent = yearsExp;
    });

    console.log(`Tigafab Engine Ready ✓ | ${yearsExp} años de experiencia`);
};
