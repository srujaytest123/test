///////////////////////////////////////////////////////////////
// To validate the input query for max 200 characters
///////////////////////////////////////////////////////////////

// Get the input field and character count span
let inputField = document.getElementById("query_input_field");
let charCount = document.getElementById("charCount");

// Add an input event listener to the input field
inputField.addEventListener("input", function() {
  let inputLength = this.value.length;  
  charCount.innerText = "You have entered more than 200 characters - Limit is of (Max ";
  charCount.innerText += inputLength + " Characters";

  if (inputLength >= 200) {
    this.classList.add("is-invalid"); // Add the is-invalid class for Bootstrap validation styling
    charCount.classList.add("text-danger");
    charCount.innerText += ")";
  } else {
    this.classList.remove("is-invalid"); // Remove the is-invalid class if character limit is below 200
    charCount.classList.remove("text-danger");
    charCount.innerText = "";
  }
});

// Add a click event listener to the submit button for showing up MODAL dialog box
document.getElementById("submitBtn").addEventListener("click", function() {
  if (inputField.value.length === 0 || inputField.value.length >= 200) {
  // if (inputField.value.length >= 200) {
    // Show Bootstrap modal if character limit is reached
    event.preventDefault();
    $('#myModal').modal('show');
  } else {
    // Submit the form if character limit is below 100
    document.getElementById("myForm").submit();
  }
});


///////////////////////////////////////////////////////////////
// Run the code prettifier on page load
///////////////////////////////////////////////////////////////
window.onload = function () {  
  prettyPrint();
};
// Run the code to copy the code from output
function copy() {
  let codeBlock = document.querySelector("code");
  let codeContent = codeBlock.innerText;
  let tempInput = document.createElement("textarea");
  tempInput.value = codeContent;
  document.body.appendChild(tempInput);
  tempInput.select();
  document.execCommand("copy");
  document.body.removeChild(tempInput);
}