---
title: "How do I change the language of the Privacy Confirmation e-mail message that is sent automatically to newly created contacts?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-change-the-language-of-the-privacy-confirmation-e-mail-message-that-is-sent-automatically-to-newly-created-contacts/
lang: en
updated: "6 Oct 2025"
---

# How do I change the language of the Privacy Confirmation e-mail message that is sent automatically to newly created contacts?

Updated on 6 Oct 2025

When I create a new contact in SuperOffice CRM, an automatic [Privacy Confirmation e-mail](https://docs.superoffice.com/en/security/privacy/learn/send-privacy-confirmation-email.html) is sent to them. How do I make sure that the e-mail is sent in the language that is preferred by the contact?

To begin with, it is important to know how SuperOffice CRM assigns the language of the Privacy Confirmation e-mail template. See the chart flow and the explanation below.

![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4911898-EKcsmtL1EZm543uk2hrFZXEGd3xMcB0zP2KCDXQ9ErjQlyZGcgI547z2Kp6IotJl-0/image.png)

1. If a **Preferred language** on a **Contact**is set and a Privacy Confirmation e-mail template\*\* is available in this language, this template will be sent to the **Contact´s** e-mail address.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6354077-mEjz0qKWiU8aOjWB3zMNqQXyUQfHkcPtamoTtdHqFpPdyUb8N0DbbYnDbXpyyFDy-0/image-20251006155301-3.png)
2. If a **Country\*\*\*** on a **Contact** is set and it has a translation of Privacy Confirmation e-mail template\*\*, this will be sent to the **Contact's** e-mail address.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6354076-KSDcxs6JoACBu82sEdItjXPjcqcyfjOy7akdK8D6on1C2RrQihPywKibaQYS7nrx-0/image-20251006155254-2.png)
3. If a **Preferred document language** for the logged-in user is selected, and it has a translation of the Privacy Confirmation e-mail template\*\*, this template will be sent to the **Contact** e-mail address.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6354079-7p39oIip4yW9lT6HjbL9D43kTzH1uBuZdljjhPN481aMdddqPzFenwqm0azuMRwW-0/image-20251006155426-4.png)
4. If an **Active Language** of the logged-in user is set to a language that can be mapped to a corresponding Privacy Confirmation e-mail template\*\*, this will be sent to the **Contact´s** e-mail address.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6354091-yfgBuC9TOYRJNrhmdec65Iz6pPx0bcEUyD5jw57xuBbfgebargfSDikcpStagFjZ-0/image-20251006155502-5.png)
5. If none of the above rules determines another language, the English Privacy Confirmation e-mail template will be sent to the **Contact´s** e-mail address.

**Please take into consideration these points:**

**\*** A preferred language field is a field in SuperOffice Service that is visible in a Contact card in SuperOffice CRM. [The languages can be defined](https://docs.superoffice.com/en/admin/options/learn/custlang/index.html) in Service, but this feature requires a license for SuperOffice Customer Centre. SuperOffice customers who have never used SuperOffice Service won't see this field in their CRM, unless they decide to use Service with Customer Center.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6354115-2fgnBjIZtGWRWGAGRPQSIsaYS3l1GMFUxHDeXeWIO8Wz5noasXjEcqILAbEF7ijk-0/image-20251006160354-7.png)

**\*\*** By default, SuperOffice CRM comes with 12 Privacy Confirmation e-mail template translations. You can easily **add (1)** a new translation or create and use a new Privacy Confirmation e-mail template. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-and-use-a-privacy-confirmation-e-mail-template/) to see how to do it.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6354113-RecdorTUw7AHcxtljrAe7NgsdGq4AxkYg0wqlLln8tcHgzXTXW8zB7fZXZTBsg2Q-0/image-20251006160159-6.png)

\*\*\* If a Contact's country is Switzerland, the default document and the e-mail language are German.

**More information**

FAQ: [How do I insert a subscription management link in the privacy confirmation e-mail template?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-insert-a-subscription-management-link-in-the-privacy-confirmation-e-mail-template/)

FAQ: [How do I disable or enable automatic e-mail, which sends out the Privacy confirmation message?](https://community.superoffice.com/en/support-faqs/faq/how-do-i-disable-or-enable-automatic-e-mail-which-sends-out-the-privacy-confirmation-message/)
