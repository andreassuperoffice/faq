---
title: "What to do when changes made in Settings and Maintenance are not visible in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-changes-made-in-settings-and-maintenance-are-not-visible-in-superoffice-crm/
lang: en
updated: "12 Jun 2025"
---

# What to do when changes made in Settings and Maintenance are not visible in SuperOffice CRM?

Updated on 12 Jun 2025

I have created and published a new user-defined field in Settings and Maintenance, but it is not visible in SuperOffice CRM. Why does it happen and what can I do about it?

It may occur that changes made in SuperOffice Settings and Maintenance are not immediately reflected in the system. For example, you may have created a new field or adjusted user roles or permissions, but the changes did not take effect. In such cases, the following two actions can be taken:

- [Flush the SuperOffice installation](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-changes-made-in-settings-and-maintenance-are-not-visible-in-superoffice-crm/#1)
- [Restart (recycle application pool) the SuperOffice installation](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-changes-made-in-settings-and-maintenance-are-not-visible-in-superoffice-crm/#2)

**Flush the SuperOffice installation**

To do this, please remove everything in the URL after default.aspx, then add ?flush directly after default.aspx, and press Enter.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6237096-jmZeHyRAlG5pB1HpAf13PTEdGTslXMHzLPt7j03ljhePKGLmL8rG97kg0FGJCPzy-0/image-20250612130835-1.png)

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6237113-rH40TOcjJ4u56kwJ6PuqiHNc1y6O9d7uG8lAQ44P0ul9rxC9c43HDTPx6pTLdZx1-0/image-20250612131159-2.png)

**Note!** This (?flush) command clears GUIconfigurations type records saved in the SuperOffice database in the BinaryObject table.

**Restart (recycle application pool) the SuperOffice installation**

If you are a SuperOffice Online installation user recycle is being done automatically every night. It can be done on the request, please [contact support by registering a request](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/).

If you are a SuperOffice Onsite installation user recycle must be done by your IT responsible person.
.
**Note!** During the recycle process, all users will be automatically logged out of SuperOffice CRM. They can log in again immediately afterward. We recommend informing all SuperOffice users in advance to avoid losing any unsaved data during the restart.

**More information**

Microsoft Article: [Recycling Settings for an Application Pool <recycling>](https://docs.microsoft.com/en-us/iis/configuration/system.applicationhost/applicationpools/add/recycling/)
