const button = document.getElementById("recommendBtn");
const textarea = document.getElementById("query");
const resultsDiv = document.getElementById("results");
const loadingDiv = document.getElementById("loading");

button.addEventListener("click", async () => {
  const query = textarea.value.trim();

  if (!query) {
    alert("Please paste a job description");
    return;
  }

  loadingDiv.classList.remove("hidden");
  resultsDiv.innerHTML = "";

  try {
    const response = await fetch("http://127.0.0.1:8000/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: query,
        top_k: 5,
      }),
    });

    if (!response.ok) {
      throw new Error("API error");
    }

    const data = await response.json();

    loadingDiv.classList.add("hidden");

    if (!data.length) {
      resultsDiv.innerHTML = "<p>No recommendations found.</p>";
      return;
    }

    let html = "<h3>Recommended Assessments</h3><ul>";

    data.forEach((item) => {
      const name =
        item.name ||
        item.assessment ||
        item["Assessment Name"] ||
        (item.metadata && item.metadata.name) ||
        "Unknown Assessment";

      html += `<li>${name}</li>`;
    });

    html += "</ul>";
    resultsDiv.innerHTML = html;
  } catch (error) {
    console.error(error);
    loadingDiv.classList.add("hidden");
    resultsDiv.innerHTML = "Failed to fetch recommendations.";
  }
});
