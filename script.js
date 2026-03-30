document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. Navbar Sticky & Active States ---
    const navbar = document.getElementById('navbar');
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    window.addEventListener('scroll', () => {
        // Sticky Navbar
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // --- 2. Mobile Menu Toggle ---
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-links');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when a link is clicked
    navLinks.forEach(n => n.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }));

    // --- 3. Hero Subdued Slider ---
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;

    function nextSlide() {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
    }

    // Change slide every 5 seconds
    setInterval(nextSlide, 5000);

    // --- 4. Scroll Reveal Animations ---
    const reveals = document.querySelectorAll('.reveal');

    function reveal() {
        const windowHeight = window.innerHeight;
        const elementVisible = 100;

        reveals.forEach(el => {
            const elementTop = el.getBoundingClientRect().top;
            if (elementTop < windowHeight - elementVisible) {
                el.classList.add('active');
            }
        });
    }
    
    // Trigger once on load to reveal elements appearing instantly
    reveal();
    window.addEventListener('scroll', reveal);

    // --- 5. Counter Animation for Stats ---
    const counters = document.querySelectorAll('.stat-number');
    let hasCounted = false;

    function animateCounters() {
        const statsSection = document.querySelector('.stats-grid');
        if(!statsSection) return;
        
        const sectionTop = statsSection.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;

        if (sectionTop < windowHeight - 100 && !hasCounted) {
            counters.forEach(counter => {
                const target = +counter.getAttribute('data-target');
                const duration = 2000; // ms
                const increment = target / (duration / 16); // 60fps

                let currentCount = 0;
                const updateCounter = () => {
                    currentCount += increment;
                    if (currentCount < target) {
                        counter.innerText = Math.ceil(currentCount);
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.innerText = target + (target > 10 ? '+' : '');
                    }
                };
                updateCounter();
            });
            hasCounted = true;
        }
    }
    
    window.addEventListener('scroll', animateCounters);

    // --- 6. Projects Filtering ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const filterValue = btn.getAttribute('data-filter');
            
            projectCards.forEach(card => {
                if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.8)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // --- 7. Image Modal/Popup ---
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImg');
    const viewBtns = document.querySelectorAll('.view-btn');
    const closeModal = document.querySelector('.close-modal');

    viewBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation(); // Avoid triggering parent events
            const card = btn.closest('.project-card');
            const img = card.querySelector('img');
            modal.style.display = 'block';
            modalImg.src = img.src;
        });
    });

    closeModal.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
});
