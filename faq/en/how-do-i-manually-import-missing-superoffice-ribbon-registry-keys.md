---
title: "How do I manually import missing SuperOffice Ribbon registry keys?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-manually-import-missing-superoffice-ribbon-registry-keys/
lang: en
updated: "30 Jan 2026"
---

# How do I manually import missing SuperOffice Ribbon registry keys?

Updated on 30 Jan 2026

I have [installed SuperOffice WebTools](https://community.superoffice.com/en/support-faqs/faq/what-is-superoffice-webtools-and-what-does-it-do/) (or MailLink), but SuperOffice Ribbon has not appeared in my MS Office application ribbon. It is no visible in the list of application Add-ins either. Why does it happen and how do I fix it?

In some cases, during the installation SuperOffice Ribbon add-in keys in HKEY\_CURRENT\_USER hive are not created, therefore the SuperOffice Ribbon will not be visible in Outlook (if you use SuperOffice Web application or Online) or Word, Excel, Powerpoint (if you use SuperOffice Windows application). Please follow the steps below to import SuperOffice Ribbon add-in keys, when they are missing:

- [Step 1. Confirm that SuperOffice Ribbon add-in keys are missing](https://community.superoffice.com/en/support-faqs/faq/how-do-i-manually-import-missing-superoffice-ribbon-registry-keys/#1)
- [Step 2. Import SuperOffice Ribbon registry keys manually](https://community.superoffice.com/en/support-faqs/faq/how-do-i-manually-import-missing-superoffice-ribbon-registry-keys/#2)

**Step 1. Confirm that SuperOffice Ribbon add-in keys are missing**

1. Log in to your Terminal Server as a user (not an administrator).
2. In the search box, type in *regedit* and open the Registry Editor program.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6353063-R5nY03dbbRwkP0t7zX9b0atc7zeYManWMPruqpnGYF82ppT9GgXQna9ZZ8AKyDNo-0/image-20251006103350-1.png)
3. Navigate to *HKEY\_CURRENT\_USER\Software\Microsoft\Office\Outlook\Addins.* Check if SuperOfficeRibbon keys are present in Outlook Addin list. In the example in the screenshot, SuperOfficeRibbon keys are present.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147301-IoAf8I19nSXAJSfTXBsw5y4U8GywsyaZ77g88eK8w9pGtl6JwePrdrFOqGFlL7Hm-0/image-20250326172813-3.png)

**Step 2. Import SuperOffice Ribbon registry keys manually**

1. [Download Windows registry keys.](https://superoffice.sendsafely.eu/receive/?thread=SAKR-DRGK&packageCode=knbquXU8E3fNFZhEvv9fV9JUg7Jaw4oEvlmRFuUDfbo#keyCode=3vhUnMeabP6h1VfJA94Np9bHGxpzUbdE4InH8Qclths)
2. Close Outlook
3. Right-click on the downloaded file it and click **Edit in Notepad**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147356-YJCMEKmlJK1x1Pf1IzgYGYsa15h9kos8dbSeNiBZzph0Yy4fJFpWXAe0umQ0Y3CH-0/image-20250326173940-8.png)
4. Make sure that the line **Manifest** points to the correct location of the Mail Link installation on your Terminal server and save the file.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147539-18mxTBU1zt5stGAxeFpiQfLnPEbW8R2ZAfm008XIfBJN7mgWW19e35Ar3K6X9NPe-0/image-20250327083809-2.png)
5. Double-click on the file, then click **Run** to import the keys.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147540-QIAEgwMPnutt1oCFQDPedPm7kPNWaKe7IbiOYbL1Pb3Q6WLCJ8gSpgBfw1iFr87r-0/image-20250327083837-3.png)
6. Click Yes to continue.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147552-BY8bGISNTr1YNmUwnzKyz1PP5NeAmfpbC5KjQeUh5FgOrqwPrcLl6EzEKA3FwLNs-0/image-20250327083926-5.png)
          ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147553-bmI1MjRSNjUa9aUwBPdR0LXpN47f8dNUYJIrDUMmCyTgU6oqMdgUOUIM2yIUP3G9-0/image-20250327083939-6.png)

​**Note!**

1. Incorrectly editing a Windows registry can permanently damage your computer or server (if you work on Citrix/Terminal Server), we do not recommend to delete or adjust any key if you are not confident why it is done. Moreover, we recommend to back up the Windows registry before making any change, check [this article](https://neosmart.net/wiki/backup-restore-registry/) to learn how to do it.

2. If you are missing the SuperOffice Ribbon add-in in MS Word, Excel, PowerPoint please follow the same instructions described above, but use SuperOffice Ribbon in Word, PowerPoint, Excel file from the attachment section. Be aware that these add-ins are available only for SuperOffice Windows application users.
