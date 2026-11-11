---
title: "What to do when a new web panel in SuperOffice CRM does not work?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-new-web-panel-in-superoffice-crm-does-not-work/
lang: en
updated: "16 Jul 2025"
---

# What to do when a new web panel in SuperOffice CRM does not work?

Updated on 16 Jul 2025

We noticed that some of the web panels stopped working. Why does it happen and how do we fix it?

There could be several reasons why a new web panel does not work. Here are a few most common situations:

- [When your user does not belong to the user group that has access to the panel](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-new-web-panel-in-superoffice-crm-does-not-work/#1)
- [When the URL, that is configured in the web panels, is not accessible](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-new-web-panel-in-superoffice-crm-does-not-work/#2)
- [When the URL, that is configured in the web panel, is using the http protocol](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-new-web-panel-in-superoffice-crm-does-not-work/#3)
- [When the same-origin policy is not respected](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-new-web-panel-in-superoffice-crm-does-not-work/#4)
- [When you created a new panel in the InfoBridge platform and did not refresh SuperOffice CRM](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-a-new-web-panel-in-superoffice-crm-does-not-work/#5)

**When your user does not belong to the user group that has access to the panel**

When you create a new panel (e.g. Google Maps (1)) and you use the **Grouping and Filtering** (2) functionality, please make sure the users who should be able to see the panel belong to the groups (3) that have access to see it. Please check [this FAQ](https://community.superoffice.com/en/support-faqs/faq/how-do-i-create-a-new-user-in-superoffice-crm2/) to see how to assign a User Group to a user.

![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6271064-3Z5gKuhZUxNOSKiBFre8oO68CF0Z6mNMup7WKPzFb7QTUYwSrQtDzB5kumdHjUGi-0/image-20250716151751-1.png)

**When the URL, that is configured in the web panels, is not accessible**

​To test if the URL defined in the web panel is accessible, please make the test described below:

1. In the [Settings and Maintenance](https://community.superoffice.com/en/support-faqs/faq/how-do-i-access-administration-part-settings--maintenance-in-superoffice-crm/) click on the **Lists** (1) section, select the **GUI - Web panel** (2) option from the drop-down menu, and then select the web panel (3), which doesn't work.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6271079-kPGTsi2BBbBz3GuKtIQtGrLqOPBOQLsP9T2h4ucDDoHlXLBmIdO2ZtPag2cwGfqZ-0/image-20250716151945-2.png)
2. Double-click to open the faulty web panel. Copy the address defined in the URL field and paste it into your internet browser. It should display the content you want to see in the web panel. If it works, please check the next section. If it doesn't display the web content you need, please investigate why the site is not accessible.

   ![](https://online3.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/6271082-CNe1odTn1OTJh908ZijN6sN11Qyp117MNLIHMSB29xQH3dr1IzWA5aCiHOC2w6ac-0/image-20250716152053-3.png)

****When the URL, that is configured in the web panel, is using the http protocol****

SuperOffice Online is accessible via the **https** protocol. If the application or the web site, which is defined in your web panel, is accessible via the **http** protocol - you will run into the situation, where the site cannot be displayed due to the "mixed content". To make sure that this is the case open ["Console" in your browser](https://balsamiq.com/support/faqs/browser-console/) and you should see the error:

*Mixed Content: The Page at '[URL to site]' was loaded over HTTPS, but requested an insecure resource  '[URL to site]'. This request has been blocked; the content must be served over HTTPS.*

If the site also provides the service in the https format, you can change the URL in the web panel setup, in the Settings and Maintenance. Then the problem should be fixed. Please read [this article](https://dev.to/mittalyashu/mixed-content-fetching-data-from-https-and-http-3n31) for more information.

****When the same-origin policy is not respected****

The same-origin policy is an important concept in the web application security model. Under this policy, a web browser permits scripts, contained on the first web page, to access the data on the second web page. This can happen only if both web pages have the same origin.

It is not handled by SuperOffice, but by the browser used by a SuperOffice user. It is the owner of the content who decides if others can use their content on a "cross-domain site". See the LinkedIn example discussed in [this](https://community.superoffice.com/en/technical/forums/product-forums/crm-windows-application/linkedin-shown-in-minicard/) forum thread.

To test if this is the case –  i.e. why the content of the web panel is not displayed – open ["Console" in your browser](https://balsamiq.com/support/faqs/browser-console/). There you should see the error: "[Refused to display '[URL to site]' in a frame because it set 'X-Frame-Options' to 'SAMEORIGIN](https://stackoverflow.com/questions/41522652/refused-to-display-url-in-a-frame-because-it-set-x-frame-options-to-sameori)."

The browser's security controls are another factor, that could explain why web panel content is not visible. When a site carries the "DENY' or "SAMEORIGIN" page, that either prohibits the site from being displayed in an iFrame altogether, or it requires that the iFrame displaying this URL is a member of the same domain (origin) as the site itself.

For example, if you try to display one of these sites within the SuperOffice iFrame and you encounter the SAMEORIGIN parameter, that means the site is not permitted to run in SuperOffice CRM, as the domain of SuperOffice and the domain of the host site are different.

**Note!**

1. There is, unfortunately, no solution for this situation, as this is enforced by browsers based on headers. If you own the site that you are trying to add via the iFrame, then you can send the headers stating that your site might be added by others, or add *online.superoffice.com* or *superoffice.com* in crossdomain.xml.
2. Some sites, like YouTube, provide this service with the "cross-domain site" support - by using another URL:

   ![](https://online2.superoffice.com/Cust1990/CS/scripts/customer.fcgi/getAttachment/4070255-xlUUNZZfdTgippbw1M8Z33TC0r5nMnJXhSa4zNt3Wlt96CAEckqZD5a6qwuT2k1f-0/image.png)

**When you created a new panel in the Panel administration site (InfoBridge) and did not refresh SuperOffice CRM**

When you create a new panel in a special [Panel administration site](https://my-panels.infobridgeuniverse.com/Account/Login?ReturnUrl=%2FHome), please click on the SuperOffice URL to flush the site.

![](https://infobridgekb.atlassian.net/wiki/download/thumbnails/20021317/image2018-12-5_15-41-57.png?version=1&modificationDate=1544107630525&cacheVersion=1&api=v2&width=850&height=45)

**Note!** In the Panel overview, you can also click the green **Refresh SuperOffice** button to refresh SuperOffice CRM.

![](https://infobridgekb.atlassian.net/wiki/download/attachments/20021317/image2018-12-3_15-45-32.png?version=1&modificationDate=1544107630890&cacheVersion=1&api=v2)

****More information:****

Docs: [GUI - Web panel](https://docs.superoffice.com/en/admin/lists/learn/web-panel-add-item.html)

Wikipedia: [Same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy)

Mozilla Developer forum: [X-Frame-Options header](https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options)

w3.org: [Mixed Content](https://www.w3.org/TR/mixed-content/)
