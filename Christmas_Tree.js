function sapin(n) {

  // Create Top of the Christmas Tree :
  let star = ["  ","+"];
  let top = [" ","/*\\"];

  function createTop (array) {
    for (i=1; i<n ; i++) {
      array.unshift(" ");
    };
    console.log(array.join(""));
  };

  createTop(star);
  createTop(top);

  // Create Middle of the Christmas Tree : 
  let line = ["/","*","\\"];

  /// To have enough blanks which will be
  /// decremented in the next loop
  for (i=1; i<=n ; i++) {
    line.unshift(" ");
  };

  for (i=1; i<=n ; i++){
    line.shift(" ");
    line.splice(n,0,"**");
    console.log(line.join(""));
  };

};

sapin(1);
sapin(2);
sapin(5);