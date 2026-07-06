async function askVertexAI() {

    // Read question from textarea
    const question = document.getElementById("question").value.trim();

    // Validate
    if (!question) {
        alert("Please enter a question.");
        return;
    }

    // Show loading message
    document.getElementById("answer").innerHTML = "Thinking...";

    // Hide feedback while generating a new response
    document.getElementById("feedback-section").style.display = "none";
    document.getElementById("feedback-message").innerHTML = "";

    try {

        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        // Display AI response
        document.getElementById("answer").innerHTML = data.answer;

        // Show feedback section
        document.getElementById("feedback-section").style.display = "block";

    } catch (err) {

        document.getElementById("answer").innerHTML =
            "Something went wrong.";

        console.error(err);
    }
}

// -----------------------------
// Suggested Question Chips
// -----------------------------
document.querySelectorAll(".suggestion").forEach(item => {

    item.addEventListener("click", function () {

        document.getElementById("question").value =
            this.innerText.trim();

    });

});

// -----------------------------
// Feedback Buttons
// -----------------------------
document.getElementById("like-btn").addEventListener("click", function () {

    document.getElementById("feedback-message").innerHTML =
        "✅ Thanks for your feedback!";

});

document.getElementById("dislike-btn").addEventListener("click", function () {

    document.getElementById("feedback-message").innerHTML =
        "🙏 Thank you! We'll use your feedback to improve the assistant.";

});