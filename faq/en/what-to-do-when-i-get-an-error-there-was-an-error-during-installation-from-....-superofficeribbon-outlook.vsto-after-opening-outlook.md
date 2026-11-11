---
title: "What to do when I get an error ¨There was an error during installation From: .... SuperOfficeRibbon-Outlook.vsto¨ after opening Outlook?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-there-was-an-error-during-installation-from-....-superofficeribbon-outlook.vsto-after-opening-outlook/
lang: en
updated: "27 Mar 2025"
---

# What to do when I get an error ¨There was an error during installation From: .... SuperOfficeRibbon-Outlook.vsto¨ after opening Outlook?

Updated on 27 Mar 2025

I am opening an Outlook and I get an error:

*There was an error during installation
From: file///C:/Programs Files (x86)/SuperOffice/SuperOffice Mail Link/SuperOfficeRibbon-Outlook.vsto
Downloading file///C:/Programs Files (x86)/SuperOffice/SuperOffice Mail Link/SuperOfficeRibbon-Outlook.vsto did not succeed*

Why does it happen and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6148875-TX5OBwbXgi0XiPnIn0RORIw0J8EkYrcylIE8URpoowMY3lDz5jwlyY4cRnrnPpzL-0/image-20250327140203-2.png)

The error occurs when:

- The VSTO (Visual Studio Tools for Office) run time version on your computer is older than VSTO 2010 (32bit or 64bit), the installation is not present or corrupted. If this is the case please try to install or reinstall the required version of VSTO, click [here](https://learn.microsoft.com/en-us/visualstudio/vsto/how-to-install-the-visual-studio-tools-for-office-runtime-redistributable?view=vs-2022) to download it.
- The location of the *SuperOffice-Outlook.vsto* component is wrong or corrupter. In this case please try to reinstall the SuperOffice Mail Link, check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-mail-link-when-i-use-the-superoffice-windows-application/) to learn how it is done. If reinstall did not help, make sure that SuperOffice Ribbon Add-in Manifest points to the correct location on your computer. [This FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-manually-import-missing-superoffice-ribbon-registry-keys/) explains how to check it.
- You have run *SuperOffice-Outlook.vsto* component manually. This is nor a recommended action, please read [this forum](https://community.superoffice.com/en/technical/forums/product-forums/crm-windows-application/why-we-should-not-run-.vsto-installer-manually) post for more information.

​If the suggestion above did not bring the SuperOffice Ribbon button back, [contact SuperOffice Support.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/)
