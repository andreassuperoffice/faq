---
title: "Hur kan jag importera kontaktpersoner utan koppling till företag till SuperOffice CRM?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-kan-jag-importera-kontaktpersoner-utan-koppling-till-foretag-till-superoffice-crm/
lang: sv
updated: "21. mars 2022"
---

# Hur kan jag importera kontaktpersoner utan koppling till företag till SuperOffice CRM?

Uppdaterad på 21. mars 2022

Jag vill importera en Excel-fil med kontakter som inte tillhör något företag. Hur gör jag det?

**Notera!**

1. SuperOffice-användare, som utför kontaktimport måste ha en roll, som har datarättinställningar, som gör det möjligt att skapa och / eller uppdatera kontakter. Kontrollera [denna FAQ](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=113624) för mer information.
2. För att importera kontakter utan företagskoppling, till SuperOffice CRM måste du aktivera inställningen "Obligatoriskt företag på kontakt" till "Nej". Kontrollera [denna FAQ](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=113592) för mer information.
3. Importer kan inte backas. Därför rekommenderar vi att skapa en databasbackup innan du gör stora datauppdateringar. Om SuperOffice är installerat på plats, vänligen se [denna FAQ](http://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=111362) som förklarar hur du kan göra detta. Om du använder SuperOffice Online behöver du inte göra något extra eftersom säkerhetskopia skapas automatiskt.

Följ stegen nedan om du vill importera kontakter utan att koppla dem till ett företag:

1. Förbered en importfil som innehåller dina nya kontakter. Kontrollera [den här artikeln](https://community.superoffice.com/sv/learning/admin-guide/import-contacts-products/import-contacts/) för tips om förberedelse av importfilen.
2. I [Inställningar och Underhål](http://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=110849)l välj **Import** (1) i Navigator-menyn till vänster, välj sedan **Kontakter**(2) och klicka på **Excel ikonen** (3).

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4394571-7bEYjrUbEe6NqpKChwYIiEHpYYHnS5570ysiFe6oz0LGLKjufzWbqnX7EPGqXEwp-0/image.png)
3. I nästa steg, ladda upp din Excel-fil i dialogrutan överför fil.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4394572-PxCJLq7FHltnCbXgmDAGcXeQ5K2Xl0KlZqfsGTSAdE3OHNznByqawnRneG1yfJIH-0/image.png)
4. Välj SuperOffice-fälten för kolumnerna i din importfil. Du behöver inte göra det för de kolumner du inte vill importera.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4394573-t4ajDWppqEUNrcj8AFLG7LEEtfWW0aC4ThCsQL3nOhhQM7wzSLwTo55XqZ8BSjmR-0/image.png)
5. Klicka på **Konfigurera import inställningar**(1) och i dialogrutan  **Import inställningar**bredvid **Om företagsnamn är tomt** välj alternativ *Importera kontakter utan företag* (2).  Gör andra justeringar och om det behövs klicka på **spara**(3).

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4394574-4ryjTdTdK5De2xbycC4liYWQX1WKNAzyTclhOt3GNwzec1uKUwdj1MWgPFYpZma7-0/image.png)
6. Om du är nöjd med installationen klicka på **Nästa.**

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4394575-nqPKeT1pGLgG5c9MS9EbG62lSuLqgBTwpjUQEb1NKgttKabM0nqPPGYJ6CKJ5sGs-0/image.png)
7. I nästa steg ser du en förhandsgranskning av importen, kontrollera om allt är korrekt och klicka på knappen **Import** för att avsluta importen.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4394576-bopkDeH22jNeXf9b3hdYoJU3leIytAFuCFg3Lyh0XZ67MbECPudloSTHY1rjWyDX-0/image.png)
8. Fönstret av import resultat visas. Klicka på **Gå till urval för nya företag/kontakter**för att öppna ett urval av importerade kontakter.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4394581-po6sok5t4WGcMnJYuTLnTCwejmCiMAoXUgW0BLU4hL2f39jtSr9d9qNID0x0RyWJ-0/image.png)
9. Om du behöver göra justeringar av de importerade kontakterna kan du enkelt göra det från ett val med hjälp av [Massredigering](https://community.superoffice.com/sv/learning/user-guide/selections/bulk-update/).

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4394582-5Hpu4sXFBeKyOczhnofBob1HYM5BYFHHG33htLb3fuXQ2pi90spcE8jrIuMoP1ft-0/image.png)

**Mer information**

Video: [How to import contacts to SuperOffice 8.0](https://www.youtube.com/watch?v=dVkCfpOkNl8)

FAQ: [Why is the “Number” field not allocated automatically during the import of companies/contacts?](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=113017)
