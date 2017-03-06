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
  var pw = document.getElementById("pw").value.toLowerCase();
  if (pw) {
    pw = getVariations(pw); // Convert any letter-to-number substitutions

    // If this gets set to true, then the password variant was found
    //   in the dicitonary word list, and this isn't a secure password
    var isSecure = true;
    var matchingWord = "";

    // Make a list of alternate versions of the string to check

    // Iterate over the list of words to see if the password is contained
    //   in the dictionary word list
    for (var i = 0; i < wordsList.length; i++) {
      // If the password variation matches the dictionary word, it's not a secure password
      if (wordsList[i] == pw) {
        isSecure = false;
        matchingWord = wordsList[i];
        break;
      }
    }

    printResults(isSecure, matchingWord);
  }
}

function getVariations(pw) {
  // Check and convert common letter-to-number substitutions
  //   (e.g. "3" -> "e", "4" -> "a")
  pw = pw.replace(/[1!]/g, "i");
  pw = pw.replace(/2/g, "z");
  pw = pw.replace(/3/g, "e");
  pw = pw.replace(/[@4]/g, "a");
  pw = pw.replace(/[$5]/g, "s");
  pw = pw.replace(/[69]/g, "g");
  pw = pw.replace(/7/g, "t");
  pw = pw.replace(/8/g, "b");
  pw = pw.replace(/0/g, "o");

  return pw;
}

function printResults(isSecure, word) {
  if (isSecure) {
    document.getElementById("results").style.color = "#01426a";
    document.getElementById("results").innerHTML = "No match found. This password is secure against dictionary attacks!";
  }
  else {
    document.getElementById("results").style.color = "#f4364c";
    var resultsStr = "That's not a secure password! This password matched the word \"" + word + "\" in the dictionary.";
    document.getElementById("results").innerHTML = resultsStr;
  }

}