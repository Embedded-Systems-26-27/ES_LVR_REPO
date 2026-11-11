# Embedded Systems: MQTT & Node-RED Dashboard met MySQL Logging

## Projectbeschrijving
Dit project is een uitwerking van de opdracht "MQTT met Node-RED" voor het vak Embedded Systems. Het doel is om een volledig IoT-systeem te bouwen op een Raspberry Pi dat gebruikmaakt van een Node-RED dashboard voor visualisatie en besturing, MQTT voor draadloze communicatie, en een MySQL/MariaDB database voor het loggen van gebeurtenissen.

**Kernfunctionaliteiten:**
*   **Input Monitoring:** Het uitlezen van een fysieke GPIO-pin (bijv. een schakelaar) en de status tonen op een Node-RED dashboard (LED-indicator).
*   **Output Control:** Het aansturen van een fysieke GPIO-pin (bijv. een relais) via een checkbox op het dashboard.
*   **MQTT Communicatie:** Het publiceren van input-wijzigingen (`CHANGE_DETECTED`) en het abonneren op output-commando's (`SET_OUTPUT`) via een MQTT-broker.
*   **Database Logging (Uitbreiding):** Het loggen van alle input-wijzigingen in een MariaDB database.
*   **Data Visualisatie (Uitbreiding):** Het tonen van de gelogde events op het dashboard, gefilterd op datum.

---

## 🛠️ Vereisten (Prerequisites)

Zorg dat de volgende software en hardware aanwezig is:

**Hardware:**
*   Raspberry Pi (met Raspbian OS)
*   Jumper-draden
*   (Optioneel) Een relais-module of LED voor de output
*   (Optioneel) Een schakelaar voor de input

**Software op de Raspberry Pi:**
*   Node.js (aanbevolen: versie 18 of hoger)
*   Node-RED
*   MariaDB / MySQL Server
*   Mosquitto MQTT Broker (optioneel, kan ook een publieke broker zijn)

**Software op de client (Laptop/PC):**
*   MQTTBox (of een vergelijkbare MQTT-client)
*   Een moderne webbrowser

---

## 🚀 Installatie & Uitvoering

Volg deze stappen om het project op de Raspberry Pi te draaien.

### Stap 1: Node-RED Installeren
```bash
# Installeer Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo bash -
sudo apt-get install -y nodejs

# Installeer Node-RED
sudo npm install -g node-red

# Start Node-RED automatisch bij boot (aanbevolen)
sudo systemctl enable nodered.service
```

### Stap 2: Benodigde Node-RED Modules Installeren
Open de Node-RED editor in je browser (`http://<IP-VAN-PI>:1880`), ga naar **Manage Palette > Install** en installeer:

*   `@flowfuse/node-red-dashboard` (Dashboard 2.0)
*   `node-red-node-pi-gpio` (Voor GPIO aansturing)
*   `node-red-node-mysql` (Voor database verbinding)

Als de zoekfunctie niet werkt, installeer ze dan via de terminal:
```bash
cd ~/.node-red
npm install @flowfuse/node-red-dashboard node-red-node-pi-gpio node-red-node-mysql
```

### Stap 3: Database Opzetten (MariaDB)
Installeer en configureer de database op de Raspberry Pi:
```bash
sudo apt-get install mariadb-server
sudo mysql -uroot
```

Voer de volgende SQL-commando's uit in de MariaDB prompt:
```sql
CREATE DATABASE globe_bank;
USE globe_bank;

CREATE USER 'webuser'@'localhost' IDENTIFIED BY 'secretpassword';
GRANT ALL PRIVILEGES ON globe_bank.* TO 'webuser'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE events (
    id INT(11) NOT NULL AUTO_INCREMENT,
    pin INT(2),
    state INT(1),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

exit;
```

### Stap 4: MQTT Broker Configureren
*   **Optie A (Lokaal):** Installeer Mosquitto op je laptop of de Pi en zorg dat deze draait op poort `1883`.
*   **Optie B (Publiek):** Gebruik `test.mosquitto.org` (poort `1883` of `8080` voor WebSockets).

> **Let op:** Pas de MQTT-server instellingen in Node-RED aan naar jouw specifieke broker IP-adres (bijv. `192.168.137.1` als je internet deelt via je laptop).

### Stap 5: Node-RED Flow Importeren
1.  Open de Node-RED editor.
2.  Klik rechtsboven op het menu (drie streepjes) > **Import**.
3.  Upload het `flows.json` bestand uit deze repository (of plak de JSON code).
4.  Controleer of de MQTT-nodes en de MySQL-node correct zijn gekoppeld aan jouw broker en database.
5.  Klik op **Deploy**.

### Stap 6: Toegang tot het Dashboard
Open je browser en ga naar:
`http://<IP-VAN-PI>:1880/dashboard`
