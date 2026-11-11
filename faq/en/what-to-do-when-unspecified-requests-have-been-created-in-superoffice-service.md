---
title: "What to do when \"unspecified\" requests have been created in SuperOffice Service?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-unspecified-requests-have-been-created-in-superoffice-service/
lang: en
updated: "28 Dec 2025"
---

# What to do when "unspecified" requests have been created in SuperOffice Service?

Updated on 28 Dec 2025

I have noticed new requests in the Service, which have a type "Unspecified". When I try to open one of them I get an error: *Something went wrong <...>* Why these requests were created and how do I remove them from SuperOffice Service?

In some situations, "Unspecified" requests can be created unintentionally because of a failed import of e-mail, script, e-mail filter, corrupted reply template, etc.

The "Unspecified" requests, which have already been created, can be deleted only directly from the database using request IDs.

The steps below explain how these IDs can be found:

1. In the SuperOffice navigator, click on the **Requests** (1)button and click on the **Find requests** (2) item in the drop-down menu.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465299-lBXapGTbKmx5t4skyaClRNIeH3QF5XhZJBAlsSOmJXqzKwT0Kw8hjZusayuFOsWf-0/image-20251228033646-1.png)
2. In the search, make sure the **Title** (2) field is included among the search fields. You can do it by clicking on the **Add criteria (1)** button.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465300-3LKispzskstATOZ0ogbrpTzxn3fBYS9HKnMbbGAJlciZ2cL9rjpEJdmai2eIPckY-0/image-20251228033851-2.png)
3. Add a tick next to the **Advanced view (1)**option to enable more search functions. Then click on the field next to **Title (2)**and choose the*is empty*option from the list, and click on the **Search (3)**button to get a list of requests.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465301-HexiUhBuQFF3cGRHNlr3mBDYlfLXRSTmiylbE06EYYceW3s3kH5lOm8yPM03xsn7-0/image-20251228034019-3.png)
4. Right-click on the **Title** column and select the **Sort ascending** option.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465302-KLtNznOtYgOFeJbdkYTkgszenXfwDW2ZnwhADTBYM38iHit3I171EiFOmFWIzMN5-0/image-20251228034113-4.png)
5. "Unspecified" requests will appear at the top of the list with an empty **Title** as in the example below.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6465303-BL8QDlji1blYoP5hNYrb6kjnmImMkwWD43wCz0RgNWbeoBAoKuQiCmmH2IeTp8ws-0/image-20251228034355-5.png)

   **Note!
   ​​​​​
   ​​**1. In the SuperOffice Online solution, empty requests should not appear. If, for unexpected reasons, they do, you should be able to delete them using [Batch Task](https://community.superoffice.com/en/learning/best-practices-tips/service/7-reasons-why-batch-management-should-be-your-favorite-feature-in-superoffice-service/). If that does not help, please [contact support](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/) and provide them with screenshots of the IDs of the empty requests.

   2. If this situation arises in the SuperOffice Onsite solution, your database administrator could delete them from the Ticket table in the database. We recommend taking a [backup](https://community.superoffice.com/en/support-faqs/faq/how-do-i-make-a-backup-of-the-superoffice-crm-database/) before making any changes directly to the database. If you need help with this, don't hesitate [to get in touch with support](https://community.superoffice.com/en/support-faqs/faq/how-do-i-register-a-support-request-from-within-superoffice-crm/).
