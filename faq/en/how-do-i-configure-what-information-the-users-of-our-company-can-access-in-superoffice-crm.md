---
title: "How do I configure what information the users of our company can access in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-what-information-the-users-of-our-company-can-access-in-superoffice-crm/
lang: en
updated: "10 Jun 2025"
---

# How do I configure what information the users of our company can access in SuperOffice CRM?

Updated on 10 Jun 2025

How and where in SuperOffice CRM can I configure access rights for our users?

SuperOffice CRM uses a role- and group- based access right system. It means that every SuperOffice user has a role and belongs to a primary group- , these are mandatory settings.

**A role** has a set of data and functional rights, and **a group** setting grants access to data objects, various SuperOffice lists and helps to set system preferences more efficiently. A user can also belong to other group. This is relevant when you are configuring access to data objects in SuperOffice CRM.

Image 1 shows a model of how the access right system works in SuperOffice CRM. This model has references (1, 2, 3 ...) to various access right settings which are illustrated with screenshots and explained later in the article.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4404125-bwJdIj4N4icPgfhcllumyYkhcN15RNHfSH8WakDpW6yKXhso0THrMadodw4gSLx5-0/image.png)

*Image 1.*

A user must have one role, which controls access rights to data objects and functions in SuperOffice CRM. The system allows you to configure access to companies, contacts, projects, project members, selections, sales, stakeholders (of sales), [follow-ups (appointments, tasks, phone calls)](https://docs.superoffice.com/en/learn/section-tabs/activities-tab.html), documents (documents, e-mails, and mailings fall under this category), relations (contact and company) and dashboards. All these different types of records are called *data objects*.

Each data object belongs to a user who might be you yourself (A), users in your primary group (B), users that belong to your other groups (C), other associates to whom you are not connected by any of your groups (D), external users (E), and anonymous users (F).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6197021-RNHQHqFsZopZtZBkyswHxlZE05hhxuUKDOJ40LN7tGf8F7nlOKxafYWemZQQtxh4-0/image-20250507164452-1.png)

*Screenshot 1.*

The ownership of different data objects is set in different fields. For example, in the Company card the field called “Our Contact” specifies the owner of the record. In the Follow-up card it is the field “Owner”, in the project “Responsible”, etc.

You can set different access rights for each data object.

|  |  |
| --- | --- |
| **Name** | **Rights** |
| None | No rights |
| Read | Read rights |
| Create | Read and create rights |
| Update | Read, create and update rights |
| Delete | Read, create, update and delete rights |

For example, in the Settings & Maintenance module, you selected a Role **User level 1** (A) and set **Delete** (B) right to a company data object under the primary group column. This configuration means that any user who has User level 1 role will be able to read, create, update and delete all the companies that belong to other users who are members of his/her primary group.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6234341-eik6r4uDYk0fgIQINjxyPn1wntxpchRfcTurucCnTlyBItRrtOie01UP4FuMTOgh-0/image-20250610163719-1.png)

*Screenshot 2.*

**A role** also has a set of functional rights (3). By moving the functional right from one column to another, you can control , what a user can and cannot do in the system. [This FAQ](https://community.superoffice.com/en/support-faqs/faq/whichare-all-availablefunctional-rights-in-superoffice-and-what-each-of-them-mean/) explains what each of the functional rights stands for.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6197046-qlbuqaeNpJupPNRItPrJoo2QgrDLTPcKcKZx4Xcy7BjiY8l2tYqCB1pNaWuFjFg9-0/image-20250507164704-3.png)

*Screenshot 3.*

**A group**, which is assigned to the user, grants access to data objects (4 - *screenshot 1*).  A user must have one primary group and can have multiple other groups. Let's take a look at example of the image 2. User A has *Marketing* as the other group and User B has *Marketing* as the primary group. In this case, if User A wants to see data created by User B, User's A Role has to have the right "Read" next to all data objects in the column Other group. It is because Marketing group is other group for user A and it is connecting him with records that user B creates.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/3695464-dD83rirR8Au63tZCBESaFrd3yiaMh8x8eTwumXSz46yqIhlA1DWJz3tSu6ZQ599e-0/image.png)

*Image 2.*

A group also can grant access to list items (among which document templates (5)) in SuperOffice CRM. This is only relevant if you use the **Grouping and filtering** setting (A) on your lists. If this setting is not set up, all users will have access to all lists in SuperOffice CRM. Grouping and filtering are especially useful when many users with various responsibilities can access the system. This way you can avoid certain users accessing the information that they are not supposed to see.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6197053-ysP8IFbRDyNEF9Gct6KRn5GWhrxpfcil5ticGku97w0QIsZR8sf9IypdC6wHyKm1-0/image-20250507164909-4.png)

*Screenshot 4.*

For example, if you want to make a particular list item visible only to some users, you need to go to the list, which stores these items (A), select the item (B) and in the box called "Visible for user groups", add a check next to the user groups which should see the list item (C).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6197097-Q5DgSbbur64qAh0UNAgx1nI0D9KAY7N5dc5enUyDXUrhzPO6WqlhRrqMfTqhPCA0-0/image-20250507165601-5.png)

*Screenshot 5.*

Having your users organized in groups is also convenient when you want to personalize SuperOffice settings, we call them preferences (6). Every preference, which can be found in the [Settings & Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/) module can be set for one user, user group or the entire system.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6197098-O4S7csiuiLC1hfABt1AScxU2DeU5fjHlqhfsPwiTqyPws7y7n1zhw3flOx4bndq1-0/image-20250507165906-6.png)

*Screenshot 6.*

The settings which are explained in this FAQ will help you customize your user's experience and control access to the information you store in SuperOffice CRM.

**More information:**

Docs: [User accounts and role-based access control](https://docs.superoffice.com/en/online/identity/user/index.html)

Docs: [Set data rights for a role](https://docs.superoffice.com/en/admin/user-management/learn/role/set-data-rights-for-role.html)

FAQ: [How do I create a new User Group in SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-a-new-user-group-in-superoffice-crm/)

FAQ: [How can I best set up data rights in SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-can-i-best-set-up-data-rights-in-superoffice-crm/)

FAQ: [How to hide data for all users except for users with user level 0?](https://community.superoffice.com/en/support-faqs/faq/how-to-hide-data-for-all-users-except-for-users-with-user-level-0/)
