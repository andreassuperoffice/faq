---
title: "Vad gör jag när SuperOffice Outlook-tillägget inte visas i Outlook?"
url: https://community.superoffice.com/sv/support-faqs/faq/vad-gor-jag-nar-superoffice-outlook-tillagget-inte-visas-i-outlook/
lang: sv
updated: "4. mars 2025"
---

# Vad gör jag när SuperOffice Outlook-tillägget inte visas i Outlook?

Uppdaterad på 4. mars 2025

SuperOffice Ribbon har försvunnit. Just innan detta fick jag en notifikation från Outlook som informerade mig om att SuperOffice Ribbon har blivit inaktiverat, samt att den ej är synlig längre från Outlook. Varför händer detta, och hur åtgärdar jag det?

Det finns 4 vanliga orsaker för detta problem:

- Du har nyligen uppdaterat Windows eller Microsoft Office på din dator.
- Outlook tror att SuperOffice Ribbon startar för långsamt / påverkar prestandan i Outlook.
- Din dator eller Microsoft Office alternativt Outlook kraschade just innan SuperOffice Ribbon försvann.
- Mail Link har blivit installerat av en annan Windows användare än den som använder Outlook.

För att få tillbaka SuperOffice Ribbon, följ stegen nedan:

1. Högerklicka på din **Outlook Ribbon** och välj **Customize the Ribbon** alternativet i menyn.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111903-rPL3KP8OueoRUncMLPQRCsEsQM0AsIhOGZ7K5xNaziDcgJFgNbo17HLkg50bo5HM-0/image-20250304163838-1.png)
2. Klicka på **Add-ins** knappen på den vänstra sidan sidan för att öppna Add-in menyn och kolla efter SuperOffice Ribbon där.

- Om du hittadar SuperOffice Ribbon i [**Aktiv (1)**](https://community.superoffice.com/sv/support-faqs/faq/vad-gor-jag-nar-superoffice-outlook-tillagget-inte-visas-i-outlook/#1) delen, kolla här.
- Om du hittadar SuperOffice Ribbon i [**Inaktiv (2)**](https://community.superoffice.com/sv/support-faqs/faq/vad-gor-jag-nar-superoffice-outlook-tillagget-inte-visas-i-outlook/#2) delen, kolla här.
- Om du hittadar SuperOffice Ribbon i [**inaktiverad (3)**](https://community.superoffice.com/sv/support-faqs/faq/vad-gor-jag-nar-superoffice-outlook-tillagget-inte-visas-i-outlook/#3) delen, kolla här.
- Om du inte hittar SuperOffice Ribbon alls, **[kolla här.](https://community.superoffice.com/sv/support-faqs/faq/vad-gor-jag-nar-superoffice-outlook-tillagget-inte-visas-i-outlook/#4)**
  ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111904-XeQ8C8sFjU9i5Hegc6BxXmX76qkz5CQ4wMpkUZFRjUFEop2n2eZqaYrexZRaECr4-0/image-20250304163855-2.png)

**SuperOffice Ribbon ligger som aktiverat**

Om du hittar SuperOffice Ribbon i avsnittet **Aktivt**, men det fortfarande inte syns i Outlook Ribbon, kan det ber på:

- Visual Studio 2010 Tools for Office Runtime (VSTO), som är en förutsättning för att SuperOffice Ribbon fungerar, inte är installerat på datorn. Ladda ner den [här](https://www.microsoft.com/en-us/download/details.aspx?id=105522).
- Problemet orsakas av [en känd bugg](https://community.superoffice.com/sv/product-releases/bugs-wishes/product-issue/?bid=22220&azure=1). Vänligen läs om den för mer information.

**SuperOffice Ribbon är under inaktiva add-ins**

Om du hittar SuperOffice Ribbon i listan över **inaktiverade** add-ins, gör följande:

1. Längst ner på skärmen, välj **COM Add-ins (1)**från **Manage fältet,** och välj därefter **Go (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111905-EKqrhOnHWRWHZpni6tWGnWKwLt5dqzBAO2mnKth0Goyn4mPc4h84Py613zZELsPu-0/image-20250304163908-3.png)
2. Klicka i checkrutan för **SuperOffice Ribbon** **(1)** och stäng dialogrutan genom att välja **OK (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111906-loWRG1gBYIDEubzuFb7f45Z1GDynMrrcMgtc43t5MMU8Fd86ubEwy34qnbxGaUkq-0/image-20250304163915-4.png)
3. SuperOffice Ribbon ska nu återigen vara synlig. I vissa fall behöver du starta om Outlook innan den dyker upp.

**Notera!** Om du bredvid texten **Load Behavior** ser statusen **Deleted** alternativt **inte laddad**, så behöver SuperOffice Ribbon Load Behavior i windows registret uppdateras. Kolla [denna FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-adjust-the-windows-registry-key-that-is-in-charge-of-loading-superoffice-ribbon-to-make-the-ribbon-visible/) för en beskrivning om hur man gör detta.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111907-E60SpgZRsQyyxcgMEtrf2OF8dZcldMFaHOmYY0NR5eFQG0laSBpkShrn7bwxG8Bm-0/image-20250304163921-5.png)

**SuperOffice Ribbon under delen Inaktiverad.**

Om du hittar SuperOffice Ribbon under **inaktiverade** add-ins, följ nedanstående steg:

1. Längst ned på skärmen, välj **Inaktiverade objekt (1)** från **Manage fältet**, och trycker därefter **Go (2)**.
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111908-mIaxiz4da17BZ1nC5zuJbcrNmfx5Qib2Bmp6OJ8IQWbn6LNwopt5hq2DNZC0K9QN-0/image-20250304163930-6.png)

2. Välj **SuperOffice Ribbon (1)**, tryck **Enable (2)**och **stängt (3)**därefter dialogrutan.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111909-5r6k3sgQKI7du4GNRHiIqfkHTf32SyR2MemDBjM8iSkFE7KtA8j4ha2YSL5ue9Q8-0/image-20250304163938-7.png)
3. Därefter från samma ställe, välj **COM Add-ins (1)** och välj **Go (2)**igen.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111911-s2d9lX6TbAeZ6EX5WXq6W9707Y8JknW0jOLRNiFTOaWrCggcTEZRm6Ng1XA5mhYF-0/image-20250304163950-8.png)
4. Markera checkrutan för **SuperOffice Ribbon (1)**, och välj **OK (2)**för att stänga rutan. SuperOffice Ribbon ska nu vara synlig igen, men ibland behöver man starta om Outlook för att ändringen ska träda i kraft.
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111969-BEGKHXUgGQ8IByxAdL6WcJZiLhrbUpbXHXFyw4fNGBehXUGWMm52R2C041isgEdp-0/image-20250304171336-9.png)

