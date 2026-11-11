---
title: "Hvordan får jeg en kopi av SuperOffice Online-databasen?"
url: https://community.superoffice.com/no/support-faqs/faq/hvordan-far-jeg-en-kopi-av-superoffice-online-databasen/
lang: no
updated: "24. aug. 2026"
---

# Hvordan får jeg en kopi av SuperOffice Online-databasen?

Oppdatert på 24. aug. 2026

Hvordan får jeg en kopi av SuperOffice Online-database?

For å få en sikkerhetskopi av databasen og/eller dokumentene og/eller dokumentmalene, følg trinnene nedenfor:

1. Send en forespørsel til [SuperOffice Support](http://cs.superoffice.com/) og be dem om å få deres sikkerhetskopi. FAQ: [How do I register a support request within SuperOffice CRM?](https://community.superoffice.com/no/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/)
2. SuperOffice Support vil informere deg når kopien er klar til nedlasting.
3. Følg instruksjonene i seksjonen som er relevant for ditt tilfelle:

- [Hvis du vil laste ned både databasen og dokumentarkivet, bruker du nedlastingsverktøyet (Download tool)](https://community.superoffice.com/no/support-faqs/faq/hvordan-far-jeg-en-kopi-av-superoffice-online-databasen/#1)
- [Hvis du bare trenger å laste ned databasen, bruk Operational Center](https://community.superoffice.com/no/support-faqs/faq/hvordan-far-jeg-en-kopi-av-superoffice-online-databasen/#2)
- [Hvis du trenger mer informasjon om hvordan du arbeider med .sdb-databasefilen](https://community.superoffice.com/no/support-faqs/faq/hvordan-far-jeg-en-kopi-av-superoffice-online-databasen/#3)

**Du vil laste ned både databasen og dokumentarkivene med nedlastingsverktøyet**

1. Klikk på teksten "SuperOffice CRM Online download tool" for å laste den ned: <https://online.superoffice.com/Download/Tool>.
2. Dobbeltklikk på filen og klikk deretter på knappen Login.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6621756-EqLX60z5h9k4wXzpLp9xhATnNoOFs7EhE1KzjbljDIyHiFHKOIEngLYZ4Piahq6u-0/image-20260409120834-1.png)
3. Dette vil åpne påloggingsdialogen i en nettleser. Logg på med påloggingsinformasjonen din, og du vil få en bekreftelsesmelding hvis påloggingen er vellykket.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6185017-mP3YPBb7uini8Rxs4XpascgRbjtUYZPG41xG5Coyh5aW6yYwnWs0QSL8iQfXhS2B-0/image-20250425111101-2.png)
4. Gå tilbake til verktøyet. Fra rullegardinlisten velg backupen (1), trykk på  **Database** (2) hvis du vil laste ned databasen. Trykk på **Files**(3)hvis du vil laste ned filer/dokumenter. Velg området hvor backupen og dokumenter skal lagres (4) og trykk på **Download** (5).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622231-0APEXArgKDXUuydB6qDzGmCEGLaYS2Y4uH3szIMR3RYhg9LZbbAhrP6p2r2w5IuY-0/image-20260409142455-2.png)

   5. Dokumentarkivet lastes ned i to filer:

   • "Files 1.zip"

   **Merk!**Dokumentene som finnes i “Files 1.zip”-mappen er ikke tilgjengelige via SuperOffice CRM-grensesnittet.

   • "Files 2"

   Databasens sikkerhetskopi vil bli lastet ned som en fil i .sdb-format. Hvis du trenger mer informasjon om hvordan du arbeider med .sdb-databasefilen, gå til [denne seksjonen](https://community.superoffice.com/no/support-faqs/faq/hvordan-far-jeg-en-kopi-av-superoffice-online-databasen/#3).

   6. Trykk på **here** (1)og deretter **Finished** (2)**.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622232-NUyuW3AU54chG6pzUn2sFiPOSoxdWt2H4u2meluJy84819qsQh8Ao48dA59cUQnl-0/image-20260409142613-3.png)

**Hvis du laster ned databasen fra Operational Center**

1. SuperOffice-administratoren din må gå til <https://online.superoffice.com/OC2/> og logge inn med sitt SuperOffice-brukernavn og passord.
2. Deretter skal man trykke på **Backup/Restore:**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622305-I5O3d605fMEUFipYQs8LAmrxPw52tsNNgeKLiFF5gLwwfdZKqKPEBfE7ie3Gp8BQ-0/image-20260409144636-6.png)
3. Klikk på databaseikonet for å laste ned databasen.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6622304-HcuXfSRjYDaoF7PfWFlYyknwJhzRI7LFDsUBKjQTKjZdq3wS5xkJn6HC26zcmZGU-0/image-20260409144548-5.png)

