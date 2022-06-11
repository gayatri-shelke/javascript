// Write a Python program to combine two dictionary adding values for common keys.
// for i,j in d1.items():
//     for x,y in d2.items():
        
//         if i==x:
//             d3[i]=(j+y)
// # print(d3)
// d4={}
// for k in (d1,d2,d3,d4):
//     d4.update(k)
// print(d4)

// d1 = {'a': 100, 'b': 200, 'c':300}
// d2 = {'a': 300, 'b': 200, 'd':400}
// // d={}
// for(i in d1){
//     // console.log(i);
//     if(i in d2){
//         // console.log(i);
//         d2[i]=d1[i]+d2[i]
//         // console.log(d2[i]);
//     }
//     else{
//         d2[i]=d1[i]
//         // console.log(d2[i]);
//     }
// }console.log(d2);
// // output should be this: {'a': 400, 'b': 400, 'd': 400, 'c': 300}




// d1 = {'a': 100, 'b': 200, 'c':300}
// d2 = {'a': 300, 'b': 200, 'd':400}
// for (i in d1){
//     if(i in d2){
//         d2[i]=d1[i]+d2[i]
//     }
//     else{
//         d2[i]=d1[i]
//     }
// }
// console.log(d2);




// for(i in d1){
//     if(i in d2){
//         d2[i]=d1[i]+d2[i]
//     }
//     else{
//         d2[i]=d1[i]
//     }
// }
// console.log(d2);


var today = new Date();
  var day = today.getDay();
  var daylist = ["Sunday","Monday","Tuesday","Wednesday ","Thursday","Friday","Saturday"];
//   console.log("Today is : " + daylist[day] + ".");
  var hour = today.getHours();
  var minute = today.getMinutes();
  var second = today.getSeconds();
  var prepand = (hour >= 12)? " PM ":" AM ";
  hour = (hour >= 12)? hour - 12: hour;
  if (hour===0 && prepand===' PM ') 
  { 
  if (minute===0 && second===0)
  { 
  hour=12;
  prepand=' Noon';
  } 
  else
  { 
  hour=12;
  prepand=' PM';
  } 
  } 
  if (hour===0 && prepand===' AM ') 
  { 
  if (minute===0 && second===0)
  { 
  hour=12;
  prepand=' Midnight';
  } 
  else
  { 
  hour=12;
  prepand=' AM';
  } 
  } 
console.log("Current Time : "+hour + prepand + " : " + minute + " : " + second);