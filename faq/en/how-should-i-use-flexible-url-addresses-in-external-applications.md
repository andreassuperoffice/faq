---
title: "How should I use flexible URL-addresses in External Applications?"
url: https://community.superoffice.com/en/support-faqs/faq/how-should-i-use-flexible-url-addresses-in-external-applications/
lang: en
updated: "13 Feb 2026"
---

# How should I use flexible URL-addresses in External Applications?

Updated on 13 Feb 2026

SuperOffice is operating its applications across different application URLs, also called endpoints or APIs.

As we are approaching a larger change to our operating environment in 2026, following best practices for integrations is more important than ever.

If External Applications integrate with SuperOffice using hard-coded addresses to endpoints, changes to the operating environment may impact customizations and the use of SuperOffice.

**How should External Applications be configured to avoid issues?**

External Applications integrating with SuperOffice should not use hard-coded addresses to endpoints.

The best practice is to ensure that the SuperOffice application URL can change without impacting your customizations or the use of SuperOffice.

To verify this, please review your External Applications and ensure the following:

1. Inspect the integration and confirm that endpoint URLs are not hard-coded.
2. Ensure that the integration follows best practice for handling flexible URL-addresses.
3. **Most importantly**, address endpoints according to the recommendations described in the article [Check tenant status](https://docs.superoffice.com/en/developer-portal/best-practices/tenant-status/check-status.html) in the SuperOffice Developer Portal.

**Note!** Even though the customer will be moved to [app.superoffice.com/cust1234](https://app.superoffice.com/cust1234), the authentication endpoint will remain [online.superoffice.com](https://online.superoffice.com). All authentication calls must be made through this main endpoint.

API calls should go to the webapi\_url claim returned in the [JWT](https://docs.superoffice.com/en/api/netserver/authentication/online/validate-security-tokens.html#superoffice-specific-claims), or API URL returned by checking customer state: [Check tenant status](http://docs.superoffice.com/en/developer-portal/best-practices/tenant-status/check-status.html).

**More information**

FAQ:[How should I use flexible URL-addresses in CRMScripts and WebPanels?](https://community.superoffice.com/en/support-faqs/faq/how-should-i-use-flexible-url-addresses-in-crmscripts-and-webpanels/)
