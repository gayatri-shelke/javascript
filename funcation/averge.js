// Write a function named average which takes 3 numbers and prints the sum of 3 numbers and the average of 3 numbers.

// Input:-

// Enter first number : 3

// Enter second number : 4

// Enter third number: 5

// Output :

// Sum of three numbers :-12

// Average of three numbers :-4
// var input = require('readline-sync');
// var number1 = input.questionInt('Enter the number1 :- ');
// var number2 = input.questionInt('Enter the number2 :- ');
// var number3 = input.questionInt('Enter the number3 :- ');
// function averge(a,b,c){
//     var input = require('readline-sync');

//     sum=0
//     var sum=number1+number2+number3
//     var avg=sum/3
        
// }
// console.log(sum,avg);
// averge()


function getVowels(str) {
    const m = str.match(/[aeiou]/gi);
    if (m === null) {
      return 0;
    }
    return m.length;
  }
  
  console.log(getVowels('sky'));