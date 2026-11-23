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

const statusRegion = document.querySelector("[data-import-status]");
let lastSnapshot = statusRegion.innerHTML.trim();
let refreshingStatus = false;

async function refreshImportStatus() {
    if (document.hidden || refreshingStatus || statusRegion.contains(document.activeElement)) {
        return;
    }
    refreshingStatus = true;
    try {
        const response = await fetch(statusRegion.dataset.importStatus, {
            signal: AbortSignal.timeout(5000),
        });
        if (response.redirected) {
            window.clearInterval(statusTimer);
            document.removeEventListener("visibilitychange", refreshImportStatus);
            return;
        }
        if (response.ok) {
            const snapshot = (await response.text()).trim();
            if (snapshot !== lastSnapshot && !statusRegion.contains(document.activeElement)) {
                statusRegion.innerHTML = snapshot;
                lastSnapshot = snapshot;
            }
        }
    } catch {
        // A later poll can refresh the status after a temporary connection error.
    } finally {
        refreshingStatus = false;
    }
}

const statusTimer = window.setInterval(refreshImportStatus, 4000);
document.addEventListener("visibilitychange", refreshImportStatus);
