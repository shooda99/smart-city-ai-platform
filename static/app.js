async function askVertexAI() {
   // Read question from textarea
   const question = document.getElementById("question").value;
   // Validate
   if (!question) {
       alert("Please enter a question.");
       return;
   }
   // Show loading message
   document.getElementById("answer").innerHTML = "Thinking...";
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
       document.getElementById("answer").innerHTML = data.answer;
   } catch (err) {
       document.getElementById("answer").innerHTML =
           "Something went wrong.";
       console.log(err);
   }
}