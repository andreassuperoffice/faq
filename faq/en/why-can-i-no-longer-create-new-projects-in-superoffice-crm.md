---
title: "Why can I no longer create new projects in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/why-can-i-no-longer-create-new-projects-in-superoffice-crm/
lang: en
updated: "7 Oct 2026"
---

# Why can I no longer create new projects in SuperOffice CRM?

Updated on 7 Oct 2026

Until recently I could create new projects in SuperOffice CRM without any problems. Now, when I try to create a new project, I get the following error message:

![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6897465-G9wj9QRg9efBl95pWIiohs1lsS9l7Tu5redBEUNsjZXlRuxMB8IhN1HdiIAuxKQQ-0/image-20261006201815-3.png)

Why does it happen and how do I fix it?

The described situation can occur when your company is on the Core plan and has more than 100 active projects.

SuperOffice CRM is no longer sold as separate licenses, such as Sales Essentials or Service Essentials. Instead, it is now offered as SuperOffice CRM Suite, which comes in several plans. Companies that had the Sales Essentials or Service Essentials licenses have been moved to the Core plan, which includes up to 100 active projects.

An active project is a project that is not marked as **Completed**. If your company has more than 100 active projects, you keep all projects and their history, but you cannot create a new project until there are 99 or fewer active projects.

When you mark a project as Completed, the project and its history are not deleted. You can still find and open the project and see its documents, correspondence and other information. You can reopen a completed project at any time by clearing the Completed tick box, and the project then counts as an active project again.

To complete the projects you no longer work on, please follow the steps below:

1. Click on **Find** (1), then **Find Project** (2).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6897490-z1A9rTkQ2lJoODnX75uoxJ9QYLSI5ARtCSAWPucr5rbklop9k9nyjFXUAF3I2YJX-0/image-20261006212224-11.png)
2. Add criterion **Completed = No**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6897491-Hes2cgS03Ee1OPg32XemdwEbkCdcZScFwRw4f4uXNM58KkgktEZZcYg3xda2t8Jo-0/image-20261006212332-12.png)
3. Add more criteria to narrow down the selection if needed, e.g. Registered, Project type or Project status. For example, to find projects registered before this year, add the Registered date criterion.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6897469-8NUo58wkPKKyN6Dyd6iyiCgAn3lfilnaK2YwFG08YZksZNBfLphG3kjBkAgAsTdb-0/image-20261006204447-6.png)
4. Save the **search as a selection**.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6897492-DYUpd6XDJpfJzlBumdCiqsUFDM32mezIeDepsDr8wiXtYnBf7jOOdxth4dFUnW7J-0/image-20261006212457-13.png)
5. Then, click on the Task button and select Bulk update.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6897480-5rr4zFP69P4T4FNF8eYW3hUeotA6P8Zb2JOX5g9E2bG2r2d05X3SBfhoX5gxxFjp-0/image-20261006205056-8.png)
6. Select the **Completed** field (1), set its new value to **Completed** (2) and click **Update** (3).

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6897481-Gmdx6Tb55wSgDZeLNowmxIkMXkGsPJRhK4eba73bJL1wy7sLfgBYhGb68hTxgIOI-0/image-20261006205234-9.png)

**Note!** Bulk update cannot be undone. That's why we recommend first testing the bulk update on a single project to confirm the desired outcome and noting the time of the action.

If your company needs more than 100 active projects, please contact the [Customer Experience Center](mailto:support@superoffice.com) or your Account Manager to discuss an upgrade to the [Growth](https://www.superoffice.com/pricing/compare-plans/) plan.

**More information**

Article: [Introducing SuperOffice CRM Suite](https://community.superoffice.com/en/product-releases/whats-new/introducing-crm-suite/)

Docs: [Update multiple records (bulk update)](https://docs.superoffice.com/en/learn/basics/bulk-update)
