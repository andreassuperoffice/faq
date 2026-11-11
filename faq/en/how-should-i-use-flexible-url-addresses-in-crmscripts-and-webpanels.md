---
title: "How should I use flexible URL-addresses in CRMScripts and WebPanels?"
url: https://community.superoffice.com/en/support-faqs/faq/how-should-i-use-flexible-url-addresses-in-crmscripts-and-webpanels/
lang: en
updated: "13 Feb 2026"
---

# How should I use flexible URL-addresses in CRMScripts and WebPanels?

Updated on 13 Feb 2026

SuperOffice is operating its applications across different application URLs, also called endpoints or APIs.

As we are approaching a larger change to our operating environment in 2026, following best practices for integrations and customizations is more important than ever.

Today, several URLs in CRMScripts and WebPanels may point directly to a specific CRM Online instance, for example:

https://online2.superoffice.com/cust1234/CS/Scripts/blogic.fcgi?action=\*\*...

If subdomains or the structure of the Online environment change, such hard-coded full path URLs may stop working.

**How should CRMScripts and WebPanels be configured to avoid issues?**

To ensure that your customizations continue to work even if SuperOffice changes subdomains or the structure of the Online environment in the future, hard-coded full path URLs should be replaced with template variables.

After the update, WebPanel URLs should use template variables, for example:

<csbl>?action=...

These template variables automatically resolve the correct customer environment. This makes your configuration more robust and minimizes the need for future updates.

We recommend reviewing all CRMScripts and WebPanels and ensuring the following:

1. Identify any hard-coded full path URLs pointing to a specific CRM Online instance.
2. Replace those URLs with the appropriate template variables. Documentation for available variables is described in [Template variables for Service](https://docs.superoffice.com/en/document/templates/variables/for-service.html).
3. If you need to modify a WebPanel, follow the instructions here: [Add or edit Web Panel](https://docs.superoffice.com/en/customization/web-panels/admin/add-web-panel.html).
4. Test the WebPanel or CRMScript to confirm it resolves correctly in your environment.

**Note!** If you are using External Applications that address SuperOffice endpoints, they should follow the recommendations described in [Check tenant status](https://docs.superoffice.com/en/developer-portal/best-practices/tenant-status/check-status.html).

**More information**

FAQ: [How should I use flexible URL-addresses in External Applications?](https://community.superoffice.com/en/support-faqs/faq/how-should-i-use-flexible-url-addresses-in-external-applications/)
