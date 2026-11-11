## Logboek AI-Assistentie

| Datum | Prompt / Vraag | Gegenereerd Resultaat | Gebruikt in Project? |
| :--- | :--- | :--- | :--- |
| 11-11-2026 | *"Hoe stel ik een Node-RED flow in om een GPIO input via MQTT te publiceren als JSON?"* | Een `function` node met JavaScript code om `msg.payload` om te zetten naar `{"pin": 13, "state": msg.payload}`. | Ja, gebruikt in de bovenste flow. |
| 11-11-2026 | *"Wat is de foutmelding ER_ACCESS_DENIED_NO_PASSWORD_ERROR in Node-RED?"* | Uitleg dat het wachtwoordveld leeg was in de MySQL configuratie node. Oplossing: wachtwoord opnieuw invullen en Deployen. | Ja, fout opgelost. |
| 11-11-2026 | *"Hoe maak ik een SQL query in Node-RED om data te filteren op datum?"* | Een `function` node met de query: `SELECT * FROM events WHERE DATE(timestamp) = ?` en uitleg over het doorgeven van de datum via `msg.payload`. | Ja, gebruikt voor de Date Picker uitlezing. |
| 12-11-2026 | *"Schrijf een README.md voor een Embedded Systems project met Node-RED, MQTT en MySQL."* | Deze README.md tekst. | Ja. |
