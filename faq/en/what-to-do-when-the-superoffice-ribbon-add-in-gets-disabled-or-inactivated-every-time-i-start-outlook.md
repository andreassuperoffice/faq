---
title: "What to do when the SuperOffice Ribbon add-in gets disabled or inactivated every time I start Outlook?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-the-superoffice-ribbon-add-in-gets-disabled-or-inactivated-every-time-i-start-outlook/
lang: en
updated: "3 Nov 2025"
---

# What to do when the SuperOffice Ribbon add-in gets disabled or inactivated every time I start Outlook?

Updated on 3 Nov 2025

Every time I open my Outlook the SuperOffice Ribbon Add-in gets disabled or inactivated. I can start it manually, but when Outlook is restarted, the SuperOffice Ribbon again is not visible. I some other situations I see this notification:

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184055-Xq19pib1CDMpMreUYG4zoz8rYgU93JlYrUmgGyHJYt8yfWFJpzUMWGA4a3L816og-0/image-20250424135126-1.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184056-mSODUYZeU6sj8tuol7xoPH0u9KeKefMFD01UDhwdLHo1omlMndHcHXWNbGBUshfD-0/image-20250424135300-2.png)

Why does it happen and how do I fix it?

If it is the first time when SuperOffice Ribbon add-in gets disabled, please try suggestions in [this FAQ](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-archiving-button-has-disappeared-from-outlook/).

If the add-in gets disabled every time you open your Outlook, first of all, please try to:

- [Force Outlook to always enable the SuperOffice Add-in](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-the-superoffice-ribbon-add-in-gets-disabled-or-inactivated-every-time-i-start-outlook/#1)
- [Change a Load Behavior value of SuperOffice Add-in](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-the-superoffice-ribbon-add-in-gets-disabled-or-inactivated-every-time-i-start-outlook/#2)

If that did not help, try the other two solutions:

- [Include a key that forces Outlook to always enable the SuperOffice Add-in](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-the-superoffice-ribbon-add-in-gets-disabled-or-inactivated-every-time-i-start-outlook/#3)
- [Remove keys from Disabled Items and CrashingAddinList](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-the-superoffice-ribbon-add-in-gets-disabled-or-inactivated-every-time-i-start-outlook/#4)

​

**Force Outlook to always enable the SuperOffice Add-in**

You can force the SuperOffice Ribbon add-in to be always enabled by following the steps below:

1. Click on the **File** in the Outlook menu bar and select **Slow and Disabled COM Add-ins**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184057-nWQsFzKG9dA5OiNbKR6WJdErkdbnaaxE1gQp0caRqw3qq6JY9sE70xN6k30FfMtT-0/image-20250424135431-3.png)
2. You'll see a list of add-ins, click **Always enable this add-in**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184062-sd0F6O6xAkpd32R4TFTdDWWGjcLYhNIccMeZbboxUMQXWzdEAzqmLeHJPWUzntlj-0/image-20250424135455-4.png)

**Note!** Starting from Outlook 2016 version, it is not possible to use the setting **Always enable this add-in**; it is only possible to stop monitoring an add-in for a maximum next 30 days.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184069-leq19Qxdhq9m5LE9TsxwRqENj2Ifhqo5IXF61go2E3jJPt15u7Mw8IIRws4S3iAT-0/image-20250424135619-5.png)

​

**Change a Load Behavior value of SuperOffice Add-in**

Please follow the steps below:

1. In the search box, type in *regedit*and open the Registry Editor program.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6351591-DhzLEyqeMumfghDsuDR6B4yWDPX0BexjbsugPGaNpyYF0OLBmpUbodmnEuHLURdW-0/image-20251003111158-1.png)
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184071-GpU6TKdLU7oWXnfJWOwMiUFmw11QYaplwsYOAmi55rfRYS7h8IClP8PwrzR24Hqr-0/image-20250424135748-7.png)
2. Navigate to *Computer\HKEY\_CURRENT\_USER\Software\Microsoft\Office\Outlook\Addins\SuperOfficeRibbon-Outlook​*and double-click on **LoadBehavior**:

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184074-jR8M5kz7iqftoBJ9XaB5ljMXI9YZL1OL48QgqphaqRSnSuSMELCydFyZDkjCtN3G-0/image-20250424140128-8.png)
3. The **LoadBehavior** registry key should have the value *0x0000000 (3)***;** if it doesn't, double-click on the key, in the **Value data** field type 3, and click **OK**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184091-MaJIargYCrm5wyNtBgptY4XQHmeHUqkSQuxgmhSdJdXgmifkEp0PAZfwJPB9O4GG-0/image-20250424140233-9.png)
4. Restart your Outlook, and now the SuperOffice Ribbon should be visible.

