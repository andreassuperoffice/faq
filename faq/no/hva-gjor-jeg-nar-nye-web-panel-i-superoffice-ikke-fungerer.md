---
title: "Hva gjør jeg når nye Web Panel i SuperOffice ikke fungerer?"
url: https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-nar-nye-web-panel-i-superoffice-ikke-fungerer/
lang: no
updated: "24. mar. 2022"
---

# Hva gjør jeg når nye Web Panel i SuperOffice ikke fungerer?

Oppdatert på 24. mar. 2022

Jeg opprettet en ny Web Panel, men den viser ikke innholdet. Hvorfor dette skjer og hvordan kan jeg fikse det?

Det kan være flere grunner til at et nytt Web panel ikke fungerer. Her er noen av de vanligste årsakene:

- [Når brukeren din ikke tilhører brukergruppen som har tilgang til Web panelet](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-nar-nye-web-panel-i-superoffice-ikke-fungerer/#1)
- [Når URL -en, som er konfigurert i Web panelet, ikke er tilgjengelig](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-nar-nye-web-panel-i-superoffice-ikke-fungerer/#2)
- [Når URL-en, som er konfigurert i Web panelet, bruker http-protokollen](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-nar-nye-web-panel-i-superoffice-ikke-fungerer/#3)
- [Når *the same origin policy*  ikke blir respektert](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-nar-nye-web-panel-i-superoffice-ikke-fungerer/#4)
- [Da Web panelet er opprettet i InfoBridge -plattformen og blir ikke oppdatert i SuperOffice CRM](https://community.superoffice.com/no/support-faqs/faq/hva-gjor-jeg-nar-nye-web-panel-i-superoffice-ikke-fungerer/#5)

**Når brukeren din ikke tilhører brukergruppen som har tilgang til Web panelet**

Når man oppretter et nytt Web panel (f.eks. GoogleMaps (1)) og man bruker **gruppering og filtrering** (2), må man sørge for at brukerne som skal kunne se Web panelet tilhører gruppene (3) som har tilgang til å se det. Vennligst sjekk [denne veiledningen](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=113784)  for å se hvordan du gir en brukergruppe til en bruker.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4784637-Pnoa1hC0x2Z929jHkZQy9bMbOfTRjyPZRPQ9h8lNSYOWuFy8m0Slf0CgQ9kXXFMc-0/image.png)

**Når URL -en, som er konfigurert i Web panelet, ikke er tilgjengelig**

For å teste om URL-en definert i Web panelet er tilgjengelig, kan du gjøre en test som er beskrevet nedenfor:

1. I [Innstillinger og vedlikehold](http://cs.superoffice.com/scripts/customer.fcgi?_sf=0&custSessionKey=&customerLang=en&noCookies=true&action=viewKbEntry&id=10106)klikk du på **Lister** (1) -delen, velg **GUI - Webpanel** (2) og deretter velg  Web panelet (3) som ikke fungerer.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4784638-RmwZEX7sy5tkucUxGq10ArSKQ6aEc2sT4QxojxBcJHaeCZpfGBLDh4WU7HZLfsTj-0/image.png)
2. Dobbeltklikk for å åpne Webpanelet som feiler. Kopier adressen som er definert i URL -feltet, og lim den inn i nettleseren din. Det skal vise innholdet du vil se på Webpanelet. Hvis det fungerer, vennligst sjekk neste avsnitt. Hvis det ikke viser innholdet du trenger, kan du undersøke hvorfor nettstedet er ikke tilgjengelig.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4784639-W4Mb53A7otNG9ECDKBABJJNQdOL6kFRjBOCpTa31cKO7lhJraEqRl6pAXZYIipCE-0/image.png)

**Når URL-en, som er konfigurert i Web panelet, bruker http-protokollen**

SuperOffice Online er tilgjengelig via **https** -protokollen. Hvis programmet eller nettstedet, som er definert i Webpanelet ditt, er tilgjengelig via **http** -protokollen -  skal nettstedet ikke vises på grunn av det vil det og du kan se en feilmelding. Åpne  ["Console"](https://wickedlysmart.com/hfjsconsole/) i nettleseren din for å se feilemdingen:

*Mixed Content: The Page at '[URL to site]' was loaded over HTTPS, but requested an insecure resource  '[URL to site]'. This request has been blocked; the content must be served over HTTPS.*

Hvis nettstedet også tilbyr tjenesten i https -format, kan du endre nettadressen i oppsettet for Webpanel, i Innstillinger og vedlikehold. Da bør problemet løses. Les [denne artikkelen](https://dev.to/mittalyashu/mixed-content-fetching-data-from-https-and-http-3n31) for mer informasjon.

**Når *the same origin policy*  ikke blir respektert**

*The same origin policy*er et viktig konsept i sikkerhetsmodellen for Webapplikasjoner. I henhold til disse retningslinjene tillater en nettleser skript, som finnes på den første websiden, for å få tilgang til dataene på den andre websiden. Dette kan bare skje hvis begge nettsidene har samme opprinnelse.

Det håndteres ikke av SuperOffice, men styres av nettleseren som brukes av en SuperOffice -bruker. Det er eieren av innholdet som bestemmer om andre kan bruke innholdet på et "cross-domain site".

For å teste om dette er tilfellet - dvs. hvorfor innholdet på Web panelet ikke vises - åpner du ["Console" i nettleseren din.](https://wickedlysmart.com/hfjsconsole/) Der bør du se feilen: "[Refused to display '[URL to site]' in a frame because it set 'X-Frame-Options' to 'SAMEORIGIN](https://www.google.no/search?hl=no&q=Refused%20to%20display%20%27%5BURL%20to%20site%5D%27%20in%20a%20frame%20because%20it%20set%20%27X-Frame-Options%27%20to%20%27SAMEORIGIN%27&ei=eioOV-OhN-LO6ATl4riADA)."

Nettleserens sikkerhetskontroller  forklarer hvorfor Webpanelets innhold ikke er synlig. Når et nettsted inneholder "DENY" eller "SAMEORIGIN" -siden, er det enten forbudt for å vise nettstedet i en iFrame helt, eller det krever at iFrame som viser denne URL -en er medlem av samme domene (opprinnelse) som selve nettstedet .

For eksempel, hvis du prøver å vise et av disse nettstedene i SuperOffice iFrame og du støter på SAMEORIGIN -parameteren, betyr det at nettstedet ikke kan kjøres i SuperOffice CRM, ettersom domenet til SuperOffice og domenet til vertssiden er forskjellige .

**Merk!**

1. Det er dessverre ingen løsning på denne situasjonen, da denne håndheves av nettlesere basert på overskrifter. Hvis du eier nettstedet du prøver å legge til via iFrame, kan du sende overskriftene om at nettstedet ditt kan legges til av andre, eller legge til online.superoffice.com eller superoffice.com i crossdomain.xml.
2. Noen nettsteder, som YouTube, tilbyr denne tjenesten støtte for "cross-domain site"  - ved å bruke en annen nettadresse:

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4070255-xlUUNZZfdTgippbw1M8Z33TC0r5nMnJXhSa4zNt3Wlt96CAEckqZD5a6qwuT2k1f-0/image.png)

**Da Web panelet er opprettet i InfoBridge -plattformen og blir ikke oppdatert i SuperOffice CRM**

Når du vil  opprette et nytt Web panel på et spesielt [Panel administration site](http://https//my-panels.infobridgeuniverse.com/Account/Login.),  klikk på URL -adressen til SuperOffice for å kjøre flush.

![](https://infobridgekb.atlassian.net/wiki/download/thumbnails/20021317/image2018-12-5_15-41-57.png?version=1&modificationDate=1544107630525&cacheVersion=1&api=v2&width=850&height=45)

**Merk!** I paneloversikten kan du også trykke på den grønne  **Refresh SuperOffice** -knappen for å oppdatere SuperOffice CRM.

![](https://infobridgekb.atlassian.net/wiki/download/attachments/20021317/image2018-12-3_15-45-32.png?version=1&modificationDate=1544107630890&cacheVersion=1&api=v2)

****Mer informasjon****

LTE: [GUI - Web panel](https://help.superoffice.com/Documentation/Help/EN/CRM/WebHelpAdmin_XML/chap08/Webpanel.htm)

[Wikipedia:](https://en.wikipedia.org/wiki/Same-origin_policy)[Same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy)

[Excellent resource from Mozilla that highlights the different options of the X-Frame-Options parameter, along with the implications of each](https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options)

[www.w3.org:](https://www.w3.org/TR/mixed-content/)[Mixed Content](https://www.w3.org/TR/mixed-content/)
