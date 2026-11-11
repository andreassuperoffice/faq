---
title: "Hva gjør jeg hvis SuperOffice-brukere har tilgang til firmaer eller andre SuperOffice-data som de ikke skal kunne se?"
url: https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-hvis-superoffice-brukere-har-tilgang-til-firmaer-eller-andre-superoffice-data-som-de-ikke-skal-kunne-se/
lang: no
updated: "28. apr. 2026"
---

# Hva gjør jeg hvis SuperOffice-brukere har tilgang til firmaer eller andre SuperOffice-data som de ikke skal kunne se?

Oppdatert på 28. apr. 2026

Min kollega kan se mine firmaer i SuperOffice. Jeg har fått beskjed om at dette ikke skal være mulig med oppsettet vårt. Hvorfor skjer dette, og hvordan kan vi rette det?

Det er et par kjente situasjoner når dette kan oppstå:

- [Når SuperOffice CRM brukerdata-rettigheter tillater tilgang til disse opptakene](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-hvis-superoffice-brukere-har-tilgang-til-firmaer-eller-andre-superoffice-data-som-de-ikke-skal-kunne-se/#1).
- [Når problemet oppstår mens du lagrer data i databasen.](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-hvis-superoffice-brukere-har-tilgang-til-firmaer-eller-andre-superoffice-data-som-de-ikke-skal-kunne-se/#2)

**Når SuperOffice CRM brukerdata-rettigheter tillater tilgang til disse opptakene.**

Dette problemet kan oppstå dersom en kollegas SuperOffice-bruker har tillatelse til å se poster som eies av andre brukere. Du kan kontrollere brukerens rolle i [Innstillinger og vedlikehold](https://community.superoffice.com/no/support-faqs/faq/hvordan-kan-jeg-administrere-superoffice-crm/) -> **Brukerrolle** (1)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6509874-TaONKAXy9YbXnipGzKwwyn368HerJNLB079BaHhz55cfoUUezthrBuG4JXIXjnim-0/image-20260130100944-1.png)

For å avklare, vennligst be SuperOffice-administratoren om å navigere til **Roller** (1), velge rollen som tilhører kollegaens bruker (2), klikke på **Data Rettigheter** (3). Deretter bekreft at i dataobjekttype-linjen (4) alle kolonner unntatt Mine egne har blitt valgt til alternativet **Ingen** (5). Det betyr at denne brukeren bare kan se sine egne opptak, men ikke andre.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6509885-pLoX30uHTNWjru3Rid7QzznNFTzqWN1G1473tMJR0BsAjeLmWI0pRdPLDrj7TY2F-0/image-20260130101315-2.png)

Sjekk [denne FAQ-en](https://community.superoffice.com/no/support-faqs/faq/hvordan-konfigureretilgangsrettigheter-som-brukere-i-superoffice-crm-har/) hvis du vil lære mer om tilgangskontroll i SuperOffice CRM.

**Når problemet oppstår****mens du lagrer data i databasen.**

Den beskrevne situasjonen kan oppstå dersom du opprettet firmaer på et tidspunkt da SuperOffice-brukeren din var tilknyttet en annen brukergruppe enn i dag. Det er da sannsynlig at kollegaen din har tilgang til poster som er opprettet av brukere i denne brukergruppen.

Det er også mulig at firmaposten du opprettet fortsatt har feltet *group\_id* fylt ut med ID-en til din tidligere brukergruppe. Mest sannsynlig har brukerens **primære** eller **andre brukergrupper** blitt endret nylig.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6509886-Fl7UdewPtX9iyArOsaePHbxUIBiU5kbQwhDhxwCP3dQF857BZnKNjDJdi6NAAO7G-0/image-20260130101421-3.png)

I dette tilfellet, er løsningen å oppdatere databasen slik at den vil lagre riktig *group\_id* i bedriftskortet. Følg trinnene nedenfor for å endre den:

1. Åpne bedriftskortet (som ikke skal være synlig for din kollega) i redigeringsmodus.
2. Endre **Vår kontakt**(1) til en annen bruker og klikk på **Lagre** (2).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6480063-J0L9tAQgP618AWdqCH1EByOEFBg5GY06WTL0DppbIx08CLaLepLHk47kxw6M83hA-0/image-20260113103028-6.png)
3. Åpne det samme bedriftskortet i redigeringsmodus og endre vår kontakt tilbake til den samme brukeren den tilhørte.

Dette vil korrigere *group\_id*-verdien på firmakortet i databasen, og bedriften vil ikke være synlig for brukere som ikke tilhører den aktuelle gruppen.
