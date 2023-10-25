document.addEventListener("DOMContentLoaded", function() {
    const openModalButton = document.getElementById("openModal");
    const closeModalButton = document.getElementById("closeModal");
    const menuModal = document.getElementById("menuModal");

    openModalButton.addEventListener("click", function() {
        menuModal.style.display = "block";
    });

    closeModalButton.addEventListener("click", function() {
        menuModal.style.display = "none";
    });
});

