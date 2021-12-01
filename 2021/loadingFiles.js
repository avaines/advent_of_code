const filepath = "./list.txt"

// Synchronous:
function readTextSync(filename){
  fs = require('fs');
  return fs.readFileSync(filename).toString().split("\n");
}

let mylist = readTextSync(filepath)
console.log(mylist)


// Asynchronous:
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

let mylist2 = readTextAsync(filepath)
mylist2.then(data => {
  console.log(data);
});


