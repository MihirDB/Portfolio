const reel1 = document.getElementById('reel1');
const reel2 = document.getElementById('reel2');
const reel3 = document.getElementById('reel3');

let icons = ["🍷", "💵", "🍒", "😁"];

const btn = document.getElementById('btn');
let bal = document.getElementsByTagName("p")[0];
let bet = document.getElementById('bet');

function spin() {
    let balance = Number(bal.textContent);
    let betNum = Number(bet.value);

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

    function change() {
        let count = 0;
        let random = setInterval(() => {count += 1; itemChanger(); console.log(reel1.textContent, reel2.textContent, reel3.textContent);
                                        if (count == 10) {
                                            clearInterval(random);
                                            itemChecker();
                                        }
                                        }, 75);
    }

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

    function itemChanger () {
        reel1.textContent = icons[Math.floor(Math.random()*icons.length)];
        reel2.textContent = icons[Math.floor(Math.random()*icons.length)];
        reel3.textContent = icons[Math.floor(Math.random()*icons.length)];
    };
};