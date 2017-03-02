var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true; 
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false; 
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
  // Get user-entered password from input box
  var pw = document.getElementById("pw").value;
  var pwsToCheck = [pw];
  console.log(pwsToCheck);

  // If this gets set to true, then the password variant was found
  //   in the dicitonary word list, and this isn't a secure password
  var isSecure = true;
  var matchingWord = "";

  // Make a list of alternate versions of the string to check

  // Iterate over the list of words to see if any of the password variations
  //   are contained in the dictionary word list
  for (var i = 0; i < wordsList.length; i++) { // for each word in the dictionary
    for (var j = 0; j < pwsToCheck.length; j++) { // for each password variation
      // If the password variation matches the dictionary word, it's not a secure password
      if (wordsList[i] == pwsToCheck[j]) {
        isSecure = false;
        matchingWord = wordsList[i];
        break;
      }
    } // end for each password variant
  } // end for each word in the dictionary

  printResults(isSecure, matchingWord);

}

function getVariations(pw) {
  return [pw];
}

function printResults(isSecure, word) {
  if (isSecure) {
    document.getElementById("results").innerHTML = "No match found. This password is secure against dictionary attacks!";
  }
  else {
    var resultsStr = "That's not a secure password! This password matched the word \"" + word + "\" in the dictionary.";
    document.getElementById("results").innerHTML = resultsStr;
  }

}