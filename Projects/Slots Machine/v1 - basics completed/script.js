const reel1 = document.getElementById('reel1');
const reel2 = document.getElementById('reel2');
const reel3 = document.getElementById('reel3');

const btn = document.getElementById('btn');
let bal = document.getElementsByTagName("p")[0];
console.log(typeof(bal.textContent));

let balance = Number(bal.textContent);

// when spin button is pressed
function spin() {

    if (balance > 0) {

        console.log("Before Spin " + bal.textContent);

        itemChanger();
        if (reel1.textContent == reel2.textContent & reel1.textContent == reel3.textContent) {
            balance += 10;
            bal.textContent = balance;
        } else if ( reel1.textContent == reel2.textContent || reel2.textContent == reel3.textContent) {
            balance += 5;
            bal.textContent = balance;
        } else {
            balance -= 10;
            bal.textContent = balance;
        }
    } else {
        console.log("Not enough balance!");
    }
    
    console.log("After Spin " + bal.textContent);
};

// Changes the content of the reels
function itemChanger () {
    reel1.textContent = Math.floor(Math.random()*5);
    reel2.textContent = Math.floor(Math.random()*5);
    reel3.textContent = Math.floor(Math.random()*5);
};

