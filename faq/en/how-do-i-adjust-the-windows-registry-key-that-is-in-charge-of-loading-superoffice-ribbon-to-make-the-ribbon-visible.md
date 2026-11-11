---
title: "How do I adjust the windows registry key that is in charge of loading SuperOffice Ribbon to make the ribbon visible?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-adjust-the-windows-registry-key-that-is-in-charge-of-loading-superoffice-ribbon-to-make-the-ribbon-visible/
lang: en
updated: "20 Mar 2026"
---

# How do I adjust the windows registry key that is in charge of loading SuperOffice Ribbon to make the ribbon visible?

Updated on 20 Mar 2026

SuperOffice Ribbon has disappeared from my Outlook Ribbon. Which is the windows registry key in charge of loading SuperOffice Ribbon and how do I adjust it to bring it back?

In the Add-ins list in Outlook, you can check the current load behavior of the SuperOffice Add-in. The load behavior should be set to "Load at Startup" like in the screenshot below, and a Windows registry key called Load behavior has a value of 3.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6198225-Z1QwQ17zueLzZT0MY9RA2iaosLX677tHpSHTYPOA4EipZhb6uhkLcRgtxHrajGBi-0/image-20250508132653-1.png)

In some situations, SuperOffice Add-in cannot be loaded, so to make it load again, you can follow the steps below:

1. In the search box, type in *regedit*and open the registry editor program.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6596259-MRbfjiYcTIhrzCeFTRom3zsk2gIIeEyGuF3mmWwHqEcZ2UPpNwMff0s4z8lzCtA9-0/image-20260320090545-1.png)
2. Navigate to *Computer\HKEY\_CURRENT\_USER\Software\Microsoft\Office\Outlook\Addins\SuperOfficeRibbon-Outlook​*

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6198249-4k2hF5XF1Mu3qJbHzAWP0ZHskeGc5iO78RuUcUTrcrAMLuBtPoWAYeOAfHgyghPM-0/image-20250508133727-2.png)
3. The **LoadBehavior** registry key should have the value *0x0000000 (3)*.If it doesn't double-click on the key, in the **Value data** field type 3, and click **OK**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6198250-9esAf1igLuNTZtfbUynu4RCQz3PQXis6tDKiXyPz8zmTK5ZCrKoNCBW59wKxaxg8-0/image-20250508133815-3.png)
4. Restart your Outlook, and now the SuperOffice Ribbon should be visible.

If, after restarting Outlook, the Load Behavior value reverts to 0, 1, or 2, we recommend reinstalling MailLink using the Windows user account with local administrator rights. Check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-webtools/) to learn how to do it.

If this did not help, please [register a support request.](https://cs.superoffice.com) We will be able to help you more quickly if you provide us with these log files:

- Mail link log file, check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-send-a-superoffice-mail-link-log-file-to-superoffice-support/) to learn how to get it.
- Event Viewer log file, check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-send-an-event-viewer-log-file-to-superoffice-support/) to learn how to get it.

**Note!** Incorrectly editing a registry can permanently damage your computer or server (if you work on Citrix/Terminal Server), so do not delete or adjust any key if you don't know specifically why you are doing it. We recommend backing up the Windows registry before making any changes. You can find instructions on how to do it in [this article.](https://neosmart.net/wiki/backup-restore-registry/)

**More information:**

FAQ: [What to do if SuperOffice Ribbon gets disabled every time we start Outlook?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-the-superoffice-ribbon-add-in-gets-disabled-or-inactivated-every-time-i-start-outlook/)
