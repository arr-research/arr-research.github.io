# AIRR voluntary-support policy — ARR-SUPPORT-1.2

**Effective:** 2026-09-06

AIRR currently charges nothing for submission, assessment, publication and
withdrawal. Voluntary support helps fund operation, preservation and
research-assessment costs. The support page offers a payment link only when the
operator has checked the public PayPal donation page and its recipient.

A contribution:

- is not a submission or publication fee;
- does not accelerate review or buy access;
- cannot influence acceptance, rejection, scoring, ranking, highlighting, appeal or
  correction decisions; and
- does not create ownership, editorial control or a tax-deductibility representation.

The recipient is **Lluis Eriksson**, AIRR's individual operator in Sweden.
This payment destination is not represented as a separate registered charity,
association or company. Any change of legal recipient requires a new payment
destination and an updated notice.

PayPal processes payments on its own service, under its own terms, privacy notice
and transaction fees. Visitors should check the recipient, amount and frequency
on PayPal before paying. AIRR uses a normal external link and loads no PayPal
widget or tracking script. AIRR does not collect card details or infer payment
success from a return URL.

PayPal provides transaction data such as donor name, email, amount, currency,
transaction identifier and any note. These are used for payment administration,
fraud handling, refunds, accounting and legal obligations. Donors are not added
to a mailing list or public donor ranking. A donor may optionally identify the
paper their support relates to, using a published paper ID or the registration
reference displayed on their private-submission receipt. A registration reference
is not a password and does not grant access to the manuscript, receipt or editor
dashboard. Never include a manuscript, private access link or sensitive information.
References are used only for support and payment administration, not editorial
decisions or assessment/ranking data.

After successful private intake, the browser receipt offers the same verified
PayPal link and a copyable note, `AIRR submission SUB-...`. This does not send the
registration number, title, abstract or PDF to PayPal automatically. The donor
chooses whether to paste the reference into PayPal's optional note. If PayPal does
not offer a note field, the donor may send the payment transaction reference and
paper registration number to the operator's support contact afterwards. The site
does not mark a donation as completed or automatically match payments to papers.
Receipt references and payment records must remain separate from scientific
assessment, ordering and admission decisions.

Questions, refund requests and conflicts should use the operator contact channel
with subject `AIRR support` and the PayPal transaction reference. A refund is considered against the payment record and
applicable PayPal rules; it cannot change any editorial decision.

## Payment-link configuration

`site/donations.json` contains either a public `paypal_business` recipient email or
a public `paypal_hosted_button_id`, never credentials. The build constructs an
HTTPS link to PayPal's public donation page. Both fields empty leave payments
unavailable. Invalid or conflicting values fail the build; the PayPal management
URL is not a donation link. Before enabling or changing the destination, check the
public checkout recipient and confirm that no unavailable-donations error is
shown. Update the displayed recipient details at the same time.

On 2026-09-06, the public email-based checkout displayed the operator's email,
an amount field, one-time/monthly options and PayPal/card payment controls. This
was a checkout inspection, not a completed payment test. The separate hosted
button's settings were not changed.

Previous versions remain in repository history.
