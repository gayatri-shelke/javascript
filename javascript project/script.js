var seconds=document.getElementById('seconds')
var miliseconds=document.getElementById('miliseconds')
var start=document.getElementById('start')
var stop=document.getElementById('stop')
var reset=document.getElementById('reset')
var sec=0;
var milisec=0;
const timer=()=>{
    milisec++;
    if(milisec<9){
        miliseconds.innerHTML='0'+milisec;
    }
    if(milisec>9){
        sec++;
        seconds.innerHTML=milisec
    }
}
