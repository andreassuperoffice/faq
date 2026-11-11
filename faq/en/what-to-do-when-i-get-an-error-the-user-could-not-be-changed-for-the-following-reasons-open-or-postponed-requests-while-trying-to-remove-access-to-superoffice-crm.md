---
title: "What to do when I get an error \"The user could not be changed for the following reasons Open or postponed requests:\" while trying to remove access to SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-the-user-could-not-be-changed-for-the-following-reasons-open-or-postponed-requests-while-trying-to-remove-access-to-superoffice-crm/
lang: en
updated: "20 Feb 2026"
---

# What to do when I get an error "The user could not be changed for the following reasons Open or postponed requests:" while trying to remove access to SuperOffice CRM?

Updated on 20 Feb 2026

I try to take away login rights from a user, but I get this error:

*"The user could not be changed for the following reasons: Open or postponed requests"*

Why does it happen, and how do I fix it?

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6547887-XSISTy9qZq1W4ltfeRuRjDauUQ1AdiOicD0nraQosJ4uk3MWpEFERYQlppik9Jb5-0/image-20260220120220-1.png)

The error comes up when the user has open requests assigned to him/her in SuperOffice Service. To be able to remove the login access, you have to either unassign or reassign all open requests that this user has before you can remove access rights. Please follow the steps below to do it:

1. Click on the **Find (1)**button, then on the **Find request option (2).**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6548460-0flsBbs2gpXHUDuFWFJIaW1FPWP7AI3agrNm4UTEmO7om8Dwkcr2Qwh5tz96XWew-0/image-20260220140327-1.png)
2. In the **Owner field, select is one of** (1), and then select the user whose access needs to be removed. If the **Internal status** (2) field is not available, add it by clicking **Add criterion**, then select is one of, choose Open status, and click the **Find** (3) button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6548493-pI1rGmwNZfsw9yA4gPrw6UBxfEQfZFyU77Ib4ZayB1KE0YnxiFKckm16Wz8l1FYo-0/image-20260220140711-2.png)
3. Select all the requests that this user has (you can do this, for example, by clicking the CTRL button and selecting all of these requests one by one), then click on **Task** - **Bulk update**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549257-PHkws2gJiyJqxdt4yiufpWzDanOFl0ldeambGY16HxOCjbxb5nSToJSEwHQA4M3x-0/image-20260220154148-3.png)
4. Then add a tick next to **Owner** and from the drop-down list choose another user who should get the open requests, or choose to leave them unassigned, and click on the **Update**button to make this change on all selected requests.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549274-uF7J2uxXpFHEN2RcEEQYbiTMbAujERUDakWc2owfHhs4IORs7OXgaDoHlrYzO3A6-0/image-20260220154741-4.png)
5. Then confirm your action by clicking on the **Yes** button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6549278-xboineDPrDoWQaPBuTzbpQ3xBcj1ikCSqRB8ZAj4H9GEYyLC4a7UtUeBlqzrlLm5-0/image-20260220154846-5.png)

   Now, requests should be moved from the user, and you can remove access to the user in [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/) once more.

**More information**

FAQ: [How do I reassign a SuperOffice licence from an old user to a new one?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-reassign-a-superoffice-licence-from-an-old-user-to-a-new-one/)
