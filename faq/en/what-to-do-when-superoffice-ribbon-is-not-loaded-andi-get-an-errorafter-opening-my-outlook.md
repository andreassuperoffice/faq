---
title: "What to do when SuperOffice Ribbon is not loaded and I get an error after opening my Outlook?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-ribbon-is-not-loaded-andi-get-an-errorafter-opening-my-outlook/
lang: en
updated: "19 May 2025"
---

# What to do when SuperOffice Ribbon is not loaded and I get an error after opening my Outlook?

Updated on 19 May 2025

After I open Outlook I get an error:

*The following errors were encountered. MailLink will exit: Unable to create object of type "MailItem": System.InvalidOperationException: Unable to load Outlook Redemption. Is SuperOffice MailLink installed correctly? (Looking for C:\Program Files (x86)\SuperOffice\SuperOffice Mail Link\redemption.dll) ---> System.IO.FileNotFoundException:Unable to locate 32-bit version of Outlook Redemption. Is SuperOffice MailLink installed correctly?*

Why does it happen and how do I fix it?

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4110761-auWftBhnnbMFwlaJlTl1tPn1w0Cr4DHPKiWyA9Zrwt0NICsFWIyWypEH4OeXUyNG-0/image008.png)

The error pops up when the folder path to*SuprOffice.Mail.Protocol.Handler.exe* component in the Windows registry is wrong, often it points to an old installation and it needs to be updated to a new one. Please follow the steps below to learn how to fix it:

1. In the search box on the taskbar, type **regedit** and open **Registry Editor** program

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147299-aHzH1OQksFdpHSLNYxoJmQ99METrmXcFmSoYcOdmMdwnuzDOEInniMI2Nx6800LH-0/image-20250326172509-1.png)
2. Navigate to the *Computer\HKEY\_CLASSES\_ROOT\SOMail\shell\open\command* (1)directory and double-click on the key (2).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6210263-Llq3Wtt5WFw0FFQMgBICwXIXa0U1jUG95JqOTzPtKoGg97pbO4DATbhOaPSKal1z-0/image-20250519121827-2.png)
3. Make sure that the folder path, which is found in the **Value data** field is pointing to the correct Mail Link installation location and has a symbol *"%1"* in the end. *E.g. "C:\Program Files (x86)\SuperOffice Mail Link\SuperOffice.Mail.ProtocolHandler.exe" "%1"*

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6210267-wXC5NZfAem9MopaU1zhipXNxj9NyNNkfj65hPxO8loit5gyrCzTAxb3G5hSJMtit-0/image-20250519121848-3.png)

   To test it, copy the folder path, which you found in the **Value data** field (without *SuperOffice.Mail.ProtocolHandler.exe part),* and paste it in the Windows Explorer. It should open the Mail Link installation folder (1) and the *SuperOffice.Mail.ProtocolHandler.exe* file (2) should be in the folder. If the path does not exist or points to the old Mail Link installation, find the current Mail Link installation on your computer and change the path to the correct one.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6210316-CZc0fiZFeEOpAUA2komXLTW615mTgGayGQ3RJoPUfPMTMtGOK8DtACIl4Mmpspcp-0/image-20250519123024-4.png)

**Note!** Incorrectly editing a registry can permanently damage your computer or server (if you work on Citrix/Terminal Server), so do not delete or adjust any key if you don't know specifically why you do it. We recommend to back up the Windows registry before making any change. You can find instructions on how to do it in [this article.](https://neosmart.net/wiki/backup-restore-registry/)

If this did not help to solve your problem, please raise a support request with SuperOffice Support via Help -> Contact Support inside your SuperOffice CRM application.

**More information**

FAQ: [What to do when SuperOffice Ribbon is not loaded and I get an error after opening my Outlook?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-ribbon-is-not-loaded-and-i-get-an-error-8007007e-the-specified-module-could-not-be-found-after-opening-my-outlook/)
