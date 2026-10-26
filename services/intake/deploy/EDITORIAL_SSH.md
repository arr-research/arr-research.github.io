# Restricted editorial SSH access

This optional bridge supports the founder's already-deposited historical cases.
It does not grant a general administrative shell. Install only after the owner
approves this specific access, expiry and device. Connection availability does not
authorize an assistant to accept or publish another paper without an instruction.

Allowed operations are exact-hash case inspection, preparing an authorized model
round, recording a genuine report, recording an external founder decision,
recording separate exact-file distribution permission, and recording a verified
AIRR GitHub release. The existing application validates each operation. This
bridge cannot issue historical deposit grants, upload PDFs, change the catalogue,
deploy software, manage users, read statistics, access backups or send shell
commands. Future extensions require a separately reviewed deployment.

The SSH public key is restricted to one fixed entry point with OpenSSH `restrict`
and expiry 2026-12-13 23:59:59 UTC. Forwarding, PTY, agent forwarding, X11 and
user rc execution are disabled. The launcher clears the SSH environment, loads
the existing root-owned application configuration, and the Python entry point
drops all supplementary groups and switches to the `airr-intake` service account
before importing the application. No client-supplied code, SQL, paths or arbitrary
URLs are executed. Requests and attached native evidence have bounded sizes.

The local client stores the private key using Windows CurrentUser DPAPI with a
file ACL limited to the Windows user and SYSTEM. It loads the key in memory,
pins the previously authenticated Netcup host key and does not copy passwords,
browser cookies or MFA seeds. This is intended for the same Windows user and
machine. A compromised Windows user session can use the credential; DPAPI is
not protection against an attacker already operating as that user.

The installer defaults to read-only preflight. `--activate` installs the reviewed
bridge from an explicit repository commit and SHA-256 and appends a uniquely
labelled public key without changing existing keys. Installation does not restart
the server or modify the web application's authentication settings. Record the
installer and bridge hashes in the operator's private activation receipt.

After installation, verify one authorized case and verify that `id`, a shell,
SFTP and forwarding requests are denied. A failed or uncertain mutation must be
reconciled through case inspection before any retry. Do not infer application
acceptance or publication from the SSH connection succeeding.

To revoke, use the authenticated administrator console to remove only the line
ending `airr-editorial-20260914` from `/root/.ssh/authorized_keys`. Preserve all
other keys. Verify that a new connection fails. Existing connections should be
closed separately if immediate revocation is required. Never remove the statistics
key, rotate unrelated credentials or disable MFA as part of this operation.

Primary references: [OpenSSH authorized keys](https://man.openbsd.org/sshd.8)
and [Windows CryptProtectData](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata).
