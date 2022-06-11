function add(){
    var a=require("readline-sync")
    var number=a.questionInt("enter the number")
    var sum=0
    var temp=number
    // var i=0
    while(number>0){
        var num=number%10
        var sum=sum+num
        var number=Math.floor(number/10)
    }
    if(temp%sum===0){
        console.log("harshd number");
    }
    else{
        console.log("not harshd numebr");
    }

}
add()