/********************************************************************
 *ChessRobotControl.ino Robot Control File                                   *
 *Witten by Nicholas Maselli                                        *
 *                                                                  *
 *Purpose: This program controls a chess robot by detecting piece   *
 *changes on the board using reed switches, control stepper motors, *
 *and relaying information to and from python.                      *                          
 *                                                                  *
 *Version: 1.0                                                      *
 *Date: June 30th, 2017                                              *
 ********************************************************************/
#include <Stepper.h>
#include <Servo.h> 
#include <Wire.h>
#include "Adafruit_MCP23017.h"

int XSwitch = 1;
int YSwitch = 1;
int ZSwitch = 1;

const int stepsPerLimit = 1;
const int stepsPerRevolution = 200;
const int stepsPerTile = 65*stepsPerRevolution;

int Xpul = 6;
int Xdir = 7;
int Ypul = 8;
int Ydir = 9;
int Zpul = 10;
int Zdir = 11;

Stepper XStepper(stepsPerRevolution, Xdir, Xpul); 
Stepper YStepper(stepsPerRevolution, Ydir, Ypul);
Stepper ZStepper(stepsPerRevolution, Zdir, Zpul);
Servo gripservo;

/*Precise Position variables*/
int XPrecisePosition = 0;
int YPrecisePosition = 0;
int ZPrecisePosition = 0;

int XCoordinates[8][8];
int YCoordinates[8][8];
int ZCoordinates[8][8];

int XCaptureCoordinates[16];
int YCaptureCoordinates[16];
int ZCaptureCoordinates[16];

/*Player Color*/
bool color = 0;

/*Capture variables*/
byte captures = 0;
bool holding = 0;

/*Detection Variables*/
byte board_length = 8;
byte board_total = 64;

byte numberOfChanges = 0;
byte changes[4];
byte changeType[4];
byte moveArray[4];

byte squares[64];
byte check_squares[64];

//Give convenient names to the control pins
#define CONTROL0 5    
#define CONTROL1 4
#define CONTROL2 3
#define CONTROL3 2

Adafruit_MCP23017 mcp1;
Adafruit_MCP23017 mcp2;

byte mux0array[16];
byte mux1array[16];
byte mux2array[16];

void setup() {
  
  //1400 max speed for x and y, 1200 for z
  XStepper.setSpeed(1400); 
  YStepper.setSpeed(1400); 
  ZStepper.setSpeed(1200);
  gripservo.attach(12); //Attaches grip servo
  
  Serial.begin(9600); 
  
  //Initialize moves
  for (int i=0; i < 4; i++) {
    changes[i] = 64;
    changeType[i] = 2;
    moveArray[i] = 64;
  }  
  
  //Initialize squares
  for (int i=0; i < board_total; i++) {
    squares[i] = 1;
  }

  //Set MUX control pins to output
  pinMode(CONTROL0, OUTPUT);
  pinMode(CONTROL1, OUTPUT);
  pinMode(CONTROL2, OUTPUT);
  pinMode(CONTROL3, OUTPUT); 
 
  mcp1.begin(0);
  mcp2.begin(1);
  
  //Squares 1-16
  for (int i=0; i<16; i++) {
      mcp1.pinMode(i, INPUT);
      mcp1.pullUp(i, HIGH);
      mcp2.pinMode(i, INPUT);
      mcp2.pullUp(i, HIGH);    
  }  
  
  //Squares 17-32
  pinMode(14, INPUT_PULLUP);

  //Squares 33-48
  pinMode(15, INPUT_PULLUP);

  //Squares 49-64
  pinMode(16, INPUT_PULLUP);

  pinMode(13, INPUT);
  
  color = getPlayerColor(); 
  calibrateCoordinates();
  home();
  setSquares();
  correctCheckSquares(); 

  if (color == 0) {
    playerWhite();
  }

  if (color == 1) {
    playerBlack();
  }
}

void playerWhite() {
  while(true) {
     /*Player Input*/
    PlayerInput();
    
    /*Computer Input*/
    ComputerInput();  
  }
}

void playerBlack() {
  while(true) {
    /*Computer Input*/
    ComputerInput();
    
    /*Player Input*/
    PlayerInput();
  }
}

