/**
 * TIGAFAB Main Engine
 * Maneja el selector de idiomas y el carrusel de reseñas
 */
window.onload = function() {
    
    // 1. Lógica del Selector de Idiomas
    const langSelector = document.getElementById('langSelector');
    const langDropdown = document.getElementById('langDropdown');

    if (langSelector && langDropdown) {
        langSelector.addEventListener('click', function(e) {
            e.stopPropagation();
            langDropdown.classList.toggle('show');
            console.log("Dropdown toggled");
        });
    }

    // Cerrar el menú si se hace clic en cualquier otro sitio de la pantalla
    document.addEventListener('click', function(e) {
        if (langDropdown && langDropdown.classList.contains('show')) {
            if (!langSelector.contains(e.target)) {
                langDropdown.classList.remove('show');
            }
        }
    });

    // 2. Motor de las Reseñas (Infinite Marquee)
    const marquee = document.querySelector('.marquee-inner');
    if (marquee) {
        // Pausar al pasar el ratón
        marquee.addEventListener('mouseenter', () => {
            marquee.style.animationPlayState = 'paused';
        });
        marquee.addEventListener('mouseleave', () => {
            marquee.style.animationPlayState = 'running';
        });
    }

    console.log("Tigafab Engine Ready");
};
