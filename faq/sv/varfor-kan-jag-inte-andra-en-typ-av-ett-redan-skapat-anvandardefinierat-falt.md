---
title: "Varför kan jag inte ändra en typ av ett redan skapat användardefinierat fält?"
url: https://community.superoffice.com/sv/support-faqs/faq/varfor-kan-jag-inte-andra-en-typ-av-ett-redan-skapat-anvandardefinierat-falt/
lang: sv
updated: "30. dec. 2025"
---

# Varför kan jag inte ändra en typ av ett redan skapat användardefinierat fält?

Uppdaterad på 30. dec. 2025

Jag har skapat ett användardefinierat fält av typen Kort text och jag skulle vilja ändra det till Lång text, men jag ser inte det här alternativet i rullistan. Varför händer detta och hur åtgärdar jag det?
![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466527-LfJRdUQJ6dYQYOSITYLi5geUPjNd6ShttelRlSdCwRCrys9zFDuZU5ahNWxUO74E-0/image-20251230103613-1.png)

Det är inte alltid möjligt att ändra typen på ett användardefinierat fält till vilken annan fälttyp som helst. Olika typer av värden för användardefinierade fält lagras i olika tabeller i databasen, och därför är inte alla konverteringar möjliga.

I SuperOffice finns det åtta olika typer av användardefinierade fält: Nummer, Kort text, Lång text, Datum, Obegränsat datum, Kryssruta, Lista och Decimal.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466539-w754Yz2mdYpgpfIaXDXpTNzTEqiK2MRGz0o9P02srFrdO29jgH47c7BLp28FSsTR-0/image-20251230104027-2.png)

Fälttyp **Nummer** kan ändras till kort text och decimal

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466541-TZca53X7wXBRm8JqjuyWhc5SHqTc453SjjiuycPLbXO42lIEcEZOUQ0PzRRPjPut-0/image-20251230104109-3.png)

Fälttyp **Lång text** kan inte ändras till någon annan fälttyp.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466542-S3idJID1pNO2aQurd8m584eYdCtX7DCflon4osoXUSysYNmpFwj8ErbrEd2SYnFE-0/image-20251230104136-4.png)

Fälttyp **Lista** kan ändras till **Kort text**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466543-5PiHZDdSJiScZaQSWieMMMHoh0ewqEkS2cZQBwxCQ5RqjM4WdHHh6ekph1uTtQST-0/image-20251230104206-5.png)

Fälttyp **Kort text** kan ändras till **Nummer**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466544-FFGFIXiPzIuFJ0PtmMg2fY4fg2hut6PtRJscE9Z3NW8JysOcGhEDYNrtnSxRBL8i-0/image-20251230104233-6.png)

Fälttyp **Datum** kan ändras till **Kort** text och **Obegränsat datum**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466546-WacQmgRMF7FBwKrjsMTBAcISNbbONgxc4eL0UEHSYUpyWXNBoc4me1cJAiJokjJM-0/image-20251230104403-7.png)

Fälttyp **Obegränsat datum** kan ändras till **Kort text.**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466549-a8TcgPI4ndR7hYglZO704u8tMFZ2caRncoXS911RRP2kmXRwhEamJPBTk7zgWR4Z-0/image-20251230104506-8.png)

Fälttyp **Checkruta**kan ändras till **Kort text.**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466558-CzooDqUzJzl7eg4cJlWQ3Gp8SLwJGR5P7eqmRjbrxelTxqufuDiaYxgLqdBguO7N-0/image-20251230104617-9.png)

Fälttyp **Decimal** kan ändras till **kort text** och **nummer**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6466559-2EXkAaPOWSSdSWp1h4JJ0LyKw2BeT694ixXxXZ0nMa46Imgdhb56W4Csaq843PFu-0/image-20251230104646-10.png)

**Mer information**

FAQ: [What is the maximum number of user defined fields which can be used?](https://community.superoffice.com/sv/support-faqs/faq/how-do-i-know-what-isthe-maximum-number-of-user-defined-fields-that-i-can-createin-superoffice-crm/)
