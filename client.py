class CouponReferralAbuseBlockerClient:
    def check_ip(self, ip_address: str) -> dict:
        return {"is_blocked": False}