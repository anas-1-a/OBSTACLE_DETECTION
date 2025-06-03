int M_R_F = 5;
int M_L_F = 9;
int M_R_B = 6;
int M_L_B = 10;
void setup() {
  Serial.begin(9600);
  pinMode(M_R_F , OUTPUT);
  pinMode(M_L_F , OUTPUT);
  pinMode(M_R_B , OUTPUT);
  pinMode(M_L_B , OUTPUT);
}
void loop() {
// decomment this to make the robot go forward
 // analogWrite(M_R_F , 100);
 // analogWrite(M_L_F , 100);  
// decomment this to make the robot go backward
 // analogWrite(M_R_B , 100);
 // analogWrite(M_L_B , 100); 
}