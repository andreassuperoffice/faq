---
title: "Hvordan setter jeg opp min Office 365 konto med Superoffice Innboks?"
url: https://community.superoffice.com/no/support-faqs/faq/hvordan-setter-jeg-opp-min-office-365-konto-med-superoffice-innboks/
lang: no
updated: "28. mar. 2022"
---

# Hvordan setter jeg opp min Office 365 konto med Superoffice Innboks?

Oppdatert på 28. mar. 2022

Hvordan setter jeg opp min Office 365 konto med Superoffice Innboks?

For å sette opp Office 365 konto med Superoffice Innboks følg trinnene nedenfor:

[Trinn 1. Sjekk at alle forutsetninger er oppfylt](https://online2.superoffice.com/Cust1990/CS/scripts/blogic.fcgi?_sf=0&action=doScreenDefinition&idString=viewFaq&entryId=113749&__formKeyId=46201883#1)

[Trinn 2.](https://online2.superoffice.com/Cust1990/CS/scripts/blogic.fcgi?_sf=0&action=doScreenDefinition&idString=viewFaq&entryId=113749&__formKeyId=46201883#2)[Velg den foretrukket SuperOffice e-postklienten](https://online2.superoffice.com/Cust1990/CS/scripts/blogic.fcgi?_sf=0&action=doScreenDefinition&idString=viewFaq&entryId=113742&__formKeyId=46009193#2)

[Trinn 3. Konfigurer SuperOffice-innboksen med e-postserverinformasjonen](https://online2.superoffice.com/Cust1990/CS/scripts/blogic.fcgi?_sf=0&action=doScreenDefinition&idString=viewFaq&entryId=113749&__formKeyId=46201883#3)

​

**Trinn 1. Sjekk at alle forutsetninger er oppfylt**

1. SuperOffice Innboks støtter bare IMAP- og SMTP-protokoller, derfor anbefaler vi å aktivere  IMAP  for din e-postkonto. Vennligst sjekk [denne artikkelen](http://docs.microsoft.com/en-au/exchange/troubleshoot/configure-mailboxes/pop3-imap-owa-activesync-office-365) for mer informasjon.
2. Hvis du bruker 2-trinns verifisering, les denne FAQ'en: [Hvordan genererer jeg et Office 365 App passord for å bruke 2-trinns verifisering med SuperOffice innboksen?](http://Hvordan genererer jeg et Office 365 App passord for å bruke 2-trinns verifisering med SuperOffice innboksen)

​

**Trinn 2. Sett opp SuperOffice som foretrukket e-postklient**

Når du logger deg på SuperOffice CRM for første gang, vises installasjonsdialogen for Web Tools. Der kan du velge hvilken e-postklient skal være standard.

Hvis du ikke har valgt at SuperOffice skal være standard e-postklient før, kan du følge disse trinnene:

1. Klikk på ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4333348-Nns3ERiYa8o5Cx9pqI6QCiN8XNkB5gY1i95afluqxXEUNOz6OKtgyn02ezd5tqxu-0/image.png) og velg**Lokale innstillinger** fra rullegardinmenyen.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359611-PpHNORPuQczp3eXaZZKIzmp0MLHnKgzbd6SQ15CtEBrh5HGo1AA8gelD7C4ODkS5-0/image.png)
2. Forsikre deg om at *SuperOffice CRM*er valgt i feltet **E-postklient**(1), og klikk deretter **OK** (2).

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359612-gnoonqSWsYTKu5hURHXQAUMjxbcJ27bkBIBQDyeOJSSCTE8FHCBhwcAAgDY7RLt4-0/image.png)

​

**Trin 3. Konfigurer SuperOffice-innboksen med e-postserverinformasjonen.**

Klikk på knappen **Innboks**(1) i navigatoren. Skriv inn påloggingsinformasjonen **e-postadressen** (1) du vil konfigurere SuperOffice-innboksen med og **passordet** (3) for å få tilgang til denne e-postkontoen og klikk på **Lagre** (4).

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359613-7rWdKod6TrXGixZuCW0otAWMPMMImUZDUI1lzoiDGa4Tknmd7QBZneYTmL3Qnex9-0/image.png)

Hvis SuperOffice gjenkjenner e-postleverandøren din, blir serverinformasjonen  fylt ut automatisk. Hvis ikke, vises flere innstillinger, og du må fylle ut de nødvendige feltene selv.

For å sikre deg  at e-postene dine blir importert til SuperOffice Innboks, vennligst fyll ut:

- **E-postserver:**outlook.office365.com:993​
- **Brukernavn**: brukernavnet ditt, som vanligvis er din fulle e-postadresse
- **Passord:** passordet ditt til e-postkontoen
- **SSL:** On

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359626-4IKUxbr42UFdaZm2eZRKDeO8Ruw0tfbAsUHbHXSAKxRzy3Zk7EjrJx8fSbMpGwtm-0/image.png)

For å sikre deg at du kan sende ut e-post fra SuperOffice Innboks, vennligst fyll ut:

- **SMTP-servernavn:**smtp.office365.com:587
- **Brukernavn:** brukernavnet ditt, som vanligvis er din fulle e-postadresse
- **Passord:**  passordet ditt til e-postkontoen
- **SSL:** On

Trykk på **Login.**

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359627-oU0a1siAbxxJQYtXCAjsnQpSPNa7gNxMHXWsjiTnow8QyOsgcrXhd5OkzbsHZFWm-0/image.png)

**Merk!** SuperOffice importerer automatisk til databasen alle e-postmeldinger som ble opprettet i løpet av de siste 30 dagene hvis du jobber med SuperOffice Online og siste 180 dager hvis du jobber med SuperOffice Onsite. Dette kan endres i web.config <Komponent> delen <add key = "NumberOfDaysToDownload"> linjen. Hvis du jobber med SuperOffice Online, vennligst [ta kontakt med SuperOffice support](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=113431).

Hvis du vil endre e-postkontoen din, kan du følge trinnene nedenfor:

1. Klikk ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4333348-Nns3ERiYa8o5Cx9pqI6QCiN8XNkB5gY1i95afluqxXEUNOz6OKtgyn02ezd5tqxu-0/image.png) og velg deretter **Alternativer for e-post.**

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359616-2rmjuMlpI0I6q2AY5epfIrzusBwnu3co9iYtu0J1oiHtDPnX4WyIFjDOBYahSBHz-0/image.png)
2. Velg **E-postkonto**-fanen (1), trykk **Rediger/slett**-knappen (2) og deretter **OK**(3)for å avslutte.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359617-dSQG6afy26MNuGH9QOyeuoWUmunjZr4UpIRrw4576BAndMKEufi2NHf4IjIC5664-0/image.png)

|  |
| --- |
| Vennligst følg [denne FAQen,](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=10105) hvis du bruker SuperOffice Onsite 8 eller en tidligere versjon. |
