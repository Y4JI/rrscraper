// Login feature client script
document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector(".auth-form");
    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            const submitBtn = loginForm.querySelector("button[type='submit']");
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = "Logging in...";
            }
        });
    }
});
