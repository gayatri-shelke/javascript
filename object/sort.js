// obj={'gayatri':6,'kajal':0,'Aabiru':2,'pooja':1}
// for(i in obj){
//     for(j in obj){
//         if(obj[i]<obj[j]){
            
//         }
//     }
// }
// console.log(obj);


console.log("WELCOME FLORA VEHICALS🚗🚕🚕🚕")
const r=require("readline-sync")
// //userinput for your current location*
var current_location=r.question("*write your current location* ")
if (current_location=="katarj" || current_location=="pune" || current_location=="satara"){
console.log("")
}else {
console.log("not avaible any service")
}
//user input for your drop location***
var drop_location=r.question("* your drop location* ")
if (drop_location=="tulsi bhag" || drop_location=="flora" || drop_location=="khopi"){
console.log("")
}else{
console.log("")
}
// userinput for option of vehical
var vehical=r.question("*which vehical do you want .car/🚕/auto/🛺 * ")
//Drivers data in the below list
var Driver_details=[
{"name":"ramesh",
"mobile_no":9027484938,
"location":"khedshivapur",
"feeedback":"drive slow and safe ",
"rate":450,
"type":"car"},

{"name":"raju",
"mobile_no":9827484938,
"location":"katraj",
"feeedback":"drive slow and safe ",
"rate":260,
"type":"auto"},

{"name":"rohit",
"mobile_no":9927789939,
"location":"khedshivapur",
"feeedback":"drive safe ",
"rate":550,
"type":"car"},

{"name":"parvin",
"mobile_no":9527484938,
"location":"pune",
"feeedback":"drive fast and safe ",
"rate":500,
"type":"car"},

{"name":"ajay",
"mobile_no":9027484938,
"location":"khedshivapur",
"feeedback":"drive fast and safe ",
"rate":200,
"type":"auto"
}

]

//using loop for our given Driver_details list
for (i in Driver_details) {
if (Driver_details[i]["type"]==vehical){
console.log(Driver_details[i])

}
}
//user input for selection of driver in given data
driverName=r.question("select driver name * ")
for (i in Driver_details){
if (Driver_details[i]["name"]==driverName){
console.log(Driver_details[i])


}
}
//Math.random use for calculate kilometer of pickup to drop point
var n = parseInt(Math.random() *100);
console.log(n,"km")

//we have to calculate price with considering km of travelling
console.log("your travelling price .....")
var totalprise=n*18
console.log("price",totalprise ,"Rs")
//userinput for ask coustomer that they want book vehical or not
booking=r.question("you want book the vehical..")
if (booking=="yes"){
console.log("your booking is done \n your vehical come in 10 min")


console.log("Wait for 5 sec for OTP")
//it is formula for using get OTP
var value=Math.floor(1000+Math.random()*9000)
console.log(value)
c=r.question("enter your OTP")
if(c=value){
console.log("successfull")
}
// user input for our money process*
paidMoney=r.question("how to paid money:-")
if (paidMoney=="UPI" || paidMoney=="cash" || paidMoney=="ATM"){
console.log(totalprise)
console.log("done!")
}
// userinput for rating **
rating=r.questionInt("How much star do u want to give ")

if (rating==1){
console.log(" ⭐ ","BAD")
}
if (rating==2){
console.log(" ⭐ ⭐ ","GOOD")
}
if (rating==3){
console.log(" ⭐ ⭐ ⭐ ","VERY GOOD")
}
if (rating==4){
console.log(" ⭐ ⭐ ⭐ ⭐ ","EXCELLENT")
}
if (rating==5){
console.log(" ⭐ ⭐ ⭐ ⭐ ⭐ ","OUTSTANDING")
}
feedBack=r.question("write your feedback here;") //user input for customer feedback**
if (feedBack==feedBack){
console.log(feedBack)
console.log("😍THANK YOU FOR YOUR FEEDBACK 😍")
}
}
else{
    console.log("Thanks for your visit")
    
    }