void loop() {
}

/*Takes in player input by moving pieces on the board and
  relays this information to python through serial port*/
void PlayerInput() {
  setSquares();
  resetChanges();

  while(mcp2.digitalRead(8) == 1) {    
    Serial.print("Number of changes:");
    Serial.println(numberOfChanges);

    printSquares();
    setSquares();    
    detectChanges();

    //Allows player to reset board if computer makes an error
    if (mcp2.digitalRead(9) == 0) {
      numberOfChanges = 0;
    }

    //Allows player to home robot if arm makes a mechanical error
    if (mcp2.digitalRead(10) == 0) {
      home();
    }
    
    delay(1000);
  }
  
  Serial.print("Final number of changes:");
  Serial.println(numberOfChanges);

  calculateMove();
  if (numberOfChanges == 2) {
    Serial.print("x");
    Serial.write(moveArray[0]);
    Serial.write(moveArray[1]);
  }

  if (numberOfChanges == 3) {
    Serial.print("y");
    Serial.write(moveArray[0]);
    Serial.write(moveArray[2]);
  }

  if (numberOfChanges == 4) {
    Serial.print("z");
    Serial.write(moveArray[0]);
    Serial.write(moveArray[1]);
 }

  resetChanges();
  delay(1000);
}

void ComputerInput() {
  String input = serialInput();
  turn(input);
  delay(1000);
}

/*******************************************/
/*****   X, Y, and Z home functions    *****/
/*******************************************/
void home() {
  ZHome();
  YHome();
  XHome(); 
}

void XHome() {
  //XSwitch = mcp2.digitalRead(15);
  XSwitch = digitalRead(13);
  while(XSwitch != 1) {
    XStepper.step(-stepsPerLimit);
    //XSwitch = mcp2.digitalRead(15);
    XSwitch = digitalRead(13);
    //Serial.println(XSwitch);  
  }

  XPrecisePosition = 0;
  Serial.println("X Limit Switch Hit");
}

void YHome() {
  YSwitch = mcp2.digitalRead(14); 
  while(YSwitch != 0) {             
    YStepper.step(-stepsPerLimit);
    YSwitch = mcp2.digitalRead(14);
    //Serial.println(YSwitch);    
  }
  
  YPrecisePosition = 0;
  Serial.println("Y Limit Switch Hit"); 
}

void ZHome() {  
  ZSwitch = mcp2.digitalRead(13); 
  while(ZSwitch != 0) {             
    ZStepper.step(stepsPerLimit);
    ZSwitch = mcp2.digitalRead(13);
    //Serial.println(ZSwitch);    
  }
  
  ZPrecisePosition = 0;
  Serial.println("Z Limit Switch Hit");
}

/**********************************************/
/***** X, Y, and Z precise move functions *****/
/**********************************************/

