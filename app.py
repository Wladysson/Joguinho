from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from core.game import Game
from core.player import Player
from core.bank import Bank
from core.utils import reset_game

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

bank = Bank(saldo=0)
new_game = Game(bank=bank, slots=[], bet_price=0, logs=[])
player = Player(coins=100_000, ganhos=0)


@app.get('/')
async def home(request: Request):
    new_game.starGame(player)
    return templates.TemplateResponse(
        request=request, name="index.html",
        context={"slots": new_game.slots, "player": player, "bank": bank},
    )

## controla os moneys
money = 1000
bet = 1

@app.get("/money")
def get_money():
    return {"money": money}

@app.get("/bet")
def get_bet():
    return {"bet": bet}

@app.post("/update_bet")
def update_bet(new_bet: int):
    global bet
    if new_bet  <= 0 or new_bet > money:
        raise HTTPException(status_code=400, detail="Bet invalid")
    bet = new_bet
    return {"bet": bet}
    
@app.post("/place_bet")
def place_bet():
    global money
    if money < bet:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    money -= bet
    return {"money": money, "bet": bet}

@app.post("/reset_bet")
def reset_bet():
    global bet
    bet = 1
    return {"bet": bet}

@app.get("/showmoney")
def showmoney():
    return {"showmoney": money}

@app.get("/btnputmoney")
def btnputmoney():
    return {"btnputmoney": btnputmoney}


@app.get("/reset-saldo")
async def reset_saldo(request: Request):
    reset_game(player, new_game)

    return {"saldo": player.coins}

@app.post("/girar")
async def girar_roleta(request: Request, bet_price: float = None):

    new_game.bet_price = bet_price
    response = new_game.girar_roleta(player)

    if response["status"] == "error":
        raise HTTPException(status_code=403, detail="Sem saldo")
    
    return templates.TemplateResponse(
        request=request,
        name="slot_desenho.html",
        context={
            "slots": new_game.slots,
            "results": response.get("results", []),
            "apenas_ganho": response.get("apenas_ganho", 0),
            "player": player,
            "logs": new_game.logs,
            "bank": bank,
        },
    )

