# Permissions & Groups Setup

## Custom Permissions (defined in `CustomUser.Meta`)
- `can_view`   → Can view user profiles
- `can_create` → Can create user profiles
- `can_edit`   → Can edit user profiles
- `can_delete` → Can delete user profiles

## Groups
- **Viewers** → Assigned `can_view`
- **Editors** → Assigned `can_view`, `can_create`, `can_edit`
- **Admins**  → Assigned `can_view`, `can_create`, `can_edit`, `can_delete`

## Testing
1. Create test users and assign them to groups.
2. Log in as each user and attempt to access:
   - `/view_profile/` → requires `can_view`
   - `/create_profile/` → requires `can_create`
   - `/edit_profile/` → requires `can_edit`
   - `/delete_profile/` → requires `can_delete`
3. Confirm that permissions are enforced:
   - Viewers → only `can_view`
   - Editors → `can_view`, `can_create`, `can_edit`
   - Admins  → all permissions
