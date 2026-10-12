
---

### `data/documentation/database.md`

```markdown
# Database Documentation

## users

Stores registered users.

Columns:

- id
- name
- email

## profiles

Stores optional profile information.

Columns:

- id
- user_id
- name
- email

Important:

A user does not necessarily have a profile.

Therefore, queries against the profiles table
may return no result.
