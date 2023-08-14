# PlantCare API - Harold De Ridder
## Informatie over het gekozen onderwerp
Deze API heeft als doel de gebruiker informatie te verschaffen over planten die hij of zij thuis heeft. De API staat namelijk in verbinding met een SQLite Database, waar "plantreminders" instaan die deze zaken bevatten:

- De naam van de plant
- Hoeveel water deze plant nodig heeft
- Hoeveel licht deze plant nodig heeft
  
Men kan als gebruiker zoeken naar een bepaalde plant om de nodige zorg te weten te komen, of men kan filteren op de nodige lichtintensiteit of de hoeveelheid water, om een overzicht te krijgen van alle planten met dezelfde noden.

## Links
### API op Okteto
* [Oketo endpoint](https://app-hderidder.cloud.okteto.net/)

## Screenshots

### GET Endpoints
1) Alle geregistreerde gebruikers opvragen
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/1d07e8c6-8cee-4db0-af2c-c4d589fdaedd)

3) Gebruiker opvragen op basis van de bijhorende id
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/c3040e8d-8c38-4031-adbc-ee2b1d712486)

4) Alle plantreminders uit de database opvragen
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/03912f2a-e81b-487c-8e64-7386dd583998)

5) Zoeken naar een plant op basis van de naam
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/8c383d17-13c9-4b4b-bb38-70d85b67d489)

6) Filteren op planten met bepaalde belichtingscriteria
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/4e341296-da32-45aa-8ce4-8797bf35d9f7)

7) Filteren op planten met bepaalde waternoden
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/22ec8ae3-1a39-4660-8943-ea3721b2a1bf)

### POST Endpoints
1) Gebruiker toevoegen aan de database
   ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/eed2114a-8f96-4a03-ad7d-7a51bceb5435)


2) Plantreminder toevoegen (gekoppeld aan een gebruiker)
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/2a6b978e-1e86-41d8-bcdf-62242fad3a76)
