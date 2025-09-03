// Variable declarations and conditionals (Part 1)
let a = 10;
let b = 5;
console.log(a+b)

if(a>b){
    console.log("a is greater than b")
}

// At least 2 custom functions (Part 2)
function subtraction(x,y){
    return x - y;

};
console.log(subtraction(9,2))


//function expression
const greeting = function(name,age){
    return `My name is ${name} i am ${age} years old`
}
console.log(greeting("Loyce",21))


//arrow function
const multiply = (a ,b) =>   a * b; console.log(multiply(53,40))

// At least 2 loop examples (Part 3)
// for  loop
for( let x = 0; x <= 8 ;x++){
    if(x % 2 ==1){
        console.log(`This number ${x} this number is odd !`)
        
    }
    else if(x % 2 == 0){
        console.log(`This is ${x} an even number`)
        
    }
    
}


// for of
const fruits = ["melon","orange","apple","mango","pineapple"]
for (let fruit of fruits ){
    if(fruit == "mango"){
        console.log("Found mango");
        break;
    }
}

// do ...while
num = 2;
do{
    console.log(`Number: ${num}`);
    num ++;
}
while(count <= 5);