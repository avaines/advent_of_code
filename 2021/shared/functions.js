// Importing Files

// Synchronously read's a file
function readTextToList(filename){
  fs = require('fs');
  return fs.readFileSync(filename).toString().split("\n");
}

// produces a list of integers from by reading a file and converting it to base 10 ints
function readTextToListInt(filename){
  return readTextToList(filename).map(function (x) { 
    return parseInt(x, 10); 
  });
}


function getFrequent(array, leastFrequent=false) {
  if (array.length == 0) return null;

  let frequencyMap = {}
  let minElements = []
  let maxElements = []

  for (var i = 0; i < array.length; i++) { // for every item in the array (indexed)
      var element = array[i];           // set el to the current element from the source array

      // Ensure the current element is represented in the map
      if (frequencyMap[element] == null) {   // if frequencyMap doesnt contain an instance of this element add it
          frequencyMap[element] = 1;
      } else {                    // otherwise, there is an instance of it, increment it
          frequencyMap[element]++;
      }
  }
  
  let minCount = frequencyMap[Object.keys(frequencyMap)[0]]
  let maxCount = frequencyMap[Object.keys(frequencyMap)[0]]
  
  // Get the lowest and highest occurence
  Object.keys(frequencyMap).forEach(key => {
      // console.log(key, frequencyMap[key]);

      if (frequencyMap[key] > maxCount){
          maxCount = frequencyMap[key]
          maxElements = [key]             // If this element has a higher count than everything before it, empty the array and it must be this one
      } else if (frequencyMap[key] == maxCount) {
          maxElements.push(key)           // If the element has same number of occurences of the the current max, add it to the max aray
      }
      
      if (frequencyMap[key] < minCount){
          minCount = frequencyMap[key]    // If this element has a lower count than everything before it, empty the array and it must be this one
          minElements = [key]
      } else if (frequencyMap[key] == minCount) {
          minElements.push(key)           // If the element has same number of occurences of the the current min, add it to the min aray
      }
  });

  if (leastFrequent==true) {
      return minElements.sort()
  } else {
      return maxElements.sort()
  }
}

// Export
module.exports = {
  getFrequent,
  readTextToList,
  readTextToListInt,
};
