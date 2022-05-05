

let tenTimes = 10;
let start;
let end;
let timeElapsed;



//// START - Creates an array with max lenght
let numbersArray = [] , max = 10000;

for( let i=1; numbersArray.push(i++) < max;);  // numbers = [1,2,3 ... max] 
console.log(`Array created with ${numbersArray.length} elements`);
//// END - Creates an array with max lenght

////Reusable function to calculate the average elapsed time
let averageTest = function average(nums) {
    return nums.reduce((a, b) => (a + b)) / nums.length;
}

//// START of Functions testing
let test1 = function () {
    let result;
    let averageTimesArray1 = [];

    for (let a = 0; a < tenTimes; a++){
    console.time('Function #1');
    start = window.performance.now()
    
     
    for(let i = 0; i < numbersArray.length; i++ ){
        result =+ numbersArray[i];
     };
    console.timeEnd('Function #1')
    end = window.performance.now()
    console.log(timeElapsed = end - start)
    averageTimesArray1.push(timeElapsed)
    
    }
    console.log(result);

    console.log(``);
    
    console.log(`the average time of execution of test1 was ${averageTest(averageTimesArray1).toFixed(3)}`);
    
    document.getElementById('average_test1').innerHTML = `Tempo médio de execução do código = ${(averageTest(averageTimesArray1).toFixed(3))} milisegundos`
};

test1()


let test2 = function () {
    let result2 
    let averageTimesArray2 = [];

    for (let a = 0; a < tenTimes; a++){
    console.time('Function #2');
    start = window.performance.now()
    
     
    l = numbersArray.reverse();
    i = l.length;
    while(i--) {
        result2 =+ +numbersArray[i];
        
    }
    console.timeEnd('Function #2')
    end = window.performance.now()
    console.log(timeElapsed = end - start)
    averageTimesArray2.push(timeElapsed)
    
    
    }
    console.log(result2);
    
    console.log(`the average time of execution of test1 was ${averageTest(averageTimesArray2).toFixed(3)}`);
    
};

test2()