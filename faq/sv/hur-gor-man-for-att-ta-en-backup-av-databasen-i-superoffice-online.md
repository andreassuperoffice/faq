---
title: "Hur gör man för att ta en backup av databasen i SuperOffice Online?"
url: https://community.superoffice.com/sv/support-faqs/faq/hur-gor-man-for-att-ta-en-backup-av-databasen-i-superoffice-online/
lang: sv
updated: "24. aug. 2026"
---

# Hur gör man för att ta en backup av databasen i SuperOffice Online?

Uppdaterad på 24. aug. 2026

Hur gör man för att ta en backup av databasen i SuperOffice Online?

Följ proceduren som beskrivs nedan för att få en säkerhetskopia av din databas och / eller dokument och / eller dokumentmallar:

1. Skicka in ett ärende till [SuperOffice Support](https://cs.superoffice.com/) och be om att få en säkerhetskopia. FAQ: [Hur registrerar jag en supportbegäran inom SuperOffice CRM?](https://community.superoffice.com/sv/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/)
2. SuperOffice support kommer att informera dig om när din nyskapade backup är redo att laddas ner.
3. Följ instruktionerna i avsnittet som är relevant för ditt fall:

- [Om du vill ladda ner både databasen och dokumentarkivet använder du verktyget Download tool.](https://community.superoffice.com/sv/support-faqs/faq/hur-gor-man-for-att-ta-en-backup-av-databasen-i-superoffice-online/#1)
- [Om du bara behöver ladda ner databasen, använd Operational Center](https://community.superoffice.com/sv/support-faqs/faq/hur-gor-man-for-att-ta-en-backup-av-databasen-i-superoffice-online/#2)
- [Om du behöver mer information om hur man arbetar med databasen i .sdb-format](https://community.superoffice.com/sv/support-faqs/faq/hur-gor-man-for-att-ta-en-backup-av-databasen-i-superoffice-online/#3)

**Du vill ladda ner både databasen och dokumentarkiven med Download tool**

1. Klicka på följande länk för att ladda ner ett nedladdningsverktyg: **<https://online.superoffice.com/Download/Tool>**
2. Dubbelklicka på filen och klicka sedan på knappen Logga in.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6621756-EqLX60z5h9k4wXzpLp9xhATnNoOFs7EhE1KzjbljDIyHiFHKOIEngLYZ4Piahq6u-0/image-20260409120834-1.png)
3. Detta kommer att öppna dialogrutan för inloggning i en webbläsare. Logga in med dina SuperOffice-inloggningsuppgifter och välj installation. Du kommer att få ett bekräftelsemeddelande om inloggningen lyckas.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6185017-mP3YPBb7uini8Rxs4XpascgRbjtUYZPG41xG5Coyh5aW6yYwnWs0QSL8iQfXhS2B-0/image-20250425111101-2.png)
4. Välj säkerhetskopian (1) i listrutan, markera **Databas** (2) om du vill ladda ner den, markera **Fil** (3) om du vill ladda ner den, välj plats där säkerhetskopierings- och dokumentfiler ska lagras (4) och klicka på knappen **Ladda ner** (5).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622231-0APEXArgKDXUuydB6qDzGmCEGLaYS2Y4uH3szIMR3RYhg9LZbbAhrP6p2r2w5IuY-0/image-20260409142455-2.png)
5. Dokumentarkivet kommer att laddas ner i två filer:

   "Filer 1.zip"

   **Notera!** Dokumenten som finns i mappen "Filer 1.zip" är inte tillgängliga via SuperOffice CRM-gränssnittet.

   "Filer 2"

   Databassäkerhetskopian laddas ner i .sdb-format. Om du behöver mer information om hur man arbetar med databasen i .sdb-format, gå till [det avsnittet](https://community.superoffice.com/sv/support-faqs/faq/hur-gor-man-for-att-ta-en-backup-av-databasen-i-superoffice-online/#3).
6. Klicka på länken **här** (1) i popup-dialogrutan för att komma åt filerna och klicka sedan på **Färdig** (2) för att stänga nedladdningsverktyget.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622232-NUyuW3AU54chG6pzUn2sFiPOSoxdWt2H4u2meluJy84819qsQh8Ao48dA59cUQnl-0/image-20260409142613-3.png)

**Om du laddar ner databasen från Operational Center**

1. Din SuperOffice-administratör har åtkomst till **<https://online.superoffice.com/OC2/>** och kan logga in med sitt SuperOffice-användarnamn och lösenord.
2. I Operational Center klickar du på avsnittet**Säkerhetskopiera/Återställ**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622305-I5O3d605fMEUFipYQs8LAmrxPw52tsNNgeKLiFF5gLwwfdZKqKPEBfE7ie3Gp8BQ-0/image-20260409144636-6.png)
3. Klicka sedan bara på databasikonen för att ladda ner databasen.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622304-HcuXfSRjYDaoF7PfWFlYyknwJhzRI7LFDsUBKjQTKjZdq3wS5xkJn6HC26zcmZGU-0/image-20260409144548-5.png)

