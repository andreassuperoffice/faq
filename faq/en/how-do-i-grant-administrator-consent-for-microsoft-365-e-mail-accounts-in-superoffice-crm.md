---
title: "How do I grant administrator consent for Microsoft 365 e-mail accounts in SuperOffice CRM?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-grant-administrator-consent-for-microsoft-365-e-mail-accounts-in-superoffice-crm/
lang: en
updated: "8 Sep 2026"
---

# How do I grant administrator consent for Microsoft 365 e-mail accounts in SuperOffice CRM?

Updated on 8 Sep 2026

Our users cannot connect their Microsoft 365 e-mail accounts in SuperOffice CRM. They get a message saying that approval from an administrator is required. Why does this happen, and how do I approve it?

SuperOffice CRM uses Microsoft Graph to send e-mail on behalf of your users. Before this can work, your organization must approve the permissions that SuperOffice requests in Microsoft Entra ID.

Without this approval, users will see an error when they try to connect their e-mail accounts.

This is a one-time setup - once it is done, everyone in your organization can connect their e-mail accounts.

**Note!** To approve the permissions, you must be signed in with a Microsoft 365 Global Administrator, Application Administrator, or Cloud Application Administrator account. If you do not have one of these roles, forward this FAQ to the person in your organization who does.

To grant consent, follow the steps below:

1. Open this link in your browser as an administrator: [https://login.microsoftonline.com/organizations/adminconsent?client\_id=d0c02962-eedd-4d1e-8a70-a315f1aa5072&redirect\_uri=https%3A%2f%2faccessgateway.superoffice.com%2fsignin-microsoftgraph](https://login.microsoftonline.com/organizations/adminconsent?client_id=d0c02962-eedd-4d1e-8a70-a315f1aa5072&redirect_uri=https:%2f%2faccessgateway.superoffice.com%2fsignin-microsoftgraph)

   Your users can also copy the same link from the message they see in SuperOffice CRM and send it to you.
2. Sign in using an administrator account. Select the correct Microsoft 365 tenant if you manage more than one.
3. Review the requested permissions. You will see the application name, the publisher (SuperOffice AS), and the list of permissions requested through Microsoft Graph. Confirm they meet your organization's policies before approving.

   ![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6856035-W6zBbbL2zMu7EJha5ONM2r7GDI0T1Wtdgbi62tU5FuANlxDPs5Fc25aUGt0m5No9-0/image-20260908184909-2.png)
4. Click **Accept**.

This grants access for all users in your organization.

If you prefer to grant access manually from the Microsoft Entra admin center, follow the steps below:

1. Go to the Microsoft Entra admin center.
2. Navigate to Identity, then **Applications**, then **Enterprise applications**.
3. Find and select **SuperOffice**.
4. Go to **Permissions** or **API permissions**.
5. Click **Grant admin consent**.

Granting admin consent allows SuperOffice to access Microsoft 365 data based on the requested permissions. Always verify the application name and publisher, review the requested permissions, and ensure the request comes from a trusted source.

**Note!**If users still cannot connect after approval, ask them to retry connecting their e-mail account, and to sign out and back in if needed.

If you cannot approve access, check that you are signed in with an administrator role, that your organization does not restrict admin consent, and that conditional access policies are not blocking the request.

**More information**

Microsoft: [Grant tenant-wide admin consent to an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent)
