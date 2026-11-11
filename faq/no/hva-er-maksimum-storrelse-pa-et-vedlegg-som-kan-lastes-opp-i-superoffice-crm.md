---
title: "Hva er maksimum størrelse på et vedlegg som kan lastes opp i SuperOffice CRM?"
url: https://community.superoffice.com/no/support-faqs/faq/hva-er-maksimum-storrelse-pa-et-vedlegg-som-kan-lastes-opp-i-superoffice-crm/
lang: no
updated: "28. mar. 2026"
---

# Hva er maksimum størrelse på et vedlegg som kan lastes opp i SuperOffice CRM?

Oppdatert på 28. mar. 2026

Hva er maksimum størrelse på et vedlegg som kan lastes opp i SuperOffice CRM?

SuperOffice CRM Online og Onsite har forskjellige begrensninger med hensyn til størrelsen på vedlegg. For mer spesifikk informasjon, vennligst les avsnittene nedenfor:

[Størrelsesgrenser for vedlegg i SuperOffice CRM Online](https://community.superoffice.com/no/support-faqs/faq/hva-er-maksimum-storrelse-pa-et-vedlegg-som-kan-lastes-opp-i-superoffice-crm/#1)

[Størrelsesgrenser for vedlegg i SuperOffice CRM Onsite](https://community.superoffice.com/no/support-faqs/faq/hva-er-maksimum-storrelse-pa-et-vedlegg-som-kan-lastes-opp-i-superoffice-crm/#2)

​

**Størrelsesgrenser for vedlegg i SuperOffice CRM Online

Dokumenter i Superoffice CRM**

Den maksimale størrelsen på dokumentopplasting i SuperOffice CRM er 94,4 MB, og tiden for filopplasting er 5 minutter.

Dette betyr at du for eksempel trenger omtrent 2,5–3 Mbit/s opplastingshastighet for å kunne legge til/redigere en 94 MB-fil til SuperOffice CRM Online.

**Vedlegg i Utsendelser og Service**

Den maksimale størrelsen på vedlegg i SuperOffice Utsendelser og Service er 25 MB, både for innkommende og utgående dokumenter.

Én sak i SuperOffice Service, for eksempel, kan ikke ha 3 vedlegg som er 10 MB hver, fordi total vedleggsstørrelse vil overstige 25 MB.

**Merk!**

Nyest informasjon om størrelsesbegrensninger for vedlegg i SuperOffice Online finnes også i Docs: [Systemkrav for SuperOffice CRM Online](https://docs.superoffice.com/en/online/system-requirements.html).

​

**Størrelsesgrenser for vedlegg i SuperOffice CRM Onsite**

SuperOffice Onsite-installasjon har ikke filstørrelsesbegrensninger. Derimot  IIS-serveren, der SuperOffice er installert kan ha noen begrensninger.

For eksempel kan det hende at IIS-serveren bare tillater prosesser (f.eks. filopplasting) å kjøre i en begrenset periode (f.eks. 60 sekunder). Filopplastningen som tar lengre tid enn det, vil mislykkes. Eller det kan være at IIS-serveren har en begrensning på innholdslengden. Dette betyr at når filen din overskrider en standardgrense (30 000 000 bytes – omtrent 28,6 MB), vil opplastingsprosessen mislykkes. For å endre denne begrensningen kan du følge trinnene nedenfor:

1. Velg SuperOffice og dobbeltklikk på **Request Filtering:**

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3507369-byrTeQnH9xeol2c6DASPhxSLXXjFB6yNZteP79GSDI60hEiC3GAwAB44Kn2P6Dsp-0/image.png)
2. Klikk på **Edit Feature Settings** og angi grenser for vedleggsstørrelser i feltet **Maximum allowed content length,**og klikk deretter **OK.**

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3507374-JKy2ydGkQlrrprruFExsjhEejj2KgCMjwUB7y3tfcRlo5tlqHqIid09iSJksfPcd-0/image.png)
