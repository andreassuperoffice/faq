---
title: "Hvordan legger jeg SuperOffice Chat widgeten til nettsiden min?"
url: https://community.superoffice.com/no/support-faqs/faq/hvordan-legger-jeg-superoffice-chat-widgeten-til-nettsiden-min/
lang: no
updated: "26. okt. 2026"
---

# Hvordan legger jeg SuperOffice Chat widgeten til nettsiden min?

Oppdatert på 26. okt. 2026

Hvordan legger jeg til en SuperOffice Chat-widget på nettsiden min?

For å aktivere SuperOffice Chat-widgeten på nettsiden din må du utføre to handlinger. Følg trinnene nedenfor for å gjøre dette:

1. [Konfigurer SuperOffice Chatkanal](https://community.superoffice.com/no/support-faqs/faq/hvordan-legger-jeg-superoffice-chat-widgeten-til-nettsiden-min/#1)

2. [Legg til JavaScript på nettside ditt Content Management system](https://community.superoffice.com/no/support-faqs/faq/hvordan-legger-jeg-superoffice-chat-widgeten-til-nettsiden-min/#2)

​

**Trinn 1. Konfigurer SuperOffice Chatkanal**

1. Logg inn på [Innstillinger og Vedlikehold](https://community.superoffice.com/no/support-faqs/faq/hvordan-kan-jeg-administrere-superoffice-crm/).
2. Velg **Chat** (1) i menyen til venstre. Deretter kan du [opprette en chatkanal](https://docs.superoffice.com/no/chat/admin/channel-create) eller velge en som allerede er opprettet (2), og klikke på **Vis** (3). Dette genererer en skriptkode som du må kopiere og lagre.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6923837-RNtF9G9EWRYreeJFZFXU1EWkK8rakdZUFCStRDItThgs8DNwCp7NRMIKd5RqMLRH-0/image-20261026114828-2.png)

​

**Trinn 2. Legg til JavaScript på nettside ditt Content Management System.**

Denne FAQ-en forklarer hvordan du legger til en chat-widget på en nettside som administreres med WordPress. Fremgangsmåten er tilsvarende for andre publiseringssystemer (CMS), som Joomla, Weebly, Drupal, Episerver, Shopify, PrestaShop osv.

1. Logg inn i administrasjonspanelet og gå til seksjonen der du kan redigere eller legge til HTML-kode. I WordPress klikker du på **Utseende** og deretter **Rediger temafiler**.

    ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6357381-YzeWJzLoRekBOrbLt0dQJrOG0xpIxZyfgCZ5pDM7XTOgDRczI2CQbuFa1WLqIy9u-0/image-20251008144437-2.png)
2. Legg JavaScript-koden i toppteksten (header) på nettsiden din hvis du vil at chat-widgeten skal vises på alle sider. Hvis du vil at chatten bare skal vises på bestemte sider, legger du JavaScript-koden kun i toppteksten på disse sidene. Når du er ferdig med å redigere koden på nettsiden, klikker du på **Oppdater fil

   Merk!** DEFER-parameteren sørger for at skriptet ikke blokkerer innlastingen av siden. Skriptet kjøres etter at siden er ferdig lastet inn.
3. Åpne nettsiden din, eller oppdater siden hvis du allerede har den åpen. SuperOffice Chat-widgeten er nå tilgjengelig nederst til høyre på skjermen og klar til bruk.

**Mer informasjon:**

Dokumenter: [Chat](https://docs.superoffice.com/no/chat/learn/index)

FAQ: [Hvordan tilpasser jeg utseende på SuperOffice chat-vindu?](https://community.superoffice.com/no/support-faqs/faq/hvordan-tilpasser-jeg-utseende-pa-superoffice--chat-vindu/)
