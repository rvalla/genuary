let bg, thecolor, origin;
let startDay, todayDay;
let curveData, points;
let section, steps;
let clicks;

function setup() {
	createCanvas(windowWidth, windowHeight);
	thecanvas = document.getElementsByTagName("canvas")[0];
	thecanvas.addEventListener("mousedown", processEv, false);
	config = getURLParams();
	startConfig(config);
	background(bg);
	frameRate(24);
	print("Genuary 2022: Make something that will look completely different in a year...");
}

function draw() {
	if (section < 365) {
		for (i = 1; i < steps + 1; i++) {
			line(points[steps * section + i - 1][0],points[steps * section + i - 1][1],
						points[steps * section + i][0],points[steps * section + i][1]);
		}
		thecolor = createColor();
		stroke(thecolor);
		section += 1;
	} else {
		noLoop();
	}
	image(button, bx, by, bw, bw);
}

function processEv() {
	if (buttonClick()){
		saveCanvas("genuary2022_day23_" + clicks);
		clicks += 1;
	} else {
		background(bg);
		section = 0;
		curveData = buildCurve();
		points = buildPoints();
		loop();
	}
	event.preventDefault();
  return false;
}

function createColor() {
	let r = map(second(), 0, 59, 0, 120) + random(60) + 30;
	let g = map(minute(), 0, 59, 0, 120) + random(60) + 30;
	let b = map(hour(), 0, 23, 0, 120) + random(60) + 30;
	return color(r,g,b)
}

function startConfig(config){
	clicks = 1;
	button = loadImage("../assets/img/logo_256.png");
	thecolor = createColor();
	bg = color(0,51,66);
	section = 0;
	startDay = new Date("2022-1-22");
	bw = width / 20;
	if (width < height){
		bw = height / 12;
	}
	bx = width - bw * 1.5;
	by = height - bw * 1.5;
	number = Number(config.steps);
  if (typeof(number) === "number" && Number.isInteger(number)) {
    steps = number;
  } else {
		steps = 34;
	}
	number = Number(config.day);
  if (typeof(number) === "number" && Number.isInteger(number)) {
    todayDay = number;
  } else {
		today = year() + "-" + month() + "-" + day();
    todayDate = new Date(today);
		timeDifference = todayDate.getTime() - startDay.getTime();
		todayDay = round(timeDifference / (1000 * 60 * 60 * 24));
	}
	origin = [width/2,height/3];
	curveData = buildCurve()
	points = buildPoints()
	strokeWeight(3);
	stroke(thecolor);
}

function buildCurve(){
	data = [];
	for (let i = 0; i < 365; i++) {
		data[i] = [steps,0.015];
	}
	for (let i = 0; i < todayDay; i++){
		data[i][1] += random() / 55;
	}
	return data;
}

function buildPoints(){
	pointsList = [];
	pointsList[0] = origin;
	lastPoint = origin;
	angle = 0;
	for (let i = 0; i < 365; i++){
		for (let j = 0; j < steps; j++) {
			angle += curveData[i][1];
			nextPoint = newPoint(lastPoint, angle);
			pointsList.push(nextPoint);
			lastPoint = nextPoint;
		}
	}
	return pointsList;
}

function newPoint(lastPoint, angle){
	let x = cos(angle) * 2
	let y = sin(angle) * 2
	return [lastPoint[0] + x, lastPoint[1] + y]
}

function buttonClick(){
	return dist(mouseX, mouseY, bx + bw / 2, by + bw / 2) < bw;
}
