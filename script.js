function checkFraud(){

let msg = document.getElementById("message").value.toLowerCase();

let fraudWords = [
"lottery",
"win money",
"otp",
"redeem code",
"bank details",
"free gift",
"click link"
];

for(let i=0;i<fraudWords.length;i++){

if(msg.includes(fraudWords[i])){

document.getElementById("result").innerHTML="⚠️ Fraud Message Detected!";
document.getElementById("result").style.color="red";
return;

}

}

document.getElementById("result").innerHTML="✅ Message Looks Safe";
document.getElementById("result").style.color="lightgreen";

}