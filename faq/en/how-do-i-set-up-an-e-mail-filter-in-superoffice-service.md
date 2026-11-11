---
title: "How do I set up an e-mail filter in SuperOffice Service?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-set-up-an-e-mail-filter-in-superoffice-service/
lang: en
updated: "27 Mar 2025"
---

# How do I set up an e-mail filter in SuperOffice Service?

Updated on 27 Mar 2025

I want those e-mails, which come from a particular domain, would end up in a dedicated category and that e-mails with specific keywords in the text body would be assigned to dedicated agents. How do I set it up using e-mail filters in SuperOffice Service?

To set up the two examples described in the question, click on the sections below:

- [Setting up an e-mail filter for a particular domain](https://community.superoffice.com/en/support-faqs/faq/how-do-i-set-up-an-e-mail-filter-in-superoffice-service/#1)
- [Setting up an e-mail filter for a particular keywords](https://community.superoffice.com/en/support-faqs/faq/how-do-i-set-up-an-e-mail-filter-in-superoffice-service/#2)
- [Setting up an e-mail filter to filter SPAM (only if mailbox is Microsoft 365 and Exchange)](https://community.superoffice.com/en/support-faqs/faq/how-do-i-set-up-an-e-mail-filter-in-superoffice-service/#3)

**Setting up an e-mail filter for a particular domain**

To set up that e-mails coming from particular domain would end up registered in a dedicated category, please follow the steps below:

1. Click on ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149503-cfhYcI4xnUeuuTS9bZ7UPPoIx0iEcMhxa3jd9ge5gXxitcCi27IKcALMxArRrew4-0/image-20250327163624-1.png) button, then choose **Settings and maintenance.**

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149504-l5wsOMzH12tFB3Uo3ohjBpIAUNZCfepEhUXYrMpF0uPNatJXRYJgHumWy9fkwCRk-0/image-20250327163642-2.png)
2. Select the **Requests (1)** tab, then navigate to **E-mail** (2) - **E-mail filters** (3) and click on the **New e-mail filter (4)** button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149506-LL4xn2wH3tnoKMI1QCCNLRxSqJuBU4JcxL406aboJ67qRpPmQgwb4kJImOlarQ09-0/image-20250327163829-3.png)
3. In the **Filter (1)**tab, add the **Description (2)** and select the option **E-mail which contains (3)** and fill it in with the e-mail domain as in the example: from: .\*(@gmail.com).\*

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149574-hKODOk3ZpHP155P8J5j3A5kG7MSPiKGisWgHP0U8BSm0b6cqtSHDkikiGQ9Mu3zD-0/image-20250327165535-15.png)
4. In the **Set properties (1)**tab, you can set specific properties for requests that are generated from e-mails that match the current filter. For example, we want to assign all the incoming e-mails with the Gmail domain to a particular **Category (2)**.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149575-Yi8w3FYr7CfIr5PCtwIwDfDXxgLaFnKqPHiYfBZRszaK1tXJK8OCJR3q8TF9JPZa-0/image-20250327165616-16.png)
5. In the **E-mail boxes (1)** tab, you can specify the mailbox or mailboxes to which this e-mail filter applies. To finish, click **OK (2)**to save the filter setup.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149562-pFuaYUbOYO3zde5oy5nKTtkY0JW23Iw7RL9ziDKKUkdsJaX3q05XA00POOHB4zGN-0/image-20250327165127-11.png)

**Setting up an e-mail filter for particular keywords**

To set up that e-mails with particular keywords would be assigned to dedicated agents, please follow the steps below:

1. Click the **New e-mail filter** button.
2. In the **Filter (1)**tab, select the option **E-mail which contains (2)** and fill it in with keywords, which should be found in the e-mail body, as it is shown in the example below.

   **Note!** For complex filter rules, we recommend using [Regular Expression](https://en.wikipedia.org/wiki/Regular_expression). For example, if you would like to use more than one keyword for search, regular expression would look like .\*(audi|bmw|ford).\*

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149535-AOoSibDEMNbhbeyWBc4iNMrYkZKSiJiCBziXqmo19bbjq7GTZC5mGI3oHMp43Wsc-0/image-20250327164839-8.png)
3. In the **Set properties (1)** tab, you can set specific properties for requests that are generated from e-mails that match the current filter. For example, we want to assign all the incoming e-mails with the word “audi” in the request message text to a particular owner (2).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149538-sPfALyNKy2G8cPRJHXljqwNpCxbLu5inqNXtTgBRDnWXw8zLAopeZuKZhqeAnFGI-0/image-20250327164923-9.png)
4. In the **E-mail boxes (1)** tab, you can specify the mailbox or mailboxes to which this e-mail filter applies. To finish, click **OK (2)**to save the filter setup.
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149546-BYteDnR58kyS4TCCUHKYgYQCiOqUT4jjyiYZe5h0DP3sIrWsmPJjh1SRXxS70j0r-0/image-20250327165117-10.png)

**Note!** The filter setup will scan a message in HTML not in plain text format. That means that all HTML tags can be recognized as your filter search string. Please take this into consideration when building your e-mail filters.

**Setting up an e-mail filter to filter SPAM (only if mailbox is Microsoft Office 365 and Exchange)**

The email header of the e-mails that are imported from the mailbox that is hosted in Microsoft Office 365 and Exchange will contain an SCL value and BCL values. This could be a great indicator whether an e-mail is spam or suspicious. Please read more about these values in Microsoft articles: [Spam confidence level (SCL) in EOP](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/spam-confidence-levels?view=o365-worldwide) and [Bulk complaint level (BCL) in EOP](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/bulk-complaint-level-values?view=o365-worldwide)

To set up that e-mails with a high spam score would be blocked, please follow the steps below:

1. Click the **New e-mail filter** button.
2. In the **Filter (1)**tab, select the option **E-mail which contains (2)** and fill it in with keywords, which should be found in the e-mail header, as it is shown in the example below.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149572-FGJ2Zthfxb0HJbhqWciBz4ug3UWTb0lSmjGacqT9fMn8oHgofwpIQu4DuXUckSY4-0/image-20250327165448-14.png)
3. In the **Set properties (1)** tab, select to **Block e-mail** (2).

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149570-EJ1uQnjrJcZO76AJCMhJ3EH3Jy7EyEm9qXm4wFkoPnbF6tOpMN2hgPE5lP7fElbn-0/image-20250327165304-13.png)
4. In the **E-mail boxes (1)** tab, you can specify the mailbox or mailboxes to which this e-mail filter applies. To finish, click **OK (2)**to save the filter setup.
   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6149563-Yfc4ifNAl9ot5oE7jBIP0akoeApqFYPlQ27aLdUooYpCyobgu0cyOlolO6p3SJC7-0/image-20250327165144-12.png)

**More information**

Docs: [Create e-mail filter](https://docs.superoffice.com/en/email/service/learn/email-filters/create-email-filter.html)
