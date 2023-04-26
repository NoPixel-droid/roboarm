#include <Servo.h>
int relayPin = 8;
char state;

// Servo nesneleri oluşturun
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

void setup() {
  // Serial haberleşme hızını ayarlayın
  Serial.begin(9600);
  
  servo1.attach(9);
  servo2.attach(10);
  servo3.attach(11);
  servo4.attach(12);

  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);
}

void loop() {
 if (Serial.available()) {
    state = Serial.read();
    if (state == 'ON') {
      digitalWrite(relayPin, HIGH);
      Serial.println("Röle açık");
    }
    else if (state == 'OFF') {
      digitalWrite(relayPin, LOW);
      Serial.println("Röle kapalı");
    }
  }



// Seri porttan gelen verileri okuyun
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    // Servo açısını ayarlamak için gelen komutu işleyin
    if (command.startsWith("1")) {>
      int angle = command.substring(2).toInt();
      servo1.write(angle);
      Serial.println("Servo 1 açısı ayarlandı: " + String(angle));
    }
    else if (command.startsWith("2")) {
      int angle = command.substring(2).toInt();
      servo2.write(angle);
      Serial.println("Servo 2 açısı ayarlandı: " + String(angle));
    }
    else if (command.startsWith("3")) {
      int angle = command.substring(2).toInt();
      servo3.write(angle);
      Serial.println("Servo 3 açısı ayarlandı: " + String(angle));
    }
    else if (command.startsWith("4")) {
      int angle = command.substring(2).toInt();
      servo4.write(angle);
      Serial.println("Servo 4 açısı ayarlandı: " + String(angle));
    }
  }
 
}
