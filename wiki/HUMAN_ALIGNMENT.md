# Human alignment vectors

A contextual, owner-controlled representation of declared preferences.

Each component names an axis, defines its endpoints and records a declared value with its source. Unknown values remain null. A value is meaningful only with its axis definition, context and version.

Keep goals, boundaries and permission preferences separate from numeric components. Preferences can change. Preserve the original statement and label an interpretation.

These numbers are not calibrated psychological measurements, diagnoses or an automatic basis for ranking people. Choosing social objectives is separate from recording a person's preferences.

## Prototype

- [JSON Schema](../schemas/human-alignment.schema.json)
- [Synthetic example](../examples/synthetic-human-alignment.json)
- Validate: `python tools/validate_alignment.py examples/synthetic-human-alignment.json`

Current contributions publish synthetic examples only. The schema reserves owner_published for future support, which requires owner review and an explicit publication design and decision. Real profiles remain in owner-controlled private storage. Permission preferences describe intentions; software must enforce actual authorization separately.

Next contribution: test whether owners can correctly inspect, revise and selectively share this representation.