**Hvordan importere .sdb til en SQL-server**

SDB-filer er gzip-komprimerte binære databasesnapshots eksportert fra en SuperOffice CRM-database. For å åpne databasen må du overskrive en eksisterende database på SQL-serveren.

Vi anbefaler at du oppretter en ny database med ODBC-tilkobling ([Create Microsoft SQL Server | SuperOffice Docs](https://docs.superoffice.com/en/onsite/install/database/create-ms-sql-server-db.html)), som du overskriver under databaseimporten (for eksempel SOimport):

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6631704-MspYXWKdwHctSNpejctomLWMKeK6B0ZgTP0knK3ZRNR65lITQd150rzSWJ8rmOzs-0/image-20260415145841-1.png)

Du kan laste ned CrmSetup [her](https://online3.superoffice.com/Cust1990/CS/scripts/rms.fcgi/getAttachment/6626597-upc6SP1k8aZZH6CltOUjkbIXj0PhlEWw2MAfb9lMLf0wattzfrkMSLwNUzCOmYYo-0/CrmSetup.zip).

Denne zippede mappen inneholder 3 filer:

- CrmSetup.exe
- Options advanced import.txt
- arg-file DBimport.txt

Her viser vi hvordan du importerer hele databasen med den medfølgende importfilen arg-file DBimport.txt.

For mer avanserte importer, se Options advanced import.txt i den nedlastede mappen, og les mer om CrmSetup her: [CrmSetup and CrmTask utilities | SuperOffice Docs](https://docs.superoffice.com/en/onsite/install/database/crmsetup-and-crmtask.html)

Fyll ut importfilen slik: Verdiene markert med rødt skal erstattes i henhold til databasen du ønsker å erstatte:

*import-database*

*--database-server SQL server name*

*--database-name DBname*

*--db-user dbusername*

*--db-password dbpassword*

*--table-prefix prefix*

*--source-file pathtofile.sdb*

Eksempel. Importfilen arg-file DBimport.txt er opprettet. Sikkerhetskopifilen ble plassert på C:-stasjonen, så stien er C:\database.sdb

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6631720-iIN0xCUM7iklmAHLMUfC7QfH5AXWKQyYxffxXkfWsFYzD0BZsFYlyLpMdZATrLC1-0/image-20260415150149-2.png)

Når du har .sdb-filen, CrmSetup.exe-filen og importfilen, kjører du CMD.EXE som administrator og kjører kommandoen for å importere databasen. I praksis peker du til importfilen:

 crmsetup --arg-file DBimport.txt

I skjermbildet nedenfor kan du se at alle 3 filene er plassert på C:-stasjonen.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6631721-5erOAzB0SAhQCEkhRZE9nH3ASZixRMcsXBSrcluiEf2QYI7riPdjapHyngMJ3OpA-0/image-20260415150227-3.png)

**Merk!** Kommandoen import-database i CrmSetup vil slette alle eksisterende SuperOffice-tabeller i måldatabasen og erstatte dem med dataene fra SDB-filen.

**Mer informasjon**

SuperOffice CRM er basert på to typer datalagring: Database og Dokumentarkiver.

- Databasereferanser: [Database table listing | SuperOffice Docs](https://docs.superoffice.com/en/database/tables/index.html).
- Mappen SO\_Arc inneholder dokumentarkivet. Filer lagres i en struktur basert på oppretterens bruker-ID, året og halvåret dokumentet ble opprettet i. Filnavn genereres automatisk ved hjelp av firmanavnet og maltypen.
- Microsoft SQL Server Database-data er separat for hver kunde. Alle databasekopier er gyldige i 30 dager. Dette betyr at en gjenopprettelse kan gjøres fra en bestemt dato/klokkeslett de siste 30 dagene. I tillegg tas det en månedlig kopi, og den lagres i 12 måneder. En årlig kopi lagres i 10 år.
- Alle dokumentarkiver har kontinuerlig speiling mellom to fysisk adskilte datasentre og har individuelle sikkerhetskopier på begge steder. Sikkerhetskopien lagres en gang om dagen (vanligvis om natten). Dokumentendringer sikkerhetskopieres og lagres i 30 dager. Sikkerhetskopien av slettede filer (dokumenter) lagres i 90 dager.
