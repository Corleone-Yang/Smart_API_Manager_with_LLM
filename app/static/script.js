document.getElementById("apiForm").addEventListener("submit", function (event) {
  event.preventDefault();

  const userInput = document.getElementById("userInput").value;

  fetch("/result", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({ userInput: userInput }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("resultContainer").innerText = data.result;
    })
    .catch((error) => {
      console.error("Error:", error);
      document.getElementById("resultContainer").innerText =
        "An error occurred while processing your request.";
    });
});
