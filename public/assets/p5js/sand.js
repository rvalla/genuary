let thecolor, blueclick, center;
let windy, wind;
let button, bw, bx, by, clicks;

function setup() {
	createCanvas(windowWidth, windowHeight);
	thecanvas = document.getElementsByTagName("canvas")[0];
	thecanvas.addEventListener("mousedown", processEv, false);
	thecolor = color(0,0,0);
	config = getURLParams();
	startConfig(config);
	background(255);
	frameRate(60);
	print("Genuary 2022: Sand...");
}

function draw() {
	stroke(thecolor);
	strokeWeight(getSandSize());
	if (windy === true){
		updateWind();
	}
	for (let i = 0; i < 10; i++){
		noiseX = i * random(-5,5) + wind[0];
		noiseY = i * random(-5,5) + wind[1];
		point(mouseX + noiseX, mouseY + noiseY);
	}
	image(button, bx, by, bw, bw);
}

function processEv() {
	if (buttonClick()){
		saveCanvas("genuary2022_day15_" + clicks);
	} else {
		updateColor(mouseX, mouseY);
		wind = [0,0];
	}
	event.preventDefault();
  return false;
}

function updateColor(x,y) {
	let r,g,b;
	r = map(mouseX, 0, width, 0, 255);
	g = map(mouseY / 2, 0, center[1], 0, 255);
	b = map(abs(mouseX - blueclick),0,width,0,255);
	blueclick = mouseX;
	thecolor = color(r,g,b);
}

function updateWind(){
	wind[0] += random(-6,6);
	wind[1] += random(-1,1);
}

function getSandSize(){
	return random([0,0,0,0,0,1,1,1,2,2,3,]);
}

function buttonClick(){
	return dist(mouseX, mouseY, bx + bw / 2, by + bw / 2) < bw;
}

function startConfig(config){
	button = loadImage("../assets/img/logo_256.png");
	bw = width / 20;
	if (width < height){
		bw = height / 20s;
	}
	bx = width / 2 - bw / 2;
	by = height - bw * 1.5;
	let w = config.windy;
	if (typeof(w) === "string" && w === "false") {
		windy = boolean(w);
	} else {
		windy = true;
	}
	wind = [0,0];
	center = [width/2,height/2];
	blueclick = 0;
}
