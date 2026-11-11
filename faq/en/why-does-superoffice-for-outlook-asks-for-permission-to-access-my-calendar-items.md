---
title: "Why does SuperOffice for Outlook asks for permission to access my calendar items?"
url: https://community.superoffice.com/en/support-faqs/faq/why-does-superoffice-for-outlook-asks-for-permission-to-access-my-calendar-items/
lang: en
updated: "17 Oct 2024"
---

# Why does SuperOffice for Outlook asks for permission to access my calendar items?

Updated on 17 Oct 2024

SuperOffice for Outlook asks me every time permission to access my calendar items. What can I do to stop this from happening?

As a Synchronizer user you have additional calendar features in the SuperOffice for Outlook add-in.

To use these new calendar features, we rely on Microsoft's Graph API for obtaining permissions (also called consent) to access your calendar. ​

To obtain these permissions, two prerequisites must be in place: ​

1. The add-in must have been deployed by tenant admin, through MS Admin Center​.
   *The reason for this is that "Office only supports consent to Graph scopes when the add-in has been deployed by a tenant admin.” If the add-in has not been deployed by a tenant admin, the below dialog box will show up even if you have done point 2. Please contact your administrator if this would be the case.*
2. If you are using Firefox "Enhanced Tracking Protection” must be disabled. ​
   If you are using Safari "Prevent cross-site tracking" must be disabled.

Firefox and Safari have privacy settings that prevent the transfer of these tokens between windows. As a result, if the access token is not obtained, it indicates that the user has not granted permission (consent) to access their calendar items. In such cases, a dialog box, as shown below, appears.​

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5910661-MRJcYS9AybYt3RStbYulsNZqdnmbbulPczPRiDQzkDAjySDNy5laEmyLy42wCynU-0/image-20240911143802-1.png)

In Firefox, this feature is referred to as "Enhanced Tracking Protection," while in Safari, it is known as "Prevent cross-site tracking." To ensure the proper functioning of the calendar in these browsers, you will need to disable these settings when using the web version of Outlook. Alternatively, you can utilize the desktop version of Outlook or switch to a different browser.

**Disable Enhanced Tracking Protection in Firefox**

1. Select the shield icon to the left of the URL of the webpage.​

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5910681-hTK1mKUWpyKQUCxoQqYQSd4UW0IWwGuxH3uIcUTU8LeA8IU75sXmTx7MCrqu7DG1-0/image-20240911144627-4.png)
2. A drop-down list will appear, listing the protections for the website.​
3. Click on the button to the right of “Enhanced Tracking Protection” to turn it off.​

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5910682-ssJkuOBdGtSFnNlJ858T8slTWcsZZG4ULSuruRIIBTIy5BqPwQJXkcIOm3kOHAPH-0/image-20240911144649-5.png)

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5910683-JtTFjJwcS1bia6IdDJx7JLjIyRQ7gB0EDGOrdlKppGj7QBWC5GCz28hB2PNTtZSy-0/image-20240911144655-6.png)

​
NOTE: ​

- Disabling Tracking Protection only applies to the site you explicitly disable it for. ​
- We suggest to disable ”Enhanced Tracking Protection” for https://outlook.office.com/

**Disable Prevent Cross-Site Tracking in Safari on Mac**

1. In the Safari app on your Mac, choose Safari > Preferences, then click Privacy.​
2. Unselect “Prevent cross-site tracking.”​

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5910714-OmlCxU5JmrWGeJJrdejgxIOoPmoSGPuhAGYtR9mfiIWMSb0D4fO9ojqJwBixkMjl-0/image-20240911145406-7.png)

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/5910715-C5BBdOpeIOrOHoor3FjZR04Z3kIjerAf31ytw9XrnOs4ASLxi0b4adxtceIrUzUn-0/image-20240911145412-8.png)

NOTE: ​

- Disabling cross-site tracking will apply to all sites.
