#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IntelligentPromo import IntelligentPromo


class KoubeiMarketingCampaignIntelligentPromoCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignIntelligentPromoCreateResponse, self).__init__()
        self._promo = None

    @property
    def promo(self):
        return self._promo

    @promo.setter
    def promo(self, value):
        if isinstance(value, IntelligentPromo):
            self._promo = value
        else:
            self._promo = IntelligentPromo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignIntelligentPromoCreateResponse, self).parse_response_content(response_content)
        if 'promo' in response:
            self.promo = response['promo']
