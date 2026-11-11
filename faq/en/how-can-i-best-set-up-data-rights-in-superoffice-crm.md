---
title: "How can I best set up data rights in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-can-i-best-set-up-data-rights-in-superoffice-crm/
lang: en
updated: "23 Apr 2025"
---

# How can I best set up data rights in SuperOffice CRM?

Updated on 23 Apr 2025

I want to set up data rights in SuperOffice, but I'm not sure how to do it correctly. What are some best practices I should follow?

The fundamental principle of SuperOffice CRM's data rights is that it's designed for data sharing, not data hiding.

With this in mind, it's crucial to understand that a user shares their data with all their user groups.

Issues often arise when mixing primary and secondary user groups.

**Example:**

User 1, "Simon," has "Sales - Primary" as his primary group and "Support" as an other group:

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6182413-rL4XPD3eWuPKYwBF3mywjKXHID0XtkIEB6u5gOuknJoleDPce7m81wKCyrYUIGAz-0/image-20250423135906-1.png)

This means that all data in the system owned by Simon will be shared with both the "Sales - Primary" and "Support" groups.

User 2, "Samuel," has only "Support" as his primary group.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6182414-l97uMJIHew4Kl3mhRBwuUTMtxCGD9EtNKgPdd92SHzrAGF0SEZB0DA7JEPbyYyyH-0/image-20250423135906-2.png)

When User 2, "Samuel," attempts to access data owned by User 1, Simon, access will be granted based on the data rights of Samuel's primary group. Since the data is shared with that group, Samuel can access it.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6182416-2k0DLCEdpto9d5i5ob7rhmcuoXdru2lm03i2ugrnM2EsQEqN1EhkQwDlMBcQrPgw-0/image-20250423135906-3.png)

Our best practice solution includes the following recommendations:

- Never mix primary and secondary groups.

- Separate all user groups into primary and secondary groups.

- Control access using roles instead of assigning users to numerous groups.

**Example of Best Practice Implementation:**

Instead of a single "Support" group, create two and provide clear descriptions for when each group should be used:

- "Support Primary"

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6182415-E8K2QXFgyxdY4LCMJF9leIAerjGDLDrnesLM9hTtBqIfIs3CdGUaI4dUW3G4dfH7-0/image-20250423135906-4.png)

- "Support Secondary"

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6182418-XSfTFYalPgWKzaau1AlnioNRj07EDbz5zLTm778JIAo3Mir5hyWBfwr0FGkwYeb2-0/image-20250423135906-5.png)

Now, assign User 1, "Simon," to the "Support Secondary" user group.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6182417-3frBzPSmnaeKXIDYzt75uDMPNmiJqx7DjapiJisB72E0RX4MBU6t47fYiiTwLbTN-0/image-20250423135906-6.png)

Assign User 2, "Samuel," to both the new groups:

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6182419-Y37a519lg24sOOplaSzdaTBnUOgHRDdGCQKQheH0wBI9YNZZei9TDWpj8RORlkRg-0/image-20250423135906-7.png)

With this setup, Samuel will no longer have primary group access to data owned by Simon because Simon isn't sharing data with the "Support Primary" group.

We are now effectively using the "other groups" rights for the data.

By dividing user groups into primary and secondary categories, you gain precise control over which data resides in which data rights column.

**More information**

FAQ: [How do I configure what information the users of our company can access in SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-what-information-the-users-of-our-company-can-access-in-superoffice-crm/)

FAQ: [How to hide data for all users except for users with user level 0?](https://community.superoffice.com/en/support-faqs/faq/how-to-hide-data-for-all-users-except-for-users-with-user-level-0/)

FAQ: [What to do when SuperOffice users have access to companies or other SuperOffice CRM data that they should not be able to see?](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-superoffice-users-have-access-to-companies-or-other-superoffice-crm-data-that-they-should-not-be-able-to-see/)

Docs: [Configure what information the users of your company can access in SuperOffice CRM](https://docs.superoffice.com/en/admin/user-management/learn/role/index.html)

**Note!** We recommend carefully planning your user group structure to ensure optimal data security and access control.
