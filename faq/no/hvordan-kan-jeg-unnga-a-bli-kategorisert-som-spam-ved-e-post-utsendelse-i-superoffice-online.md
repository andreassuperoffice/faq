---
title: "Hvordan kan jeg unngå å bli kategorisert som spam ved e-post utsendelse i SuperOffice Online?"
url: https://community.superoffice.com/no/support-faqs/faq/hvordan-kan-jeg-unnga-a-bli-kategorisert-som-spam-ved-e-post-utsendelse-i-superoffice-online/
lang: no
updated: "13. mar. 2025"
---

# Hvordan kan jeg unngå å bli kategorisert som spam ved e-post utsendelse i SuperOffice Online?

Oppdatert på 13. mar. 2025

Etter at jeg har sendt ut en utsendelse fra SuperOffice CRM Online har jeg lagt merke til at mange mottakere av utsendelsen min har status "Bounced".  Samtidig la jeg merke til et problem i SuperOffice Service. De fleste e-postene vi sender forårsaker en bounce-melding, og svarene våre kommer ikke fram til kundene våre.

Hvorfor skjer dette, og hvordan kan jeg løse det?

Hver CRM Online-kunde med adgang til Markedsføring og Service-modulene mottar utsendelsestjenesten som leveres av MailGun og får en e-postkonto for SuperOffice Service i form av "customer@domain.suocrm.XX" (.eu eller .com).

Kunder vil ofte bruke sine egne e-postadresser til å sende e-post (utsendelser eller svar på saker i Service). Når dette er tilfelle, kan mottagerens e-postserver identifisere disse meldingene som spam, fordi domenet til avsenders e-postadresse er forskjellig fra det virkelige domenet for e-postadressen (levert av SuperOffice) som sender ut e-posten.

Hvis du for eksempel bruker din e-postadresse i Fra-feltet i SuperOffice Utsendelser eller du bruker din e-post som Standard "fra adresse" i innstillingene i SuperOffice Service, vil mottagerens e-postserver se at utsendelsen eller e-postmeldingen er sendt fra “e-mail@customer.suocrm.com” - domenet, men “fra”-adressen er forskjellig, dvs. den inneholder et annet domenenavn.  Dette kan føre til at din melding blir identifisert som spam, og derfor blir e-postene kategorisert som spam.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6127167-sEf1MxrK0lwHXsl6C7XoshxaiUrUCOmtRuD3LttDuC8WJK99JFJHlksFXLmjZ5hH-0/image-20250313153155-1.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6127174-jLPtEe8P1yoYwRdZYyijqhpwQ63wi1HmnMPsF6sGeGgIXnXPTRawGJM3OtkdMbXn-0/image-20250313153214-2.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6127175-EQAB8iApOAbQELZCdjsusBTWcXmcmerRnXjq1OOr9etxOK9U3zIz5Sd77erZutUo-0/image-20250313153228-3.png)

For å unngå at situasjonen over ikke påvirker dine meldinger, foreslår vi å opprette en såkalt record som tillater SuperOffice Online MailGun-service å sende meldinger på vegne av ditt domene. Dette utføres ved å bruke SPF records.

Du trenger da å opprette en database i DNS for ditt domene “@[yourdomain].com” som bekrefter at SuperOffice SMTP-server er en klarert avsender for “@[yourdomain].com”.

TXT record som må legges til er "v=spf1 include:\_spf.online.superoffice.com ~all".

**Merk!**Dette bør utføres av din IT-ansvarlig, din e-postserver-administrator, eller noen som administrerer DNS for ditt domene.

**Mer informasjon:**

Docs: [Set up SPF](https://docs.superoffice.com/email/mailgun/spf/set-up.html)

Google anbefalinger for deres service, gå til [Om SPF records](https://support.google.com/a/answer/33786?hl=en)

Office 365 anbefalinger for deres tjenester, gå til [Samle informasjonen du trenger for å opprette Office 365 DNS records](https://support.office.microsoft.com/en-us/article/Gather-the-information-you-need-to-create-Office-365-DNS-records-77f90d4a-dc7f-4f09-8972-c1b03ea85a67) og [SPF i Office 365 til hjelp for å forhindre falske avsendere](https://technet.microsoft.com/nb-no/library/dn789058(v=exchg.150).aspx)

 FAQ: [Hvordan unngår jeg å bli svartelistet etter å ha sendt ut våre nyhetsbrev fra SuperOffice CRM?](https://community.superoffice.com/no/support-faqs/faq/what-to-do-when-the-newsletters-get-blacklisted-after-sending-them-out-from-superoffice-mailing/)
