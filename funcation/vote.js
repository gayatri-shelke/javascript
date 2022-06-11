// Write a function named eligible_for_vote which takes age as a parameter and prints if he/she is eligible to vote or not. ( Consider minimum age of voting to be 18. )

// Example:

// If a user given age as less than 18 prints “not eligible “ or else if a user enters 18 or more than 18 prints “you are eligible”.

// Input:

// 18

// 16

var a=require("readline-sync")
function age(){
    var b=a.questionInt("enter the age")
    if(18<b){
        console.log("vote eligible");
    }
    else{
        console.log("not eligible");
    }

    
}age()