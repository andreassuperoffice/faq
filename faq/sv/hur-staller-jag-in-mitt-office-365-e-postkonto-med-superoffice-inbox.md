---
title: "Hur ställer jag in mitt Office 365-e-postkonto med SuperOffice Inbox?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-staller-jag-in-mitt-office-365-e-postkonto-med-superoffice-inbox/
lang: sv
updated: "28. mars 2022"
---

# Hur ställer jag in mitt Office 365-e-postkonto med SuperOffice Inbox?

Uppdaterad på 28. mars 2022

Hur ställer jag in mitt Office 365-e-postkonto med SuperOffice Inbox?

Följ stegen nedan för att ställa in ditt Office 365-konto med SuperOffice Inbox:

[Steg 1. Kontrollera att alla förutsättningar är uppfyllda](https://community.superoffice.com/sv/support-faqs/faq/hur-staller-jag-in-mitt-office-365-e-postkonto-med-superoffice-inbox/#1)

[Steg 2. Ställ in SuperOffice som en föredragen e-postklient](https://community.superoffice.com/sv/support-faqs/faq/hur-staller-jag-in-mitt-office-365-e-postkonto-med-superoffice-inbox/#2)

[Steg 3. Ange din Office 365-server och e-postkontoinformation för att ansluta den till SuperOffice Inbox](https://community.superoffice.com/sv/support-faqs/faq/hur-staller-jag-in-mitt-office-365-e-postkonto-med-superoffice-inbox/#3)

​

**Steg 1. Kontrollera att alla förutsättningar är uppfyllda**

1. SuperOffice Inbox stöder de enda IMAP- och SMTP-protokollen så kolla om IMAP är aktiverat för ditt e-postkonto. Kontrollera [den här artikeln](http://docs.microsoft.com/en-au/exchange/troubleshoot/configure-mailboxes/pop3-imap-owa-activesync-office-365) för mer information.
2. Om du använder en 2-stegs autentisering, läs denna FAQ: [Hur genererar du ett Office 365 App-lösenord för att använda 2-stegs verifiering med SuperOffice-inbox?](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=se&noCookies=true&action=viewKbEntry&id=113210)

​

**Steg 2. Ställ in SuperOffice som den önskade e-postklienten**

När man loggar in på SuperOffice CRM för första gången visas installationsverktyget för webbverktyg. Där kan man välja vilken e-postklient som ska vara standard.

Om du inte har valt att SuperOffice ska vara standard-e-postklienten tidigare, följ dessa steg:

1. Klicka på ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4333348-Nns3ERiYa8o5Cx9pqI6QCiN8XNkB5gY1i95afluqxXEUNOz6OKtgyn02ezd5tqxu-0/image.png) och välj **Local settings**i rullgardinsmenyn.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359596-dtW2KwQiQXdgiTS4JxszduDtzm0XqX91uR80IQNTLk7ynY7YM2YP76IlcROHcukj-0/image.png)
2. Kolla om SuperOffice CRM är markerat i fältet **E-mail client**(1) och klicka på **OK**(2).

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359597-g22Fy0MTALnn8J8La7ywd50FQL0xX7rHNf1h6SKUGSDc8me8tWWAnCJAqOcAn6wk-0/image.png)

​

**Steg 3. Konfigurera SuperOffice Inbox med information om ditt e-postkonto**

Klicka på knappen **Inkorgen**(1) i navigatorn. Ange inloggningsformuläret **e-postadressen** (2) du vill konfigurera med SuperOffice-inkorgen och **lösenordet**(3) för att komma åt detta e-postkonto och klicka på **Spara**(4).

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359598-4KFtUmNjmHkk3jZQ5NQOILhDD6eA5AjzJPoZ2thutGtGKnFn0CPGb0NsKNAjegIP-0/image.png)

Om SuperOffice känner e-postleverantören kommer serverinställningarna att konfigureras automatiskt och inkorgen kommer att laddas. Annars kommer skärmen med fler inställningar att visas och ge möjlighet att fylla i de fält som krävs för att konfigurera inboxen.

Fyll i: för att se till att dina e-postmeddelanden importeras till SuperOffice Inbox:

- **E-post server:**outlook.office365.com:993​
- **Användernamn**: din fulla e-postadress
- **Lösenord:** din Office 365 konto lösenord
- **SSL:** På

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359629-SQt1EqitTW4qEh6tuwyPMO7muGiDf0QrxETM4nUG523f3cU2AMkojwgintW5luu2-0/image.png)

Fyll i: för att se till att du kan skicka e-postmeddelanden från SuperOffice Inbox:

- **Outgoing server name:** smtp.office365.com:587
- **User name:** your full e-mail address
- **Password:** your Office 365 account password
- **SSL:** On

Sedna klicka på **Logga in.**

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359631-QNj8r482qIkBtcLiGopqhoJyjnbarK7YjU7E44jr1BOEYfu5H7eOSDIQ8iMp9z0P-0/image.png)

**Notera!** SuperOffice importerar automatiskt till databasen alla e-postmeddelanden som skapades under de senaste 30 dagarna om du arbetar på SuperOffice Online och sista 180 dagar om du arbetar på SuperOffice Onsite. Detta kan ändras i raden web. .config <Component> section <add key="NumberOfDaysToDownload"> line.Om du arbetar med SuperOffice Online, vänligen kontakta SuperOffice support.

Följ stegen nedan om du vill ändra ditt e-postkonto:

1. Klicka på ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4333348-Nns3ERiYa8o5Cx9pqI6QCiN8XNkB5gY1i95afluqxXEUNOz6OKtgyn02ezd5tqxu-0/image.png) och välj **E-mail options.**

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359601-52sSAdRu54JTMEUcaCChTMwjB3Agbs4SUYIDjYjQ385QRmbFEy8grZGMwUtxAsnW-0/image.png)
2. Välj **E-mail account** (1) och klicka på knappen **Edit/remove**(2) och sedan klicka på **OK**för att slutföra.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4359602-p6nybZ0Ao9LOBSN9kxQ593n5ngdX1ImX7LBLCCbq2CCH7ENBdAU0oGjwPjBP7XXU-0/image.png)

|  |
| --- |
| Följ vänligen [denna FAQ](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=111469)om du använder SuperOffice Onsite 8 eller någon tidigare version. |
