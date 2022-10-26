CUSTOM_PERMISSIONS = {
    'C1': ('c_create_trip', 'Can create new trip'),
    'C2': ('c_list_trip', 'Can list the created trips'),
    'C3': ('c_manage_team', 'Can manage team trips'),
    'C4': ('c_participated_trips', 'Can view participated trips'),
    'C5': ('c_create_trip_request', 'Can create trip requests'),
    'C6': ('c_manage_trip_request', 'Can manage trip requests'),
    'C7': ('c_access_ads_shared_trips', 'Can view all the shared with ADS trips'),
    'C8': ('c_access_external_shared_trips', 'Can view all the trips shared externally')
}


class CPermission:
    @staticmethod
    def _get_permission_string(p_string: str) -> str:
        return f"users.{p_string}"

    @staticmethod
    def get_create_trip_permission():
        return CPermission._get_permission_string(CUSTOM_PERMISSIONS['C1'][0])
