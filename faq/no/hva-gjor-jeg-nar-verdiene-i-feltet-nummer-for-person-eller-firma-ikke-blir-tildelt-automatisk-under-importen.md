---
title: "Hva gjør jeg når verdiene i feltet Nummer for person eller firma ikke blir tildelt automatisk under importen?"
url: https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-nar-verdiene-i-feltet-nummer-for-person-eller-firma-ikke-blir-tildelt-automatisk-under-importen/
lang: no
updated: "15. mai 2026"
---

# Hva gjør jeg når verdiene i feltet Nummer for person eller firma ikke blir tildelt automatisk under importen?

Oppdatert på 15. mai 2026

Jeg har importert selskaper og lagt merke til at nummer-feltene på de importerte postene i SuperOffice er tomme. Dette er et obligatorisk felt i vårt system, så nå kan jeg ikke lagre en importert post uten å fylle inn nummerfeltet når jeg redigerer den. Hvorfor ble ikke firma-/personnummeret tildelt automatisk, og hvordan kan jeg fylle inn nummerfeltet automatisk?

SuperOffice CRM tildeler ikke verdier i Nummer-feltet automatisk ved import av nye firmaer eller personer, selv om dette feltet er obligatorisk i systemet ditt. Dette er forventet systematferd. Det finnes imidlertid et registrert [ønske](https://community.superoffice.com/no/product-releases/bugs-wishes/product-issue/?bid=8686&azure=1) i systemet om å forbedre denne funksjonaliteten.

Hvis du importerer nye personer og/eller firmaer og Nummer er et obligatorisk felt i systemet ditt, må du inkludere disse verdiene i importfilen og importere dem sammen med all annen informasjon.

Hvis du allerede har importert firmaer/personer uten å inkludere verdier i importfilen, kan du legge til nummerverdiene i filen din og gjennomføre importen på nytt. Følg trinnene nedenfor for å gjøre dette.

1. Logg inn i [Innstillinger og vedlikehold](https://community.superoffice.com/no/support-faqs/faq/hvordan-kan-jeg-administrere-superoffice-crm/).
2. Klikk på **Systemvalg (1)** og deretter på fanen **Nummertildeling (2)**. På skjermen finner du typen post du importerer. Ved siden av ser du verdien som vil bli brukt for neste post som opprettes i systemet. Noter denne verdien.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6682646-Z9iw2P8qC89PuD7EkM13Mgqb013UK5DrBl01JzXkkTB1MpcNgkpdIOkGz427O5aD-0/image-20260514130539-1.png)
3. Rediger importfilen din ved å legge til en kolonne for nummer. Fyll inn verdiene, og start med nummeret du noterte tidligere.
4. Gjenta importen. I **importinnstillingene** velger du alternativet *Flett – oppdater tomme felt* i feltet **Handling**. Dette vil sørge for at nummerfeltet for firmaer eller personer blir fylt ut med verdiene du har lagt inn i filen din.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6682661-I6TlA7YJjSPaTpTlRiTXlBeRql9ws65345DkoRToF8EIwIUqI7k11BHTm4HiZRFz-0/image-20260514131056-3.png)
5. Gå tilbake til fanen **Nummertildeling**, dobbeltklikk på nummeret for firma eller person, og fyll inn nummeret som skal tildeles nye poster i feltet Neste nummer. Dette nummeret skal være 1 høyere enn det siste nummeret i importfilen din.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6682674-JwaAeW8IPlB6QOOfWUELPt1hDbgxmwrnaj43ybYZpneCwuw7iFhQAGX3hsrtHj8H-0/image-20260514131451-5.png)

**Merk!**

1. Vi anbefaler å ta en sikkerhetskopi før du gjør endringer direkte i databasen. Denne [FAQ-en](https://community.superoffice.com/no/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) forklarer hvordan du gjør det.
2. Sørg for at ingen nye firmaer eller personer blir opprettet mens du utfører importen, da dette kan påvirke nummersekvensen.
3. Hvis du er usikker på prosessen, anbefaler vi å benytte deg av SuperOffice-konsulenter. Konsulenttjenester er avgiftsbelagte. Ta kontakt med din SuperOffice-kontaktperson dersom du ønsker mer informasjon om denne tjenesten.
4. Hvis du ønsker å endre oppsettet slik at nummer-feltet ikke er obligatorisk på postkortet, velger du alternativet **Tillat tom** (1) i tellerdialogen.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6682699-JBK6wueo7m4gS8DQyJiIPCKHna96m3932T7qZrAdKl0D3Y9hkxeJrcw5b8gThgd8-0/image-20260514131842-6.png)

**Mer informasjon**

Forum: [Provisional Solution to: Company and contact number field not updated during import](https://community.superoffice.com/no/technical/forums/product-forums/crm-web-application/provisional-solution-to-company-and-contact-number-field-not-updated-during-import/)

Wish: [Import and Number allocation problem](https://community.superoffice.com/no/product-releases/bugs-wishes/product-issue/?bid=8686&azure=1)
