---
title: "Vad ska jag göra när mina skickade utskick studsar i SuperOffice Online eller om jag får många studsmeddelanden i SuperOffice Service?"
url: https://community.superoffice.com/sv/support-faqs/faq/vad-ska-jag-gora-nar-mina-skickade-utskick-studsar-i-superoffice-online-eller-om-jag-far-manga-studsmeddelanden-i-superoffice-service/
lang: sv
updated: "13. mars 2025"
---

# Vad ska jag göra när mina skickade utskick studsar i SuperOffice Online eller om jag får många studsmeddelanden i SuperOffice Service?

Uppdaterad på 13. mars 2025

Efter att ha skickat ett utskick från SuperOffice CRM Online märkte jag att många mottagare av min utskick har status "Returnerat". Samtidigt märkte jag problem i SuperOffice Service. De flesta e-postmeddelanden som vi skickar genererar ett studssmeddelande och våra svar når inte våra kunder.

Varför händer det och hur fixar jag det?

Varje CRM Online-kund som har tillgång till marknadsförings- och servicemoduler får sändningstjänsten som tillhandahålls av MailGun och får ett e-postkonto för SuperOffice Service i form av "customer@domain.suocrm.XX" (.eu eller .com) .

Ofta använder kunder dock sina egna e-postadresser för att skicka e-post (utskick eller svar på förfrågningarna i Service). Om så är fallet kan mottagarens e-postserver identifiera dessa meddelanden som skräppost, eftersom avsändarens e-postadressdomän skiljer sig från den faktiska e-postadressdomänen (tillhandahållen av SuperOffice) som skickar e-postmeddelandet.

Till exempel, om du i SuperOffice-Marknadsföring i fältet "Från" använder din e-postadress eller i SuperOffice Service inställningar använder din e-post som standard "från adress", då ser mottagarens e-postserver att utskick eller e-post meddelandet skickas från "e-mail@customer.suocrm.com" -domänen, men "från" -adressen är annorlunda, dvs. det innehåller ett annat domännamn. Detta kan orsaka att ditt meddelande identifieras som skräppost och därför avvisar e-postmeddelandena.
![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6127206-Gd2odn9Ka5p0llztMAXrBTZUkNtOJ9epyNlaahHKIemHBhpZzDoOW9ZYD2J7qUXI-0/image-20250313153818-1.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6127207-MGTKIZbQfM8ixzD8gQhI3bDnEfJjPthljR2Fi73tNRbxLXx0Bq1Cl4SHppciMGZL-0/image-20250313153837-2.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6127208-y1cby26OX4mKoN7jLiRBTf7C7TJ7GXPYKMKjHcd3Ssio871uzdtHqtyYXbl6lEI1-0/image-20250313153915-3.png)

För att säkerställa att situationen ovan inte påverkar dina meddelanden föreslår vi att du skapar en post som tillåter SuperOffice Online MailGun-tjänsten att skicka meddelanden för er domän. Detta görs med SPF-poster.

Du måste skapa en post i DNS för din domän "@ [dindomän] .com" som anger att SuperOffice SMTP-server är en pålitlig avsändare för "@ [dindomän] .com".

TXT-posten som ska läggas till är "v=spf1 include:\_spf.online.superoffice.com ~ all".

**Notera!** Detta bör göras av er IT-ansvarige, din e-postserveradministratör eller någon som administrerar DNS för din domän.

**Mer information:**

Docs: [Set up SPF](https://docs.superoffice.com/email/mailgun/spf/set-up.html)
