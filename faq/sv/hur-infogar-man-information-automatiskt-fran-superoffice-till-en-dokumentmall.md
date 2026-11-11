---
title: "Hur infogar man information automatiskt från SuperOffice till en dokumentmall?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-infogar-man-information-automatiskt-fran-superoffice-till-en-dokumentmall/
lang: sv
updated: "6. jan. 2026"
---

# Hur infogar man information automatiskt från SuperOffice till en dokumentmall?

Uppdaterad på 6. jan. 2026

Hur använder jag mallvariabler för att automatiskt infoga information från SuperOffice i en dokumentmall?

För att kunna hämta information från SuperOffice CRM in i dokumenten, som du genererar från SuperOffice, måste du skapa en dokumentmall med mallvariabler. Vänligen se [denna FAQ](https://community.superoffice.com/sv/support-faqs/faq/how-do-i-use-superoffice-crm-template-variables-to-automatically-insert-information-into-a-document/) för att lära dig hur du skapar en ny dokumentmall. För att hitta en lista med alla mallvariabler som kan användas i dokument, kolla [denna hjälpfil](https://docs.superoffice.com/en/document/templates/learn/template-variables.html).

För att du ska lyckas när du skapar och använder dokumentmallar med variabler vill vi dela med dig några tips:

1. När du skriver in en mallvariabel i det nya dokumentet rekommenderar vi att börja med att skapa parenteser {} och sedan infoga en variabeltext i parenteserna. Skriv variabeln för hand eller klistra in den oformaterad.
2. När du vill att din dokumentmall ska infoga information från fält som du skapat själv i SuperOffice CRM, måste du först hitta ett variabelnamn.

   För att hitta variabeln öppna [Inställningar och underhåll](http://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=10106), klicka sedan på **Fält** (1) och välj fliken där fältet skapades (2). Hitta sedan fältnamnet i listan (3) och dubbelklicka för att öppna det. Mallvaraiblen är längst ner i den rutan som öppnas.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471128-ABlEC54SR7msekahRH5jOqQxy1FqIINucMzjCeuiZRKSHE9igSRTfxYD4UrWOgGk-0/image-20260106140252-2.png)

Längst ner i dialogrutan hittar du mallvariabelns namn (4) för informationen lagrad i detta fält.
![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6471129-pRLCTrkPAhuqxReRrZg7WhpH4PZdxIOwoNqQH0jXpf4akjHzGjqKDUXsyP9LzgEj-0/image-20260106140420-3.png)

**Notera!**Om mallvariabeln av någon anledning inte fungerar, försök att ta bort den, spara dokumentet. Öppna sedan dokumentet och skriv in mallvariabeln igen.

**Mer information**

Video: [How to edit a document template in SuperOffice](https://www.youtube.com/watch?v=FnhcmjP-TgE&ab_channel=SuperOfficeNetwork)

Docs: [Document templates troubleshooting](https://docs.superoffice.com/document/templates/troubleshooting.html)
