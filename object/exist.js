// Write a program to take 1 input and check whether given input exists in our object or not, if it exists print exists or else prints not exist.

// Example :
// var a=require("readline-sync")
// var n=a.question("enter the name")
// dict={"name":"Raju", "marks":56}
// for(i in dict){
//     if(i==n){
//         console.log("exsit");
//         break
//     }
//     else{
//         console.log("not exsite");
//     }
// }

// var readline = require('readline-sync');
// let n =readline.question('Enter the property name:');
// let dict={"name":"Raju", "marks":56}
// for (i in dict){
// if (i==n){
// console.log("exists");
// break
// }else{
// console.log("not exist");
// break
// }
// }




// // if input is “name” then output will be “exist”

// // If input is “class” then output will be “not exists”.



var mainStr = "the quick brown fox jumped  the lazy dog. the dog slept over the verandah."
var subStr = "over";
 
var c = mainStr.split(" ");
output="";
for(var i of c){
   output=output+i+" "
}
console.log(output);
