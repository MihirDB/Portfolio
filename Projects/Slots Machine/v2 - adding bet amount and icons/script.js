const reel1 = document.getElementById('reel1');
const reel2 = document.getElementById('reel2');
const reel3 = document.getElementById('reel3');

let icons = ["💳", "💵", "💰" ]

const btn = document.getElementById('btn');
let bal = document.getElementsByTagName("p")[0];
let bet = document.getElementById('bet');
console.log(typeof(bal.textContent));

let balance = Number(bal.textContent);


// when spin button is pressed
function spin() {
    let betNum = Number(bet.value);

    if (balance > 0 & betNum > 0 & betNum <= balance ) {

        console.log("Before Spin Balance " + bal.textContent);
        console.log("Bet Amount after spin is pressed " + betNum);
        
        itemChanger();
        console.log(reel1.textContent, reel2.textContent, reel3.textContent);

        if (reel1.textContent == reel2.textContent & reel1.textContent == reel3.textContent) {
            balance += betNum;
            bal.textContent = balance;
        } /*else if ( reel1.textContent == reel2.textContent || reel2.textContent == reel3.textContent) {
            balance += betNum;
            bal.textContent = balance;
        } */else {
            balance -= betNum;
            bal.textContent = balance;
        }
    } else {
        console.log("Not enough balance or bet amount not added!");
    };
    
    console.log("After Spin " + bal.textContent);
};

// Changes the content of the reels
function itemChanger () {
    reel1.textContent = icons[Math.floor(Math.random()*3)];
    reel2.textContent = icons[Math.floor(Math.random()*3)];
    reel3.textContent = icons[Math.floor(Math.random()*3)];
};