/*Manual coordinate calibration*/
void calibrateCoordinates() {

  /*Top Right Square is (0,0) for coordinate arrays*/
  
  /*Squares 56-63*/
  XCoordinates[0][0] = 0;
  XCoordinates[1][0] = 72;
  XCoordinates[2][0] = 135;
  XCoordinates[3][0] = 197;
  XCoordinates[4][0] = 265;
  XCoordinates[5][0] = 325;
  XCoordinates[6][0] = 405;
  XCoordinates[7][0] = 455;

  YCoordinates[0][0] = 0;
  YCoordinates[1][0] = 20;
  YCoordinates[2][0] = 20;
  YCoordinates[3][0] = 25;
  YCoordinates[4][0] = 25;
  YCoordinates[5][0] = 30;
  YCoordinates[6][0] = 30;
  YCoordinates[7][0] = 30;

  ZCoordinates[0][0] = 130;
  ZCoordinates[1][0] = 130;
  ZCoordinates[2][0] = 130;
  ZCoordinates[3][0] = 130;
  ZCoordinates[4][0] = 125;
  ZCoordinates[5][0] = 125;
  ZCoordinates[6][0] = 125;
  ZCoordinates[7][0] = 125;

  /*Squares 48-55*/
  XCoordinates[0][1] = 12;
  XCoordinates[1][1] = 76;
  XCoordinates[2][1] = 139;
  XCoordinates[3][1] = 204;
  XCoordinates[4][1] = 270;
  XCoordinates[5][1] = 322;
  XCoordinates[6][1] = 380;
  XCoordinates[7][1] = 450;

  YCoordinates[0][1] = 72;
  YCoordinates[1][1] = 79;
  YCoordinates[2][1] = 87;
  YCoordinates[3][1] = 87;
  YCoordinates[4][1] = 97;
  YCoordinates[5][1] = 97;
  YCoordinates[6][1] = 102;
  YCoordinates[7][1] = 102;

  ZCoordinates[0][1] = 130;
  ZCoordinates[1][1] = 130;
  ZCoordinates[2][1] = 130;
  ZCoordinates[3][1] = 130;
  ZCoordinates[4][1] = 125;
  ZCoordinates[5][1] = 125;
  ZCoordinates[6][1] = 125;
  ZCoordinates[7][1] = 125;

  /*Squares 40-47*/
  XCoordinates[0][2] = 10;
  XCoordinates[1][2] = 74;
  XCoordinates[2][2] = 136;
  XCoordinates[3][2] = 201;
  XCoordinates[4][2] = 265;
  XCoordinates[5][2] = 330;
  XCoordinates[6][2] = 390;
  XCoordinates[7][2] = 450;

  YCoordinates[0][2] = 138;
  YCoordinates[1][2] = 143;
  YCoordinates[2][2] = 155;
  YCoordinates[3][2] = 162;
  YCoordinates[4][2] = 157;
  YCoordinates[5][2] = 162;
  YCoordinates[6][2] = 165;
  YCoordinates[7][2] = 165;

  ZCoordinates[0][2] = 130;
  ZCoordinates[1][2] = 130;
  ZCoordinates[2][2] = 125;
  ZCoordinates[3][2] = 125;
  ZCoordinates[4][2] = 125;
  ZCoordinates[5][2] = 120;
  ZCoordinates[6][2] = 120;
  ZCoordinates[7][2] = 120;

  /*Squares 32-39*/
  XCoordinates[0][3] = 10;
  XCoordinates[1][3] = 70;
  XCoordinates[2][3] = 134;
  XCoordinates[3][3] = 201;
  XCoordinates[4][3] = 267;
  XCoordinates[5][3] = 330;
  XCoordinates[6][3] = 390;
  XCoordinates[7][3] = 455;

  YCoordinates[0][3] = 190;
  YCoordinates[1][3] = 200;
  YCoordinates[2][3] = 207;
  YCoordinates[3][3] = 212;
  YCoordinates[4][3] = 222;
  YCoordinates[5][3] = 228;
  YCoordinates[6][3] = 233;
  YCoordinates[7][3] = 233;

  ZCoordinates[0][3] = 130;
  ZCoordinates[1][3] = 125;
  ZCoordinates[2][3] = 125;
  ZCoordinates[3][3] = 125;
  ZCoordinates[4][3] = 120;
  ZCoordinates[5][3] = 110;
  ZCoordinates[6][3] = 110;
  ZCoordinates[7][3] = 110;

  /*Squares 24-31*/
  XCoordinates[0][4] = 5;
  XCoordinates[1][4] = 70;
  XCoordinates[2][4] = 134;
  XCoordinates[3][4] = 201;
  XCoordinates[4][4] = 267;
  XCoordinates[5][4] = 330;
  XCoordinates[6][4] = 395;
  XCoordinates[7][4] = 455;

  YCoordinates[0][4] = 255;
  YCoordinates[1][4] = 265;
  YCoordinates[2][4] = 275;
  YCoordinates[3][4] = 290;
  YCoordinates[4][4] = 295;
  YCoordinates[5][4] = 300;
  YCoordinates[6][4] = 302;
  YCoordinates[7][4] = 300;

  ZCoordinates[0][4] = 125;
  ZCoordinates[1][4] = 125;
  ZCoordinates[2][4] = 115;
  ZCoordinates[3][4] = 110;
  ZCoordinates[4][4] = 105;
  ZCoordinates[5][4] = 105;
  ZCoordinates[6][4] = 100;
  ZCoordinates[7][4] = 100;

  /*Squares 16-23*/
  XCoordinates[0][5] = 5;
  XCoordinates[1][5] = 72;
  XCoordinates[2][5] = 134;
  XCoordinates[3][5] = 201;
  XCoordinates[4][5] = 267;
  XCoordinates[5][5] = 330;
  XCoordinates[6][5] = 390;
  XCoordinates[7][5] = 455;

  YCoordinates[0][5] = 315;
  YCoordinates[1][5] = 327;
  YCoordinates[2][5] = 340;
  YCoordinates[3][5] = 350;
  YCoordinates[4][5] = 360;
  YCoordinates[5][5] = 365;
  YCoordinates[6][5] = 368;
  YCoordinates[7][5] = 368;

  ZCoordinates[0][5] = 120;
  ZCoordinates[1][5] = 120;
  ZCoordinates[2][5] = 115;
  ZCoordinates[3][5] = 105;
  ZCoordinates[4][5] = 100;
  ZCoordinates[5][5] = 95;
  ZCoordinates[6][5] = 95;
  ZCoordinates[7][5] = 95;

  /*Squares 8-15*/
  XCoordinates[0][6] = 5;
  XCoordinates[1][6] = 72;
  XCoordinates[2][6] = 134;
  XCoordinates[3][6] = 201;
  XCoordinates[4][6] = 267;
  XCoordinates[5][6] = 330;
  XCoordinates[6][6] = 390;
  XCoordinates[7][6] = 455;

  YCoordinates[0][6] = 382;
  YCoordinates[1][6] = 395;
  YCoordinates[2][6] = 405;
  YCoordinates[3][6] = 415;
  YCoordinates[4][6] = 430;
  YCoordinates[5][6] = 433;
  YCoordinates[6][6] = 433;
  YCoordinates[7][6] = 433;

  ZCoordinates[0][6] = 120;
  ZCoordinates[1][6] = 120;
  ZCoordinates[2][6] = 105;
  ZCoordinates[3][6] = 100;
  ZCoordinates[4][6] = 95;
  ZCoordinates[5][6] = 90;
  ZCoordinates[6][6] = 85;
  ZCoordinates[7][6] = 85;

  /*Squares 0-7*/
  XCoordinates[0][7] = 5;
  XCoordinates[1][7] = 72;
  XCoordinates[2][7] = 134;
  XCoordinates[3][7] = 190;
  XCoordinates[4][7] = 260;
  XCoordinates[5][7] = 325;
  XCoordinates[6][7] = 385;
  XCoordinates[7][7] = 445;

  YCoordinates[0][7] = 455;
  YCoordinates[1][7] = 460;
  YCoordinates[2][7] = 470;
  YCoordinates[3][7] = 492;
  YCoordinates[4][7] = 492;
  YCoordinates[5][7] = 492;
  YCoordinates[6][7] = 492;
  YCoordinates[7][7] = 492;

  ZCoordinates[0][7] = 120;
  ZCoordinates[1][7] = 115;
  ZCoordinates[2][7] = 105;
  ZCoordinates[3][7] = 90;
  ZCoordinates[4][7] = 80;
  ZCoordinates[5][7] = 80;
  ZCoordinates[6][7] = 80;
  ZCoordinates[7][7] = 85;

  /*Capture Coordinates Here*/
  XCaptureCoordinates[0] = 580;
  XCaptureCoordinates[1] = 580;
  XCaptureCoordinates[2] = 580;
  XCaptureCoordinates[3] = 580;
  XCaptureCoordinates[4] = 580;
  XCaptureCoordinates[5] = 580;
  XCaptureCoordinates[6] = 580;
  XCaptureCoordinates[7] = 580;
  XCaptureCoordinates[8] = 580;
  XCaptureCoordinates[9] = 580;
  XCaptureCoordinates[10] = 580;
  XCaptureCoordinates[11] = 540;
  XCaptureCoordinates[12] = 550;
  XCaptureCoordinates[13] = 550;
  XCaptureCoordinates[14] = 550;
  XCaptureCoordinates[15] = 550;

  YCaptureCoordinates[0] = 40;
  YCaptureCoordinates[1] = 85;
  YCaptureCoordinates[2] = 130;
  YCaptureCoordinates[3] = 175;
  YCaptureCoordinates[4] = 220;
  YCaptureCoordinates[5] = 265;
  YCaptureCoordinates[6] = 310;
  YCaptureCoordinates[7] = 355;
  YCaptureCoordinates[8] = 400;
  YCaptureCoordinates[9] = 445;
  YCaptureCoordinates[10] = 490;
  YCaptureCoordinates[11] = 40;
  YCaptureCoordinates[12] = 85;
  YCaptureCoordinates[13] = 130;
  YCaptureCoordinates[14] = 175;
  YCaptureCoordinates[15] = 220;

  ZCaptureCoordinates[0] = 120;
  ZCaptureCoordinates[1] = 120;
  ZCaptureCoordinates[2] = 120;
  ZCaptureCoordinates[3] = 115;
  ZCaptureCoordinates[4] = 115;
  ZCaptureCoordinates[5] = 115;
  ZCaptureCoordinates[6] = 115;
  ZCaptureCoordinates[7] = 110;
  ZCaptureCoordinates[8] = 110;
  ZCaptureCoordinates[9] = 110;
  ZCaptureCoordinates[10] = 110;
  ZCaptureCoordinates[11] = 120;
  ZCaptureCoordinates[12] = 120;
  ZCaptureCoordinates[13] = 120;
  ZCaptureCoordinates[14] = 120;
  ZCaptureCoordinates[15] = 120;  
}

