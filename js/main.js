class App {
  constructor() {
    this.init();
  }
  init() {
    console.log("Tigafab App Initialized");
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.app = new App();
  initPremiumMarquee();
});

function initPremiumMarquee() {
  const slider = document.getElementById('reviewSlider');
  if (!slider) return;

  const inner = slider.querySelector('.marquee-inner');
  if (!inner) return;

  let currentX = 0;
  let isDown = false;
  let startX;
  let scrollLeft;
  let animationId;
  let isHovered = false;

  const step = () => {
    if (!isDown && !isHovered) {
      currentX -= 1; // Velocidad del motor
      // Si llegamos a la mitad (donde empieza el clon), reseteamos a 0 de forma invisible
      if (Math.abs(currentX) >= inner.offsetWidth / 2) {
        currentX = 0;
      }
      inner.style.transform = `translateX(${currentX}px)`;
    }
    animationId = requestAnimationFrame(step);
  };

  // Iniciar el motor
  animationId = requestAnimationFrame(step);

  // --- CONTROLES DE RATÓN ---
  slider.addEventListener('mouseenter', () => { isHovered = true; });
  slider.addEventListener('mouseleave', () => { 
    isHovered = false; 
    isDown = false; 
  });

  slider.addEventListener('mousedown', (e) => {
    isDown = true;
    slider.style.cursor = 'grabbing';
    startX = e.pageX - inner.offsetLeft;
    // Capturamos el punto de inicio para el arrastre
    startX = e.pageX;
  });

  document.addEventListener('mouseup', () => {
    isDown = false;
    slider.style.cursor = 'grab';
  });

  document.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    
    const x = e.pageX;
    const walk = (x - startX); // Calculamos cuánto hemos movido el ratón
    startX = x; // Actualizamos para el siguiente frame
    
    currentX += walk;

    // Límites para el efecto infinito manual
    const halfWidth = inner.offsetWidth / 2;
    if (currentX > 0) currentX = -halfWidth;
    if (Math.abs(currentX) > halfWidth) currentX = 0;

    inner.style.transform = `translateX(${currentX}px)`;
  });
}