**Notera!** Om du bredvid texten **Load Behavior** ser statusen **Deleted** alternativt **inte laddad**, så behöver SuperOffice Ribbon Load Behavior i windows registret uppdateras. Kolla [denna FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-adjust-the-windows-registry-key-that-is-in-charge-of-loading-superoffice-ribbon-to-make-the-ribbon-visible/) för en beskrivning om hur man gör detta.

**SuperOffice Ribbon syns inte alls i denna lista**

Om du är säker på att SuperOffice Mail Link är installerad på din dator, men att SuperOffice Ribbon inte är synlig i Outlooks lista över Add-ins överhuvudtaget, försök ominstallera Web Tools, denna [FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-web-tools/) beskriver hur man gör detta.

Om SuperOffice Ribbon inte är synlig även efter en ominstallation, dubbelkolla så att registernycklarna i Windows registry har blivit skapade för din Windows profil. För att göra detta i regedit.exe, navigera till HKEY\Current User\Software\Microsoft\Office\Outlook\Addins där ska du se en nyckel som heter SuperOfficeRibbon-Outlook.
![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111970-6mYYWUUmAuJQpIqp4PbxsA9RZfbRxEY52enSdyowKC14i9XeBJOWppKjrtdWplpm-0/image-20250304171351-10.png)

Om den inte skapas per automatik, så beror det oftast på begränsade rättigheter för användarens Windows profil. I detta läge rekommenderar vi antingen att ge användaren lokala adminbehörigheter för datorn och därefter försöka ominstallera på nytt med .msi filen, alternativt att importera dessa registernycklar från en dator där SuperOffice Ribbon är synlig. Kolla [denna FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-manually-import-missing-superoffice-ribbon-registry-keys/) för hur att göra detta.

**Notera!** Att inkorrekt redigera registret kan permanent skada din dator eller server (om du arbetar i Citrix/Terminal Server), så radera eller konfigurera inte dessa nycklar om du inte vet specifikt varför du gör det. Vi rekommenderar att ni tar en backup av registret innan några ändringar. Ni hittar instruktioner för hur man gör detta i [denna artikel](https://neosmart.net/wiki/backup-restore-registry/).

**Mer information:**

FAQ: [Vad gör jag om SuperOffice Ribbon blir inaktiverad varje gång vi startar Outlook?](https://community.superoffice.com/sv/support-faqs/faq/what-to-do-when-the-superoffice-ribbon-add-in-gets-disabled-or-inactivated-every-time-i-start-outlook/)
