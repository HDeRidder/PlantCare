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

### Postman

#### GET Endpoints

1) Alle geregistreerde gebruikers opvragen
   
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/1d07e8c6-8cee-4db0-af2c-c4d589fdaedd)

2) Gebruiker opvragen op basis van de bijhorende id
   
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/c3040e8d-8c38-4031-adbc-ee2b1d712486)

3) Alle plantreminders uit de database opvragen

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/03912f2a-e81b-487c-8e64-7386dd583998)

4) Zoeken naar een plant op basis van de naam

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/8c383d17-13c9-4b4b-bb38-70d85b67d489)

5) Filteren op planten met bepaalde belichtingscriteria
   
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/4e341296-da32-45aa-8ce4-8797bf35d9f7)

6) Filteren op planten met bepaalde waternoden

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/22ec8ae3-1a39-4660-8943-ea3721b2a1bf)

7) De huidige ingelogde gebruiker weergeven (eerst access token nodig)

   ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/10f9b525-0db1-40bf-8e1b-c538181c79f6)

#### POST Endpoints

1) Gebruiker toevoegen aan de database

   ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/eed2114a-8f96-4a03-ad7d-7a51bceb5435)


2) Plantreminder toevoegen (gekoppeld aan een gebruiker)

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/2a6b978e-1e86-41d8-bcdf-62242fad3a76)


3) Token genereren
  
   ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/9372f2f0-eb50-469f-b0b1-c251ffeb15d9)


#### PUT Endpoints

1) Gebruikersgegevens wijzigen
   
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/f27d8ca1-79be-4e6c-bcda-2d9dcc62c7cc)


#### DELETE Endpoints

1) Verwijder gebruiker op basis van id

    ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/a57b1f04-b8fe-4087-90ec-3f4363576688)


2) Verwijder plantreminder op basis van id

   ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/e57aac1d-7a58-4da9-883a-9edeeb57f96f)

### FastAPI Docs

1) Authoriseren
   
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/6b2e07d3-b1d1-4dcd-91cf-d7b1cf2800be)

2) Nieuwe gebruiker aanmaken
   
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/b193cf11-8318-48fb-846d-960c5ccbf4e6)

3) Huidige ingelogde gebruiker weergeven (na authorisatie)

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/a63cc6ea-454f-4114-b074-7fb35c18e857)

4) Alle geregistreerde gebruikers weergeven
   
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/3d135e87-4929-4488-93fb-294b3e5e1e2f)

5) Gebruiker met bepaalde id weergeven

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/eda2cce9-39ae-4bfe-861b-521da2bee0e8)

6) Update email van gebruiker met bepaalde id

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/f4834035-bd23-4814-9121-69cf07a9ce3d)
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/7b07ba60-3d33-4353-ab0a-6f729bfb0113)

7) Alle geregistreerde plantreminders weergeven

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/db6f5718-93f7-4c6c-8eff-69afb1812ae8)

8) Plantreminders weergeven op basis van lichtinfo

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/66248c7b-d28a-4bf2-9578-b2730d748beb)

9) Plantreminders weergeven op basis van waterinfo

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/f679e8fe-9b18-4da7-9b8f-b2e0f6dc9471)

10) Nieuwe plantreminder aanmaken, gekoppeld aan een bestaande gebruiker

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/d8210bea-2d21-492f-b737-c9f832aa1b01)
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/e27cfc55-afdc-47bb-be39-5ec07395a802)

11) Gebruiker verwijderen

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/0a0bd892-ac33-4d37-ac47-ddc84b78edde)

12) Token aanmaken

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/060dbcaa-85ca-4351-87dd-b25690e200cd)
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/ee852437-4c39-4bb4-92d9-154f52cbb209)

13) Plantreminder verwijderen op basis van id

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/0288c032-296b-4d16-b996-0767a355dbd3)

14) Schemas

  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/6fb984fe-7a26-46ad-8057-8015c7583f87)
  ![image](https://github.com/HDeRidder/PlantCare/assets/71796628/3659e578-1cca-494e-990e-f86283c87efb)
