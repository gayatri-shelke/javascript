// function check_numbers(num1,num2){
//     if(num1%2 ===0 && num2%2===0){
//     console.log("Both are Even");
//     }
//     else{
//     console.log("Both are not Even");
//     }
//     }check_numbers(4,2)


var a= require("readline-sync")
function even(){
    var b=a.questionInt("enter the number")
    if(b%2==0){
        console.log("even");
    }
    else{
        console.log("odd");
    }
}even()