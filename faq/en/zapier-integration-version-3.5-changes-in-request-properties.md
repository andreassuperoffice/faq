---
title: "Zapier integration version 3.5: changes in Request properties"
url: https://community.superoffice.com/en/support-faqs/faq/zapier-integration-version-3.5-changes-in-request-properties/
lang: en
updated: "9 Oct 2025"
---

# Zapier integration version 3.5: changes in Request properties

Updated on 9 Oct 2025

Starting from 24th October 2025, the SuperOffice Zapier integration will be updated to version 3.5. This version changes how **Request message properties** are structured in Zapier. If your automations (Zaps) use Request data — such as **ID**, **body**, or **attachments** — you will need to review and update your field mappings to ensure your automations continue to work after the update.

What’s changing in version 3.5?

Currently, Request fields like **ID**, **body**, and **attachments** are available directly in Zapier. In version 3.5, these fields will be grouped under a new **Message** property.

This means:

- Automations using these fields will still run
- But the data will appear empty until you update the field mappings

**How do I know if I’m affected?**

You only need to update if your Zaps use SuperOffice Service (Requests). Common examples include:

- Sending request messages to Slack, Teams, or email

- Saving attachments to Google Drive or Dropbox

- Creating tasks or tickets in another system using request content

If your automations don’t use these Request fields, no action is required.

**What do I need to do?**

To keep your automations working after the update:

1. Open your Zapier dashboard

2. Edit any Zaps using Request fields

3. Re-map the affected fields under **Message** → **ID**, **body**, **attachments**

4. Test your Zap to confirm it works

5. Save and publish your changes

**Field mapping quick reference**

Here’s how the old fields map to the new structure in version 3.5:

Old structure (left), new structure (right). Note that in the new structure the Attachments property is on a lower hierarchical level, under the message property.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6355520-kNwUDppLIghy5FJXryXBQMxDjjuD6CLZ9YDz81Td14AxHrsnShP52haE4bjxSrRR-0/image-20251007142051-1.png)

Use this to quickly update your Zaps by selecting the new fields under the **Message** property.

**Troubleshooting (after the update)**

- ***My Zap shows missing fields or empty values***

If you notice that your Zap is running but request message fields are blank, it means the Zap is still pointing to the old structure. Edit the Zap and re-map the fields using the new **Message** property.

- ***My attachments stopped showing up***

Attachments will no longer be attached directly to the Request itself. They are part of the Message → Attachments property.

- Update your Zap to point to Message → Attachments
- Save and re-test the Zap

- ***Do I need to reconnect Zapier?***

No. You don’t need to reconnect your SuperOffice account — only the field mappings are affected.

- ***What happens if I don’t update?***

Your Zaps will continue to run, but:

- Request message fields will appear empty
- Any step depending on those fields may not behave as expected (e.g., missing content in notifications, no attachments saved)

- ***Where can I get help?***

If you need assistance updating your Zaps:

- Follow the step-by-step instructions above to re-map fields
- Review the troubleshooting tips on this page for common issues
- Still stuck? Contact our support team at [support@superoffice.com](mailto:support@superoffice.com)

**Example of one zap with error message after upgrade to 3.5**

After the update of Zapier 3.5, you may encounter an error stating that the Attachments

Attachment property is missing:

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6355563-zWQC0XDZlH27nmyNMKy8gLjnsBkT5upxLqPnIbwbLMCfcwL0ZcfYdTPNGUOEFHhm-0/image-20251007142403-2.png)![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6355561-Pz1LZ2ra05OXBzCn2F2iyIFxQKun22oicxEC6udgQYtNuh1zhyY0EaUlKPOGgDX5-0/image-20251007142403-3.png)

To fix that, make sure you are referencing the new structure by using Message Attachments Attachment property

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6355562-1qynj6cP5cboGP0jqDRm6ZbmsN23fY0h25sXDR3myYypskJ0M7s28BJx5PdHiUXC-0/image-20251007142403-4.png)
