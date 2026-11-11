---
title: "What to do when SuperOffice archiving button has disappeared from Outlook?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-archiving-button-has-disappeared-from-outlook/
lang: en
updated: "21 Jun 2025"
---

# What to do when SuperOffice archiving button has disappeared from Outlook?

Updated on 21 Jun 2025

The SuperOffice archiving button disappeared from Outlook. Why does it happen and how do I fix it?

There are 4 common causes of this situation:

- You have recently updated Windows or Microsoft Office on your computer.
- Outlook believes that SuperOffice Ribbon is running too slow, affecting the overall Outlook performance.
- Your computer, the Microsoft Office package, or the Outlook application crashed just before SuperOffice Ribbon disappeared.
- Mail Link has been installed by another Windows user than the one which is using Outlook.

To get your SuperOffice Ribbon back follow the steps below:

1. Right-click on the **Outlook Ribbon** and click on the **Customize the Ribbon** item on the menu.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111766-QrpX4XKy7LmAjOgZt2TY7kZJgjlapl6NAE4uIeMmPuROmMkz0qd04wxDPOF9ZChG-0/image-20250304161912-1.png)
2. Click on the **Add-ins** button on the left-hand side to open the Add-in screen and look for SuperOffice Ribbon there.

- If you found SuperOffice Ribbon in the **Active (1)**section, [check this section.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-archiving-button-has-disappeared-from-outlook/#1)
- If SuperOffice Ribbon is in the **Inactive (2)** section, [check this section.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-archiving-button-has-disappeared-from-outlook/#2)
- If SuperOffice Ribbon is in the **Disabled (3)** section, [check this section.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-archiving-button-has-disappeared-from-outlook/#3)
- If you cannot find SuperOffice Ribbon on the list, [check this section.](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-archiving-button-has-disappeared-from-outlook/#4)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111774-AIdjspfjw15BCWgotJhan0mgRm9iOPy0pIjRUdTkwHTpWm9xq2wACzkf9tMFMqd6-0/image-20250304161927-2.png)

​

**SuperOffice Ribbon is in the Active section**

If you find SuperOffice Ribbon in the **Active** section, but it is still not visible in the Outlook Ribbon, it could be that:

- Visual Studio 2010 Tools for Office Runtime (VSTO), which is a prerequisite for SuperOffice Ribbon to work is not installed on the computer. Please download it from [here](https://www.microsoft.com/en-sg/download/details.aspx?id=105522).
- The issue is caused by a [known bug](https://community.superoffice.com/en/product-releases/bugs-wishes/product-issue/?bid=22220&azure=1), please check it for more information.

​

**SuperOffice Ribbon is in the Inactive section**

If you find SuperOffice Ribbon in the **Inactive** section, you should do the following:

1. At the bottom of the screen, select **COM Add-ins (1)** from the **Manage field** menu and click **Go (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111775-8KawpbJeQYPDwAaalKYMJ2kH18W0OTmTBwFLsRBN1SLtzbF64yUMm8qX45ONJtj5-0/image-20250304162002-3.png)
2. Tick the box next to **SuperOffice Ribbon (1)** and close the dialog by clicking **OK (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111776-G3itLyEqZDCYeoI19DHPyWAkPOOADOhakjfzS5JpBI80SBLpE3P8Z6Zkgcozx4JO-0/image-20250304162012-4.png)
3. SuperOffice Ribbon should be visible now. In some cases, you might need to restart your Outlook before the ribbon reappears.

   **Note!** If next to **Load Behavior** you see status **Deleted** or **Not loaded**, SuperOffice Ribbon Load Behavior Windows Registry needs to be adjusted, check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-adjust-the-windows-registry-key-that-is-in-charge-of-loading-superoffice-ribbon-to-make-the-ribbon-visible/) telling how to do it.
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111777-ZRgEAI0RZ6f3KpiC9OE6UlOBNY0IMEZTfKxgEDPMYO5Eg1DzGOQfcD9djwa19aDz-0/image-20250304162025-5.png)

​

**SuperOffice Ribbon in the Disabled section**

If you find SuperOffice Ribbon in the **Disabled**section, you should do the following:

1. At the bottom of the screen, select **Disabled Items** from the **Manage field** menu, and click **Go**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111788-NNXQJMwDRlH98yfqioZr4ulGLDC0kp2NrIEi0a3ayyforBSFW1DezuPqb0U9i4b4-0/image-20250304162044-6.png)
2. Select **SuperOffice Ribbon (1),** click **Enable (2),**and **Close (3)**the dialog box.
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111865-OD1jNtUQsDlXFsB2gguhDs6aB1NDbzkJAZ5tP9SfPzKZj71BGFtmydaUp20Cl80g-0/image-20250304162904-2.png)
3. Then, in the same place select **COM Add-ins (1)**and again click **Go (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111790-Bi8UJPyNTpFozTslBoaK88jbDNL6bqyQA9OEsWUl7cshqh4seRMmqFrP3yDcm4c5-0/image-20250304162107-8.png)
4. Tick the box next to **SuperOffice Ribbon (1)** and close the dialog by clicking **OK (2)**. SuperOffice Ribbon should be visible now. In some cases, you might need to restart your Outlook before the ribbon reappears.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111791-fJjaugMm7iQqH4sP5ldmmDL4J1D35TnG7obyjH687flX6ZGez7odlLAns8K4Wj7j-0/image-20250304162121-9.png)

   **Note!** If next to **Load Behavior** you see status **Deleted** or **Not loaded**, SuperOffice Ribbon Load Behavior Windows Registry needs to be adjusted, check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-adjust-the-windows-registry-key-that-is-in-charge-of-loading-superoffice-ribbon-to-make-the-ribbon-visible/) telling how to do it.

​

**SuperOffice Ribbon cannot be found in the list**

If you are sure that SuperOffice Mail Link is installed on your computer, but the SuperOffice Ribbon does not appear in the Outlook Add-in list at all, try to [reinstall Mail Link, check this FAQ how to do it.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-webtools/)

If after reinstalling Mail Link SuperOffice Ribbon is still invisible then check if the SuperOffice registry key has been created in your Windows profile. To do so in *regedit.exe* navigate to *HKEY\Current User\Software\Microsoft\Office\Outlook\Addins* where you could see a key called *SuperOfficeRibbon-Outlook*.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6111864-abMQUqoR745BI6194ZzpAIi3ogS0mRh96O0a9uOsfb2nuqlUYT6WYxW4Ec2fNTMG-0/image-20250304162857-1.png)

If it is not created automatically, most of the time that is due to missing rights on the Windows profile. In this situation, we suggest either give the user local administrator rights on the computer and try to install Mail link *with the .msi file* or import/copy missing registry keys from the computer where SuperOffice Ribbon is visible, [check this FAQ how to do it.](https://community.superoffice.com/en/support-faqs/faq/how-do-i-manually-import-missing-superoffice-ribbon-registry-keys/)

**Note!** Incorrectly editing a registry can permanently damage your computer or server (if you work on Citrix/Terminal Server), so do not delete or adjust any key if you don't know specifically why you do it. We recommend to back up the Windows registry before making any change. You can find instructions on how to do it in [this article.](https://neosmart.net/wiki/backup-restore-registry/)

**More information:**

FAQ: [What to do if SuperOffice Ribbon gets disabled every time we start Outlook?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-the-superoffice-ribbon-add-in-gets-disabled-or-inactivated-every-time-i-start-outlook/)

FAQ: [What can I do when I run into the problems with archiving e-mails from Outlook to SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/what-can-i-do-when-i-run-into-the-problems-with-archiving-e-mails-from-outlook-to-superoffice-crm/)
