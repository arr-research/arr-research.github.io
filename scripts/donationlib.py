# SPDX-License-Identifier: AGPL-3.0-or-later
"""The public site and private receiver share one verified payment destination."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote


def load_donation_url(path: Path) -> str:
    config = json.loads(path.read_text(encoding="utf-8"))
    button_id = config.get("paypal_hosted_button_id", "")
    business = config.get("paypal_business", "")
    if button_id == "" and business == "":
        return ""
    if button_id == "":
        if not isinstance(business, str) or not re.fullmatch(r"[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", business):
            raise ValueError("Donations require a verified PayPal recipient email")
        return f"https://www.paypal.com/donate/?business={quote(business, safe='')}"
    if business != "":
        raise ValueError("Configure only one PayPal donation destination")
    if not isinstance(button_id, str) or not re.fullmatch(r"[A-Z0-9]{13}", button_id):
        raise ValueError("Donations require a verified PayPal hosted button ID, not a management URL")
    return f"https://www.paypal.com/donate/?hosted_button_id={button_id}"
