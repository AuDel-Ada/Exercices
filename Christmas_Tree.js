function sapin(n) {

  // Create Top of the Christmas Tree :
  let star = ["  ","+"];
  let top = [" ","/*\\"];

  function createTop (array) {
    for (i=1; i<n ; i++) {
      array.unshift(" ");
    }
    console.log(array.join(""));
  }

  createTop(star);
  createTop(top);

  // Create Middle of the Christmas Tree : 
  let line = ["/","*","\\"];
  let place = 1;

  for (i=1; i<=n ; i++){
    line.unshift(" ");
    place ++;
    line.splice(place,0,"**");
    console.log(line.join(""));
  };
};

sapin(3);