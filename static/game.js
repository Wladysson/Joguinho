const txtbet = document.querySelector('#bet');
const elwin = document.querySelector('#el-win');
const txtwin = document.querySelector('#win');
const elmoney = document.querySelector('#el-money');
const txtmoney = document.querySelector('#money');
const elgame = document.querySelector('#game-area');
const btnbet = document.querySelector('#btn-bet');
const btnspin = document.querySelector('#btn-spin');
const btnputmn = document.querySelector('#btn-putmoney');

let money = 0;
let bet = 1;

async function getMoney() {
    try {
        const response = await fetch('http://localhost:8000/money');
        const data = await response.json();
        money = data.money;
        console.log('Money:', money);
    } catch (error) {
        console.error('Error fetching money:', error);
    }
}

async function getBet() {
    try {
        const response = await fetch('http://localhost:8000/bet');
        const data = await response.json();
        bet = data.bet;
        console.log('Bet:', bet);
    } catch (error) {
        console.error('Error fetching bet:', error);
    }
}

async function setBet(newBet) {
    try {
        const response = await fetch('http://localhost:8000/update_bet', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ new_bet: newBet }),
        });

        if (!response.ok) {
            throw new Error('Invalid bet');
        }

        const data = await response.json();
        bet = data.bet;
        console.log('Bet updated to:', bet);
    } catch (error) {
        console.error('Error setting bet:', error);
    }
}

async function placeBet() {
    try {
        const response = await fetch('http://localhost:8000/place_bet', {
            method: 'POST',
        });

        if (!response.ok) {
            throw new Error('Insufficient funds or invalid bet');
        }

        const data = await response.json();
        money = data.money;
        console.log('New money value:', money);
    } catch (error) {
        console.error('Error placing bet:', error);
    }
}

getMoney();
getBet();
// ate aqui

let betstep = 0;
const betarr = [1,3,5,10,20,30,50,100,200,500,1000];
const arr = ['🍏','🍎','🍐','🍊','🍋','🍌','🍉','🍇','🍓','🍒','🥭','🥝'];
//const arr = ['🍏','🍎','🍐','🍊'];
function getItem(i){
    return arr[i];
}
const cols = document.querySelectorAll('.column');
const col1 = cols[0];
const col2 = cols[1];
const col3 = cols[2];
const col4 = cols[3];
const col5 = cols[4];

