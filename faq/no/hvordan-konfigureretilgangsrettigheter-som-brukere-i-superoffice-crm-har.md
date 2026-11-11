---
title: "Hvordan konfigurere tilgangsrettigheter som brukere i SuperOffice CRM har?"
url: https://community.superoffice.com/no/support-faqs/faq/hvordan-konfigureretilgangsrettigheter-som-brukere-i-superoffice-crm-har/
lang: no
updated: "10. jun. 2025"
---

# Hvordan konfigurere tilgangsrettigheter som brukere i SuperOffice CRM har?

Oppdatert på 10. jun. 2025

Hvordan konfigurere tilgangsrettigheter som brukere i SuperOffice CRM har?

SuperOffice CRM-systemet har rolle- og gruppebasert tilgangssystem. Det betyr at alle SuperOffice-brukere skal ha tildelt en rolle og skal tilhøre en primærgruppe. Det er obligatorisk.

**En rolle** har et sett med data- og funksjonelle rettigheter, og **en primærgruppe** gir tilgang til datarettigheter, ulike SuperOffice-lister og bidrar til å sette systeminnstillinger mer effektivt. En bruker kan også tilhøre flere grupper. Dette er relevant når du konfigurerer tilgang til datarettigheter i SuperOffice CRM.

Bilde 1 viser en modell av hvordan tilgangsrettighetssystemet fungerer i SuperOffice CRM. Denne modellen har referanser (1, 2, 3 ...) til forskjellige innstillinger for tilgangsrettigheter som er illustrert med skjermbilder og forklart senere i artikkelen.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4404136-5pEjXutxNQG6fm7HxJmMWwXZp8KjgAT1yA0k7CnUKNLO7WO9F4LNKxqIPZbA38Mz-0/image.png)

Bilde 1.

En bruker skal tilhøre en primærgruppe. Samme bruker kan tilhøre flere grupper. Se eksempelet på bildet 2. Hvis Bruker A tilhører Markedsføring som den andre gruppen, og Bruker B - Markedsføring som den primære gruppen, da tilhører Bruker A og Bruker B samme Markedsføringsgruppe. Dette er viktig å vite når du angir datarettighetene til brukerne.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3695464-dD83rirR8Au63tZCBESaFrd3yiaMh8x8eTwumXSz46yqIhlA1DWJz3tSu6ZQ599e-0/image.png)

Bilde 2.

En bruker må ha en rolle som styrer datarettigheter og funksjonelle rettigheter i SuperOffice CRM. Systemet lar deg konfigurere tilgang til firmaer, personer, prosjekter, prosjektmedlemmer, utvalg, salg, interessenter (av salg), [oppfølginger (avtaler, oppgaver, telefonsamtaler)](https://docs.superoffice.com/no/learn/section-tabs/activities-tab.html), dokumenter (dokumenter, e-post og utsendelser som faller under denne kategorien), relasjoner (person og firma) og dashbord. Dette kalles for dataobjekter.

Hvert dataobjekt tilhører en bruker som kanskje er deg selv (A), brukere i din primærgruppe (B), brukere som tilhører de andre gruppene dine (C), andre medarbeidere som ikke er tilkoblet noen av gruppene dine (D), eksterne brukere (E) og anonyme brukere (F).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6234319-yufmu8kwrUCDkXOQ9HB2qUPx2mumNTSEU8E55pgNf1M2b7b6TCW1fuX6ArlUzwrs-0/image-20250610163149-1.png)

*Skjermbilde 1.*

Eierskapet til forskjellige dataobjekter bestemmes i forskjellige felt. For eksempel, på firmakort er det et felt "Vår kontakt" som bestemmer eier av firmakortet. På Oppfølgingskortet er det et felt "Eier", på Prosjektkortet - "Ansvarlig", etc.

Du kan angi forskjellige tilgangsrettigheter for hvert dataobjekt.

|  |  |
| --- | --- |
| **Navn** | **Datarettighet** |
| Ingen | ingen rettighet |
| Les | rettighet til å lese |
| Opprett | rettighet til å lese og opprette |
| Oppdater | rettighet til å lese, opprette og oppdatere |
| Slett | rettighet til å lese, opprette, oppdatere og slette |

