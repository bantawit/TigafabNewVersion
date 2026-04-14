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

  // Iniciar motor
  animationId = requestAnimationFrame(step);

  slider.addEventListener('mouseenter', () => { isHovered = true; });
  slider.addEventListener('mouseleave', () => { isHovered = false; isDown = false; });

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