void XPreciseMove(int newPosition) {
  int revolutions = newPosition - XPrecisePosition;
  Serial.print("X Move new precise position: ");
  Serial.println(newPosition);

  //Using loops because arduino can't handle large numbers
  if (revolutions < 0) {
    for (int i = 0; i > revolutions; i--) {
        XStepper.step(-stepsPerRevolution);
    }
  }
  else if (revolutions > 0) {
    for (int i = 0; i < revolutions; i++) {
        XStepper.step(stepsPerRevolution);
      }   
    }
  XPrecisePosition = newPosition;
}

void YPreciseMove(int newPosition) {
  int revolutions = newPosition - YPrecisePosition;
  Serial.print("Y Move new precise position: ");
  Serial.println(newPosition);

  //Using loops because arduino can't handle large numbers
  if (revolutions < 0) {
    for (int i = 0; i > revolutions; i--) {
        YStepper.step(-stepsPerRevolution);
    }
  }
  else if (revolutions > 0) {
    for (int i = 0; i < revolutions; i++) {
        YStepper.step(stepsPerRevolution);
      }   
    } 
  YPrecisePosition = newPosition;
}

void ZPreciseMove(int newPosition) {
  int revolutions = newPosition - ZPrecisePosition;
  Serial.print("Z Move new precise position: ");
  Serial.println(newPosition);

  //Using loops because arduino can't handle large numbers
  if (revolutions < 0) {
    for (int i = 0; i > revolutions; i--) {
        ZStepper.step(stepsPerRevolution);
    }
  }
  else if (revolutions > 0) {
    for (int i = 0; i < revolutions; i++) {
        ZStepper.step(-stepsPerRevolution);
      }   
    }  
  ZPrecisePosition = newPosition;
}

