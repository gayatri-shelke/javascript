
// You need to count the number of occurrences of each 
// unique character of a word "MISSISSIPPI" and store them 
// in an object in key, value pairs.

// Example:-

// Output :-

// dic={M:1,I:4,S:4,P:2}
// dic="MISSISSIPPI"
// i=0
// d={}
// for(i in dic.length){
    
    
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



const list1=[]
var word="gayatri"
var d={}
for(var i of word){
    if(list1.includes(i)){
        d[i]=d[i]+1
    }
    else{
        // list1.push(i)
        d[i]=1
    }
}
console.log(d);r