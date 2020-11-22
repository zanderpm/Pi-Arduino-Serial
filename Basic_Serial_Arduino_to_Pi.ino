void setup() {
  Serial.begin(9600);
}

void loop() {
while (true){
  String line="";
  line=readFromSerial();
  if (line != '\0'){
    printToSerial("Sent from Arduino: " + line);
  }
}
}

void printToSerial(String string) {
  Serial.println(string);
}

String readFromSerial(){
  if (Serial.available()>0){
    String data=Serial.readStringUntil('\n');
    return data;
  }
  else return "";
}
