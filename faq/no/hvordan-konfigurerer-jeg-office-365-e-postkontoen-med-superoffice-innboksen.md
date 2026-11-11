---
title: "Hvordan konfigurerer jeg Office 365-e-postkontoen med SuperOffice-innboksen?"
url: https://community.superoffice.com/no/support-faqs/faq/hvordan-konfigurerer-jeg-office-365-e-postkontoen-med-superoffice-innboksen/
lang: no
updated: "7. des. 2021"
---

# Hvordan konfigurerer jeg Office 365-e-postkontoen med SuperOffice-innboksen?

Oppdatert på 7. des. 2021

Hvordan konfigurerer jeg Office 365-e-postkontoen med SuperOffice-innboksen?

For å konfigurere Office 365-e-postkontoen din med SuperOffice-innboksen, følg trinnene nedenfor:

1. [Kontroller at alle forutsetninger er oppfylt.](https://community.superoffice.com/no/support-faqs/faq/hvordan-konfigurerer-jeg-office-365-e-postkontoen-med-superoffice-innboksen/#1)
2. [Konfigurer SuperOffice for å bruke integrert innboks.](https://community.superoffice.com/no/support-faqs/faq/hvordan-konfigurerer-jeg-office-365-e-postkontoen-med-superoffice-innboksen/#2)
3. [Skriv inn Office 365-serveren din og e-postkontoinformasjonen for å koble den til SuperOffice.](https://community.superoffice.com/no/support-faqs/faq/hvordan-konfigurerer-jeg-office-365-e-postkontoen-med-superoffice-innboksen/#3)
4. [Konfigurer navnene på e-postmappene dine](https://community.superoffice.com/no/support-faqs/faq/hvordan-konfigurerer-jeg-office-365-e-postkontoen-med-superoffice-innboksen/#4)

**Trinn 1. Kontroller at alle forutsetninger er oppfylt**

1. SuperOffice Inbox støtter bare [IMAP- og SMTP-protokoller.](https://docs.superoffice.com/onsite/requirements/iis.html) Pass på at IMAP er aktivert for din e-postkonto.
2. For å sende ut e-post fra SuperOffice må e-postadressen du bruker med SuperOffice Inbox, bli registrert i kontaktkortet ditt. For mer informasjon les denne [FAQ](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=112980).
3. Hvis du bruker 2 trinn ( FAQ er ikke på norsk enda)

**Trinn 2. Konfigurer SuperOffice for å bruke integrert innboks**

Les [denne FAQ](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=110872). Trinn 2 forklarer hvordan gjør du det.

**Trinn 3. Skriv inn Office 365-serveren din og e-postkontoinformasjonen for å koble den til SuperOffice**

- **Hvis du bruker SuperOffice versjon 8.1 eller nyere**, vil SuperOffice prøve å fylle ut e-postserveren din automatisk etter at du har skrevet inn e-postadresse  og passord. Hvis det ikke vil kunne gjette disse detaljene riktig eller e-postadressen og passordet du skrev inn ikke er korrekt, blir du omdirigert til "Flere innstillinger" -dialogboksen. Der må du manuelt skrive inn eller sjekke konfigurasjonsinformasjon for Innkommende og utgående servere.

- **Hvis du bruker SuperOffice versjon 8.0 eller eldre**, må du manuelt fylle ut informasjon for innkommende og utgående servere. Se på eksempel nedenfor:

1. For å få e-postene dine importert til SuperOffice, fyll ut følgende informasjon:

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3007049-GttfwSprFQhRJ3FSn8FCza7P4TLL5pTEnk3ESgXrsuhQsdy3QMWgJ0JPTlGJDFcX-0/image.png)

- **E-post server:** outlook.office365.com:993​
- **Brukernavn**: din e-postadresse.
- **Passord:**  passordet til din Office 365 konto.
- **SSL:** På

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3007056-X9OjqfgNeWwSPCOC1gDkcA7paaW6xWelWKRaYYfBjNSBYOu3E8481JGmrkaZULA9-0/image.png)

- **Utgående server:** smtp.office365.com:587
- **Brukernavn**: din e-postadresse.
- **Passord:**  passordet til din Office 365 konto.
- **SSL:** På

**Trinn 4. Konfigurer navnene på e-postmappene dine​**

Dette trinnet er bare nødvendig for SuperOffice versjon 8.0 og eldre. Sjekk denne FAQen om [hvordan du konfigurerer e-postmappenavn i SuperOffice CRM-innboksen?](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=113160)

**Mer informasjon:**

[Hva gjør du hvis du ikke kan sende e-post fra Superoffice ?](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=113050)

[What to do if I get an error when sending email from SuperOffice?](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=112980)
