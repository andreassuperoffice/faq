---
title: "Hur börjar jag använda SuperOffice Inbox?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-borjar-jag-anvanda-superoffice-inbox/
lang: sv
updated: "10. feb. 2026"
---

# Hur börjar jag använda SuperOffice Inbox?

Uppdaterad på 10. feb. 2026

Hur börjar jag använda SuperOffice Inbox?

Följ stegen nedan för att börja använda SuperOffice Inbox för att läsa, skicka och arkivera e-post direkt från SuperOffice CRM:

[Steg 1. Bekräfta att ditt e-postkonto har uppfyllt förutsättningarna](https://community.superoffice.com/sv/support-faqs/faq/hur-borjar-jag-anvanda-superoffice-inbox/1)

[Steg 2. Ställ in SuperOffice som den önskade e-postklienten](https://community.superoffice.com/sv/support-faqs/faq/hur-borjar-jag-anvanda-superoffice-inbox/#2)

[Steg 3. Konfigurera SuperOffice Inbox med dina e-postkontouppgifter](https://community.superoffice.com/sv/support-faqs/faq/hur-borjar-jag-anvanda-superoffice-inbox/#3)

​

**Steg 1. Bekräfta att ditt e-postkonto har uppfyllt förutsättningarna**

SuperOffice Inbox stöder endast IMAP- och SMTP-protokollen, så se till att båda är aktiverade för ditt e-postkonto. Om du använder Office 365 kan du läsa följande FAQer: [IMAP](https://learn.microsoft.com/en-au/troubleshoot/exchange/user-and-shared-mailboxes/pop3-imap-owa-activesync-office-365) och [SMTP](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission).

Kontrollera [den här artikeln](https://docs.superoffice.com/en/online/system-requirements.html) för kontrollera SuperOffice-krav.

OBS! Gmail kräver nu app-lösenord för tredjepartsappar istället för ditt vanliga lösenord. Se denna [FAQ](https://community.superoffice.com/sv/support-faqs/faq/how-do-i-generate-a-googleapp-password-to-use-2-step-verification-with-superoffice-inbox/). Från januari 2025 kommer IMAP att vara permanent aktiverat för alla Gmail-konton, så ingen åtgärd behövs angående IMAP-inställningar.

​

**Steg 2. Ställ in SuperOffice som den önskade e-postklienten**

När man loggar in på SuperOffice CRM för första gången visas installationsverktyget för webbverktyg. Där kan man välja vilken e-postklient som ska vara standard.

Om man inte har valt att SuperOffice ska vara standard-e-postklienten tidigare, följ dessa steg:

1. Klicka på ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149227-HPZANxNnbF03KiWKirpIzMkD3yO3wnKZ6awMyFdE1NunOQmolcoRCt3sTNo0MeI0-0/image-20250327153351-1.png) och välj **Local settings** i rullgardinsmenyn.
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6527913-AjM99XsxP4wZaQPRZsAZliDd7YhZm0XlsS1g0jpFgc0PwegZBq6KAWhHqHgSelkx-0/image-20260210074320-1.png)
2. Kolla om SuperOffice CRM är markerat i fältet **E-mail client**(1) och klicka på **OK** (2).
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6527915-tioMZAgiAaJUSCYOSm96uDK7SI33jxlNjf8AARM8TybAPQjSI8qpWnqFx7JZIB5l-0/image-20260210074458-3.png)

​

**Steg 3. Konfigurera SuperOffice Inbox med information om ditt e-postkonto**

Klicka på knappen **Inkorgen** (1) i navigatorn. Ange inloggningsformuläret **e-postadressen** (2) du vill konfigurera med SuperOffice-inkorgen och tryck på Nästa**:**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6527916-QDox1w100Eb54MygAZmy4rEAWM6OtC4N1Uu9ndIkUL41cZTTt7cXB9soM2B2kuRn-0/image-20260210074736-4.png)

Sedan behöver du ange ditt lösenord och trycka på Logga in:
![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6527917-lpLzEzFzukXJkJAxCmCPsIh5AKYWFs9tPqGWZLDDyAby2hYFUH07mZo4fOXTz8WM-0/image-20260210074820-5.png)

Om SuperOffice känner igen e-postleverantören (som Gmail), kommer serverinställningarna att konfigureras automatiskt och inkorgen ska laddas upp. Om nej, så kommer skärmen med fler inställningar att visas och du måste fylla i de fält som krävs.

          Fyll i för att se till att dina e-postmeddelanden importeras till SuperOffice Inbox:

- E-postserver: dina IMAP-serveruppgifter
- Användarnamn: ditt användarnamn, som för det mesta är din full e-postadress
- Lösenord: ditt lösenord för ditt e-postkonto
- SSL: beroende på din e-postleverantörs inställningar kan den vara på eller av

  Fyll i för att se till att dina e-postmeddelanden skickas från SuperOffice Inbox:
- E-postserver: dina SMTP-serveruppgifter
- Användarnamn: ditt användarnamn, som för det mesta är din fulla e-postadress
- Lösenord: ditt lösenord för ditt e-postkonto
- SSL: beroende på din e-postleverantörs inställningar kan den vara på eller av

Klicka sedan på **Spara.**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6270381-Z0plDEeFMOzgyfJsbCe8sTkKAQn8fus1pEoXS72IE3QrsflRM8AMEPBn1PjfArzq-0/image-20250716091454-5.png)

**Notera!**

1. Om du arbetar med SuperOffice Onsite och porten måste anges för att få tillgång till e-postservern, använd en kolon ":" after the email server name till exempel.: "my.mail.server:80".
2. SuperOffice importerar automatiskt till databasen alla e-postmeddelanden som skapades under de senaste 30 dagarna om du arbetar på SuperOffice Online och sista 180 dagar om du arbetar på SuperOffice Onsite. Detta kan ändras i raden web. .config <Component> section <add key="NumberOfDaysToDownload"> line.Om du arbetar med SuperOffice Online, vänligen kontakta SuperOffice support.

Följ stegen nedan om du vill ändra ditt e-postkonto:

1. Klicka på ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149279-QFjr0CpM1anqnYd8cOdxDeKAJCb9FJlslch51YHNemAsxJEbu6uwDuk1P4W9syzH-0/image-20250327154847-8.png) och välj **Alternativ för e-post.**
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6527918-foP6hXmDfCLFRkrywtLsjY8xj0yGBc9ftoYN3eL8DTGLkUeFylPGf43LMzt7E4Es-0/image-20260210074905-6.png)
2. Välj **E-post konto** (1) och klicka på knappen **Redigera/ta bort**(2) och sedan klicka på **OK** för att slutföra.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6527919-tPyw8b2IGgxD5x5It3K36WyGESLQEaEQEaiqcq9NR6BNUCnGwTiO1of1QQwpG80q-0/image-20260210075001-7.png)

Mer information:

[Hur ställer jag in mitt Office 365-e-postkonto med SuperOffice Inbox?](https://community.superoffice.com/sv/support-faqs/faq/how-to-set-up-my-office-365-email-account-withsuperofficeinbox/)
[Konfigurera inkorgen i SuperOffice | SuperOffice Docs](https://docs.superoffice.com/sv/email/inbox/learn/setup.html)
