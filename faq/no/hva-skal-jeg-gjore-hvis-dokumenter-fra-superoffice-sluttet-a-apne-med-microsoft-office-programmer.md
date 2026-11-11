---
title: "Hva skal jeg gjøre hvis dokumenter fra SuperOffice sluttet å åpne med Microsoft Office programmer?"
url: https://community.superoffice.com/no/support-faqs/faq/hva-skal-jeg-gjore-hvis-dokumenter-fra-superoffice-sluttet-a-apne-med-microsoft-office-programmer/
lang: no
updated: "22. jun. 2026"
---

# Hva skal jeg gjøre hvis dokumenter fra SuperOffice sluttet å åpne med Microsoft Office programmer?

Oppdatert på 22. jun. 2026

Jeg pleide å kunne åpne, redigere og lagre dokumenter fra SuperOffice CRM med Microsoft Office-programmer. Nå blir dokumenter fra SuperOffice CRM lastet ned og åpnet lokalt, og endringer som gjøres i eksisterende dokumenter blir ikke lagret tilbake til SuperOffice CRM.

Hvorfor skjer dette, og hvordan fikser jeg det?

De beskrevne situasjonene kan oppstå når SuperOffice WebTools ikke er installert eller ikke er koblet til datamaskinen din. For å fikse det, følg trinnene nedenfor:

[Skritt 1. Sørg for at nyeste versjon av WebTools er installert](https://community.superoffice.com/no/support-faqs/faq/hva-skal-jeg-gjore-hvis-dokumenter-fra-superoffice-sluttet-a-apne-med-microsoft-office-programmer/#1)

[Skritt 2. Sørg for at Webtools er aktiv og tilkoblet](https://community.superoffice.com/no/support-faqs/faq/hva-skal-jeg-gjore-hvis-dokumenter-fra-superoffice-sluttet-a-apne-med-microsoft-office-programmer/)

[Skritt 3. Konfigurer SuperOffice WebTools til din SuperOffice CRM konto](https://community.superoffice.com/no/support-faqs/faq/hva-skal-jeg-gjore-hvis-dokumenter-fra-superoffice-sluttet-a-apne-med-microsoft-office-programmer/#2)

​

**1. Sjekk at SuperOffice WebTools er installert**

    1. Åpne **Programs and Features** på datamaskinen din.

    2. Kontroller at SuperOffice Web Extensions finnes i programlisten. [Klikk her](https://community.superoffice.com/no/product-releases/release-notes/) for å finne versjonsnummeret til den nyeste versjonen.

![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746493-EpTpfPYlX1oxNo5quD8kycJHwXhimIRGDntgHro0BhItdQnCFtubYMRuzbXx69hw-0/image-20260621203609-1.png)

    3. Hvis du ikke finner Web Extensions, må du installere og konfigurere det. Les [denne](https://community.superoffice.com/en/support-faqs/faq/how-do-i-download-and-install-webtools-for-superoffice-crm/)[FAQ-](https://community.superoffice.com/en/support-faqs/faq/how-do-i-download-and-install-webtools-for-superoffice-crm/)en for mer informasjon om hvordan du gjør det.

​

**2. Sjekk at SuperOffice WebTools er koblet til SuperOffice CRM**

1. Høyreklikk på SuperOffice WebTools-ikonet nederst til høyre i Windows-oppgavelinjen og velg **Preferanser**. Hvis du ikke ser SuperOffice WebTools-ikonet, kan det hende at WebTools ikke er startet. Kontakt IT-avdelingen for å sikre at **SuperOffice.TrayApp.Client.Exe** alltid er aktiv.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746499-uOQYYsyw8kKf2PtpJA233sBtWnKnN8o5gXAMwuJHQEF090CNtXLTaiKMeikBdH3E-0/image-20260621205854-7.png)
2. I WebTools-innstillingene, sjekk om du ser firmanavnet til bedriften din:

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6233017-TIgdJPdMKoHi3EkuSrKCR8hnoYBqnB2hmdLg7NctDZGPWHIx9Q9PL8jkL9lg4nYa-0/konfig.png)

   Hvis feltet er tomt, er ikke WebTools riktig konfigurert. Gå da direkte til det siste trinnet (**Trinn 3**) i denne veiledningen.
3. Hvis du ser firmanavnet ditt, lukk innstillingsvinduet. Høyreklikk på SuperOffice WebTools-ikonet i oppgavelinjen igjen, og velg denne gangen **Logg inn**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746500-qpgA2K0CIc9UboOEMJunDse5MjaOLwyascz4GkSAaZlCKAx9NIEZ3U2lKa2n5YAn-0/image-20260621210133-8.png)
4. I den nye fanen som åpnes, prøv å åpne et lagret dokument. Hvis det fortsatt ikke åpnes direkte i et Office-program, fortsett til trinn 3 nedenfor.

​

**3. Konfigurer SuperOffice WebTools til din SuperOffice CRM konto

Merk!** Dette trinnet er bare nødvendig hvis trinn 2 viste at WebTools ikke er riktig konfigurert. Prøv alltid trinn 2 først.

1. Trykk på personlinge innstilinger øverst til høyre i SuperOffice og velg **Last ned**- **SuperOffice WebTools**

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746566-7bOWKBTSg6l0kLxajUZ1yQI89Fex9XigW24Ow7ZpP91hApxN6A5T3aOFTtXYi94n-0/image-20260622081954-1.png)
2. Et av to ulike vinduer for Last ned SuperOffice WebTools åpnes.

   **-** **Hvis du ser vinduet Jobb raskere med dokumenter**, klikker du på Klikk her for å koble deg til.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746567-kknns9kQRh91nuAYdXP0YhW30D6HFgtHZR5M9jm8A5BxTxKBwYbEok33w4guXoyO-0/image-20260622082121-2.png)

   **- Hvis du ser vinduet Personal computer Home/Office**, velger du Personal computer Home/Office, velger e-postklienten du bruker, og går videre til neste skjermbilde. Klikk deretter på Kilkk her for å koble WebTools til denne SuperOffice-installasjonen.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746575-O0ZFA1KqbQBergdug6o8ZwZLa781FawtrqFLcfJAXX54uujdgdou9DgQnn90y649-0/image-20260622082444-3.png)
