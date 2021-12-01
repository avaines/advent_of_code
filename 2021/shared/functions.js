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



// Bad ideas be here:

// Asynchronously read a file
function readTextAsync(filename){
  return new Promise((resolve, reject) => {
    fs = require('fs');

    fs.readFile(filename, 'utf8', (err,data) => {
      if (err) {
        reject(err);
      }
      resolve(data.split("\n"));
    });
  });
}


// Export
module.exports = { 
  readTextToList,
  readTextToListInt,
  readTextAsync,
};
