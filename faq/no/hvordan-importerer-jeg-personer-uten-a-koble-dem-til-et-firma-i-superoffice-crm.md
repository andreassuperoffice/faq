---
title: "Hvordan importerer jeg personer uten å koble dem til et firma i SuperOffice CRM?"
url: https://community.superoffice.com/no/support-faqs/faq/hvordan-importerer-jeg-personer-uten-a-koble-dem-til-et-firma-i-superoffice-crm/
lang: no
updated: "26. okt. 2026"
---

# Hvordan importerer jeg personer uten å koble dem til et firma i SuperOffice CRM?

Oppdatert på 26. okt. 2026

Jeg ønsker å importere en Excel-fil med kontakter som ikke er tilknyttet noe firma. Hvordan gjør jeg det?

**Merk!**

1. SuperOffice-brukeren som utfører importen av kontakter, må ha en rolle med [datarettigheter](https://docs.superoffice.com/no/admin/user-management/role/set-data-rights-for-role) som gir tillatelse til å opprette og/eller oppdatere kontakter. Se [denne FAQ-en](https://community.superoffice.com/no/support-faqs/faq/hvordan-konfigureretilgangsrettigheter-som-brukere-i-superoffice-crm-har/) for mer informasjon.
2. For å importere kontakter uten firmatilknytning til SuperOffice CRM, må du sette preferansen "**Obligatorisk firma for personer**" til "**Nei**". Se [denne FAQ-en](https://community.superoffice.com/no/support-faqs/faq/how-do-i-create-contacts-without-a-company-connection/) for mer informasjon.
3. En import kan ikke angres. Derfor anbefaler vi å ta en sikkerhetskopi av databasen før du gjør større oppdateringer av data. Hvis SuperOffice er installert lokalt, kan du se [denne FAQ-en](https://community.superoffice.com/no/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) som forklarer hvordan du gjør dette. Hvis du bruker SuperOffice Online, kan du kontakte [Support](https://community.superoffice.com/no/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/).

Følg trinnene nedenfor for å importere kontakter uten å knytte dem til et firma:

1. Klargjør en importfil som inneholder nye kontakter. Se [denne artikkelen](https://docs.superoffice.com/no/admin/import/create-spreadsheet) for tips om hvordan du klargjør importfilen.
2. I [Innstillinger og vedlikehold](https://community.superoffice.com/no/support-faqs/faq/hvordan-kan-jeg-administrere-superoffice-crm/) velger du **Import** (1) i navigatormenyen til venstre. Velg deretter **Firma/person**(2) og klikk på **Excel**-ikonet (3).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6923273-BoTcETal4U0eklBh42Mupfpf9NUgRFAdHaS8ZaRzENdSMdM3UWFSLsjmjY7upLAQ-0/image-20261026093642-1.png)
3. I neste trinn laster du opp Excel-filen din i dialogboksen "Last opp fil".

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6923295-qJQKMNJDRbz3ZWKPSy4SxXJN8pFWqoJsGuCnsw3mE3g0aGcfUtp0xDTTAkzTcyqA-0/image-20261026094523-2.png)
4. VVelg SuperOffice-feltene som tilsvarer kolonnene i importfilen din. Du trenger ikke å gjøre dette for kolonnene du ikke ønsker å importere.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6923300-JaeU2RjB5clM9ua8oNHbK4XjokGodp2ye4DOR8IcoTjWqDJarIgwRZT79Zldbt1I-0/image-20261026094911-3.png)
5. Klikk på **Konfigurer importinnstillinger** (1), og velg alternativet **Importer personer uten firma** (2) ved siden av **Hvis firmanavn er tomt**i dialogboksen **Importinnstillinger**. Gjør eventuelle andre nødvendige justeringer, og klikk på **Lagre** (3).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6923353-eG0DzNS07yLbyJOBY4NHPryPIif6cj11XlJ2KJprWabfpGYpLu13r2Sf9bPlWk1a-0/image-20261026095554-4.png)
6. Når du er fornøyd med oppsettet, klikker du på **Neste**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6923357-3xM4C6A9QrW7otmtWlRyJxbpC7UOMxShdIYtZL4P19rmHOlPb34gprwFBy3ETAoL-0/image-20261026095753-5.png)
7. I neste trinn får du se en forhåndsvisning av importen. Kontroller at alt er riktig, og klikk på **Importer** for å fullføre importen.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6923375-uxFxyYeykTjPis9UDyFpyCZGnzQL13ihb3Ssbgbs6A5xlomQAS9tSNHhmPzOMubf-0/image-20261026100016-6.png)
8. Skjermbildet med importresultatet vises. Klikk på **Gå til utvalg med nye firmaer/personer** for å åpne et utvalg med de importerte personene.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6923376-dqzjBtSwiZjsWWlBJl8KgOGbrKM0jNN1q7jMdJlmPCZ8d3w5tsNuU27rBp4q7nOk-0/image-20261026100200-7.png)
9. Hvis du trenger å gjøre endringer på de importerte personene, kan du enkelt gjøre dette fra et utvalg ved hjelp av funksjonen [Masseredigering](https://docs.superoffice.com/no/learn/basics/bulk-update).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6923427-cheyBB69T5xxHX0HCyuBHmeNRzpD7ie3SKJga0JAS82TccNGDgKOMWrglS06mg7W-0/image-20261026101554-8.png)

**Mer informasjon**

FAQ: [Hva gjør jeg når verdiene i feltet Nummer for person eller firma ikke blir tildelt automatisk under importen?](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-nar-verdiene-i-feltet-nummer-for-person-eller-firma-ikke-blir-tildelt-automatisk-under-importen/)
