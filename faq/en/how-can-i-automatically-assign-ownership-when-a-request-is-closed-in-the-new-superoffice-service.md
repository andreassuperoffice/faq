---
title: "How can I automatically assign ownership when a request is closed in the new SuperOffice Service?"
url: https://community.superoffice.com/en/support-faqs/faq/how-can-i-automatically-assign-ownership-when-a-request-is-closed-in-the-new-superoffice-service/
lang: en
updated: "2 Jul 2025"
---

# How can I automatically assign ownership when a request is closed in the new SuperOffice Service?

Updated on 2 Jul 2025

In the old version of SuperOffice Service, whenever a user changed the status of a request to *Closed*, they automatically became the owner of that request. In the new SuperOffice Service module, this automatic change no longer happens.

**Why was this behavior removed, and how can I replicate it if I still want the same result?**

In the new Service module, the automatic assignment of the user as the owner when setting a request to *Closed* has been removed.

The reason for this change is to simplify the system logic and allow more flexibility for customers to define their own behavior using macros or scripts. This approach avoids enforcing fixed functionality and instead allows customers to choose if and how they want ownership to be assigned.

You can easily recreate the previous behavior using macros or automation script.

**To set it up as a macro, please follow the steps below:**

1. Navigate to Settings and Maintenance – CRMScript (1) – Triggers (2) and click New trigger (macro) (3).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6258838-5FKTsocaIFcfLXRgZr4Kp2phtcScUah9MPZz69bANBOsf8pdJPCJRNDuYp5zPMxn-0/image-20250702210216-1.png)
2. Use the trigger "Request closed".

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6258839-OA5I85b3zKjJadWzFMqd7dAmMbZnF1OyYbfp2XntdquJ8ZzgFIqrLHB4qEaA7i5g-0/image-20250702210417-2.png)
3. Pick the action “Change a request”.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6258841-jjdA10f400Dwcp2Z1RRcR4oNfyqNHyBu5uNmj0GwWGsgHazHFoDQfJowYwA6y53M-0/image-20250702210621-4.png)
4. Check "Owner" (1), then click the small cogwheel (2) and use the environment value and current user ID (3).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6258842-OIsMPARSkQk0zKB5MDOn3s0tH6MUnaUIx0mGsmggSOhWjZ91G7H12FXG7HQnUdAR-0/image-20250702210844-5.png)
5. Enable the macro by clicking the toggle.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6258844-W3JAR5HC0Y5qdG7KXfJ2t3jq8enkAt48JDhYA8cqKngAMKZTEwglGaDEdzHObw5L-0/image-20250702211125-7.png)

When a user now sets a request to *Closed*, the macro will automatically assign that user as the **Owner** of the request.

This can also be solved with script for more advanced solutions.

**Note!** If you need help configuring this feature or writing a script, please contact our [Support team](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/). For advanced customizations, our consultants are available to help adapt SuperOffice to your company’s specific needs.

**More information:**

FAQ: [How do I start using CRMScript in SuperOffice Online?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-start-using-crmscript-in-superoffice-online/)

Docs: [Macros and scripts](https://docs.superoffice.com/en/automation/crmscript/learn/macro-script.html)

FAQ: [How do I configure SuperOffice Service that the customer gets an automatic notification when his request has been forwarded to a supplier?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-configure-superoffice-service-that-the-customer-gets-an-automatic-notification-when-his-request-has-been-forwarded-to-a-supplier/)
