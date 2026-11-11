---
title: "How do I configure SuperOffice CRM that a sales manager would get a notification when a new sale is created?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-crm-that-a-sales-manager-would-get-a-notification-when-a-new-sale-is-created/
lang: en
updated: "28 Dec 2025"
---

# How do I configure SuperOffice CRM that a sales manager would get a notification when a new sale is created?

Updated on 28 Dec 2025

Whenever a new sale (opportunity) is created, a sales manager should be informed about it. How do I configure SuperOffice so that the sales manager will get a notification when the sales executor creates a new sale?

SuperOffice CRM has the feature [Triggers](https://docs.superoffice.com/en/customization/macros-and-scripts/admin/trigger.html), which executes actions for specific events in the system, such as when a new sale is created. Please follow the steps below to set up the SuperOffice CRM so that it sends a notification e-mail when a new sale is created:

**Note!** This feature requires a license for [Development Tools](https://docs.superoffice.com/en/admin/license/expander-services.html).

1. Log in to [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/).
2. Click on **CRMScript (1)**, then the tab **Triggers (2),**and click the **New trigger (macro)** button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465422-HmaFwDMHifjQgEbha4mZnlXh9akrtPWjEN2ArbZUkpBM3dwykcqsE1C1SJQhBpyf-0/image-20251228205406-1.png)
3. In the trigger list, scroll to the bottom and in the section **CRM: after save,**click on the button **After saving sale.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465423-BW9U7xcWRGmXRiZzlTA92th8mMM2gdXooZkxxOO2XXefuRWshxj0qyloXi1YZfrx-0/image-20251228205503-2.png)
4. In the **Description (1),**explain what the trigger will do and click onthe **Send an e-mail or SMS** (2) button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465424-bhIrF6nbjqBsngGzCx6CpdmUBZSaNbflSPCQCby2mIk5mqrkrWSDXG85SkuCEGYY-0/image-20251228205616-3.png)
5. In the If field select option **All conditions are true (1)** and below set up the condition that notification would be sent only when a new sale is created, in other words **- is new is true (2).** Then fill in **Subject (3), From (3), To (4), Text message (6)** fields with information that the system should deliver to the sales manager. **Enable** (7) the trigger and click **OK**(8) to finish.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465425-6u3BiUR8LP4lU6OeSXf9GsaxeHc0FtWFHWkn6N8R79ABeQ9dOiSqRIhq1h9TIeBp-0/image-20251228210044-4.png)
6. Now the person whose e-mail address has been entered in the To field will get a notification every time a new sale is created.

**Note!**

1. Scripts, Macros, Triggers, and Scheduled tasks can be created for you by a SuperOffice consultant.

2. All support questions related to Scripts and SuperOffice SDK need to be posted in [SuperOffice Community Developer Forum.](https://community.superoffice.com/en/technical/forums/)

**More information:**

FAQ: [How do I start using CRMScript in SuperOffice Online?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-crmscript-in-superoffice-online/)

Article: [Beginner's guide to triggers and CRMScript](https://community.superoffice.com/en/technical/blogs/archive/beginners-guide-to-triggers-and-crmscript/)

Docs: [Macros and scripts](https://docs.superoffice.com/en/automation/crmscript/learn/macro-script.html)
