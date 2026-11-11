---
title: "How are selection settings saved in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-are-selection-settings-saved-in-superoffice-crm/
lang: en
updated: "8 Jul 2026"
---

# How are selection settings saved in SuperOffice CRM?

Updated on 8 Jul 2026

I changed columns, column order, grouping, or other settings in a selection. The same setup sometimes appears in other selections of the same type, but I want one specific selection to keep its own setup.

How are selection settings saved, and how can I save settings for one specific selection?

Selection settings are saved based on the type of selection you are working with.

**Each selection type has its own setup**. For example, selections based on projects, sales, requests, companies, or contacts store columns and settings separately.

This means that if you change the column setup in one project selection, the same setup can also appear when you open another project selection. The same setup will not automatically apply to request selections, sales selections, company selections, or contact selections.

![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6777406-yAYsQ4hiR1hi61sbP4NIUlaPrf3GRy03G1SzY6uu1LBuZPGnzUTlJStQ0YJY7Ssd-0/image-20260708155259-1.png)

![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6777408-6sS4rqOitSInQjHDnbLIjQwJNNRXnOtL9M7k9Or7xI2ecNW714WBcAE6BsUm65PC-0/image-20260708155330-2.png)

Selection setup is saved in two different ways:

- **Columns** are saved in the database as a preference.
- **Settings and grouping** are saved as cookies in the browser.

This means that if you change columns, column order, grouping, or other settings in one selection, the change normally applies to other selections of the same type. For example, if you change the column order, add grouping, or add a new column in one project selection, the same setup will also appear when you open another project selection.

![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6777442-SIRBRcKYOUGfQtkb3p7Z60OuJWTPLU07qUIBRy1Dh7kGgLQg5RIRXW9s1bT8uZnZ-0/image-20260708162127-4.png)

To save a **unique setup for one specific** **selection**, follow the steps below:

1. Open the selection.
2. Click the settings icon to the right of the column headers.
3. Change the columns, column order, grouping, or other settings, and enable **Save settings for all users viewing this selection**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6777411-NEEJ21RIX8kes5UmJqgC6S2oDZzQD1cqJCRQSHfhufafCSzbBRo1MKjPsCxueo6D-0/image-20260708155716-3.png)
4. Click OK.

When Save settings for all users viewing this selection is enabled, the current column setup is saved for that specific selection.

All users who open the selection will see the same columns. If any user changes the columns, the change affects all other users viewing that selection.

Settings and grouping are saved differently. They are saved as browser cookies and are unique for your user and browser. This means they are not transferred to other users.

This makes it possible to have different column setups, grouping, and settings for different selections of the same type. For example, one project selection can have grouping enabled with one set of columns, while another project selection can use a different setup.

The saved settings are kept as long as browser cookies are not cleared, and Save settings for all users viewing this selection remains enabled for the selection.

**Request selections**

Request selections can behave differently because they can be opened inside the request module. This means that several request selections can be open at the same time.

Request selections read cookie settings when they are opened or when the full page is refreshed. Because of this, you may be able to change several request selections to show different columns, settings, and grouping, **even** when Save settings for all users viewing this selection is not enabled.

However, after refreshing the browser or logging in another day, request selections that do not have Save settings for all users viewing this selection enabled will use the same columns, settings, and grouping again.

**Note!**

If you enable Save settings for all users viewing this selection in another user’s selection and click OK, your current column setup will be saved and applied to other users viewing that selection.

**More information**

Docs: [Selection](https://docs.superoffice.com/en/search-options/selection/learn/index.html)

FAQ: [How do I get a list of all created selections in our SuperOffice CRM?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-get-a-list-of-all-created-selections-in-our-superoffice-crm/)
