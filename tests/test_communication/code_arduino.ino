void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String str_diff = Serial.readStringUntil('\n');
    int diff = str_diff.toInt();
  Serial.println(diff); // open serial monitor to see if the communication work 
  }