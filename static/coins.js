const canvas = document.getElementById("coinCanvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const coinImage = new Image();
coinImage.src = "/static/imageanimations/coin_sprinte.png"; 
const spriteWidth = 64; 
const spriteHeight = 64;
const totalFrames = 16;
let frameIndex = 0; 

class Coin {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.vy = Math.random() * -10 - 10; 
        this.vx = (Math.random() - 0.5) * 10; 
        this.gravity = 0.5;
        this.frame = Math.floor(Math.random() * totalFrames); 
    }

    update() {
        this.vy += this.gravity;
        this.y += this.vy;
        this.x += this.vx;
        this.frame = (this.frame + 1) % totalFrames; 
    }

    draw() {
        ctx.drawImage(
            coinImage,
            this.frame * spriteWidth, 0, 
            spriteWidth, spriteHeight,
            this.x, this.y,
            40, 40 
        );
    }
}

const coins = [];
function spawnCoins(count) {
    for (let i = 0; i < count; i++) {
        coins.push(new Coin(canvas.width / 2, canvas.height - 50));
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    coins.forEach((coin, index) => {
        coin.update();
        coin.draw();
        if (coin.y > canvas.height) coins.splice(index, 1);
    });

    frameIndex = (frameIndex + 1) % totalFrames; 
    requestAnimationFrame(animate);
}

coinImage.onload = () => {
    spawnCoins(200);
    animate();
};
