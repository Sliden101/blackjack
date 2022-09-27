const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  

let dealerValue = 0;
let playerValue = 0;
let values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"];
let cards = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']
function getDeck(){
	let deck = new Array();
	for(let i = 0; i < cards.length; i++){
			let card = {Card: cards[i], Value: values[i]};
			deck.push(card);
    } return deck;
}
function shuffle(deck){
	for (let i = 0; i < 1000; i++){
		let location1 = Math.floor((Math.random() * deck.length));
		let location2 = Math.floor((Math.random() * deck.length));
		let tmp = deck[location1];
		deck[location1] = deck[location2];
		deck[location2] = tmp;
	}
}
function dealCard(deck){
    return deck.pop();
}
let deck = getDeck();
shuffle(deck);
let player1 = dealCard(deck);
let player2 = dealCard(deck);
let playerHand = [player1.Card, player2.Card];
playerValue = parseInt(player1.Value) + parseInt(player2.Value);
let dealer1 = dealCard(deck);
let dealer2 = dealCard(deck);
let dealerHand = [dealer1.Card, dealer2.Card];
dealerValue = parseInt(dealer1.Value) + parseInt(dealer2.Value);
console.log('Welcome to blackjack!');
console.log('Rules: You play against the dealer.\nYou start with two cards.\n You can hit as many times as you want.\n If you go over 21, you lose.\n If you get 21, you win.\n If you get a higher value than the dealer without going over 21, you win.\n If you get a lower value than the dealer without going over 21, you lose.\n If you get the same value as the dealer, you lose.\n');
console.log('Your hand: '+ playerHand);
rl.question('Hit or Stand? ', answer => {
    answer = answer.toLowerCase()
    if (answer == 'hit'){
        hit()
    }
    else{
        stand()
    }
    rl.close();
})
function stand(){
    while (dealerValue <= 16){
        let card0 = dealCard(deck);
        dealerHand.push(card0.Card);
        dealerValue += parseInt(card0.Value);
    }
    console.log('Dealer hand:' + dealerHand)
    if (dealerValue>21){
        console.log('You Win!');return
    }
    if (dealerValue==21){
        console.log('You Lose!');return
    }
    if (playerValue>dealerValue){
        console.log('You Win!');return
    }
    if (playerValue<dealerValue){
        console.log('You Lose!');return
    }
}
function hit(){
    let card0 = dealCard(deck);
    playerHand.push(card0.Card);
    playerValue += parseInt(card0.Value);
    console.log('Your hand:' + playerHand)
    rl.question('Hit or Stand? ', answer1 => {
        answer1 = answer1.toLowerCase()
        if (answer1 == 'hit'){
            hit()
        }
        else{
            stand()
            if (dealerValue==21){
                console.log('You Lose!');return
            }
            if (playerValue>dealerValue){
                console.log('You Win!');return
            }
            if (playerValue<dealerValue){
                console.log('You Lose!');return
            }
        }
        rl.close();
    })
    
}
