# ARR governance and conflict controls

## Roles

- **Founder, registry operator, responsible editor and data controller:** Lluis
  Eriksson. He operates intake, signs ordinary external decisions and maintains the
  public registry.
- **Independent editor:** a named person with no relevant conflict, appointed for
  founder-authored/conflicted submissions and appeals.
- **Depositor/author:** supplies the work and disclosures; has no access to another
  submission and cannot alter the public registry.

“VD/CEO” is reserved for a duly formed entity with that office. ARR currently uses
the accurate natural-person roles above.

## Non-delegable manual gate

No upload, automated check, model score or pull request can publish a record. A
human editor must sign the exact version, decision basis, integrity hash, conflict
declaration and applicable protocol. Acceptance only authorizes the separate public
packaging workflow; it does not perform it automatically.

## Founder–editor–author conflict

A direct conflict includes authorship, co-authorship in the previous three years,
supervision, close institutional dependence, family/close personal relationship,
financial interest, active dispute or another circumstance reasonably affecting
impartiality. The submitter and editor must disclose it.

When the operator is an author or directly conflicted:

1. he may perform administrative and security triage but cannot issue final
   acceptance or decide an appeal;
2. his “accept” action becomes `awaiting_independent_decision`;
3. a named independent editor reviews the same version and records the final basis;
4. the public record discloses the founder relationship and independent sign-off;
5. absent an available independent editor, the case remains private or is declined
   without a quality inference.

An editor never decides their own work. Appeals are reviewed by someone other than
the original decision-maker. Aggregate counts of submissions, outcomes, appeals,
conflicts and reversals should be published annually once the pilot has activity,
without exposing rejected manuscripts or personal data.

## Change control

Policy changes are versioned in Git. Changes cannot retroactively convert a private
submission into a public deposit, remove an appeal already offered, or weaken an
accepted license without the affected party's agreement. Emergency restrictions
are logged and reviewed after the immediate risk has passed.
