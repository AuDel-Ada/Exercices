function sapin1(n) {
  const star = "  +"
  const top = " /*\\";

  console.log(star);
  console.log(top);

  for (i=1; i<=n ; i++){
    const line = "/***\\";
    console.log(line)
  };
};

sapin1(1);

function sapin2(n) {
  let star = ["  ","+"];
  let top = [" ","/*\\"];
  let line1 = ["/*","*","*\\"];

  // Create Top of the Christmas Tree :
  for (i=1; i<n ; i++){
    star.unshift(" ");
    top.unshift(" ");
    line1.unshift(" ");
  };

  console.log(star.join(""));
  console.log(top.join(""));
  console.log(line1.join(""))

  // Create Middle of the Christmas Tree : 
  let line2 = ["/*","*","*\\"];

  for (i=1; i<=n ; i++){
    line2.splice(n, 0, "*");
  };
  console.log(line2.join(""))
};

sapin2(2);