// Write a function named check_numbers_list which takes two lists of integers and checks 
// the numbers of the same index numbers whether they both are even or not. 
// For checking both even or not you can use the function written in the 
// previous question.

// If you give these lists [2, 6, 18, 10, 3, 75] and
//  [6, 19, 24, 12, 3, 87] then the output should come like this.


function list(a,b){
    if(a%2==0 && b%2==0){
        console.log("dono hai");
    }
    else{
        console.log("nahi hai");
    }

}list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])