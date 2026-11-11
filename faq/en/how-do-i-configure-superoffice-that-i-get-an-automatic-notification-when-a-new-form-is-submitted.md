---
title: "How do I configure SuperOffice that I get an automatic notification when a new form is submitted?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-that-i-get-an-automatic-notification-when-a-new-form-is-submitted/
lang: en
updated: "16 Jul 2025"
---

# How do I configure SuperOffice that I get an automatic notification when a new form is submitted?

Updated on 16 Jul 2025

How do I configure SuperOffice that I get an automatic notification when a new form is submitted?

If your form is set to be processed manually, SuperOffice will notify you with visual notification in the Marketing screen by default.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6270729-NG19IHxE1wKAPfjqFKc7l1d9etf45bJAlfTk0I84PXfddh214RNSjxSzro8D2ZhE-0/image-20250716123433-1.png)

If you want to get an e-mail notification whenever a new form submission is processed you can either:

1. [Service generated notification](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-that-i-get-an-automatic-notification-when-a-new-form-is-submitted/#1). Create your form so that a new submission would automatically create a request in Service, where you have many options to configure notifications.
2. [Macro generated notification](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-that-i-get-an-automatic-notification-when-a-new-form-is-submitted/#2). Create a Macro to be notified, when a new form is processed.

To learn how to set up these scenarios, follow the instructions in the sections below.

​

**Service generated notification**

To set up e-mail notifications from the Service category please do the following steps:

1. Go to the **Edit form** screen, in the **Actions**(1) section, select the **Notify of submissions by creating requests** (2) option.
2. Fill in the default values such as**Title (3), Request category (4), Request priority (5)** and **Request type (6)**, which a new request should get after SuperOffice will automatically create it.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6270738-BNBh46tThG5hsMhmW4BwmqDBakFNXUG1p8ZqjWq03cR7CKiM2H9b1ZCkAaq8CNNy-0/image-20250716124401-3.png)
3. Click on **Main Menu** button and open **Settings and Maintenance**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6270891-PJZUszFIZ9jOOTIsKcAAGwRgYkMEQFmwWsCgFbUotzRj2G9Gkjq7tRRR7pfdX0Hf-0/image-20250716140906-4.png)
4. Click on **Requests** (1) and select the **Categories** (2) option. Next, click on the **category** (3)that specifies where your form submissions should be placed. After that, tick the **Send notifications to members about new request** (4)box if you want all members of the category (assigned in the **Members** section) to receive notifications. Alternatively, **enter the specific email addresses** (5) of people who should receive notifications.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6270940-bKLB6TkIjAH9IFZChnFug7l4Ye3RNAAnOIaLfCTWlQ4caZaGqgr3miJokniUtLpM-0/image-20250716142945-6.png)

​

**Macro generated notification**

To set up e-mail notifications with Macro, please take the following steps:

1. Go to the administration client by click on [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/) and choose **CRMScript** (1) in the Navigator menu.
2. Click on the **Macros and scripts (2)** tab and then on the**New macro (3)** button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6270971-IbxGgkPf1lcshcAUMzKdpeyeLumP7XD91rOJzAH21H93ItLAJSCe9R7fAwFjQGN4-0/image-20250716143753-7.png)
3. Fill in the information section with the necessary details about your macro and in the **Actions (1)** section click the **Send an e-mail or SMS (2)** option.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6270984-srIOaiNNNSSykJ90XU2zY3zc95khrhqGmTCp3MAXclx8pe8eZGoW0fbB2ar3Pwgn-0/image-20250716143923-8.png)
4. Make sure that the **Always (1)**option is set, then fill in other relevant fields (2) set up your notification and click **OK (3)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6270985-geWJRFAhjWl3ciqisx6pcsKU5gkp8BlTbG3WI2aX4RC2Lak7ieF38Ghq18c4s0Yf-0/image-20250716144151-9.png)
5. Go to the **Edit form** screen in your form, click on the **Actions** (1)section and in the **Execute CRMScript** (2)field select the macro you have created in previous steps, click **Save** (3)to finish.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6270986-XjwZr5XCQmjzQozhMwExyj7jWPnLFrTKW6ZxkpIAx686B2MdhSAFojmCtDczrdG0-0/image-20250716144426-10.png)

   **Note!**

1. Scripts, Macros, Event Handlers and Scheduled tasks can be created for you by a SuperOffice Consultant.

2. All support questions related to Scripts and SuperOffice SDK need to be posted in [SuperOffice Community Developer Forum.](https://community.superoffice.com/en/technical/forums/)

3. Only users with the complete user plan can create and execute the macro.

**More information:**

FAQ: [How do I start using CRMScript in SuperOffice Online?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-crmscript-in-superoffice-online/)

Blog: [Beginner's guide to triggers and CRMScript](https://community.superoffice.com/en/technical/blogs/archive/beginners-guide-to-triggers-and-crmscript/)

Docs: [Expander Services – a toolbox for customizing SuperOffice CRM](https://docs.superoffice.com/en/admin/license/expander-services/)
