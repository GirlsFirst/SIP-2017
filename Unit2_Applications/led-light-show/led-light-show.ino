
// Red, Green, Blue
int led1[] = {11, 10, 9};
int led2[] = {6, 5, 3};

int red[] = {255, 0, 0};
int green[] = {0, 255, 0};
int blue[] = {0, 0, 255};
int purple[] = {255, 0, 255};
int yellow[] = {225, 225, 0};
int off[] = {0, 0, 0};
int white[] = {255, 255, 255};

int rainbow[7][3] ={
  {255, 0, 0},    // red
  {255, 165, 0},  // orange
  {255, 255, 0},  // yellow
  {0, 128, 0},    // green
  {0, 0, 255},    // blue
  {74, 0, 130},   // indigo
  {238, 130, 238} // violet
  };



void setup() {
  // put your setup code here, to run once:

pinMode(led1[0], OUTPUT);
pinMode(led1[1], OUTPUT);
pinMode(led1[2], OUTPUT);

pinMode(led2[0], OUTPUT);
pinMode(led2[1], OUTPUT);
pinMode(led2[2], OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  for(int x = 0; x < 10; x++){

    for(int y = 0; y<7; y++){

      int color1[] = {rainbow[y][0], rainbow[y][1], rainbow[y][2]};
      int color2[] = {rainbow[7-y][0], rainbow[7-y][1], rainbow[7-y][2]};
      displayColor(led1, color1);
      delay(500);
      displayColor(led2, color2);
      delay(500);
      
    }
  }


}

void displayColor(int pins[], int colors[]){

  // cycle through arrays for the pins to light up LED in specific color.
  for(int x = 0; x < 3; x++) {

      analogWrite(pins[x], colors[x]);
  }


}