For eksempel, i Innstillinger og Vedlikehold-modulen har du valgt Brukernivå 1/User Level 1 (A) og satt Slett (B) til et firmadataobjekt under den primære gruppekolonnen. Denne konfigurasjonen betyr at enhver bruker, som har rolle 1 på brukernivå 1, vil kunne lese, opprette, oppdatere og slette alle firmaene som tilhører andre brukere, som er medlemmer av hovedgruppen.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6234340-iLs4bs8sLlK6m0wqxh1CuEPE3L8Xog17azbyilD1ppQRGiItMSR3n2bK14M4zsWW-0/image-20250610163554-2.png)

*Skjermbilde 2.*

En rolle har også et sett med funksjonelle rettigheter (3). Ved å flytte en funksjonell rettighet fra høyre til venstre og omvendt, kan du kontrollere hva en bruker kan og ikke kan gjøre i systemet. [Denne FAQ-en](https://community.superoffice.com/no/support-faqs/faq/whichare-all-availablefunctional-rights-in-superoffice-and-what-each-of-them-mean/) forklarer hva hver funksjonelle rettighet står for.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6234342-7Bt6oPZX69hpDPdtWxlTftMpg3UbB15XA6U13Zbf4o5NXLQSfxPaOEORIW87fgLc-0/image-20250610163843-3.png)

*Skjermbilde 3.*

En gruppe som er tildelt brukeren, gir tilgang til dataobjekter (4. skjermbilde). Den kan gi tilgang til lister (blant annet dokumentmaler (5)) i SuperOffice CRM. Dette er bare relevant hvis du bruker innstillingen Gruppering og filtrering (A) på listene. Hvis denne innstillingen ikke er konfigurert, har alle brukere tilgang til alle listene i SuperOffice CRM. Gruppering og filtrering er spesielt nyttig når mange brukere med ulike ansvar har tilgang til systemet. På denne måten kan du unngå at enkelte brukere får tilgang til informasjonen de ikke skal se.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6234346-RaGBKcDGTyJSOf6k0Kdy0rYwOFoYXsohEaHtskbor6ZrBMh46mSfmGiIEQjXAwrJ-0/image-20250610164124-4.png)

*Skjermbilde 4.*

Hvis du for eksempel vil gjøre et bestemt listeelement synlig bare for enkelte brukere, må du gå til listen, som lagrer disse elementene (A). Velg elementet (B) og i boksen "Synlig for brukergrupper": legg til en sjekk ved siden av brukergruppene som skal se listeelementet (C).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6234351-mnIqzmZwHST6WR1F8gipiN0fntbiDPmOLR3Z6S92tWBmAFtdos2Yw9g4qYOBJ1Cy-0/image-20250610164256-5.png)

*Skjermbilde 5.*

Å ha brukerne organisert i grupper er også praktisk, når du vil tilpasse SuperOffice-innstillingene. Det kalles preferanser (6). Hver preferanse, som finnes i innstillings- og vedlikeholdsmodulen, kan settes for en bruker, brukergruppe eller hele systemet.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6234354-gKs0An8djKaIM55DNbCLdLwgTYREe7O0S1ZgpLElGsEJDZc9JXUnldUqxkpupeWr-0/image-20250610164630-6.png)

*Skjermbilde 6.*

Innstillingene som forklares i denne FAQ-en, hjelper å tilpasse tilgangssystemet og ha kontroll over informasjons tilgjengelighet i SuperOffice CRM.

**Mer informasjon**

Docs: [User accounts and role-based access control](https://docs.superoffice.com/en/online/identity/user/index.html)

Docs: [Set data rights for a role](https://docs.superoffice.com/en/admin/user-management/learn/role/set-data-rights-for-role.html)

FAQ: [How do I create a new User Group in SuperOffice CRM?](https://community.superoffice.com/no/support-faqs/faq/how-do-i-create-a-new-user-group-in-superoffice-crm/)

FAQ: [How can I best set up data rights in SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-can-i-best-set-up-data-rights-in-superoffice-crm/)

FAQ: [How to hide data for all users except for users with user level 0?](https://community.superoffice.com/en/support-faqs/faq/how-to-hide-data-for-all-users-except-for-users-with-user-level-0/)
