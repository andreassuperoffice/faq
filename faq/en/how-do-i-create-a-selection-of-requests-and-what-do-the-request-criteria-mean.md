---
title: "How do I create a selection of requests, and what do the request criteria mean?"
url: https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-a-selection-of-requests-and-what-do-the-request-criteria-mean/
lang: en
updated: "31 Mar 2026"
---

# How do I create a selection of requests, and what do the request criteria mean?

Updated on 31 Mar 2026

I want to create a selection for requests. How can I do this, and what does each criterion mean?

To create a new selection for requests, follow the steps below:

1. Click on the **Find** button (1) and select **Find Request** (2)

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6379441-Y8huXOSqtcfrd0s36yreFgWrtg8450xkLzxcSsOBkpdQ5iMT79EtATRzLB0AdHbH-0/image-20251028075215-2.png)
2. You will see a screen with pre-defined criteria for the **Find Request** search. You can use this screen to search for the requests by adding items that you want to search for.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6379531-GHgKs6jxPnoKcmuAxGDIlWCJULlp3jOfdQoGGd5SApFT7rOUlSTGp6HUpgf8YM7P-0/image-20251028091424-4.png)
3. At the bottom of the criteria list, you have the option to **Add criterion**. Click it if you want to include more criteria in your selection.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6379465-iz5iIdqsGYQ4rqPZyyDTboROgwlIpzZqM2tntMNy2orZrmQ8j8BAezmKjpAypU0H-0/image-20251028081130-3.png)

   The following list explains all available search criteria and what they stand for:

- **Access level:**External or internal access level
- **Author:**External person's name in a message
- **Category:**Categories in the system
- **Category ID:**The database ID of the category
- **Closed at:** The date and time when the request was closed
- **Content:**Freetext search to search for words inside messages
- **Created:** The date and time when the request was created
- **Created by:** Whom the request was created by
- **Created by - Primary group:** The primary group of the user who created the request.
- **Created by flow:**Filter requests created automatically by a flow.
- **Deadline:** Deadline for the request
- **First read by owner:** The datetime for when the request was first read by the current owner.
- **First read by user:** The datetime for when the request was first read by a user.
- **Has attachment:** If the requests have attachments(yes or no)
- **Internal status:** The status of the request from the status list (not the same as system status)
- **Language:** The language of the first external message
- **Last changed:**The date and time the request was last modified
- **Number of messages:** Number of messages in a request
- **Number of replies:** Number of replies on a request internally
- **Origin:** Source of the request(Unknown, E-mail, SMS, Fax, Phone, Facebook, Twitter, Internal, Customer Center, eMarketing, Automatic, Chat, Form)
- **Owner:**Owner of the request (internally)
- **Owner - Full name:** Owner's full name
- **Owner - Primary group:**Shows requests owned by users who belong to the chosen primary group.
- **Postponed to:**The date and time the request is postponed until.
- **Priority:** Priority of the request
- **Priority ID:**The database ID of the priority of the request
- **Read:** Read status of the request (Read by owner, new information, not read by owner)
- **Read by contact:** The date and time when the request was read externally
- **Read by owner:**The date and time when the request was read internally
- **Real time externally:**The total time, within 24x7 hours, the request has been in an external waiting status (configurable), not including the current state
- **Real time in queue:**The total time, within 24x7 hours, the request has been in a queue status, not including the current state
- **Real time internally:**The total time, within 24x7 hours, the request has been in an open status (configurable), not including the current state
- **Real time to close:** The time between when the request was created and when it was closed. Calculated 24x7
- **Real time to reply:** The time between when the request was created and when it was replied to. Calculated 24x7
- **Replied at:**The datetime for when the request was replied to. I.e., the first external message added to the request
- **Request ID:** The request ID of the request
- **Request type:** Filter requests by their assigned request type
- **Sentiment:**The indexed AI set sentiment of the last external message in the request
- **Sentiment confidence:**The confidence value of the AI set sentiment of the last external message
- **Status:**The database/system status of the request (Active, Closed, Postponed, Deleted, etc.)
- **Status ID:**The database ID of the internal status from the status list in request settings.
- **Suggested category:**The category that the AI categorization tool suggested for the request
- **Tags:**The tags assigned to the request
- **Time spent:**Sum of time spent by users creating all messages in the request
- **Time spent externally:**The total time within the request priority's timeframe that the request has been in an external waiting status (configurable), not including the current state
- **Time spent in queue:**The total time within the request priority's timeframe that the request has been in a queue status, not including the current state
- **Time spent internally:**The total time within the request priority's timeframe the request has been in an open status (configurable), not including the current state
- **Time to close:**The time between when the request was created and when it was closed. Calculated based on the request priority´s timeframe
- **Time to reply:** The time between when the request was created and when it was replied to. Calculated based on the request priority´s timeframe
- **Title:**Title of the request

**Note!** Additional criteria may appear in the list when custom fields are added to requests.

**More information:**

FAQ: [How can I see all our requests in all categories in SuperOffice Service?](https://community.superoffice.com/en/support-faqs/faq/how-can-i-see-all-our-requests-in-all-categories-in-superoffice-service/)

Docs: [ticket Table](https://docs.superoffice.com/en/database/tables/ticket.html)
