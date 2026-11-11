---
title: "How to hide data for all users except for users with user level 0?"
url: https://community.superoffice.com/en/support-faqs/faq/how-to-hide-data-for-all-users-except-for-users-with-user-level-0/
lang: en
updated: "21 Jun 2025"
---

# How to hide data for all users except for users with user level 0?

Updated on 21 Jun 2025

I want to create companies, sales, projects, documents and/or appointments that only certain users are allowed to see. How can I do that?

You can make certain records only available to users of a certain role by using a dummy user that will be the owner of the record, or by creating a dummy user group that will be used to set the visibility of the record.

Follow the steps below to learn how to hide records like companies, activities, projects, etc. from certain users.

[**Method 1: Hiding companies, persons and projects from other users by assigning them to a dummy user.**](https://community.superoffice.com/en/support-faqs/faq/how-to-hide-data-for-all-users-except-for-users-with-user-level-0/#a1)

[**Method 2. Hiding appointments, documents and sales from other users by using the Visible for setting.**](https://community.superoffice.com/en/support-faqs/faq/how-to-hide-data-for-all-users-except-for-users-with-user-level-0/#a2)

**Method 1: Hiding companies, persons and projects from other users by assigning them to a dummy user.**

1. To create a new user group in the administrator module, go to the list **General - User group**. In this example, let's call the group "Confidential Group".

**Note!** Don't use the same user group in method 2.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6246659-azpcchioiHnlrD6eP0rypnJmkyAAnYBZD5ZJrxjTXrNDrbQEMQbs1uybTLQNSKiW-0/image-20250621111331-1.png)

2. Create a new (dummy) user in the **Users** tab of the administrator module. This user will be the only user to be assigned to the new Confidential Group. In this example, let's call the user "Confidential User". This user does not require a license/user plan. It is important that **Former employee** is not marked, that the new Confidential Group is assigned as **Primary group** and that there are no **Other groups** assigned to the user.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6246660-ALbn16MN0jql8NN3hMJqYkTgf68LqZogoIoYShTMhyYlxdGGtfj4YESlAOrPBdnP-0/image-20250621111531-2.png)

3. Go to **Roles**, and for each role check the column **Other associates**of the **Data rights.**Since no user will be in the new Confidential Group, the rights on the data owned by the Confidential User will be decided by the 'Other associates' column in the data rights. If you want to give access to the data you want to hide for others only to the user level 0, then give use level 0 full access for this column.

User level 0 will get full access to the column **Other associates**:

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6246661-MlftfeQKCIQiXmZ1GB4tRB2UTIPZCLQmUbna3O7RXZ3GDwqUer2lFnDzBRK1EJns-0/image-20250621111713-3.png)

And all other roles will get no access to the column **Other associates**.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6246662-N3GwWY2x7qYK2ntRpauyqU5cKQbGStQlPnFEF42QyFKHEE13KSUI6Y2UXhCDemRk-0/image-20250621111852-4.png)

**Note!** If you only want to hide only the company, but not other data, then you should change only the company column.

Please note that these changes to user roles may also affect other data in the system where users do not share any groups. That's why, before making any changes, we advise you to learn how data rights work and how they are setup in your SuperOffice installation.

**Additional information:** [How do I configure what information the users of our company can access in SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-what-information-the-users-of-our-company-can-access-in-superoffice-crm/)

If you need assistance with setting this up, please contact a SuperOffice consultant.

4. Create companies, persons and projects and make the Confidential User the owner of the record.
For projects the **Responsible** field that defines who owns that record.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6246663-OFlwfJLr1xWhRITxOqz6WPTms2rWoriuCDFXr3NkSkDgdbQf7ITUcktdHL8ZmR8m-0/image-20250621112146-5.png)

**Method 2. Hiding appointments, documents and sales from other users by using the Visible for setting.**

1. To create a new user group in the administrator module, go to the list **General - User group**. In this example, let's call the group "Limited Visibility Group".

**Note!** Don't use the same user group in method 1.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6246664-Zysol7SNoqNiHQRSalkg6kh1fScsR5fJXXPpXFBdPMpJwP6Y1FrJP19KRz8m61M0-0/image-20250621112523-6.png)

2. Add all users that should be able to see the records in question to this group. In the administrator module, go to the **Users** tab and open each user account. Then, add the the Limited Visibility Group as **Other groups** to all users that should see the data you want to hide from others.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6246665-kCS2nxPDwjHFJDhJ2N4fd5ZzMTBeRGHjpDPq0Xi8ULEXS1Ntk1MTd6BieCjfqGjN-0/image-20250621112740-7.png)

3. Give the (users that will create the records that you want to hide) the license "Confidential activities". These users have to be members of the new user group.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6246666-asNlHo9uzAIFm8N4IH74By3AwAeOXGBjyQ0s3Pe003afwqom75dXNP90WWNJAOYt-0/image-20250621112835-8.png)

4. Now the members of the new user group that have the license for confidential activities, can create appointments, documents and sales while adding the new user group in the **Visible for** field.

**Note!** Users may need to logout and login again before they will see the **Visible for** field. It can also be that the field is hidden for your user group or for a certain follow-up type. In such cases, an administrator has to add this field via [Screen Designer](https://docs.superoffice.com/en/ui/screen-designer/learn/index.html).

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6246683-oqnYjpDg88lfFQqsycxpclxj0qUA9DDnEo9xWJ0uIuuRmjjoMMOuei3XelG1KFzN-0/image-20250621140356-1.png)

**More information**

**FAQ:**[How do I make some of my activities invisible from other SuperOffice users (private)?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-some-of-my-activities-invisible-from-other-superoffice-users-private/)
