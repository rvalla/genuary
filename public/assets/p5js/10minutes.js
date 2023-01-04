let b;
let c, notc;

function setup() {
	createCanvas(windowWidth, windowHeight);
	thecanvas = document.getElementsByTagName("canvas")[0];
	thecanvas.addEventListener("mousedown", processEv, false);
	setColors();
	background(0,51,66);
	b = new ball(c, 20, width/2,height/2);
	frameRate(60);
	print("Genuary 2023: 10 minutes...");
}

function draw() {
	if (dist(mouseX, mouseY, b.x, b.y) < b.d){
		b.accelerate(mouseX - pmouseX, mouseY- pmouseY);
		setColors();
		b.updateColor(c);
	}
	b.display();
	b.update();
	checkBallPosition();
	noStroke();
	fill(notc);
	ellipse(mouseX, mouseY, 20, 20);
}

function checkBallPosition(){
	if (b.x < 0){
		b.x = width;
	}
	if (b.x > width){
		b.x = 0;
	}
	if (b.y < 0){
		b.y = height;
	}
	if (b.y > height){
		b.y = 0;
	}
}

function processEv() {
	saveCanvas("Genuary2023_2", "jpg");
}

function setColors() {
	red = hour()*10+random(24);
	green = minute()*3+random(60);
	blue = second()*3+random(60);
	c = color(red,green,blue);
	notc = color(255-red,255-green,255-blue);
}


