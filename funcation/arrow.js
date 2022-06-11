// function sum(list1,list2){
//     sum1=list1+list2
//     console.log(sum1);
// //     i=0
//     sum=0
//     while(i<list1.length){
//         sum=sum+list1[i]

//     }i++
//     j=0
//     sum1=0
//     while(j<list2.length){
//         sum1=sum1+list2[j]
//     }j++

// sum3=sum1+sum
// console.log(sum3);
// // sum([2,3,4],[5,4,3])
// }
// sum([2,3,4,],[5,4,3])

// const obj = JSON.parse('{"name":"John", "age":30, "city":"New York"}');

// let sum=(a,b)=>{
//     c=a+b
//     console.log(c);
// }
// sum(2,3)

// let sum=function(a,b){
//     c=a+b
//     console.log(c);
// }
// sum(2,3)


// (function add(){
//     var name="hello gayatri"
//     console.log(name);
    
// })
// ()

// sum(2,3)
// var sum =(a,b)=>{
//     // c=a+b
//     console.log(a+b);
// }
// // sum(2,3)

function name() {
    console.log("Gayatri");
    console.log("kajal");
}
console.log("dimpal");
function sum() {
    setTimeout(() => {
        console.log("riya");    
    },3000);
    function add(a,b) {
        c=a+b
        setTimeout(()=>{
            console.log(c);
        },4000)    
    }
    add(6,5)
}
sum()
console.log("piya");
name()