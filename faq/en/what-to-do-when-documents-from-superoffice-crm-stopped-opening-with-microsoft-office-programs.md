---
title: "What to do when documents from SuperOffice CRM stopped opening with Microsoft Office programs?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-documents-from-superoffice-crm-stopped-opening-with-microsoft-office-programs/
lang: en
updated: "22 Jun 2026"
---

# What to do when documents from SuperOffice CRM stopped opening with Microsoft Office programs?

Updated on 22 Jun 2026

I used to be able to open, edit, and save documents from SuperOffice CRM with Microsoft Office programs. Now, documents from SuperOffice CRM are downloaded and opened locally, and changes made in existing documents are not saved back to SuperOffice CRM.

Why does it happen, and how do I fix it?

The described situations can occur when SuperOffice WebTools are not installed or not connected to your computer. To fix it, please follow the steps below:

[Step 1. Make sure the latest version of the SuperOffice WebTools are installed](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-documents-from-superoffice-crm-stopped-opening-with-microsoft-office-programs/#1)

[Step 2. Make sure the WebTools are active and connected](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-documents-from-superoffice-crm-stopped-opening-with-microsoft-office-programs/)

[Step 3. Configure the SuperOffice WebTools for your SuperOffice CRM account](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-documents-from-superoffice-crm-stopped-opening-with-microsoft-office-programs/#2)

​

**Step 1. Make sure the latest version of the SuperOffice WebTools are installed**

1. Open **Programs and Features** on your computer.
2. Make sure**SuperOffice Web Extensions** are in your Programs list. [Click here](https://community.superoffice.com/en/product-releases/release-notes/) to find the version number of the latest release.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746493-EpTpfPYlX1oxNo5quD8kycJHwXhimIRGDntgHro0BhItdQnCFtubYMRuzbXx69hw-0/image-20260621203609-1.png)
3. If you cannot find Web Extensions, please install and configure them. Read [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-download-and-install-webtools-for-superoffice-crm/) for more information on how to do this.

​

**Step 2. Make sure that the SuperOffice WebTools are active and connected.**​

1. Right-click the SuperOffice WebTools icon in the lower right corner of the Windows taskbar and select **Preferences.** If you do not see the SuperOffice WebTools icon, the WebTools may not be started. Contact your IT to make sure that the SuperOffice.TrayApp.Client.exe is always active.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746499-uOQYYsyw8kKf2PtpJA233sBtWnKnN8o5gXAMwuJHQEF090CNtXLTaiKMeikBdH3E-0/image-20260621205854-7.png)
2. In the WebTools **preferences**, check if you see your **Company name**:

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6136881-fjrSeJWTwphrYqfUtUr8KPoJl8RQwZ2AqjcLK3L36bUWs8iy1s5O7DdGLx59AZpn-0/image-20250320080412-3.png)

   If it is empty, the WebTools are not configured correctly. Please go to the last step (Step 3) of this FAQ.
3. If you see your Company name, close the preferences window. Right-click the SuperOffice WebTools icon in the taskbar again and this time, select **Login**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746500-qpgA2K0CIc9UboOEMJunDse5MjaOLwyascz4GkSAaZlCKAx9NIEZ3U2lKa2n5YAn-0/image-20260621210133-8.png)
4. In the new tab that opens, try to open a saved document. If it still does not open directly in an Microsoft Office application, continue to step 3 below.

​

**Step 3. Configure the SuperOffice WebTools to your SuperOffice CRM account.**

**Note!** This step is only necessary if Step 2 showed that your WebTools are not configured correctly. Always try step 2 first.

1. Click on the personal settings icon in the top right corner and choose **Download** - **SuperOffice WebTools.**

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746498-SobM6uSi5QUoiwN0YkxMcgOMX2LYz5KK753ohUpfcbylaUhNwZUYX4enM2cHtytx-0/image-20260621205724-6.png)
2. **One of two versions** of the Download SuperOffice WebTools window will open.

   - **If you see the Work faster with documents window**, click Click here to connect.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746494-MbSkG80g5R91GDd14EADnMSwR86DORBBhhEtWLDeryHFp3K68WiDoWK8zh3xk9AX-0/image-20260621205119-2.png)

   - **If you see the Personal computer Home/Office window**, select Personal computer Home/Office, select the e-mail client you use, and continue to the next screen. Then click "Click here to connect WebTools to this SuperOffice installation".

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746495-f23z8hj3U02Ap3hXXpo95uIRHENmeqLMxx389B1W1hlTnYt56Oxtkl3kBNP5IhoQ-0/image-20260621205245-3.png)
3. When the xxxxxx.*SoConfig* file is downloaded, please click on it to run.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6746497-eUeHLRgEI6jq5FSl4G5lafQiYSLq44RDZFR1E3Ntd68rxaEiyGDnGXtEhpwalZte-0/image-20260621205357-5.png)
4. You'll see a dialog in the right corner of your screen stating that SuperOffice needs to authenticate you to your SuperOffice CRM installation. Click **OK**, it will start an authentication via the browser, and when it happens, you'll see a success message.

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5375273-ldhZOkZc0oMWHk04PcjJco1atgRuXiryowZBd5fnrcsl4xi0d3lkTYUXYtXfjrKr-0/image-20230501112308-5.png)

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5375272-PmPp9tuP544hSFsyAu3sAdPGtqao4H8dGyz9JCUecc7SdKIf9J0j8d2K9jqRouwM-0/image-20230501112259-4.png)

   **Note!** If you use an authentication provider (Microsoft 365 or Google), you might be redirected to their webpage for re-authentication (enter your user name and password) to complete the connection to SuperOffice CRM.

   Then click **OK,**refresh your internet browser, and your connection to the SuperOffice WebTools is repaired.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6136889-hTUHoxQ8sImqaIYl3SfAXY0GwhOBL5P9yBHwA5W4xjeb9AbB8gA0gGFzF7xqYI4t-0/image-20250320080905-1.png)

**Note!**This FAQ explains how to troubleshoot SuperOffice Web Extensions, which is used for opening and saving documents from SuperOffice CRM. If e-mails no longer open in Outlook and you still use MailLink, make sure that MailLink is installed and configured. MailLink is installed separately from Web Extensions. You can find more information [here](https://community.superoffice.com/en/support-faqs/faq/why-is-maillink-not-installed-when-i-download-webtools/).

**More information**

FAQ: [What can I do when I run into problems with SuperOffice WebTools?](https://community.superoffice.com/en/support-faqs/faq/what-can-i-do-when-i-run-into-the-problems-with-superoffice-webtools/)

FAQ: [What is "SuperOffice WebTools" and what does it do?](https://community.superoffice.com/en/support-faqs/faq/what-is-superoffice-webtools-and-what-does-it-do/)

FAQ**:**[How do I reinstall SuperOffice WebTools?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-webtools/)
