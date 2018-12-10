void setup(){
  pinMode(A7, INPUT);
  pinMode(2, INPUT);
  Serial.begin(9600);
}

void loop(){
  int value;
  int d_value;
  float db;
  value = analogRead(A7);
  d_value = digitalRead(2);
  
  db = (value+83.2073)/11.003;
  Serial.println(db);
  delay(50);
}
