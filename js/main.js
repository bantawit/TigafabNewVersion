class App {
  constructor() {
    this.init();
  }
  init() {
    console.log("Tigafab App Initialized");
  }
}

// Usamos window.onload para asegurar que los anchos de las tarjetas 
// se calculen con las fuentes y estilos ya aplicados.
window.onload = () => {
  window.app = new App();
  initPremiumMarquee();
};

function initPremiumMarquee() {
  const slider = document.getElementById('reviewSlider');
  if (!slider) return;

  const inner = slider.querySelector('.marquee-inner');
  if (!inner) return;

  const isRTL = document.documentElement.dir === 'rtl';
  let currentX = 0;
  let isDown = false;
  let startX;
  let animationId;
  let isHovered = false;

  const step = () => {
    if (!isDown && !isHovered) {
      // En RTL movemos hacia el otro lado
      currentX += isRTL ? 1 : -1; 
      
      const halfWidth = inner.offsetWidth / 2;
      if (Math.abs(currentX) >= halfWidth) {
        currentX = 0;
      }
      inner.style.transform = `translateX(${currentX}px)`;
    }
    animationId = requestAnimationFrame(step);
  };

  // Inicwindow.onload = function() {
    // Dropdown Toggle
    const langSelector = document.getElementById('langSelector');
    const langDropdown = document.getElementById('langDropdown');

    if (langSelector) {
        langSelector.addEventListener('click', function(e) {
            e.stopPropagation();
            langDropdown.classList.toggle('show');
        });
    }

    // Cerrar al hacer clic fuera
    document.addEventListener('click', function() {
        if (langDropdown && langDropdown.classList.contains('show')) {
            langDropdown.classList.remove('show');
        }
    });

    // Slider reviews (Marquee)
    const marquee = document.querySelector('.marquee-inner');
    if (marquee) {
        let isPaused = false;
        marquee.addEventListener('mouseenter', () => isPaused = true);
        marquee.addEventListener('mouseleave', () => isPaused = false);
    }
}
 isDown = false; });

  slider.addEventListener('mousedown', (e) => {
    isDown = true;
    slider.style.cursor = 'grabbing';
    startX = e.pageX;
  });

  document.addEventListener('mouseup', () => {
    isDown = false;
    if (slider) slider.style.cursor = 'grab';
  });

  document.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    const x = e.pageX;
    const walk = (x - startX);
    startX = x;
    currentX += walk;

    const halfWidth = inner.offsetWidth / 2;
    if (currentX > 0 && !isRTL) currentX = -halfWidth;
    if (currentX < 0 && isRTL) currentX = halfWidth;
    if (Math.abs(currentX) > halfWidth) currentX = 0;

    inner.style.transform = `translateX(${currentX}px)`;
  });
}
