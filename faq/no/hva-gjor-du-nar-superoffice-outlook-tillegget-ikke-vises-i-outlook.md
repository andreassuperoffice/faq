---
title: "Hva gjør du når SuperOffice Outlook-tillegget ikke vises i Outlook?"
url: https://community.superoffice.com/no/support-faqs/faq/hva-gjor-du-nar-superoffice-outlook-tillegget-ikke-vises-i-outlook/
lang: no
updated: "12. mar. 2025"
---

# Hva gjør du når SuperOffice Outlook-tillegget ikke vises i Outlook?

Oppdatert på 12. mar. 2025

SuperOffice-tillegget har forsvunnet. Like før det, mottok jeg en Outlook-varsel som informerte meg om at SuperOffice-tillegget ble deaktivert og ikke lenger synlig i Outlook. Hvorfor skjer dette og hvordan løser jeg det?

Det kan være fire grunner til denne situasjonen:

- Du har nylig oppdatert Windows eller Microsoft Office på datamaskinen din.
- Outlook mener at SuperOffice-tillegget kjører for sakte, noe som påvirker den totale Outlook-ytelsen.
- Datamaskinen din, Microsoft Office-pakken eller Outlook-programmet krasjet like før SuperOffice-tillegget forsvant.
- Mail Link ble installert av en annen Windows-bruker enn den som bruker Outlook.

For å få SuperOffice Ribbon tilbake, følg trinnene nedenfor:

