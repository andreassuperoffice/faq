---
title: "What to do when SuperOffice Ribbon is not loaded and I get an error \"8007007e\" The specified module could not be found\" after opening my Outlook?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-ribbon-is-not-loaded-and-i-get-an-error-8007007e-the-specified-module-could-not-be-found-after-opening-my-outlook/
lang: en
updated: "12 Jun 2025"
---

# What to do when SuperOffice Ribbon is not loaded and I get an error "8007007e" The specified module could not be found" after opening my Outlook?

Updated on 12 Jun 2025

After I open an Outlook application I get an error and an error in Mail Link log file is:

*OUTLOOK.EXE: The following errors were encountered. MailLink will exit: Unable to create object of type "MailItem": System.IO.FileNotFoundException: Retrieving the COM class factory for component with CLSID {4BC25952-118E-4558-AC1F-9F88E9996D20} failed due to the following error: 8007007e The specified module could not be found. (Exception from HRESULT: 0x8007007E).

Unable to create object of type "MapiUtils": System.IO.FileNotFoundException: Retrieving the COM class factory for component with CLSID {F429108D-6DD8-4827-9F01-8C13BE5CF8DD} failed due to the following error: 8007007e The specified module could not be found. (Exception from HRESULT: 0x8007007E).

Unable to create object of type "RDOSession": System.IO.FileNotFoundException: Retrieving the COM class factory for component with CLSID {39AB7A13-B531-450E-8F7A-EA94C3F3C05F} failed due to the following error: 8007007e The specified module could not be found. (Exception from HRESULT: 0x8007007E).*

Why does it happen and how do I fix it?

There are three known solutions on how to fix this error:

- [Correct the folder path to redemption.dll](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-ribbon-is-not-loaded-and-i-get-an-error-8007007e-the-specified-module-could-not-be-found-after-opening-my-outlook/#1)
- [Re-register the .dll file](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-ribbon-is-not-loaded-and-i-get-an-error-8007007e-the-specified-module-could-not-be-found-after-opening-my-outlook/#2)
- [Repair or reinstall MS Office](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-ribbon-is-not-loaded-and-i-get-an-error-8007007e-the-specified-module-could-not-be-found-after-opening-my-outlook/#3)

**Note!** Before Web Tools versions 11 *redemption.dll* was called *soredemption.dll*

​

**Correct the folder path to *redemption.dll***

To fix the incorrect path to ***redemption.dll*** please follow the steps below:

1. Open the Windows Registry Edit by typing 'Regedit' in the search bar on your computer.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147299-aHzH1OQksFdpHSLNYxoJmQ99METrmXcFmSoYcOdmMdwnuzDOEInniMI2Nx6800LH-0/image-20250326172509-1.png)
2. Click on the **Edit** and the **Find** buttons

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6237322-9uR01MkfWBJhRARCxI7mDwWWGmt3qLUZPhuYt78iLDjdtuBC54kCM1DSwnWpeB2t-0/image-20250612141551-1.png)
3. In the search dialog type ***redemption.dll***

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6237329-Wilje6DzPf42mtF4i2Qe7pMmRPuBTaLqIfdMHqAq6DYRjRoBCy0MFEqBgWs4HbGl-0/image-20250612141832-2.png)
4. Make sure that all the references to ***redemption.dll*** are pointing to the correct folder structure.

   **Note!** Incorrectly editing a registry can permanently damage your computer or server (if you work on Citrix/Terminal Server), so do not delete or adjust any key if you don't know specifically why you do it. We recommend to back up the Windows registry before making any change. You can find instructions on how to do it in [this article.](https://neosmart.net/wiki/backup-restore-registry/)

​

**Try to re-register the *redemption.dll***

 To re-register ***redemption.dll***follow the steps below:

1. Open the Command Prompt (CMD) by typing 'CMD' into the search bar

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6237342-5hNimrmjchqgXi0JeEa28536bkyWZQLbMOyLo3uluA2aNWjXYroC2ON4BuNLIDmJ-0/image-20250612142157-3.png)
2. In the CMD [navigate](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands) to path **%superofficefolder%\MailLink**
3. Then type in **regsvr32 *Redemption.dll*** This command will re-register dll.

​

**Repair or reinstall MS Office**

If the suggestions above did not help, please try to:

1. Try to use the *Repair* function in Microsoft Office. Please read a Microsoft article [Repair an Office application](https://support.office.com/en-us/article/Repair-an-Office-application-7821d4b6-7c1d-4205-aa0e-a6b40c5bb88b) to learn more about it.
2. If Office repair did not help, please try to reinstall Microsoft Office application.

.

**More information**

FAQ: [What to do when SuperOffice Ribbon is not loaded and I get an error after opening my Outlook?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-ribbon-is-not-loaded-andi-get-an-errorafter-opening-my-outlook/)
