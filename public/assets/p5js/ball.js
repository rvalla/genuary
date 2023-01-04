class ball {

	constructor(c, d, x, y){
	  this.c = c;
	  this.d = d;
	  this.x = x;
	  this.y = y;
	  this.dx = 0;
	  this.dy = 0;
	}
  
	display(){
	  fill(this.c);
	  noStroke();
	  ellipse(this.x, this.y, this.d, this.d);
	}
  
	update(){
	  this.brake();
	  this.x += this.dx;
	  this.y += this.dy;
	}

	updateColor(theColor){
	  this.c = theColor;
	}
  
	brake(){
	  this.dx = this.dx * 0.96;
	  this.dy = this.dy * 0.96;
	}
  
	bounce(){
	  this.dx = this.dx * -1;
	  this.dy = this.dy * -1;
	}
  
	move(x, y){
	  this.x = x;
	  this.y = y;
	}
  
	accelerate(ax, ay){
	  this.dx += ax;
	  this.dy += ay;
	}
  
	reset(){
	  this.x = windowWidth / 2;
	  this.y = windowHeight / 2;
	  this.dx = 0;
	  this.dy = 0;
	}
  
  }
  