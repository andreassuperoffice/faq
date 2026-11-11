---
title: "Which SuperOffice references should I remove when doing advanced reinstall of SuperOffice WebTools and/or MailLink?"
url: https://community.superoffice.com/en/support-faqs/faq/which-superoffice-references-should-i-remove-when-doing-advanced-reinstall-of-superoffice-webtools-andor-maillink/
lang: en
updated: "26 Nov 2025"
---

# Which SuperOffice references should I remove when doing advanced reinstall of SuperOffice WebTools and/or MailLink?

Updated on 26 Nov 2025

I have been recommended to uninstall SuperOffice WebTools and clean up all the old references to WebTools installation, that could be causing the problem. Which are these references that I have to remove manually?

**Note!** Editing the Windows registry and AppData folder can permanently damage your computer or server (if you work on Citrix/Terminal Server), so do not delete or adjust any key or file if you don't know specifically why you are doing it.

To do an advanced (clean) SuperOffice WebTools re-installation, follow the steps below:

1. Uninstall SuperOffice WebTools from the **Programs and Features,** check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-webtools/) if you are not sure how to do it.
2. Some of the old references, after uninstalling SuperOffice WebTools, can be found in the AppData folder and in the Windows registry.

To remove references to the old WebTools installation from an **AppData** folder, follow the steps below:

1. Navigate to the *C:\Users\[user]\AppData\Local\SuperOffice*
2. In the SuperOffice folder, you should find a **SuperOffice 7 Web Extensions** folder, which you have to delete.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147286-dxBiRCMXBrkesYio5gYP46XSgCfjRmyR8qlW8CLhxtJAz9lGdTeuoPIs379rnzhX-0/image-20250326171113-2.png)
3. Navigate to the *C:\Users\[user]\AppData\Roaming\SuperOffice*
4. In the SuperOffice folder, you should find the **MailLink** and **TrayApp** folders; delete them.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147287-7SSyuTHzxteKXo9pASjOD3x0NFe17YTpRSKSqSYqe9hgZEh35WXNTDWE94wgja08-0/image-20250326171137-3.png)

To remove references to the old installation from the Windows registry, follow the steps below:

1. Open the Windows Registry Editor (also known as "regedit") by searching for it in the Taskbar and typing "Regedit".

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147294-kxEhmycEt98kzt4R8sI4ZoNC6kh5Mk9flfdJC2RLhqe0587unaM6i9xZtG9CclDS-0/image-20250326171749-4.png)
2. Click on **Edit** and **Find**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147295-MMtMHqfGliBXlQ6u2ayMwxw5ASDT19H6acjlKIJ4Nxh4GTPSUzFsHpBf88eS2WbB-0/image-20250326171842-5.png)
3. In the **Find what** field, type in *superoffice* and click **Find Next**, it will find registry keys, which have the keyword *"SuperOffice"* in the name.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147296-HzLLue8kX1aS1hn6lFlQnJo6xayG38hhRcQPqD6RaliHC3FKcYo3AtDGBP1YcANl-0/image-20250326171929-6.png)
4. Select the key, right-click on it, and choose **Delete**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6147298-aKPf44RlMUN2OKwgrStFXDO8cxfCJFDtkwK9wFNioqIOLfPpi6tJoqTBkWyI9IEO-0/image-20250326172119-8.png)
5. Repeat step 3 until the registry is cleaned up from SuperOffice keys. To do a cleanup faster, you can use the **F3** button, which is a shortcut to search the last search string faster.

**More information**

Docs:[Technical overview on SuperOffice WebTools](https://docs.superoffice.com/en/document/webtools/technical-overview.html)