3. Når **xxxxxx.SoConfig**-filen er lastet ned, klikk på den for å kjøre den.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746497-eUeHLRgEI6jq5FSl4G5lafQiYSLq44RDZFR1E3Ntd68rxaEiyGDnGXtEhpwalZte-0/image-20260621205357-5.png)
4. Du vil se en dialogboks nederst i høyre hjørne av skjermen som sier at SuperOffice må autentisere deg mot din SuperOffice CRM-installasjon. Klikk **OK**, så starter autentiseringen i nettleseren, og når det er fullført, vil du se en bekreftelsesmelding.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6233071-TLerfJ6wNQfgs1KGAgbEp60plLFxLSpmMS98ujwh0flWMoBtZpHlOAUJlUETEA6R-0/aut.png)

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5375272-PmPp9tuP544hSFsyAu3sAdPGtqao4H8dGyz9JCUecc7SdKIf9J0j8d2K9jqRouwM-0/image-20230501112259-4.png)

   **Merk!** Hvis du bruker en autentiseringsleverandør (Microsoft 365 eller Google), kan du bli omdirigert til leverandørens nettside for ny autentisering (skriv inn brukernavn og passord) for å fullføre tilkoblingen til SuperOffice CRM.

   Deretter klikker du på OK, oppdaterer nettleseren og tilkoblingen til SuperOffice WebTools blir gjenopprettet.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6136889-hTUHoxQ8sImqaIYl3SfAXY0GwhOBL5P9yBHwA5W4xjeb9AbB8gA0gGFzF7xqYI4t-0/image-20250320080905-1.png)

**Merk!** Denne FAQ-en forklarer hvordan du feilsøker SuperOffice Web Extensions, som brukes til å åpne og lagre dokumenter fra SuperOffice CRM. Hvis e-poster ikke lenger åpnes i Outlook og du fortsatt bruker MailLink, må du kontrollere at MailLink er installert og konfigurert. MailLink installeres separat fra Web Extensions. Du finner mer informasjon [her](https://community.superoffice.com/en/support-faqs/faq/why-is-maillink-not-installed-when-i-download-webtools/).

**Mer informasjon**

FAQ: [What can I do when I run into problems with SuperOffice WebTools?](https://community.superoffice.com/en/support-faqs/faq/what-can-i-do-when-i-run-into-the-problems-with-superoffice-webtools/)

FAQ: [What is "SuperOffice WebTools" and what does it do?](https://community.superoffice.com/no/support-faqs/faq/what-is-superoffice-webtools-and-what-does-it-do/)

FAQ**:**[How do I reinstall SuperOffice WebTools?](https://community.superoffice.com/no/support-faqs/faq/how-do-i-reinstall-superoffice-webtools/)
