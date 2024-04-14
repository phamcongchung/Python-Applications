// Khai báo chân digital led kết nối arduino 
int cold_led = 8;
int normal_led = 9;
int hot_led = 10;

int buzz = 11;
String data;
int x;
void setup(){
  Serial.begin(9600);
  pinMode(cold_led,OUTPUT);
  pinMode(normal_led,OUTPUT);
  pinMode(hot_led,OUTPUT);
  pinMode(buzz,OUTPUT);
}
void loop(){
  data=Serial.readStringUntil('\n'); // Đọc dữ liệu từ màn hình serial đến khi xuống dòng
  x=data.toInt(); // Chuyển string sang int
  int value = analogRead(A0);
  float vol = value*5.0/1024.0;
  float temp = vol*100.0;
  Serial.println(temp);

  if (x==1)
  {
    digitalWrite(cold_led, HIGH);
    digitalWrite(buzz, HIGH);
    digitalWrite(normal_led, LOW);
    digitalWrite(hot_led, LOW);
  }
  else if (x==2)
  {
    digitalWrite(cold_led, LOW);
    digitalWrite(buzz, LOW);
    digitalWrite(normal_led, HIGH);
    digitalWrite(hot_led, LOW);
  }
  else if (x==3)
  {
    digitalWrite(cold_led, LOW);
    digitalWrite(buzz, HIGH);
    digitalWrite(normal_led, LOW);
    digitalWrite(hot_led, HIGH);
  }
  else
  {
    digitalWrite(cold_led, LOW);
    digitalWrite(buzz, LOW);
    digitalWrite(normal_led, LOW);
    digitalWrite(hot_led, LOW);
  }
  
  delay(1000);
}
