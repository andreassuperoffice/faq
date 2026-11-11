---
title: "Hur exporterar jag data från SuperOffice CRM?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-exporterar-jag-data-fran-superoffice-crm/
lang: sv
updated: "26. mars 2026"
---

# Hur exporterar jag data från SuperOffice CRM?

Uppdaterad på 26. mars 2026

När jag vill exportera data från **SuperOffice CRM**, vilka alternativ har jag?

Det finns tre sätt att exportera data från SuperOffice CRM:

- [Exportera från Sektionsfliken eller från ett urval till en Excel-fil](https://community.superoffice.com/sv/support-faqs/faq/hur-exporterar-jag-data-fran-superoffice-crm/#1)
- [Exportera från Urval till en textfil](https://community.superoffice.com/sv/support-faqs/faq/hur-exporterar-jag-data-fran-superoffice-crm/#2)
- [Exportera all CRM-data till en .bak eller .sdb databasfil](https://community.superoffice.com/sv/support-faqs/faq/hur-exporterar-jag-data-fran-superoffice-crm/#3)

**Exportera från Sektionsfliken eller från ett urval till en Excel-fil**

I SuperOffice CRM, under **Företagskortet (huvudkortet)** samt i **Minikortet**, kan du se en **Sektionsflik (1)**. Sektionsfliken kan till exempel innehålla listor med kontakter, projektmedlemmar, försäljningar och aktiviteter som är kopplade till den relevanta posten på huvudkortet.

När knappen **Export (2)** är aktiverad (se noteringen nedan för hur du aktiverar den) visas den längst ner till vänster i avsnittet. Detta gör det möjligt att exportera data från sektionsfliken till en **Excel-fil**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471181-loEjCU11WbRii7edL4bu6BLuJ0DAg3YwG0kHB9UuTCjMJjGHslZBTMSrD3tlcXRp-0/image-20260106142611-2.png)

Du kan exportera data till ett Excel-ark i **Urval (1)**. Klicka bara på knappen **Uppgift (2)** för att hitta alternativet **Exportera till Excel (3)**.
![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471192-IMXDDrd5tRJZ8dIbOxD5Dmyi8ZS2uhxxyRd41hFAoZH2um0cC9l2qCKsn4AaejQq-0/image-20260106143639-3.png)

**Observera!** Om du saknar data i den exporterade filen beror det på att kolumnen med denna information inte var inställd i **Sektionsfliken** före exporten.
Du kan konfigurera kolumner genom att klicka på **inställningshjulet** och därefter välja relevanta kolumner.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471201-qWtjBIoEXbL1qQaacLWy20mR3qEdxwxtTMsNQBgOjsnwSU4sbqHluinMlgkk8OcJ-0/image-20260106143921-4.png)

**Exportera från ett urval till en textfil**

När du behöver utföra **regelbundna, fördefinierade dataexporter** är export till fil ett bra alternativ. Du kan fördefiniera exportfilens format i en mall och återanvända den. Du kan skapa hur många mallar som helst, till exempel för företag, kontakter, aktiviteter, försäljningar osv.

Följ stegen nedan för att lära dig hur du exporterar data till en **avgränsad textfil**:

**1.** **Skapa en SXF-mall i Excel.**

Fyll i SuperOffice-variabler i fälten på första raden med hjälp av vinkelparenteser `<>`.
Till exempel används `<cpho>` för företagets telefonnummer. Du kan lägga till så många variabler du vill.
Spara filen som en **tabbavgränsad TXT-fil**. Efter att filen har sparats, ändra filändelsen till **.sxf**.
Klicka [här](https://docs.superoffice.com/en/document/templates/learn/template-variables.html) för att få en lista över alla SuperOffice-variabler.

2. **Ladda upp mallen i Inställningar & Underhåll** under **Dokumentmallar**.

Mallen måste lagras i **online**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471248-pFwfC1QSf9LbfjUQS3Lk91fdw3oUEkgOUaGzRCtcZLpxW7inFftrHIAX7Yx1nE9m-0/image-20260106150000-5.png)

3. **Öppna ditt urval (1)**, klicka på knappen **Uppgift (2)** och välj därefter alternativet **Exportera till fil (3)**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471343-7jeIrUmwl7Ki81JX6ptMiO2WKywEBcJDXdMK5Ioz71uZZkCk5zk3b7WCcD6DwuLx-0/image-20260106152225-6.png)

**4.** **Välj exportfilen** i rullgardinsmenyn och klicka på **Skapa** för att exportera data.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471345-fPg88H8uDboAN0KQFmisxCAr8xepwPzTouy1atkhKY0LALEZpoZ2YaDgqT7bHoJh-0/image-20260106152356-7.png)

5. **En .txt-fil laddas ner**, som du vid behov kan öppna i Excel.

**Exportera all CRM-data till en .bak eller .sdb databasfil.**

### Observera!

1. För att kunna exportera data till **Excel** eller till en **textfil** måste SuperOffice-användaren ha en roll som inkluderar den funktionella rättigheten **”Kan exportera data till fil”**.

Gör så här: Gå till [**Inställningar och underhåll**](https://community.superoffice.com/sv/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/) och klicka på **Roller (1)**. Välj den roll som din SuperOffice-användare har i rollistan **(2)**. Klicka på fliken **Funktionella rättigheter (3)**. Säkerställ att den funktionella rättigheten **Kan exportera urval till fil (4)** finns i kolumnen till höger.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471431-GQuZumrf4Hw9WBRxGNiAhgHDNUrw6MAucs5H5jT8O5hhPkz7juIbtrPGoP1guYrF-0/image-20260106154107-9.png)

2. För att kunna se **Export-knappen** i **Sektionsflikarna** måste SuperOffice CRM-användaren ha en inställning (preferens) som aktiverar detta. Den kan aktiveras som **personlig preferens** eller **systempreferens**.

Gör så här i [**Inställningar och underhåll**](https://community.superoffice.com/sv/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/): Klicka på **Inställningar (Preferences) (1)**. Välj **Funktioner (Functions) (2)** i rullgardinsmenyn. Välj preferensen **Visa Export-knapp i sektionsflikarna (Show Export button in the section tabs) (3)**. Klicka på **+ Lägg till (4)**. Ange preferensen för **användare, grupp eller hela systemet (5)**. Spara inställningen genom att klicka på **Spara (6)**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471437-m8esyXQuKEoUIfOmEjSwPUyDf25uKFOZmA2DQPS8aGkuxPmMp0nLxapzgecnbAS2-0/image-20260106154805-11.png)

**Mer information**

**Blogg:** [Exportera data från SuperOffice som XML med hjälp av SQL](https://community.superoffice.com/sv/technical/blogs/archive/exporting-data-from-superoffice-as-xml-using-sql/)

**SuperOffice App Store:** [DataBridge för SuperOffice](https://appstore.superoffice.com/infobridge-software-b-v-/databridge-for-superoffice)
