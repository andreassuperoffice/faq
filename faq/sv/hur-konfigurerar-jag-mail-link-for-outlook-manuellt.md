---
title: "Hur konfigurerar jag Mail Link för Outlook manuellt?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-konfigurerar-jag-mail-link-for-outlook-manuellt/
lang: sv
updated: "30. juli 2026"
---

# Hur konfigurerar jag Mail Link för Outlook manuellt?

Uppdaterad på 30. juli 2026

Jag kan inte arkivera eller klicka på Inkorgen i SuperOffice och få Outlook-applikationen att öppnas. Jag har WebTools och MailLink installerat. Varför händer detta och hur kan jag åtgärda det?

Om du har upplevt förändringar i din datormiljö (t.ex. uppdateringar av operativsystem eller webbläsare, ny webbläsare, ny dator osv.) kan detta leda till att MailLink-konfigurationen går förlorad.

Kontrollera först att både MS Office (Outlook) och SuperOffice WebTools är installerade lokalt på datorn. Du hittar båda programmen under Kontrollpanelen - Program och funktioner.

Om både WebTools och Outlook är installerade kan du konfigurera MailLink manuellt genom att följa dessa två steg:

[1. Konfigurera i SuperOffice CRM](https://community.superoffice.com/sv/support-faqs/faq/hur-konfigurerar-jag-mail-link-for-outlook-manuellt/#1)

[2. Konfigurera i Outlook](https://community.superoffice.com/sv/support-faqs/faq/hur-konfigurerar-jag-mail-link-for-outlook-manuellt/#2)

**Steg 1: Konfigurera i SuperOffice CRM**

1. Klicka på ikonen **Personliga inställningar** högst upp till höger på skärmen och välj **Lokala inställningar** i dropdown-menyn.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6798780-uNo61yEqxytieeliDXt3ILwA6jl2d9NwLnpiU1Q0aWnQBqlW2NqiF6e1pgkwwa85-0/image-20260730131713-2.png)
2. Välj **Microsoft Outlook** som e-postklient och tryck på **OK**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6468816-q5celegT1T8N3mPJBrzpMg2SKM1342XrCl45qDrNuxDNfG2iaRs3OzDF2aw8q6Zq-0/image-20260105133129-2.png)

   **Obs!** Kontrollera att SuperOffice WebTools är installerat på datorn genom att gå till Kontrollpanelen - Program och funktioner. Om det inte är installerat måste du **[installera WebTools först](https://community.superoffice.com/en/support-faqs/faq/how-do-i-download-and-install-webtools-for-superoffice-crm/)**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6798901-ZIcrDjFx3yJMjU55C0spCi3a0qxufkePCoujSFnpwu9sHk25TuLi7g0chLL0CNT0-0/image-20260730140641-1.png)

**Steg 2: Konfigurera i Outlook**

1. Klicka på **SuperOffice-pilen** i **SuperOffice-fliken** som finns i Outlook-menyn.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6468834-mr1MDrIC6OllURJ8lTrGuCOmcx45mJow1foY0KHCP1ck5MCQME4N0s1QneLpuWRY-0/image-20260105133559-7.png)
2. Under **Allmänna inställningar**, klicka på pilen ![](http://content.screencast.com/users/mrfrodeberntsen/folders/Snagit/media/7fe83d1d-68c9-4fb9-8fe3-206f687c01da/03.26.2013-09.47.png) . Bredvid **Advanced settings**, och i fältet **URL för SuperOffice CRM**, kopiera din **SuperOffice CRM-URL-adress**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6798882-P71UggU6Edq94LKCSyaaOyIY5iifSOCfiWf2hIKLFBGj74w6erWH4fnI306TQ6Pi-0/image-20260730135940-5.png)
3. I fältet **Användarnamn (1)** anger du ditt användarnamn och klickar på knappen **Testa anslutning (2)**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6798885-joJkpNDe7whPGWOSKLp5C7oPcf81AEwyYrQz1WZfHPEoWd4FRI43YSc0T1qtORPH-0/image-20260730140324-6.png)
4. Om du använder **SuperOffice Online** kommer du att bli ombedd att autentisera dig via webbläsaren. Klicka på **OK** för att fortsätta.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6468932-sDfzE1OTCbUNOcZ1Am4etuz0XBf3yKo1jbJCilBcpW4HPlXRXZJyufHPs3oTNJ5P-0/image-20260105135246-10.png)
5. Om du använder **SuperOffice Onsite**, ange ditt SuperOffice-användarnamn och lösenord i **MailLink-inloggningsdialogen** och klicka på **OK**.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3828724-CuJAmWa9y9gYItxPXb7CyWNWf3aeAw2FCdl1GTaL0ZI1TESmdCGm63FFb2LatfUp-0/image.png)
6. När du ser en dialogruta som bekräftar att anslutningen lyckades, klicka på **Stäng** och **OK** för att stänga de öppna fönstren.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6166308-ICdhA4qxyZ6isjs2E5I1uYH4t0d0N97Eb1dHThimUW3BmE9CipX5Dt7PUeaZWaj7-0/image-20250407201738-8.png)
7. Du kan bli ombedd att autentisera dig via webbläsaren igen. Klicka på **OK** och stäng sedan fönstret som öppnas i webbläsaren.

**Mer information**

FAQ: [Vad gör jag när SuperOffice Outlook-tillägget inte visas i Outlook?](https://community.superoffice.com/sv/support-faqs/faq/vad-gor-jag-nar-superoffice-outlook-tillagget-inte-visas-i-outlook/)

FAQ: [Hur laddar man ned och installerar WebTools SuperOffice CRM?](https://community.superoffice.com/sv/support-faqs/faq/hur-laddar-man-ned-och-installerar-webtools-superoffice-crm/)
