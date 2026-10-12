# Profile API returns 500

## Problem

The profile API returns HTTP 500 when a user
does not have a profile.

## Expected behavior

The API should return HTTP 404.

## Actual behavior

The API returns HTTP 500.

## Error

AttributeError:
'NoneType' object has no attribute 'name'

## Affected endpoint

GET /users/{user_id}/profile