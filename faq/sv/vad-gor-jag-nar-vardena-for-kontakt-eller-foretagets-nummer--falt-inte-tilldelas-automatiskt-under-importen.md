---
title: "Vad gör jag när värdena för kontakt eller företagets \"Nummer\" -fält inte tilldelas automatiskt under importen?"
url: https://community.superoffice.com/sv/support-faqs/faq/vad-gor-jag-nar-vardena-for-kontakt-eller-foretagets-nummer--falt-inte-tilldelas-automatiskt-under-importen/
lang: sv
updated: "15. maj 2026"
---

# Vad gör jag när värdena för kontakt eller företagets "Nummer" -fält inte tilldelas automatiskt under importen?

Uppdaterad på 15. maj 2026

Jag har importerat företag och lagt märke till att fältet **nummer** på de importerade posterna i SuperOffice är tomma. Det är ett obligatoriskt fält i vårt system så nu när jag redigerar en importerad post kan jag inte spara den utan att fylla i nummerfältet. Varför tilldelades inte företags- / kontaktnummer automatiskt och hur fyller jag automatiskt in information i nummerfältet?

SuperOffice CRM tilldelar inte nummerfälten automatiskt vid import av nya företag eller kontakter, även om detta fält är obligatoriskt i ditt system. Det är ett förväntat systembeteende, men det finns en registrerad [önskning](https://community.superoffice.com/sv/product-releases/bugs-wishes/product-issue/?bid=8686&azure=1) i vårt system som föreslår att denna funktion förbättras.

Om du importerar nya kontakter och/eller företag och nummer är ett obligatoriskt värde i ditt system, kan du inkludera dessa värden i din importfil och importera tillsammans med all annan information.

Om du redan har importerat företag/kontakter utan att inkludera nummer i din importfil kan du inkludera nummer i dina nuvarande filer och upprepa importen. Följ stegen nedan för att göra det.

1. Logga in på [Inställningar och underhåll](https://community.superoffice.com/sv/support-faqs/faq/hur-far-jag-tillgang-till-att-administrera-installningar-och-underhall-superoffice-crm/).
2. Klicka på **Systemval (1)** och sedan på fliken **Nummertilldelning (2)**. Ta reda på vilken typ av post du importerar. Bredvid den ser du värdet, som ska användas för nästa post, som skapas i systemet. Anteckna det.
3. ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6684104-UBYagW1W0l5bHCHGH8DOjDfHJDTmI3eUm0uGPhExkQuwdXRPSXDQwtEbkb08HCEY-0/image-20260515151227-1.png)
4. Redigera din importfil genom att ta med nummerkolumnen. Fyll i värdena, som bör börja med det nummer du har noterat tidigare.
5. Upprepa importen. I **Konfigurera** i**mportinställningarna** väljer du alternativet *Slå ihop – uppdatera tomma fält* i fältet **Åtgärd**. Detta kommer att se till att företags- eller kontakternas nummerfält fylls i med de värden du inkluderade i din fil.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6684105-s1ttAzGCjydXHHkozYTYfkx2b3iPSK1aTNFo9buumMig9Qq0sWkbmd6ph2IFjwLp-0/image-20260515151355-2.png)
6. Gå tillbaka till fliken **Nummertilldelning**, dubbelklicka på företags- eller kontaktnummer och i fältet Nästa nummer fyll i numret som ska tilldelas de nya posterna. Detta nummer ska vara 1 nummer större än det sista numret i din importfil.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6684107-1ZAFUdkPwJqjwLxG5azh2268T6ZjNj3Hw2wwwRB99H0IpXdM3oTPxlAmXsqyo9b4-0/image-20260515151506-3.png)

**Notera!**

1. Vi rekommenderar att du tar en säkerhetskopia innan du gör några ändringar direkt i databasen. Denna [FAQ](https://community.superoffice.com/sv/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) förklarar hur man gör det.
2. Se till att inga nya företag/kontakter skapas när du utför en import eftersom det kan påverka nummersekvensen.
3. Om du inte är säker på processen rekommenderar vi att du använder SuperOffice-konsulter. Konsulttjänsten innebär en avgift. Vänligen kontakta din SuperOffice-kontaktperson om du vill få mer information om den här tjänsten.
4. Om du vill ändra konfigurationen så att nummerfältet inte är obligatoriskt på kontaktkortet, välj alternativet **Tillåt tomma (1)** i räknardialogen.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6684127-UCBa6cs9ZlaXdgPoKNBqtiz90HtUNZlIcZAr8x7XGhiJCjdu6ffAOojIE5TQZGce-0/image-20260515151622-4.png)

**Mer information**

Forum: [Provisional Solution to: Company and contact number field not updated during import](https://community.superoffice.com/sv/technical/forums/product-forums/crm-web-application/provisional-solution-to-company-and-contact-number-field-not-updated-during-import/)

Önskning: [Import and Number allocation problem](https://community.superoffice.com/sv/product-releases/bugs-wishes/product-issue/?bid=8686&azure=1)
