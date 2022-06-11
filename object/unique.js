// const list1=[]
// const word="MISSISSIPPI"
// let d={}
// for (var i of word) {
// if(list1.includes(i)){
// d[i]=d[i]+1


// }else{
// list1.push(i);
// d[i]=1;
// }
// }
// console.log(d);


// const list1=[]
// const word="gayatri"
// const  d={}
// for( var i of word){
//     if(list1.includes(i)){
//         d[i]=d[i]+1
//     }
//     else{
//         list1.push(i)
//         d[i]=1
//     }
// }console.log(d);

// var a=require("readline-sync")
// var name=a.question("type your name")

// const b=[]
// const d={}
// for(var i of name){
//     if(b.includes(i)){
//         d[i]=d[i]+1
//     }
//     else{
//         b.push(i)
//         d[i]=1
//     }

// }console.log(d);

array=["gayatri","neha","kajal","neha","kajal","rani","gayatri"]
list1=[]
for(var i of array){
    if(!list1.includes(i)){
        list1.push(i)
        // console.log(list1);
    }
    // console.log(list1);


}
console.log(list1);

