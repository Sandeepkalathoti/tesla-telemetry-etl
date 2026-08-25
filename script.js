function scrollToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({
        behavior: "smooth"
    });
}


// Animate statistics when they appear on screen
const statCards = document.querySelectorAll(".stat-card h2");

const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.style.transform = "scale(1.15)";

                setTimeout(() => {
                    entry.target.style.transform = "scale(1)";
                }, 300);
            }
        });
    },
    {
        threshold: 0.5
    }
);

statCards.forEach((stat) => {
    observer.observe(stat);
});


// Navbar shadow on scroll
const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {

    if (window.scrollY > 30) {
        navbar.style.boxShadow = "0 5px 20px rgba(0,0,0,0.35)";
    } else {
        navbar.style.boxShadow = "none";
    }

});


// Pipeline cards animation
const cards = document.querySelectorAll(
    ".pipeline-card, .tech-card, .model-card"
);

const cardObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {

            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
            }

        });
    },
    {
        threshold: 0.15
    }
);

cards.forEach((card) => {

    card.style.opacity = "0";
    card.style.transform = "translateY(30px)";
    card.style.transition = "all 0.6s ease";

    cardObserver.observe(card);

});
