//Dependency Dongle Software (Arduino side)
#include <SoftwareSerial.h>
String AuthKey = "wtubfonpue2p5be";
String VerifKey = "ml5c4lgg4o39liq";
String GlobalKey = "v8r1i7lqxf0f4lpt7i37ahqnjg1kez1sw34hkrcu";
String Ser;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, HIGH);
  
}

void loop() {
  // put your main code here, to run repeatedly:

  Ser = Serial.readString();
  if (Ser == "auth")
  {
    digitalWrite(13, HIGH);
    Serial.println(AuthKey);
  
    
  };

  if (Ser == "key")
  {
    digitalWrite(13, HIGH);
    Serial.println(GlobalKey);
  
    
  };  

  if (Ser == "DependencyDongleAuth0000%@")
  {
      Serial.println(VerifKey);
  };
  Ser = "";
}
