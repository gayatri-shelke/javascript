// function is_equal_lenth(str1,str2){
//     if(str1.length === str2.length){
//     console.log(str1);
//     console.log(str2);
//     }
//     else if(str1.length > str2.length){
//     console.log(str1);
//     }
//     else{
//     console.log(str2);
//     }
//     }

// const sum = ()=> "good morning"
//     // console.log("hello");



// console.log(sum());

// var myDict= {
//     1: 'NAVGURUKUL',
//     2: 'IN',
//     3:{
//     'A' : 'WELCOME',
//     'B' : 'To',
//     'C' : 'DHARAMSALA'
//     }
//     }
    
//     delete myDict[3]['A']

//     console.log(myDict);
    


// function sum(a,b){
//     sum=0
//     for(i in a){
//         // for(j in b)
//         sum=sum+a[i]
//         console.log(sum);
//     }
// }sum([2,4,5,6],[2,3,4,5])


var readline = require('readline-sync');
var students={}
for (let step = 0; step <3; step++){
var name =readline.question("Enter your name:");
var marks=readline.questionInt("Enter the marks");
students[name]=marks;
}
console.log(students);