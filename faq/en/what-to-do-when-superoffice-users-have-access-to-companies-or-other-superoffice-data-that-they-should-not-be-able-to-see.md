---
title: "What to do when SuperOffice users have access to companies or other SuperOffice data that they should not be able to see?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-users-have-access-to-companies-or-other-superoffice-data-that-they-should-not-be-able-to-see/
lang: en
updated: "12 Jan 2026"
---

# What to do when SuperOffice users have access to companies or other SuperOffice data that they should not be able to see?

Updated on 12 Jan 2026

My colleague can see my companies in SuperOffice. I have been told that this should not be possible with our system setup. Why does it happen, and how do we fix it?

There are a couple of known situations when this can occur:

- [When SuperOffice CRM user data rights permit access to these records](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-users-have-access-to-companies-or-other-superoffice-data-that-they-should-not-be-able-to-see/#1)
- [When storing data in the database issue happens](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-users-have-access-to-companies-or-other-superoffice-data-that-they-should-not-be-able-to-see/#2)

**When SuperOffice user data rights permit access to these records**

This issue can occur if a colleague’s SuperOffice user has permission to view records owned by other users. You can check the user's role in In [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/) -> **User Role (1)**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479503-9qKFiuZpyA9FLjzeJ47LNnNZXWdkPcWGhkaZmQbfg2OIyI8Yf8Japt7T45P4gjlI-0/image-20260112195750-1.png)

To clarify, please ask your SuperOffice administrator to navigate to **Roles (1)**, select the role of your colleague's user (2), click on the **Data rights** **(3)** tab, and confirm that in the data object type line (4) all except My own columns has **None (5)**option selected. That means that this user can see only his own records, but nobody else.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479506-PdQ6718YD36nE6KEgjaw0a41L1zQwOcXda8LSGRiwN1u86qctx8tDD8BKYNylmHu-0/image-20260112200428-2.png)

Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-what-information-the-users-of-our-company-can-access-in-superoffice-crm/) if you want to learn more about access control in SuperOffice CRM.

**When storing data in the database issue happens**

The described situation can occur if you have created companies when your SuperOffice user had assigned another User group when you were creating a record. Most probably, your colleague could see records created by users in that user group. It is possible that the company record that you created still has the *group\_id* field filled with your previous User group's ID. Most probably, your user's **Primary** or **Other groups** have been changed recently.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479508-JwXWU967wZepUXHY56zb9iwZ9DdWExTkgEk9iG4WsjZp8kpJePfPUuhBpHOIOBDQ-0/image-20260112200640-4.png)

In this case, you need to update the database so that it will store the correct *group\_id* in the company's record. To do it, please follow the steps below:

1. Open in edit mode the card of the company that is visible, but should not be visible.
2. Change the **Our contact** (1) field to some other user from the system and **Save (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6479509-cgXCLPFD8yRLdE0SoEmCgZeN3pgxQWjcPPbshl3BUrcSqLkFEcHE2Ypdpw7uCBkf-0/image-20260112200831-5.png)
3. Then open the same company record in edit mode again and change **Our contact** back to your user and click **Save** again.

This action will correct the *group\_id* value in the database, and the company will not be visible for users who do not belong to your group.
