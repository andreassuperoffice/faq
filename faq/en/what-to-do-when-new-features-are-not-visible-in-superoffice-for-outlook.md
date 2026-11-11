---
title: "What to do when new features are not visible in SuperOffice for Outlook?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-new-features-are-not-visible-in-superoffice-for-outlook/
lang: en
updated: "11 Jun 2026"
---

# What to do when new features are not visible in SuperOffice for Outlook?

Updated on 11 Jun 2026

A new version of SuperOffice for Outlook has been released; however, the new features are not yet visible in Outlook. Why does this happen, and how do I fix it?

There could be several reasons why new features are not visible in SuperOffice for Outlook.

The most common reasons include:

- [Your organization’s IT policies require admin approval](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-new-features-are-not-visible-in-superoffice-for-outlook/#t1)
- [Propagation delay after admin approval](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-new-features-are-not-visible-in-superoffice-for-outlook/#t2)
- [Outlook is using a cached version of the add-in](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-new-features-are-not-visible-in-superoffice-for-outlook/#t3)

**​**

**Your organization’s IT policies require admin approval**

Some releases of SuperOffice for Outlook include features that require additional Microsoft 365 permissions, for example, access to additional Microsoft Graph APIs or new OAuth scopes. This is the most common reason new features are not visible after a release.

If SuperOffice for Outlook was deployed centrally in your organization, users cannot approve these permission changes themselves. A Microsoft 365 Global Admin must approve the update before the new features become available.

If you are a Global Admin, follow the steps below to approve the update:

1. Sign in to [Microsoft 365 Admin Center](https://admin.microsoft.com/).
2. Go to **Settings**, then **Integrated apps**.
3. Find SuperOffice for Outlook in the list of deployed apps.
4. If there is a pending update, the app will show a status such as **Update pending** or **More apps available**. Click the app to open the management pane.
5. On the Overview tab, click Deploy or Update, depending on what is shown.
6. On the Accept permission request page, review the new permissions being requested and click Accept permissions.
7. Select the users or groups to deploy the update to, click Update, and then click Done.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6731358-Eh0JPtiOMZT14IaRY9nxUGQtlj8fB4gazeOX2yIXE77Q9OZdRFU1Nr6YKd67syk5-0/image-20260611130441-1.png)

**Note!** Only the admin who originally deployed the add-in, or a Global Admin, can approve updates. Exchange Admins cannot approve updates that require new Microsoft Graph API consent.

**Propagation delay after admin approval**

Even after the update has been approved in the Microsoft 365 Admin Center, it can take up to 24–72 hours before the new features become available in Outlook.

The approval itself is immediate, but distribution to Outlook clients can take time. During this period, some users may see the new features earlier than others, even if they work in the same organization or environment. Users in different regions may also receive the update at different times.

There is no manual way to force this propagation.

**Note!** If the new features are still not visible after 72 hours, we recommend contacting your IT administrator.

**Outlook is using a cached version of the add-in**

Outlook caches the add-in manifest locally. Even after the update has propagated, Outlook may still be using an older cached version of SuperOffice for Outlook.

To reload the add-in, follow the steps for the Outlook version you use.

**If you use the Outlook desktop application, follow the steps below:**

1. Fully close Outlook. Use File - Exit, or quit Outlook from the taskbar. Do not only minimize the application.
2. Wait 30 seconds, then open Outlook again.
3. Open an e-mail and check whether the SuperOffice for Outlook panel shows the new features.

**If you use Outlook on the web, follow the steps below:**

1. Open a browser and go to [outlook.office.com](http://outlook.office.com).
2. Open an e-mail.
3. Open SuperOffice for Outlook from the ribbon or the apps menu.
4. Check whether the new features are visible.

**Note!** Outlook on the web usually fetches the latest add-in manifest faster than the Outlook desktop application. We recommend using Outlook on the web as the quickest way to confirm whether the update is available.

**More information**

Microsoft Article: [Deploy Office Add-ins in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide)

Microsoft Article: [Manage add-ins in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center?view=o365-worldwide&tabs=word-excel-powerpoint)
