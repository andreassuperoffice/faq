---
title: "Hur lägger jag till SuperOffice chat widget till min hemsida?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-lagger-jag-till-superoffice-chat-widget-till-min-hemsida/
lang: sv
updated: "28. mars 2022"
---

# Hur lägger jag till SuperOffice chat widget till min hemsida?

Uppdaterad på 28. mars 2022

Hur lägger jag till SuperOffice Chat widget till min hemsida?

För att lägga till SuperOffice Chat Widget till din hemsida, är det dessa två steg du behöver följa:

[1. Konfigurera SuperOffice Chat kanalen.](https://community.superoffice.com/sv/support-faqs/faq/hur-lagger-jag-till-superoffice-chat-widget-till-min-hemsida/#1)

[2. Lägga till JavaScriptet till din hemsidas Content Management system.](https://community.superoffice.com/sv/support-faqs/faq/hur-lagger-jag-till-superoffice-chat-widget-till-min-hemsida/#2)

​

**Steg 1. Konfigurera SuperOffice Chat-kanal**

1. Logga in på [Inställningar och underhåll](https://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=110849).
2. Välj **Chat (1)** till vänster i menyn, skapa sedan en [chattkanal](https://help.superoffice.com/Documentation/Help/SE/CRM/10.0/UserHelp/index.htm#t=Chat%2Fchat_admin%2Fchat_channel_create.htm&rhsearch=chat%20channel&rhhlterm=chat%20channel&rhsyns=%20) eller välj den som har skapats tidigare (2) och klicka på **View (3)**. Detta genererar skriptkoden som du ska kopiera och spara.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4397560-a2W4R8HpCHO0jKRex1FKa1w6kTdDftsrIkexkweZZAnelassdcGeRYdOTKptR5EI-0/image.png)

​

**Steg 2. L****ägg till JavaScriptet till din hemsidas Content Management System.**

I denna FAQ kommer vi använda WordPress som ett exempel, men stegen är liknande för andra content management system som Joomla, Weebly, Drupal, Episerver, Shopify, PrestaShop etc.

1. Logga in till administration panelen och gå till delen där du kan redigera eller lägga till HTML kod. I WordPress klickar du på **Appearance** and **Editor** sections.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4397543-nyM1Ea31GnQqOLMSdJxXcsif2jT3y6AawnUHrKj81E3GuU6MLIuO0nTTJBG5rc7g-0/image.png)
2. Lägg till JavaScriptet till din hemsidas header, om du vill att chatt widgeten ska synas på alla sidor. Om du endast vill att chatten ska synas på vissa sidor, lägg till JavaScriptet enbart i header för valda sidor. När du är färdig med att redigera din hemsidas kod tryck **Update file**.

   **OBS!** DEFER parametern säkerställer att detta skript inte blockerar hemsidan för att ladda. Skriptet kommer laddas efter hemsidan laddats klart.
3. Öppna din hemsida eller uppdatera hemsidan om du redan har den öppen. SuperOffice Chatt widget är nu tillgänglig i det högra hörnet i botten på din hemsida, och redo att användas.

**Mer information:**

Video: [How to set up and configure the Chat widget in SuperOffice CRM 9](https://www.youtube.com/watch?v=94uhmeP1Xig&list=PL9fefjwA0X290ZZ8bMUHWh_d6s3Y2P0Jr&index=7&ab_channel=SuperOfficeNetwork)

Video: [How to add the Chat widget to your website in SuperOffice CRM 8](https://www.youtube.com/watch?v=SSPtfPFPnUE)

Users Guide: [How to get started with SuperOffice Chat](https://community.superoffice.com/sv/learning/user-guide/chat/)

FAQ: [How do I brand my chat widget layout?](https://online2.superoffice.com/Cust1990/CS/scripts/blogic.fcgi?_sf=0&action=doScreenDefinition&idString=viewFaq&entryId=113097)

Forum: [Publish SuperOffice Chat through Google Tag Manager](https://community.superoffice.com/sv/technical/forums/api-forums/service-crmscript/the-chat-module-and-google-tag-manager-gives-an-error/)
