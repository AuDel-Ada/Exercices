function sapin(n) {

  // Create Top of the Christmas Tree :
  let star = ["  ","+"];
  let top = [" ","/*\\"];
  let line1 = ["/*","*","*\\"];

  function createTop (array) {
    for (i=1; i<n ; i++) {
      array.unshift(" ");
    }
    console.log(array.join(""));
  }

  createTop(star);
  createTop(top);
  createTop(line1);

  // Create Middle of the Christmas Tree : 
  let line2 = ["/*","*","*\\"];

  if (n == 1) {
    return
  } else {
    for (i=1; i<=n ; i++){
      line2.splice(n,0,"*");
    };
    console.log(line2.join(""))
  };
};

sapin(2);