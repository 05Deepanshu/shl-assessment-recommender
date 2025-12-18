const button = document.getElementById("recommendBtn");
const queryInput = document.getElementById("query");
const loading = document.getElementById("loading");
const resultsDiv = document.getElementById("results");

button.addEventListener("click", recommend);

async function recommend() {
  const query = queryInput.value.trim();
  if (!query) return;

  resultsDiv.innerHTML = "";
  loading.classList.remove("hidden");

  try {
    const response = await fetch("http://127.0.0.1:8000/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query, top_k: 10 })
    });

    const data = await response.json();
    loading.classList.add("hidden");

    data.forEach(item => {
      const card = document.createElement("div");
      card.className = "card";

      card.innerHTML = `
        <span class="badge">${item.test_type || "Assessment"}</span>
        <h3>${item.name || item["Assessment Name"]}</h3>
        <p>${item.description || "No description available."}</p>
      `;

      resultsDiv.appendChild(card);
    });
  } catch (err) {
    loading.classList.add("hidden");
    resultsDiv.innerHTML = "<p>Failed to fetch recommendations.</p>";
  }
}
