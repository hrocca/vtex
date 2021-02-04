from .base_api import BaseApi


class LicenceManagerApi(BaseApi):
    def _build_url(self, endpoint):
        midpoint = "/api/vlm/account/stores"
        url = self.base_url + midpoint + endpoint
        return url
    
    def get_store_by_account(self):
        url = self._build_url('')
        return self.get_result(url)