​

**Include a key that forces Outlook to always enable the SuperOffice Add-in**

Another possibility is to force Outlook to always load the SuperOffice MailLink add-in by adjusting the Windows Registry. Follow the steps below to do it:

1. In the search box, type in *regedit*and open the Registry Editor program.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6351591-DhzLEyqeMumfghDsuDR6B4yWDPX0BexjbsugPGaNpyYF0OLBmpUbodmnEuHLURdW-0/image-20251003111158-1.png)
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184071-GpU6TKdLU7oWXnfJWOwMiUFmw11QYaplwsYOAmi55rfRYS7h8IClP8PwrzR24Hqr-0/image-20250424135748-7.png)
2. Navigate tothe *Computer\HKEY\_CURRENT\_USER\Software\Microsoft\Office\16.0\Outlook\Resiliency\DoNotDisableAddinList*
3. Create a new value by right-clicking on the key area and choosing DWORD value.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184100-AXRQTFUzc4yukCxn9BA18ID4RuR0W5RSDMM76ip6dBH4rhEbZeOoGLhBo3lb9ZHu-0/image-20250424140702-10.png)
4. Set the name of the key to *SuperOfficeRibbon-Outlook* and fill the value with 1.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184107-9jyx2GEhHyep8n2jffocMfLMor1hahPyKpfxQQUg6gg1YXycuppxK9ZucQU6zg7D-0/image-20250424140800-11.png)
5. With this configuration, Outlook can still disable the SuperOffice Outlook Ribbon if it crashes, but it will not disable it because it loads too slowly.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184108-5PKlboR53Dk4txUyEwzGTkOstMuGNmrdAyPcMSO8hDzHMLoegUH3kPAMuojJJC2U-0/image-20250424140840-12.png)

   **Note!** If you use Outlook 2013, the registry value should look like this example: *HKEY\_CURRENT\_USER\Software\Policies\Microsoft\office\15.0\outlook\resiliency\addinlist RG\_SZ= add-in name Value = 1.*If this key does not exist in the registry, create it manually.

​

**Remove registry keys from Disabled Items and CrashingAddinList**

When MS Office identifies that an add-in caused an issue, it will ask the user if they want to disable the add-in. If the user clicks Yes, then it will be added to the DisabledItems key. You can follow the instructions below to learn how to remove these keys:

1. Shut down your Outlook**.**
2. In the Windows registry, navigate to the **DisabledItems** key:

   Outlook 2016: *HKEY\_CURRENT\_USER\Software\Microsoft\Office\16.0\Outlook\Resiliency\DisabledItems*
   Outlook 2013: *HKEY\_CURRENT\_USER\Software\Microsoft\Office\15.0\Outlook\Resiliency\DisabledItems*
   Outlook 2010: *HKEY\_CURRENT\_USER\Software\Microsoft\Office\14.0\Outlook\Resiliency\DisabledItems*
3. Right-click on the REG\_BINARY value you will find in the**DisabledItems** key and click on the **Delete** item in the menu**.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184125-SPp80GoHMu1JPWfAwheA1bStQc9t9qWc0nKDQWwUsBs6JFFbT8YhTcefGxN9Th8K-0/image-20250424141245-13.png)
4. If the **CrashingAddinList** key exists and there is a REG\_BINARY value under the key, delete it as explained above.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6184184-cZTGKuLkjLZLyZBEshbecXUypAJZrfLJmkkR0EkIZxcLRbjO0EsGgEtBRn0Cssn8-0/image-20250424143101-14.png)

**Note!** Incorrectly editing a registry can permanently damage your computer or server (if you work on Citrix/Terminal Server), so do not delete or adjust any key if you don't know specifically why you do it. We recommend backing up the Windows registry before making any changes. You can find instructions on how to do it in [this article.](https://neosmart.net/wiki/backup-restore-registry/)

You can also try to reinstall WebTools. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reinstall-superoffice-webtools/) to learn how to do it.

**Note!** This is not recommended on the Terminal Server or Citrix environments.

If this did not help, please [register a support request](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/). We will be able to help you more quickly if you provide us MailLink log file. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-send-a-superoffice-mail-link-log-file-to-superoffice-support/) to see how to get it.

**More information:**

Microsoft article: [Support for keeping add-ins enabled](https://docs.microsoft.com/en-us/office/vba/outlook/concepts/getting-started/support-for-keeping-add-ins-enabled)
