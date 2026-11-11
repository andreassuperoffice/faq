---
title: "Hur ominstallerar man SuperOffice WebTools?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-ominstallerar-man-superoffice-webtools/
lang: sv
updated: "24. juli 2026"
---

# Hur ominstallerar man SuperOffice WebTools?

Uppdaterad på 24. juli 2026

Jag har blivit rekommenderad att ominstallera WebTools. Hur gör jag?

Innan du börjar, kontrollera vilken del av SuperOffice WebTools du behöver installera om.

Använd denna FAQ om dokument från SuperOffice CRM inte öppnas, redigeras eller sparas korrekt. Denna FAQ förklarar hur du installerar om den del av SuperOffice WebTools som används för dokumenthantering på Windows och Mac.

Observera att du endast ska avinstallera det program som du har för avsikt att installera om. Avinstallera inte MailLink som en del av denna process, om detta inte uttryckligen har rekommenderats av din IT-avdelning eller SuperOffice Support.

Vänligen följ dessa instruktioner för att ominstallera SuperOffice WebTools.

- Om du använder Windows kan du [klicka här.](https://community.superoffice.com/sv/support-faqs/faq/hur-ominstallerar-man-superoffice-webtools/#1)
- Om du använder Mac kan du [klicka här.](https://community.superoffice.com/sv/support-faqs/faq/hur-ominstallerar-man-superoffice-webtools/#2)

**Ominstallera SuperOffice WebTools när man har Windows som operativsystem.**

1. Först så behöver du stänga av SuperOffice.
2. Du behöver avinstallera de befintliga komponenterna som är relaterade till **SuperOffice** **WebTools**. För att göra detta, öppna listan över installerade program på din dator. Du kan komma åt den på två sätt – via **Appar och funktioner** eller **Program och funktioner**. Se [denna artikel](http://support.microsoft.com/en-us/help/4028054/windows-10-repair-or-remove-programs) för mer information om hur du hittar **Appar och funktioner** eller **Program och funktioner**.

   I den här guiden använder vi **Program och funktioner**
3. Leta sedan upp **SuperOffice Web Extensions**(1) listan av program, markera det och välj **avinstallera** (2).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793206-bM2c3zS508yiQF7Wh7qwTDCNJtjYeUAjAaJWZ2AMrl7nJPbhPLDYT2UyTuRZQ15k-0/image-20260724082442-4.png)
4. För att säkerställa att alla WebTools inställningar är borttagna efter avinstallationen så ta bort mappen **TrayApp**(2) i **AppData Roaming** (1) och mappen  **SuperOffice 7 Web Extensions**(4)i **Appdata Local**(3).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793205-AaAtPouPUwFIZO4CPoIQh8tRuTlWQeCAysurzJP88LQuwjwS9y4JCNe0mTP6NBDJ-0/image-20260724082427-3.png)

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793208-sEWFCZfhP9WPBbc4oqNCxj8Qw6kGCAjcX4hjFD6nn3CmhBDqF2YDcaMFUOM9ih2K-0/image-20260724082505-5.png)
5. För att installera SuperOffice WebTools igen så kan du följa [denna FAQ](https://community.superoffice.com/sv/support-faqs/faq/hur-laddar-man-ned-och-installerar-webtools-superoffice-crm/).

**Notera!**

Denna FAQ förklarar hur du installerar om SuperOffice Web Extensions.

I sällsynta fall kan Windows-användare bli ombedda att installera om MailLink. Detta ska endast göras om det uttryckligen har rekommenderats av din IT-avdelning eller SuperOffice Support.

Om du behöver installera om MailLink ska du ta bort SuperOffice MailLink från Program och funktioner och även ta bort mappen MailLink från mappen AppData Roaming. Därefter kan du ladda ner och installera det separat från [SuperOffice Download Service](https://downloadservice.superoffice.com/).

För mer information, läs FAQ: [Why is MailLink not installed when I download WebTools?](https://community.superoffice.com/en/support-faqs/faq/why-is-maillink-not-installed-when-i-download-webtools/)

**Ominstallera SuperOffice Webtools när man använder Mac operativ.**

1. Stäng ner SuperOffice CRM, Outlook, och WebTools. För att stänga av WebTools så kan du högerklicka SuperOffice ikonen i din tray och välja **Quit/Avsluta**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793209-BHgCDfjDwCOMpJWYFbjjpQRu6jwLkrPD0cxeiznGIShza9QpKC1ryz4FsUGcpgix-0/image-20260724082531-6.png)
2. Öppna Finder och välj Program.
3. Hitta alla filer som har namn SuperOffice WebTools. Högerklicka på dessa och tryck på Move to bin.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6793210-SxYfcMCxpWyYQh6lksdM37Ef5Qsc3T2ywRe3k2usbuB3UeiRW0e6Il8hyOih93U8-0/image-20260724082546-7.png)
4. Följ denna instruktion för att [this FAQ](https://community.superoffice.com/sv/support-faqs/faq/hur-laddar-man-ned-och-installerar-webtools-superoffice-crm/) WebTools igen.

**Notera!** Om har blivit rekommenderad att installera den senaste versionen av WebTools så hittar du programmet här: [SuperOffice Download Service](https://downloadservice.superoffice.com/)

**Ytterligare information**

FAQ:[What to do when I get an error "Installation failed" while installing SuperOffice WebTools or MailLink applications?](https://community.superoffice.com/sv/support-faqs/faq/what-to-do-when-i-get-an-error-installation-failed-while-installing-superoffice-webtools-or-maillink-applications/)
