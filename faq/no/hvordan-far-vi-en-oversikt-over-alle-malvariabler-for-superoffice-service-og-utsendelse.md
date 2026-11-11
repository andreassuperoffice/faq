---
title: "Hvordan får vi en oversikt over alle malvariabler for SuperOffice Service og Utsendelse?"
url: https://community.superoffice.com/no/support-faqs/faq/hvordan-far-vi-en-oversikt-over-alle-malvariabler-for-superoffice-service-og-utsendelse/
lang: no
updated: "4. aug. 2026"
---

# Hvordan får vi en oversikt over alle malvariabler for SuperOffice Service og Utsendelse?

Oppdatert på 4. aug. 2026

Hvordan får jeg en oversikt over alle malvariabler for SuperOffice Service og Markedsføring?

Du kan bruke malvariabler for å sette inn informasjon automatisk fra SuperOffice CRM i meldinger som sendes til kunder. For å få en oversikt over alle tilgjengelige malvariabler, følger du trinnene nedenfor:

- [Hvis du trenger malvariabler for saker](https://community.superoffice.com/no/support-faqs/faq/hvordan-far-vi-en-oversikt-over-alle-malvariabler-for-superoffice-service-og-utsendelse/#1)
- [Hvis du trenger malvariabler for utsendelser](https://community.superoffice.com/no/support-faqs/faq/hvordan-far-vi-en-oversikt-over-alle-malvariabler-for-superoffice-service-og-utsendelse/#2)

**Få en liste over alle tilgjengelige malvariabler du kan bruke i svarmaler i saker**

1. Klikk på **Hovedmeny** (1), deretter **Kunnskapsbase** (2) og **Svarmaler** (3).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802271-aoCToC94Kx6u2mXM8rbE5TqJkOjM8QQ2rJkJCGXled9gBiGuwWhibMghkwd2BtGm-0/image-20260804105939-1.png)
2. Klikk på knappen **Ny svarmal (1)** i det øverste høyre hjørnet for å lage en ny svarmal. Vennligst les [denne artikkelen](https://docs.superoffice.com/no/knowledge-base/learn/reply-templates/create.html) for å lære mer om hvordan du lager svarmaler.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802272-I4P42GPhITdussU6ukmthEu5Gq5gECdL524lDFxwDWQ76RcXnreaZ8KUbYI6EZsA-0/image-20260804110104-2.png)
3. For å få en liste over alle malvariabler kan du enten skrive **"% PARSER\_TREE%"** (2) i **HTML-tekst** (1) -fanen eller klikke på **Malvariabler** (3) og velge en svarmal i **Liste over alle tilgjengelige malvariabler** (4) og trykke på **OK** (5) for å lagre.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802273-RnqW9fS9I7Zu5tDif4q8ApWDrAnzDWEHciEpLeFYCxLy57eDGn1gGG9UtdCi0npR-0/image-20260804110219-3.png)

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802277-7Uf7ECF90GLZITtZA94TEJTLUFyc1ofDyfDExR8j4FJRc7rObDiY6JAF7NAD3ffF-0/image-20260804110323-4.png)
4. Når du bruker denne svarmalen i en sak, vil den hente ut alle tilgjengelige malvariabler som kan bli brukt, også verdier som ville blitt fylt ut i malen, som brukte malvariabelen.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802278-PPTxtDtjGwrlAKUq3mFjNQCk3820Jnq7YkFPr56d7Q4O7TeWu8atrUgPymrs6u3P-0/image-20260804110626-5.png)

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802279-mGqHNwgtiwm0YWBe79I4hL3nFo9F7HePcdBUzCE4AyD2IB49s1kd41n28rWFaspy-0/image-20260804110657-6.png)
5. For å bruke malvariabler, skriv dem i parentes i en svarmal, og neste gang du vil bruke denne svarmalen, vil informasjonen i malvariabelen bli fylt ut med informasjonen fra SuperOffice CRM.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802316-CNEDntEywbJJ9TcTCG49gz4b8nkxfhFxGfwIQ8XhTGBrKX0UDTpnQdpyxxXqAZGx-0/image-20260804111646-7.png)

