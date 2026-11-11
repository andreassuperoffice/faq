---
title: "Hur konfigurerar jag mitt Office 365 mejlkonto med SuperOffice Inbox?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-konfigurerar-jag-mitt-office-365-mejlkonto-med-superoffice-inbox/
lang: sv
updated: "7. dec. 2021"
---

# Hur konfigurerar jag mitt Office 365 mejlkonto med SuperOffice Inbox?

Uppdaterad på 7. dec. 2021

Hur konfigurerar jag mitt Office 365 mejlkonto med SuperOffice?

För att konfigurera  ditt Office 365-konto med SuperOffice Inbox, följ stegen nedan:

1. [Kontrollera att alla förutsättningar är uppfyllda.](https://community.superoffice.com/sv/support-faqs/faq/hur-konfigurerar-jag-mitt-office-365-mejlkonto-med-superoffice-inbox/#1)
2. [Konfigurera SuperOffice till att använda den integrerade inkorgen.](https://community.superoffice.com/sv/support-faqs/faq/hur-konfigurerar-jag-mitt-office-365-mejlkonto-med-superoffice-inbox/#2)
3. [Ange din Office 365-server och e-postkontoinformation för att ansluta den till SuperOffice.](https://community.superoffice.com/sv/support-faqs/faq/hur-konfigurerar-jag-mitt-office-365-mejlkonto-med-superoffice-inbox/#3)
4. [Konfigurera dina e-postmappsnamn](https://community.superoffice.com/sv/support-faqs/faq/hur-konfigurerar-jag-mitt-office-365-mejlkonto-med-superoffice-inbox/#4)

**Steg 1. Kontrollera att alla förutsättningar är uppfyllda**

1. SuperOffice Inbox stöder endast [IMAP- och SMTP-protokoll.](https://docs.superoffice.com/onsite/requirements/iis.html) Se till att IMAP är aktiverat för ditt e-postkonto.
2. För att skicka ut e-post från SuperOffice måste e-postadressen du använder med SuperOffice Inbox registreras i ditt kontaktkort. Läs denna [FAQ](http://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=112980) för mer information.
3. Om du använder 2-stegs autentisering läs denna FAQ: [Hur genererar du ett Office 365 App-lösenord för att använda tvåstegs verifiering med SuperOffice Inbox?](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=113210)

**Steg 2. Konfigurera SuperOffice för att använda integrerad inkorg**

Denna [FAQ](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=111469) Steg 2, förklarar hur man gör detta.

**Steg 3. Ange din Office 365-server och e-postkontoinformation för att ansluta till SuperOffice**

            - **Om du använder SuperOffice version 8.1 eller** senare kommer SuperOffice att försöka fylla i din e-postserverinformation automatiskt efter att du har angett ditt e-postadress och lösenord. Om inte SuperOffice kommer att kunna hitta dessa uppgifter korrekt eller om e-postadressen och lösenordet du angav inte är korrekt kommer du att dirigeras till dialogrutan "Fler inställningar". Där måste du manuellt ange eller kontrollera konfigurationsinformation för inkommande och utgående servrar.

            - **Om du använder SuperOffice version 8.0 eller** äldre behöver du manuellt skriva in eller kontrollera konfigurationsinformation för Inkommande och utgående servrar. Se exempel nedan:

1. För att få dina e-postmeddelanden importerade till SuperOffice fyll i:

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3016282-MS8GCXXidRYuT8Zmbp9wy6tM6P9Wfiw1tINXwLI57T6htyrasfjbogNCw91QCdea-0/image.png)

**E-postserver:** outlook.office365.com:993
**Användarnamn:** Din fullständiga e-postadress
**Lösenord:** ditt Office 365-konto lösenord
**SSL:** On

2. För att kunna skicka ut e-post från SuperOffice, fyll i:

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3016283-9UQi56y5dB3giWMHINtwnqMH2tTbRDwNSIaRnrw41ZihD5Gj5Nwh2QMSlpW9lcka-0/image.png)

**Utgående servernamn:** smtp.office365.com:587
**Användarnamn:** Din fullständiga e-postadress
**Lösenord:** ditt Office 365-konto lösenord
**SSL:** On

**Steg 4. Konfigurera dina namn på e-postmappar**

Detta steg gäller endast för SuperOffice 8.0 och äldre. Kolla i denna FAQ hur du gör det: [Så här konfigurerar du e-postmappsnamn i SuperOffice CRM Inbox?](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=113211)

**Mer information:**

[What to do if I can't send e-mail from SuperOffice?](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=111187)

[What to do if I get an error when sending email from SuperOffice?](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=112980)
