# Permissions and Groups in Django

## Groups:
- Admins: Full permissions on Book model.
- Editors: can_create, can_edit
- Viewers: can_view

## Custom Permissions:
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Views Protection:
Used `@permission_required()` decorator to restrict actions.

## How to Test:
1. Create users.
2. Assign to one of the groups.
3. Login and test access to views.