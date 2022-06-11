function reverseStr(str) {
    // str = "world";
    
    // step 1: split the string by using of String.prototype.split()
    let splitStr = str.split(""); 
    /*
      splitStr = str.split("");
      ["w", "o", "r", "l","d"]
    */
    
    //step 2: reverse the new created array by String.prototype.reverse()
    let reverseArr = splitStr.reverse();
    /*
      reverseArr = splitStr.reverse();
      ["d", "l", "r", "o","w"]
    */
    
    //step 3: join the reverseArr by the using of String.prototype.join()
    let joinStr = reverseArr.join("");
    /*
      joinStr = reverseArr.join("");
      "dlrow"
    */
    
    return joinStr;
  }