void ServoMove(int state) {
  delay(500);
  gripservo.write(state);
  delay(500);
}

/*******************************/
/***** Get player function *****/
/*******************************/
bool getPlayerColor() {
  String str = "";

  //Must wait for serial input to become available
  if (!Serial.available()) {
    Serial.print("R");
  }
  while(!Serial.available()) { //Initial while loop to catch buffered data
  }
  
  while (Serial.available()) { //Ensures data is only read when it is available    
    delay(30);
    if (Serial.available() > 0) {
      char input = Serial.read(); //Obtain 1 byte from input move
      str += input;
    }
    else {
      break;
    }
  }

  if (str == "white") {
    return(0);
  }
  else if (str == "black") {
    return(1);
  }
  else {
    Serial.println("Error, white or black not chosen");
    Serial.println(str);
    return(0);  
  }
  
}

/**************************************************/
/***** Player turn and serial input functions *****/
/**************************************************/

/*Function for parsing the serial input from Python*/
String serialInput() {
  String str = "";

  //Must wait for serial input to become available
  if (!Serial.available()) {
    Serial.println("Waiting for Computer move");
  }
  while(!Serial.available()) { //Initial while loop to catch buffered data
  }
  
  while (Serial.available()) { //Ensures data is only read when it is available    
    delay(30);
    if (Serial.available() > 0) {
      char input = Serial.read(); //Obtain 1 byte from input move
      str += input;
    }
    else {
      break;
    }
  }
  return(str);
}

