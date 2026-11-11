---
title: "SuperOffice for Outlook: Authorisation guide"
url: https://community.superoffice.com/en/support-faqs/faq/superoffice-for-outlook-authorisation-guide/
lang: en
updated: "12 Oct 2026"
---

# SuperOffice for Outlook: Authorisation guide

Updated on 12 Oct 2026

To meet Microsoft’s enhanced security requirements, the SuperOffice for Outlook add-in (version 6) uses Microsoft’s Graph API to securely access email and calendar data.

**To continue using the add-in, a Microsoft 365 Global Administrator must authorise it by granting permissions (consent) on behalf of all users.**

**Prepare for the update**

To avoid service interruptions, we recommend that Microsoft 365 Global Administrators authorise the add-in before the update (see method a) below).

By acting in advance, users won’t encounter unexpected permission requests and can continue using the add-in seamlessly.

**You can authorise the add-in using one of these methods:**

1. Using a generic authorisation URL (Recommended)
2. Using a URL provided by a user
3. From the add-in in Outlook

**1) Using a generic authorisation URL** (Recommended)

- Open or paste this URL into your browser as a Microsoft 365 Global Administrator:
  <https://login.microsoftonline.com/common/adminconsent?client_id=c360f919-92d2-4f74-9133-a446c6124e29&redirect_uri=https%3A%2F%2Fsuperofficeforoutlook.superoffice.com%2Fconsent-granted>
- Select the correct Microsoft 365 tenant if managing multiple tenants.
- Follow the steps to authorise the add-in (see fig 1).
- When you see the text “Success! You can close the tab now”, the authorisation is done, and you can close the tab in the browser.

  **Note:** Completing this step before the upgrade ensures users won’t encounter permission requests after the update.

**2) Using a URL provided by users of the add-in**

- Users may copy an authorisation URL from the dialogue they encounter.
- Paste the URL into your browser as a Microsoft 365 Global Administrator.
- Follow the steps to authorise the add-in (see fig 1).
- When you see the text “Success! You can close the tab now”, the authorisation is done, and you can close the tab in the browser.

**3) From the add-in in Outlook**

- Open the add-in in Outlook with Microsoft 365 Global Administrator rights.
- Follow the steps to grant consent for all users (see fig 2).

**⚠ Important**: Ensure the checkbox for **“Consent on behalf of your organisation”** is selected; otherwise, the consent will only apply to your account and not all users.

**Note:** Pop-ups must not be blocked for this method to work.

![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6904282-3SLmAe6bFlmxuT8zgsO86YSkNTJ7fxmFP5qgtSakW9mWqdArNyz376YPMxh0RHqI-0/image-20261012160536-1.png)

*Fig 1: Image of dialogue for administrators using URL, method a) and b)*

![](https://app.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6904283-PpL5wFNprrB5Grmm1qokK7MZ3NLHbTG7tScBY84doAoeUsFmdLPb0CZ0DeyWd1Wp-0/image-20261012160649-2.png)

*Fig 2: Image of dialogue for administrators from the add-in in Outlook, method c)*

**User experience after the update**

If authorisation has not been completed, users will encounter an authorisation dialogue when they open SuperOffice for Outlook after the update. This dialogue requires action from either a Microsoft 365 Global Administrator or a user with sufficient rights to grant permissions.

**Example of dialogue for users without sufficient rights:**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6049526-RClrGKPr1aibqjGsfRl62mPBalyktPGLJidGYZlM7wAimm3QSIm223c2OLkzO6xJ-0/image-20250113133454-18.png)

If users don’t have admin rights, they can choose “Return to the application without granting consent.” This will display a follow-up dialogue with an option to copy a link to share with a Microsoft 365 Global Administrator.

**Example of follow-up dialogue:**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6049523-3j7HX5Lp7HBILCTMo8933w3SX51iUjque5jFzYB7KG5tstsIR6PS4yFJSbGliK5g-0/image-20250113133454-19.png)

The administrator can use the link from the dialog to authorise the add-in for the entire organisation, method b) above.

**For users with app-specific approval rights**

If a user has specific rights to approve apps, they will see a different dialogue allowing them to grant access for their own account only.

**⚠ Note:** This only authorises the add-in for the individual user, not for the entire organisation.

**Example of app-specific approval dialogue:**

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6050704-h5RFkH1IqgfFnKm0LsqYHQNaiCxEYA9W9psi0bTj3std2LMDQrour9KpKSGZeGGt-0/image-20250114132150-1.png)

**Need help?**

If you encounter any issues or have additional questions, please contact your SuperOffice support team.