//ADICIONAVA DINHEIRO, BOTAO PUTMONEY
btnputmn.addEventListener('click',()=>{//AJEITAR
    if(money == 0){
        money = 1000;
        elmoney.classList.remove('col-red');
        startGame();
    }
},false);

    function startGame(){
        function showMoney(){
        elwin.style.display = 'none';
        elmoney.style.display = '';
        txtmoney.innerHTML = money;
    }
    async function showMoney() { 
        try {
            const response = await fetch('http://localhost:8000/money'); // Busca na API
            if (!response.ok) {
                throw new Error('Falha ao obter o valor de money');
            }
            const data = await response.json();
            money = data.money;  // Atualiza o valor da variável global
    
            // Atualiza a interface
            elwin.style.display = 'none';
            elmoney.style.display = '';
            txtmoney.innerHTML = money;
        } catch (error) {
            console.error('Erro ao obter o valor de money:', error);
        }
    }

    showMoney();
    function showWin(w){
        elmoney.style.display = 'none';
        elwin.style.display = '';
        txtwin.innerHTML = w;
        setTimeout(()=>{
            showMoney();
            enableBtns();
        }, 2000);
    }
    function setBet(){//AJEITAR
        betstep++;
        if(betstep < betarr.length){
            bet = betarr[betstep];
        }else{
            betstep = 0;
            bet = betarr[betstep];
        }
        txtbet.innerHTML = bet;
        elmoney.classList.remove('col-red');
    }

    btnbet.addEventListener('click',setBet,false);
    function getRandomInt(){
        var max = arr.length;
        return Math.floor(Math.random()*max);
    }
    function addItems(el,n){
        for(var i=0;i<n;i++){
            var ind = getRandomInt();
            var d = document.createElement('div');
            d.setAttribute('data-ind',ind);
            d.innerHTML = `<i>${getItem(ind)}</i>`;
            el.prepend(d);
        }
    }
    function getColumns(){
        addItems(col1,10);
        addItems(col2,20);
        addItems(col3,30);
        addItems(col4,40);
        addItems(col5,50);
    }
    function getStartItems(){
        for(const c of cols){
            addItems(c,3);
        }
    }

    getStartItems();
    function checkMoney(){//AJEITAR
        if(money > 0 && money >= bet){
            return true;
        }else if(money > 0 && money < bet){
            elmoney.classList.add('col-red');
            return false;
        }else{
            elmoney.classList.add('col-red');
            return false;
        }
    }

    function disableBtns(){
        btnbet.setAttribute('disabled','1');
        btnspin.setAttribute('disabled','1');
    }
    function enableBtns(){
        btnbet.removeAttribute('disabled');
        btnspin.removeAttribute('disabled');
    }

    /* animaçao das roletas */
    function gradualSpin(duration = 10000) {
        let speed = 0.1; // Começa MUITO rápido (0.05s)
        let elapsedTime = 0;
        let interval = setInterval(() => {
            if (elapsedTime >= duration) {
                clearInterval (interval);
                enableBtns(); // Habilita os botões ao final
                checkWin(); // Verifica o resultado final
                return;
            }
    
            var check = checkMoney();
            if (check) {
                money -= bet;
                showMoney();
                disableBtns();
                getColumns();
    
                for (const c of cols) {
                    c.style.transition = `${speed}s ease-out`;
                    var n = c.querySelectorAll('div').length;
                    var b = (n - 3) * 160;
                    c.style.bottom = `-${b}px`;
                }
    
                col5.ontransitionend = () => {
                    checkWin();
                    for (const c of cols) {
                        let items = c.querySelectorAll('div');
                        for (let i = 0; i < items.length; i++) {
                            if (i >= 3) {
                                items[i].remove();
                            }
                        }
                        c.style.transition = '0s';
                        c.style.bottom = '0px';
                    }
                };
            }
    
            elapsedTime += 500; // A cada 0.5s a velocidade diminui
            speed += 0.1; // Aumenta o tempo de giro suavemente
        }, 500);
    }
    
    // Modifica o botão para iniciar a roleta gradualmente
    btnspin.addEventListener('click', () => {
        disableBtns();
        gradualSpin(20000); // Faz a roleta girar 
        triggercoins();
    }, false);

    btnspin.addEventListener('click',Spin,false);
    function checkWin(){
        var arrLine1 = [];
        var arrLine2 = [];
        var arrLine3 = [];
        for(const c of cols){
            var l1 = Number(c.querySelectorAll('div')[0].dataset.ind);
            var l2 = Number(c.querySelectorAll('div')[1].dataset.ind);
            var l3 = Number(c.querySelectorAll('div')[2].dataset.ind);
            arrLine1.push(l1);
            arrLine2.push(l2);
            arrLine3.push(l3);
        }

        function copiesArr(arr, copies) {
            let map = new Map();
            for (let elem of arr) {
                let counter = map.get(elem);
                map.set(elem, counter ? counter + 1 : 1);
            }
            let res = [];
            for (let [elem, counter] of map.entries())
                if (counter >= copies)
                    res.push(elem+':'+counter);
            return res;
        }
        var arrC1 = copiesArr(arrLine1, 3);
        var arrC2 = copiesArr(arrLine2, 3);
        var arrC3 = copiesArr(arrLine3, 3);
        ///

        function getCountCopies(arr){
            var str = arr[0];
            return Number(str.split(':')[1]);
        }
        function setBG(arr,row){
            var str = arr[0];
            var ind = str.split(':')[0];
            var cnt = Number(str.split(':')[1]);
            for(const c of cols){
                var bitem = c.querySelectorAll('div')[row];
                if(bitem.dataset.ind == ind){
                    bitem.classList.add('bg');
                }
            }
        }

        var stopspin = false;
        var resL1 = 0;
        var resL2 = 0;
        var resL3 = 0;
        if(arrC1.length > 0){//AJEITAR
            stopspin = true;
            var cnt = getCountCopies(arrC1);
            setBG(arrC1,0);
            if(cnt == 3) resL1 = 2*bet;
            if(cnt == 4) resL1 = 5*bet;
            if(cnt == 5) resL1 = 1000*bet;
        }
        if(arrC2.length > 0){
            stopspin = true;
            var cnt = getCountCopies(arrC2);
            setBG(arrC2,1);
            if(cnt == 3) resL2 = 100*bet;
            if(cnt == 4) resL2 = 1000*bet;
            if(cnt == 5) resL2 = 100000*bet;
        }
        if(arrC3.length > 0){
            stopspin = true;
            var cnt = getCountCopies(arrC3);
            setBG(arrC3,2);
            if(cnt == 3) resL3 = 2*bet;
            if(cnt == 4) resL3 = 5*bet;
            if(cnt == 5) resL3 = 1000*bet;
        }
        
        if(stopspin){
            var win = resL1+resL2+resL3;
            showWin(win);
            money = money + win;
        }else{
            enableBtns();
        }
    }
}