/*Function processes robot's move from the serial input string*/
void turn(String command) {
  Serial.println("In turn");
  int length = command.length();
  int inputs = 0;
  int file = 1;
  int rank = 1;
  for (int i = 0; i < length; i++) {
    if (command[i] != 't') {
      if (inputs == 0) {
        file = command[i]-48; //-48 because string is converting to ascii characters
        inputs = inputs + 1;
      }
      else {
        rank = command[i]-48; //-48 because string is converting to ascii characters
        inputs = 0;        
      }
    }
    else if (command[i] == 't') {
      preciseCapture();
      continue;
    }

    /*Make move*/
    if (inputs == 0) {
      preciseMove(file, rank);
    }
  }  
}

/**************************/
/***** Move functions *****/
/**************************/
void preciseMove(int file, int rank) {
  
  /*Convert file and rank to proper revolutions using the arrays
    and then precise move them*/
  int XNewPosition = XCoordinates[file-1][rank-1];
  int YNewPosition = YCoordinates[file-1][rank-1];
  int ZNewPosition = ZCoordinates[file-1][rank-1];

  YPreciseMove(YNewPosition);
  XPreciseMove(XNewPosition);

  /*Test Code*/
  //ZPreciseMove(ZNewPosition);
  //ServoMove(0);
  
  if (holding == 1) {
    ZPreciseMove(ZNewPosition);
    ServoMove(90);
    holding = 0;
  }
  else {
   ServoMove(90);
   ZPreciseMove(ZNewPosition);
   ServoMove(0);
   holding = 1;    
  }
  ZHome();  
}

/*Move to capture currently held piece*/
void preciseCapture() {
  
  /*Convert file and rank to proper revolutions using the arrays
    and then precise move them */
  int XNewPosition = XCaptureCoordinates[captures];
  int YNewPosition = YCaptureCoordinates[captures];
  int ZNewPosition = ZCaptureCoordinates[captures];
  captures = captures + 1;

  //YFirst to avoid hitting wood
  YPreciseMove(YNewPosition);
  XPreciseMove(XNewPosition);  
  ZPreciseMove(ZNewPosition);
  
  ServoMove(90);
  ZHome();
  holding = 0;
}

/*******************************/
/***** Detection functions *****/
/*******************************/

