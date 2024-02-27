const reel1 = document.getElementById('reel1');
const reel2 = document.getElementById('reel2');
const reel3 = document.getElementById('reel3');

// array that stores all the possible items a reel can display
let icons = ["🍷", "💵", "🍒", "😁"];

const btn = document.getElementById('btn');
let bal = document.getElementsByTagName("p")[0];
let bet = document.getElementById('bet');

// when the spin button is pressed the following will happen
function spin() {
    // changing values from string to number
    let balance = Number(bal.textContent);
    let betNum = Number(bet.value);

    // main logic of the game; checking balance and bet amount before user can initiate a spin
    if (betNum == 0) {
        console.log("You have not entered the bet amount!");
    } else if (betNum < 0) {
        console.log("You have entered an invalid bet amount!");
    } else if (balance == 0 || betNum > balance) {
        console.log("You do not have enough money!");
    } else {
        console.log("this would have spun");
        change();
    }

    // changes the content of the reels randomly
    function change() {
        let count = 0;
        let random = setInterval(() => {count += 1; itemChanger(); console.log(reel1.textContent, reel2.textContent, reel3.textContent);
                                        if (count == 10) {
                                            clearInterval(random);
                                            itemChecker();
                                        }
                                        }, 75);
    }

    // checks the items to see if the user will win or lose
    function itemChecker() {
        console.log("Balance before Spin: " + balance);
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
        
        console.log("Bet amount: " + betNum);
        console.log("Balance after Spin: " + balance);
    }

    // random number is generated based on the array length and then sets it to the index of the array (works with any size array)
    function itemChanger () {
        reel1.textContent = icons[Math.floor(Math.random()*icons.length)];
        reel2.textContent = icons[Math.floor(Math.random()*icons.length)];
        reel3.textContent = icons[Math.floor(Math.random()*icons.length)];
    };
};