# WhatsApp Meta Campaign Integration Guide

This guide details exactly how we built the Meta (WhatsApp & Instagram) bulk campaign broadcast system in the **Mahindra** and **Volvo** applications. Use this as a blueprint to replicate the exact same feature in your other bulk calling campaign apps.

## 1. Database Requirements (Prisma)
You need a way to store the system-level credentials for Meta. We used a generic `SystemConfig` table.

```prisma
model SystemConfig {
  key       String   @id
  value     String?
  updatedAt DateTime @updatedAt
}
```
**Required Keys:**
*   `META_ACCESS_TOKEN`: The permanent System User token generated in Meta Business Suite.
*   `META_PHONE_NUMBER_ID`: The unique ID of the WhatsApp phone number.
*   `META_CONFIG`: A JSON string representing the active configuration (e.g., `{"access_token": "..."}`).

## 2. Setting Up the Backend APIs

### A. Credentials API (`/api/credentials/system/route.ts`)
Creates an endpoint to save the credentials from the admin dashboard. 
*   **Logic**: When `META_ACCESS_TOKEN` is saved, automatically sync it to the `META_CONFIG` key as a JSON object so the campaign routes can read it easily.

### B. WhatsApp Push API (`/api/meta/campaign/push/route.ts`)
This is the core engine for sending messages.

**Step 1: Upload Media (If applicable)**
WhatsApp requires images to be uploaded to their server first to get a `media_id`.
```typescript
// Example: Converting base64 image from frontend to Blob and uploading
const formData = new FormData();
formData.append('messaging_product', 'whatsapp');
formData.append('file', blob, 'banner.jpg');

const uploadRes = await fetch(`https://graph.facebook.com/v18.0/${phoneNumberId}/media`, {
  method: 'POST',
  headers: { 'Authorization': `Bearer ${access_token}` },
  body: formData
});
const { id: mediaId } = await uploadRes.json();
```

**Step 2: Construct and Send the Message Payload**
For **Free-form Messages** (Interactive):
```typescript
const payload = {
  messaging_product: "whatsapp",
  recipient_type: "individual",
  to: phoneNumber, // Must NOT include '+' symbol, just country code and number
  type: "interactive",
  interactive: {
    type: "cta_url", // For URL buttons
    body: { text: "Your message body here" },
    action: {
      name: "cta_url",
      parameters: {
        display_text: "Click Here",
        url: "https://example.com"
      }
    }
  }
};
// Note: Meta prohibits media IDs in free-form cta_url headers. If sending an image with a URL button outside of a template, the image must be sent as a separate message first.
```

## 3. The Frontend Dashboard

### A. Configuration Page (`/dashboard/config/page.tsx`)
Add two secure password input fields:
1.  **WhatsApp Phone Number ID**
2.  **Permanent Access Token** (System User Token with `whatsapp_business_messaging` permissions)

### B. Campaign Manager (`/dashboard/campaigns/page.tsx`)
Create a UI with the following states:
*   **Audience Selector**: Dropdown to select the target group (must extract phone numbers array).
*   **Image Uploader**: Standard file input, read via `FileReader` as a base64 Data URL (`imageBlob`).
*   **Message Body**: Textarea for the main ad copy.
*   **Button Configurator**: Inputs for `buttonText` and `buttonUrl`.

When the user clicks "Push", bundle these states into a JSON payload and `POST` to `/api/meta/campaign/push`.

## 4. Understanding WhatsApp Message Types (Important Limitation)

When replicating this, it is critical to understand the difference between **Free-form Messages** and **Template Messages**.

### Free-form Messages (What we built initially)
*   Can only be sent if the customer replied to you within the last 24 hours.
*   Highly restricted formatting. For example, if you add a URL button (`cta_url`), Meta strictly forbids attaching an uploaded image to the same bubble. You must send the image separately.
*   Limited to 1 URL button or up to 3 Quick Reply buttons.

### Approved Template Messages (The "Bajaj Finance" Style)
*   Can be sent to ANY user at ANY time (perfect for cold bulk broadcasts).
*   Allows combining an Image Header, Text Body, Footer, and **up to 10 buttons** (mixed URL, Phone numbers, and Quick Replies) into **one single, unified chat bubble**.
*   Requires templates to be created and approved in the Meta WhatsApp Manager dashboard. The API payload changes to `type: "template"`.