/*Sets the squares for the array representing the chessboard*/
void setSquares() {
  for (int i=0; i<16; i++) {
    digitalWrite(CONTROL0, (i&15)>>3); 
    digitalWrite(CONTROL1, (i&7)>>2);  
    digitalWrite(CONTROL2, (i&3)>>1);  
    digitalWrite(CONTROL3, (i&1)); 
    mux0array[i] = digitalRead(14);
  }

  for (int i=0; i<16; i++) {
    digitalWrite(CONTROL0, (i&15)>>3); 
    digitalWrite(CONTROL1, (i&7)>>2);  
    digitalWrite(CONTROL2, (i&3)>>1);  
    digitalWrite(CONTROL3, (i&1)); 
    mux1array[i] = digitalRead(15);
  }

  for (int i=0; i<16; i++) {
    digitalWrite(CONTROL0, (i&15)>>3); 
    digitalWrite(CONTROL1, (i&7)>>2);  
    digitalWrite(CONTROL2, (i&3)>>1);  
    digitalWrite(CONTROL3, (i&1)); 
    mux2array[i] = digitalRead(16);
  }
  
  /*Row 1*/
  squares[0] = mcp1.digitalRead(8);
  squares[1] = mcp1.digitalRead(9);
  squares[2] = mcp1.digitalRead(10);
  squares[3] = mcp1.digitalRead(11);
  squares[4] = mcp1.digitalRead(12);
  squares[5] = mcp1.digitalRead(13);
  squares[6] = mcp1.digitalRead(14);
  squares[7] = mcp1.digitalRead(15);

  /*Row 2*/
  squares[8] = mcp1.digitalRead(7);
  squares[9] = mcp1.digitalRead(6);
  squares[10] = mcp1.digitalRead(5);
  squares[11] = mcp1.digitalRead(4);
  squares[12] = mcp1.digitalRead(3); 
  squares[13] = mcp1.digitalRead(2);
  squares[14] = mcp1.digitalRead(1);
  squares[15] = mcp1.digitalRead(0);  

  /*Row 3*/
  squares[16] = mux0array[7];
  squares[17] = mux0array[6];
  squares[18] = mux0array[5];
  squares[19] = mux0array[4];
  squares[20] = mux0array[3];  
  squares[21] = mcp2.digitalRead(7); //mux0array[2];
  squares[22] = mux0array[1];
  squares[23] = mux0array[0];

  /*Row 4*/
  squares[24] = mux1array[7];
  squares[25] = mux1array[6];
  squares[26] = mux1array[5];
  squares[27] = mux1array[4];
  squares[28] = mux1array[3];
  squares[29] = mux1array[2];
  squares[30] = mux1array[1];
  squares[31] = mux1array[0];

  /*Row 5*/
  squares[32] = mux2array[7];
  squares[33] = mux2array[6];
  squares[34] = mux2array[5];
  squares[35] = mux2array[4];
  squares[36] = mux2array[3];
  squares[37] = mux2array[2];
  squares[38] = mux2array[1];
  squares[39] = mux2array[0];

  /*Row 6*/
  squares[40] = mux2array[8];
  squares[41] = mux2array[9];
  squares[42] = mux2array[10];
  squares[43] = mux2array[11];  
  squares[44] = mux2array[12];
  squares[45] = mux2array[13];
  squares[46] = mux2array[14];
  squares[47] = mux2array[15];
  
  /*Row 7*/
  squares[48] = mux1array[8];
  squares[49] = mux1array[9];
  squares[50] = mux1array[10];
  squares[51] = mux1array[11];
  squares[52] = mux1array[12];
  squares[53] = mux1array[13];
  squares[54] = mux1array[14];
  squares[55] = mux1array[15];
  
  /*Row 8*/ 
  squares[56] = mux0array[8];
  squares[57] = mux0array[9];
  squares[58] = mux0array[10];
  squares[59] = mux0array[11];
  squares[60] = mux0array[12];
  squares[61] = mux0array[13];
  squares[62] = mux0array[14];
  squares[63] = mux0array[15];
}

/*Detects changes in the squares (board representation) array*/
void detectChanges() {
  bool movedPiece = false;
  for (int i=0; i < board_total; i++) {
    if (check_squares[i] != squares[i]) {
      changes[numberOfChanges] = i;
      changeType[numberOfChanges] = squares[i];
      numberOfChanges += 1;
      movedPiece = true;  
    }
  }

  if (movedPiece == true) {
    correctCheckSquares();
  }
}

