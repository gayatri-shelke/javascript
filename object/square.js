var prompt = require('readline-sync');
// var n = prompt.questionInt('How many more times? ');
// d = {}
// // for (let i = 0; i <= n; i++) {
// // d[i] = i ** 2
// // }
// // console.log(d);

// i=1
// while(i<=n){
//     d[i]=i*i
//     i++
// }
// console.log(d);

d={}
i=1
while (i<2){
    const name=prompt.question("enter the name")
    const surname=prompt.question("enter the surname")
    d[name]=surname
    i++
}
console.log(d);