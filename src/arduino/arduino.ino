int MRF = 5;
int MLF = 9;
int MRB = 6;
int MLB = 10;

void setup() {
  Serial.begin(9600);
  pinMode(MRF, OUTPUT);
  pinMode(MLF, OUTPUT);
  pinMode(MRB, OUTPUT);
  pinMode(MLB, OUTPUT);
}

void clear_buffer() {
  while (Serial.available() > 0) {
    Serial.read();
  }
}
void loop() {
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n');
    message.trim();
    int parti_lowla = message.indexOf(',');
    int surface = message.substring(0, parti_lowla).toInt();
    if (surface < 240 && surface  > 290 ) {
      analogWrite(MRF, 170);
      analogWrite(MLB, 170);
      delay(800);
      analogWrite(MRF, 170);
      analogWrite(MLF, 170);
      delay(800);
      analogWrite(MLF, 170);
      analogWrite(MRB, 170);
      delay(1000);
      analogWrite(MRF, 170);
      analogWrite(MLF, 170);
      delay(800);
    } else {
      analogWrite(MRF, 170);
      analogWrite(MLF, 170);
    }
  }
  clear_buffer();
}
}
