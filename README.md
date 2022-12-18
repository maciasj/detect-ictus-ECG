# detect-ictus-ECG
Aplicació que recupera i prepara les dades d'electrocardiogrames de FitBit per a l'entrega a un clúster on una IA valorarà el risc de ictus. 

**Features**: Simple interfaç gràfica amb un bot funcional que al clickar faría el següent:

- Demana al usuari les credencials de la seva compte de Fitbit per tal d'autoritzar l'aplicació 
- Descarrega els arxius que contenen el heart-rate, el transforma a .csv i després a .mat
- Envía els arxius a través de l'API de OSCAR al cluster, els processa i retorna un arxiu .log amb els resultats de la inferència
- Per l'aplicació surt la linea del resultat del .log 
- Per asegurar que el nom de cada log és únic i que no hagin colisions al clúster, s'identifiquen per userID + timestamp.

**Inconvenients**: 

- L'API de fitbit demana les credencials només el primer cop que s'inicia la app, quan això passa si trigues molt en afegir les credencials l'aplicació crashea. 
- Els arxius del fitbit no es procesen bé ja que fan servir una taxa de mostreig diferent al que la IA pot reconeixer degut al seu entrenament 
- Com el resultat del log que interpreta el arxiu no te cap label, per tal de treure'l per pantalla hem de imprimir el número de linia exacte, això provoca que sí el format de output canvia, no podem asegurar que l'output sempre sigui correcte.

**framework**:

- Hem utilizat el framework `kivy` de python ja que és fàcilment exportable a una Android APK

**per utilizar-la**:

- executar main.py
- `cleandata.sh` es una script que esborra el contingut dels diferents directoris de data

Per: Ferran Fuentes, Joel Macias, Marcel Sánchez, Sergio Sanz
