document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');
    const navbar = document.querySelector('.navbar');
    let currentSection = '';

    function activateNavLink(sectionId) {
        navLinks.forEach(link => {
            if (link.getAttribute('href') === '#' + sectionId) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }

    function checkActiveSection() {
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            if (pageYOffset >= sectionTop - navbar.offsetHeight && pageYOffset < sectionTop + sectionHeight - navbar.offsetHeight) {
                currentSection = section.id;
            }
        });

        activateNavLink(currentSection);
    }

    window.addEventListener('scroll', checkActiveSection);
    checkActiveSection(); // ইনিশিয়াল চেক পেজ লোডের সময়
});