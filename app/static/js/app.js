const form = document.getElementById("proposal-form");

const loadingState = document.getElementById("loading-state");
const errorState = document.getElementById("error-state");
const resultSection = document.getElementById("result-section");

const proposalOutput = document.getElementById("proposal-output");
const ctaOutput = document.getElementById("cta-output");
const subjectOutput = document.getElementById("subject-output");
const followupOutput = document.getElementById("followup-output");

if (form) {

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        loadingState.classList.remove("hidden");
        errorState.classList.add("hidden");
        resultSection.classList.add("hidden");

        const formData = new FormData(form);

        const payload = {
            niche: formData.get("niche"),
            platform: formData.get("platform"),
            tone: formData.get("tone"),
            client_problem: formData.get("problem")
        };

        try {

            const response = await fetch("/api/generate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error("Generation failed");
            }

            const data = await response.json();

            proposalOutput.textContent = data.proposal;
            ctaOutput.textContent = data.cta;
            subjectOutput.textContent = data.subject_line;
            followupOutput.textContent = data.follow_up;

            resultSection.classList.remove("hidden");

        } catch (error) {

            errorState.classList.remove("hidden");
            console.error(error);

        } finally {

            loadingState.classList.add("hidden");

        }

    });

}

document.querySelectorAll(".copy-btn").forEach((button) => {

    button.addEventListener("click", async () => {

        const targetId = button.dataset.copy;
        const target = document.getElementById(targetId);

        if (!target) {
            return;
        }

        try {

            await navigator.clipboard.writeText(target.textContent);

            const originalText = button.textContent;

            button.textContent = "Copied";

            setTimeout(() => {
                button.textContent = originalText;
            }, 1500);

        } catch (error) {

            console.error("Clipboard copy failed", error);

        }

    });

});
