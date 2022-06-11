// const campus={"camp_name":"Bangalore_campus","establish":2016,"election":"three_months"}
// for(let eachKey in campus){
//   console.log(eachKey)
// }
 
// var person={"name":"gouri","surname":"maity","age":37}
 
// for (person_details in person){
// console.log(person_details+ "= "+person[person_details]);
// }


// var person={"name":"gouri","surname":"maity","age":37}
 
// for (person_details in person){
// console.log(person_details);
// }

// const campus_list=["Bangalore","Dharamshala","Pune","Bangalore_another"]
// for(let campus in campus_list){
//    console.log(campus)
// }

// var myDetails={
//     "name":"kumar",
//     "age":24
//  }
//  console.log(myDetails.hasOwnProperty("name"));
 
// var myHome = {
//     "name": "Mannat",
//     "location":"Mumbai",
//     "Colour":"black",
//     "owner":"sharukh khan",
//     "neighbours": ["everything!"],
//     "isGood":true
//   };
  
//   delete myHome.name;
//   console.log(myHome)
 
 
// var myHome = {
//     "name": "Mannat",
//     "location":"Mumbai",
//     "Colour":"black",
//     "owner":"sharukh khan",
//     "neighbours": ["everything!"]
//   };
  
  
// myHome.name="gayu";
  
// console.log(myHome);

// let myFavouriteGames = ["chess", "Ludo", "Badminton"]
// console.log(myHome[2])


const person = {
    firstName: "John",
    lastName : "Doe",
    language : "EN"
  };
  
  // Change a property
  Object.defineProperty(person, "language", {value : "NO"});
  console.log();
 