1. Høyreklikk på Outlook-faneområdet og klikk på **Customize the Ribbon** i menyen.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111809-OrsT9sQumGTeYbuAiSWG07dtl4IKdWI4IHMDe4mM4gpdgQ5YMCPWecYq7FiYpu0b-0/image-20250304162500-1.png)
2. Naviger til seksjonen Add-Ins og søk etter SuperOffice-tillegg der:

   •    Hvis du fant SuperOffice-tillegg i **Aktiv tillegg**(1),  [følg denne veiledningen.](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-du-nar-superoffice-outlook-tillegget-ikke-vises-i-outlook/#1)

   •    Hvis SuperOffice-tillegg er i **Inaktive tillegg**(2), [følg denne veiledningen.](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-du-nar-superoffice-outlook-tillegget-ikke-vises-i-outlook/#2)

   •    Hvis SuperOffice-tillegg er i **Deaktiverte tillegg**(3), [følg denne veiledningen.](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-du-nar-superoffice-outlook-tillegget-ikke-vises-i-outlook/#3)

   •    Hvis du ikke finner SuperOffice-tillegg i listen,  [følg denne veiledningen.](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-du-nar-superoffice-outlook-tillegget-ikke-vises-i-outlook/#4)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111810-9ETWfB2yoRUWgDuKAIN9B5MKilICf7A3TkKLQsqMFhKqmPzs6kdwuzFfwADBwOdg-0/image-20250304162507-2.png)

**SuperOffice**-**tillegg er i delen Aktive tillegg**

Hvis du finner SuperOffice-tillegg i Aktive tillegg-delen, selv om den ikke er synlig i Outlook tillegg, kan det være at:

- Visual Studio 2010 Tools for Office Runtime (VSTO), som er en forutsetning for at SuperOffice Ribbon skal fungere, er ikke installert på datamaskinen. Last ned den [herfra.](https://www.microsoft.com/en-sg/download/details.aspx?id=105522)
- Problemet skyldes en kjent feil. Informasjon om den finner du [her.](https://community.superoffice.com/no/product-releases/bugs-wishes/product-issue/?bid=22220&azure=1)

​**SuperOffice-tillegg er i delen Inaktive tillegg**

Gjør følgende:

1. Nederst i skjermen velg **COM Add-ins (1)** fra **Manage-menyen**, og klikk **Go (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111811-yI3zs0IuLqigA0NMJJzb4UwIJTiipKegRuSbXgCoON4ct01fYqnc2BqXLzFbPMCp-0/image-20250304162610-3.png)
2. Huk av for SuperOffice-tillegg (1) og lukk dialogboksen ved å klikke **OK (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111812-LrmTDn71SZM01iRQuN7iBg9lGuIxRq723MAKAItrGIRsQpiQSJASzkOWuMFo08rF-0/image-20250304162620-4.png)
3. SuperOffice-tillegg skal være synlig nå. I noen tilfeller må du starte Outlook på nytt før Tillegg dukker opp igjen.

   **Merk!** Hvis du ved siden av **Load Behavior** ser status **Slettet** eller **Ikke lastet**, må SuperOffice-tillegg Load Behavior Windows Registry justeres, sjekk [denne FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-adjust-the-windows-registry-key-that-is-in-charge-of-loading-superoffice-ribbon-to-make-the-ribbon-visible/)en som forteller hvordan du gjør det.
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111813-IGFUkaB8ZFb286ZR4Zmzc8OXrKTx3rLmDbN1aSJMz5nJPy6Ktppkmk28ugmzw4NF-0/image-20250304162627-5.png)

**SuperOffice-tillegg er i delen Deaktiverte tillegg**

Gjør følgende:

1. Nederst i skjermen, velg **Deaktiverte elementer (1)** fra **Manage-menyen**, og klikk **Go (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111835-R7nGEb9pM3lLbiBYiqjoOc8m5kJRPfFPK2Lq0Les4DRY55oBah9sj36YekjYirD9-0/image-20250304162651-6.png)
2. Velg **SuperOffice-tillegg (1)**, klikk **Aktiver (2)** og **Lukk (3)** dialogboksen.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111838-0BjwcoYPSmsZGeNGYdsJxDmkOrpTgDTJ4sso1Sr4hYs08k84cLJxaJ3YX4a7C9k4-0/image-20250304162758-9.png)
3. Deretter velger du **COM Add-ins (1)** på samme sted og klikker **Go (2)** igjen.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111839-ZEB6nDks1w34hMeBKOL6XeK2KPJMKD8GRcJiSQyanJurk8r8Oj5hs8xFLGZAT676-0/image-20250304162810-10.png)
4. Huk av for **SuperOffice-tillegg (1)** og lukk dialogboksen ved å klikke **OK (2)**. SuperOffice-tillegg skal være synlig nå. I noen tilfeller må du kanskje starte Outlook på nytt før Tillegg  dukker opp igjen.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111840-1XEPZ4U2aw8llZDpgJ3zMu3C4OS6OQORCJu9t1mOPeEMS8oK7EgNzIwBnHwCHp1m-0/image-20250304162817-11.png)

   **Merk!** Hvis du ved siden av **Load Behavior** ser status **Slettet** eller **Ikke lastet**, må SuperOffice -tillegg Load Behavior Windows Registry justeres, sjekk [denne FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-adjust-the-windows-registry-key-that-is-in-charge-of-loading-superoffice-ribbon-to-make-the-ribbon-visible/)en som forteller hvordan du gjør det.

**SuperOffice-tillegg finnes ikke i listen**

Hvis du er sikker på at SuperOffice Mail Link er installert på datamaskinen, men SuperOffice-tillegg ikke vises i Outlook-tilleggslisten, [prøv å installere Mail Link på nytt. Sjekk denne FAQen hvordan du gjør det.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-web-tools/)

Etter å ha installert Mail Link på nytt, sjekk om SuperOffice-tillegg er synlig. Hvis ikke, må du sjekke om en SuperOffice registernøkkel (regedit.exe) er opprettet i Windows-profilen din. For å gjøre det i regedit.exe, naviger til *HKEY \ Current User \ Software \ Microsoft \ Office \ Outlook \ Addins* der du kan se en nøkkel som heter SuperOfficeRibbon-Outlook.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111863-QicFU1X7ezAFTZteg6qwXXIP030qCPoBhwTy9DBY4rps1ZJckjPIN60Cy9pIQ0SI-0/image-20250304162829-12.png)

Hvis den ikke ble opprettet automatisk, skyldes det oftest manglende rettigheter på Windows-profilen. I denne situasjonen foreslår vi:

- enten å gi brukeren lokale administratorrettigheter på datamaskinen og prøve å installere Mail-linken med *.msi-filen*
- eller å importere / kopiere manglende registernøkler fra datamaskinen der SuperOffice Ribbon er synlig, [se denne FAQen hvordan du gjør det.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-manually-import-missing-superoffice-ribbon-registry-keys/)

**Merk!** Feil redigering av Windows-register kan skade din datamaskin eller din server permanent (hvis du jobber med Citrix / Terminal Server), så ikke rediger og ikke slett noen nøkler hvis du ikke er sikker på hvorfor du gjør det. Vi anbefaler deg å ta kopi av Windows-registeret før du foretar noen endringer. Du finner instruksjoner om dette i [denne artikkelen.](https://neosmart.net/wiki/backup-restore-registry/)

​

**Mer informasjon**

FAQ: [What to do if SuperOffice Ribbon gets disabled every time we start Outlook?](https://community.superoffice.com/no/support-faqs/faq/what-to-do-when-the-superoffice-ribbon-add-in-gets-disabled-or-inactivated-every-time-i-start-outlook/)

FAQ: [What can I do when I run into the problems with archiving e-mails from Outlook to SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/what-can-i-do-when-i-run-into-the-problems-with-archiving-e-mails-from-outlook-to-superoffice-crm/)
