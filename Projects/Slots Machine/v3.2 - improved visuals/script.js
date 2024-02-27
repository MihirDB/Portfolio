const reel1 = document.getElementById('reel1');
const reel2 = document.getElementById('reel2');
const reel3 = document.getElementById('reel3');

// array that stores all the possible items a reel can display
let icons = ["🍷", "💵", "🍒", "😁"];

const btn = document.getElementById('btn');
let bal = document.getElementById('balNum');
let bet = document.getElementById('bet');

// when the spin button is pressed the following will happen
function spin() {

    // spin button is disabled so user cannot spam click
    btn.disabled = true;

    // changing values from string to number
    let balance = Number(bal.textContent);
    let betNum = Number(bet.value);

    // main logic of the game; checking balance and bet amount before user can initiate a spin
    if (betNum == 0) {
        console.log("You have not entered the bet amount!");
        btn.disabled = false;
    } else if (betNum < 0) {
        console.log("You have entered an invalid bet amount!");
        btn.disabled = false;
    } else if (balance == 0 || betNum > balance) {
        console.log("You do not have enough money!");
        btn.disabled = false;
    } else {
        console.log("this would have spun");
        change();
    }

    // changes the content of the reels randomly and added delay to reel 1 & 2
    function change() {
        let count = 0;
        let random = setInterval(() => {count += 1; reel1.textContent = icons[Math.floor(Math.random()*icons.length)]; 
                                        if (count == 10) {
                                            clearInterval(random);
                                        }
                                        }, 80);
        let count2 = 0;
        let random2 = setInterval(() => {count2 += 1; reel2.textContent = icons[Math.floor(Math.random()*icons.length)]; 
                                        if (count2 == 14) {
                                            clearInterval(random2);
                                        }
                                        }, 80);
        let count3 = 0;
        let random3 = setInterval(() => {count3 += 1; reel3.textContent = icons[Math.floor(Math.random()*icons.length)]; 
                                        console.log(reel1.textContent, reel2.textContent, reel3.textContent);
                                        if (count3 == 18) {
                                            clearInterval(random3);
                                            itemChecker();
                                        }
                                        }, 80);
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
        btn.disabled = false;
    }
};