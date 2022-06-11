// Define an Anonymous function and call it by taking two 
// arguments to whether they are equal or not?

// var Anonymous=function(name,surname){
//     var a=(name===surname)
// }
// console.log(Anonymous("gayatri","shelke"));


// var name = function(str1,str2){
//     console.log(str1===str2)
//     }
//     name("gayatri","gayatri");



var is_array = function(input) {
    if (toString.call(input) === "[object Array]")
      return true;
    return false;   
      };
  console.log(is_array('w3resource'));
  console.log(is_array([1, 2, 4, 0]));
  