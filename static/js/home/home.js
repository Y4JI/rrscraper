const importForm = document.getElementById("novel-import-form");
const importButton = importForm.querySelector("button[type='submit']");

importForm.addEventListener("submit", (event) => {
    if (importButton.disabled) {
        event.preventDefault();
        return;
    }
    importButton.disabled = true;
    importButton.textContent = "Importing…";
});

window.addEventListener("pageshow", () => {
    importButton.disabled = false;
    importButton.textContent = "Import novel";
});
