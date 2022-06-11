const a=require("readline-sync")
const number=a.questionInt("enter the number")
let array=[1,2,3,4, 5,6,7,3,4,6,8]
empty=[]
for(var i=0;i<array.length-number;i++){
    empty.push(array[i])
    for(var j=0;j<=number;j++){
        empty.push(array[-j])
    }

}
console.log(empty);