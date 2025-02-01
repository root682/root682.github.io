// Inicializar las animaciones AOS
AOS.init({
    duration: 1000,
    once: true
});

// Función para copiar número de WhatsApp
function copyWhatsApp() {
    const number = "+1234567890";  // Reemplazar con tu número real
    navigator.clipboard.writeText(number).then(() => {
        alert("Número de WhatsApp copiado al portapapeles!");
    });
}

// Animación suave al hacer scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Animación del logo
document.querySelector('.logo').addEventListener('mouseover', function() {
    this.style.transform = 'scale(1.1)';
});

document.querySelector('.logo').addEventListener('mouseout', function() {
    this.style.transform = 'scale(1)';
});

// Efecto parallax en el hero
window.addEventListener('scroll', function() {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    hero.style.backgroundPositionY = -(scrolled * 0.5) + 'px';
});