/*Calculates the move given the changes in the array*/
void calculateMove() {
  int movingPiece = 64;
  int landingSquare = 64;
  
  if (numberOfChanges == 2) {
    for (int i = 0; i < numberOfChanges; i++) {
      if (changeType[i] == 1) {
        movingPiece = changes[i]; 
      }
      else if (changeType[i] == 0) {
        landingSquare = changes[i];
      }
    }
    moveArray[0] = movingPiece;
    moveArray[1] = landingSquare;
  }

  if (numberOfChanges == 3) {
    int movedPieces[2];
    movedPieces[0] = 64;
    movedPieces[1] = 64;
    int moveIndex = 0;
    for (int i = 0; i < numberOfChanges; i++) {
      if (changeType[i] == 1) {
        movedPieces[moveIndex] = changes[i];
        moveIndex += 1; 
      }
      else if (changeType[i] == 0) {
        landingSquare = changes[i];
      }
    }

    //Find the landing square (capture square) make that moveArray[1]
    if (movedPieces[0] == landingSquare) {
      moveArray[0] = movedPieces[1];
      moveArray[1] = movedPieces[0];
      moveArray[2] = landingSquare;
    }
    else if (movedPieces[1] == landingSquare) {
      moveArray[0] = movedPieces[0];
      moveArray[1] = movedPieces[1];
      moveArray[2] = landingSquare;  
    }
    else if ((landingSquare-8 == movedPieces[0]) || (landingSquare+8 == movedPieces[0])) { // En Passant Testing
      moveArray[0] = movedPieces[1];
      moveArray[1] = movedPieces[0];
      moveArray[2] = landingSquare; 
    }
    else if ((landingSquare-8 == movedPieces[1]) || (landingSquare+8 == movedPieces[1])) { // En Passant Testing
      moveArray[0] = movedPieces[0];
      moveArray[1] = movedPieces[1];
      moveArray[2] = landingSquare; 
    }
  }

  if (numberOfChanges == 4) {
    int movedPieces[2];
    movedPieces[0] = 64;
    movedPieces[1] = 64;
    int moveIndex = 0;
    
    int landedSquares[2];
    landedSquares[0] = 64;
    landedSquares[1] = 64;
    int landIndex = 0;

    int movingPiece = 64;
    int landingSquare = 64;
    for (int i = 0; i < numberOfChanges; i++) {
      if (changeType[i] == 1) {
        movedPieces[moveIndex] = changes[i];
        moveIndex += 1;
        
        /*if statement to determine if white king or black king*/
        if (color == 0) {
          if (changes[i] == 4) {
             movingPiece = 4;
          }
        }
        else if (color == 1) {
          if (changes[i] == 3) {
             movingPiece = 3;
          }  
        }
      }
      else if (changeType[i] == 0) {
        landedSquares[landIndex] = changes[i];
        landIndex += 1;

         /*if statement to determine if white king or black king*/
        if (color == 0) {
          if (changes[i] == 2 || changes[i] == 6) {
             landingSquare = changes[i];
          }
        }
        else if (color == 1) {
          if (changes[i] == 1 || changes[i] == 5) {
             landingSquare = changes[i];
          }
        }
      }
    }
    moveArray[0] = movingPiece;
    moveArray[1] = landingSquare;
  }
}

/*Reset function resets all detection arrays*/
void resetChanges() {
  correctCheckSquares();
  for (int i = 0; i < 4; i++) {
    changes[i] = 64;
    changeType[i] = 2;
    moveArray[i] = 64;
  }
  numberOfChanges = 0;
}

/*Sets the check array equal to the board representation array*/
void correctCheckSquares() {
  for (int i=0; i < board_total; i++) {
    check_squares[i] = squares[i];
  }
}

/***************************/
/***** Print functions *****/
/***************************/
void printSquares() {
  for (int j = 0; j < 8; j++) {
    for (int i = 0; i < 8; i++) {
      Serial.print(squares[(7-j)*8 + i]);
    }
    Serial.println("");
  }
  Serial.println("");
}

/****************************************************/
/***** X, Y, and Z precise input test functions *****/
/****************************************************/

void XPreciseInput() {
  Serial.print("X Precise Position: ");
  Serial.println(XPrecisePosition);
  Serial.print("Input new precise position: ");
  while(true) {
    
    int newPosition = Serial.parseInt();
    if (newPosition > 0) {
      XPreciseMove(newPosition);      
      Serial.print("X Precise Position: ");
      Serial.println(XPrecisePosition);
      Serial.print("Input new precise position: ");
    }
  }
}

void YPreciseInput() {
  Serial.print("Y Precise Position: ");
  Serial.println(YPrecisePosition);
  Serial.print("Input new precise position: ");
  while(true) {
    
    int newPosition = Serial.parseInt();
    if (newPosition > 0) {
      YPreciseMove(newPosition);
      
      Serial.print("Y Precise Position: ");
      Serial.println(YPrecisePosition);
      Serial.print("Input new precise position: ");
    }
  }
}

void ZPreciseInput() {
  Serial.print("Z Precise Position: ");
  Serial.println(ZPrecisePosition);
  Serial.print("Input new precise position: ");
  while(true) {
    
    int newPosition = Serial.parseInt();
    if (newPosition > 0) {
      ZPreciseMove(newPosition);
      
      Serial.print("Z Precise Position: ");
      Serial.println(ZPrecisePosition);
      Serial.print("Input new precise position: ");
    }
  }
}