**Hur man arbetar med databasen i .sdb-format**

SDB-filer är gzip-komprimerade binära databassnapshots som exporterats från en SuperOffice CRM-databas. För att öppna databasen behöver du skriva över en befintlig databas på SQL Server.

Vi rekommenderar att du skapar en ny databas med en ODBC-anslutning ([Create Microsoft SQL Server | SuperOffice Docs](https://docs.superoffice.com/en/onsite/install/database/create-ms-sql-server-db.html)), som du sedan skriver över under databasimporten, till exempel SOimport.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6631704-MspYXWKdwHctSNpejctomLWMKeK6B0ZgTP0knK3ZRNR65lITQd150rzSWJ8rmOzs-0/image-20260415145841-1.png)

Du kan ladda ner CRMSetup [här](https://online3.superoffice.com/Cust1990/CS/scripts/rms.fcgi/getAttachment/6626597-upc6SP1k8aZZH6CltOUjkbIXj0PhlEWw2MAfb9lMLf0wattzfrkMSLwNUzCOmYYo-0/CrmSetup.zip).

Den här zippade mappen innehåller 3 filer:

- CrmSetup.exe
- Options advanced import.txt
- arg-file DBimport.txt

Här visar vi hur man importerar hela databasen med den medföljande importfilen arg-file DBimport.txt.

För mer avancerade importer, se Options advanced import.txt i den nedladdade mappen och läs mer om CrmSetup här: [CrmSetup and CrmTask utilities | SuperOffice Docs](https://docs.superoffice.com/en/onsite/install/database/crmsetup-and-crmtask.html).

Fyll i importfilen så här. De värden som är markerade med rött ska ersättas enligt den databas du vill ersätta:

*import-database*

*--database-server SQL server name*

*--database-name DBname*

*--db-user dbusername*

*--db-password dbpassword*

*--table-prefix prefix*

*--source-file pathtofile.sdb*

Exempel: Importfilen arg-file DBimport.txt skapades. Backup-filen placerades på C-disken, så sökvägen är C:\database.sdb.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6631720-iIN0xCUM7iklmAHLMUfC7QfH5AXWKQyYxffxXkfWsFYzD0BZsFYlyLpMdZATrLC1-0/image-20260415150149-2.png)

När du har en .sdb-fil, en CrmSetup.exe-fil och importfilen, kör du CMD.EXE som administratör och kör kommandot för att importera databasen. I princip pekar du ut importfilen:

 crmsetup --arg-file DBimport.txt

I skärmbilden nedan kan du se att alla 3 filer är placerade på C: disken.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6631721-5erOAzB0SAhQCEkhRZE9nH3ASZixRMcsXBSrcluiEf2QYI7riPdjapHyngMJ3OpA-0/image-20260415150227-3.png)

**Obs!** Kommandot import-database i CrmSetup kommer att ta bort alla befintliga SuperOffice-tabeller i måldatabasen och ersätta dem med data från SDB-filen.

**Mer information**

SuperOffice CRM bygger på två typer av datalagring: Databas och Dokumentarkiv.

- Databasreferenser: [Database table listing | SuperOffice Docs](https://docs.superoffice.com/en/database/tables/index.html)
- Mappen SO\_Arc innehåller dokumentarkivet. Filer lagras i en struktur baserad på: skaparnas användar-ID, året och halvåret då dokumentet skapades. Filnamn genereras automatiskt med hjälp av företagsnamnet och malltypen.
- Data i Microsoft SQL Server-databasen är separerad för varje kund. Alla databaser har en 30-dagars backup av typen “point in time”. Det betyder att en återställning kan göras från ett specifikt datum/klockslag inom de senaste 30 dagarna. Dessutom tas en månadsbackup som sparas i 12 månader. En årsbackup sparas i 10 år.
- Alla Document Archives har kontinuerlig spegling mellan två fysiskt separerade datacenter och har individuella säkerhetskopior på båda platserna. Backup körs en gång per dag, vanligtvis på natten. Dokumentändringar säkerhetskopieras och sparas i 30 dagar. Backup av raderade filer (dokument) sparas i 90 dagar.
