"use strict";


function wordsInCommon(words1, words2) {
  const words1Set = new Set(words1);
  const words2Set = new Set(words2);

  const result = new Set();

  for (const word of words1Set) {
    if (words2Set.has(word)) {
      result.add(word);
    }
  }
return result 
}


function kidsGame(names) {
  const output = [names.pop(0)];

  const first_letter_to_words = {};

  for (const name of names) {
    const firstChar = name[0];
    if (!first_letter_to_words[firstChar]) {
      first_letter_to_words[firstChar] = [name];
    }
    else {
      first_letter_to_words[firstChar].push(name);
    }
  }
  console.log(first_letter_to_words)
  while (true) {
    const lastWord = output[(output.length) - 1]
    const startLetter = lastWord[(lastWord.length) - 1]

    if (startLetter in first_letter_to_words) {
      const word = first_letter_to_words[startLetter].pop(0);
      output.push(word);
    }
    else {
      break;
    }
  }
  return output
}
