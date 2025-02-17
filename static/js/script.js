document.querySelectorAll(".card").forEach((card) => {
    card.addEventListener("mouseover", () => {
        card.style.transform = "scale(1.05)";
    });
    card.addEventListener("mouseleave", () => {
        card.style.transform = "scale(1)";
    });
});