**Få en liste over alle tilgjengelige malvariabler du kan bruke i teksten i utsendelser**

1. Åpne en utsendelse som du kan bruke til testing, skriv inn [[PARSER\_TREE]] (1) i et tekstfelt og klikk på **Send test** (2). Skriv inn e-postadressen du vil sende testmeldingen til, og klikk på OK.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802326-F08cegx4iUK9ApUShqweafwe2T4q1J0X2WMEuAZOMYcM7MhTop7r1Xd9chXbXPaP-0/image-20260804112008-8.png)

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802327-qtkr7CGcsizTnN6iF163sirO34pM5jhGdZoeLC4mCl6gaLdmmXK0Czs6Cjh0b5aX-0/image-20260804112158-9.png)
2. Du vil motta en melding som inneholder alle tilgjengelige malvariabler du kan bruke i en utsendelse. Du kan bruke data fra felter på:
   - Mottakerens firma
   - Mottakerens personkort
   - Mottakerens personlige lenker for e-markedsføring
   - Informasjon om lisens og vedlikehold
   - Brukeren som er angitt som Vår kontakt på mottakerens firmakort

     |  |
     | --- |
     | ourContact.company.address  ourContact.company.url  ourContact.company.name  ourContact.direct  ourContact.cellphone  ourContact.salutation  ourContact.title  ourContact.lastname  ourContact.middlename  ourContact.firstname  ourContact.email  ourContact.name |
   - Brukeren som er angitt som Vår salgskontakt på mottakerens firmakort

     |  |
     | --- |
     | ourSalesContact.company.address  ourSalesContact.company.url  ourSalesContact.company.name  ourSalesContact.direct  ourSalesContact.cellphone  ourSalesContact.salutation  ourSalesContact.title  ourSalesContact.lastname  ourSalesContact.middlename  ourSalesContact.firstname  ourSalesContact.email  ourSalesContact.name |

     **Merk!** Med malvariabler kan du også sette inn verdier fra brukerdefinerte felter i utsendelser. Dette gjør du ved å bruke Prog ID for det brukerdefinerte feltet som en variabel i meldingen.

     ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802358-qcoE459ODcRbPY4IOpyjlPCEq22c1jrDXHtXp4kupKHoKcnWZSeYhIj5yu9nIcu0-0/image-20260804113628-11.png)

     ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6802359-sdgnJlYDZ1BakqnIi1tdLzfMJNUeygyi9h9BLrMIhQd9QE8hjIlele6Ke5t3ENpX-0/image-20260804113644-12.png)

**Merk!** Du kan også bruke funksjoner som henter spesifikk informasjon. Du kan endre hvordan en dato vises ved å endre formatet på variabelen. Følgende formater kan brukes:

YY4 = year, 4 digits
YY2 = year, 2 digits
MM2 = month, 2 digits
MM1 = month, 1 or 2 digits
DD2 = day of month, 2 digits
DD1 = day of month, 1 or 2 digits
MONTH = Name of month. Array of names must be passed as 3rd argument.
WDAY = Name of weekday. Array of names, starting with sunday, as 4th argument.

HH24: Hour of day, 2 digits, 24 hour format
H24: Hour of day, 1 or 2 digits, 24 hour format.
HH12: Hour of day, 2 digits, 12 hour format.
H12: Hour of day, 1 or 2 digits, 12 hour format
MI2: Minutes. 2 digits.
SS2: Seconds. 2 digits.
AMPM: AM/PM indicator, "am" or "pm"

**Mer informasjon**

Docs: [Malvariabler (Service)](https://docs.superoffice.com/no/knowledge-base/learn/reply-templates/template-variables.html)
