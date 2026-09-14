// Register feature client script
document.addEventListener("DOMContentLoaded", () => {
    const regForm = document.querySelector(".auth-form");
    if (regForm) {
        regForm.addEventListener("submit", (e) => {
            const pwd = document.getElementById("password");
            const confirmPwd = document.getElementById("confirm_password");
            if (pwd && confirmPwd && pwd.value !== confirmPwd.value) {
                e.preventDefault();
                alert("Passwords do not match!");
                confirmPwd.focus();
                return;
            }
            const submitBtn = regForm.querySelector("button[type='submit']");
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = "Registering...";
            }
        });
    }
});
