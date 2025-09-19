int sensorLumi = A0;
int led = 8;
int const claro = 350;
int const escuro = 450;

void setup() {
  pinMode(sensorLumi, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  float luminosidade = analogRead(sensorLumi);

  if(luminosidade <= claro) {
    Serial.print("Claro: ");
    Serial.print(luminosidade);
    Serial.print("\n");
    digitalWrite(led, LOW);
  } else {
    Serial.print("Escuro: ");
    Serial.print(luminosidade);
    Serial.print("\n");
    digitalWrite(led, HIGH);
  }

  delay(200);
}
