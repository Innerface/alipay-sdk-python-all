#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeQueryModel(object):

    def __init__(self):
        self._org_pid = None
        self._out_trade_no = None
        self._trade_no = None

    @property
    def org_pid(self):
        return self._org_pid

    @org_pid.setter
    def org_pid(self, value):
        self._org_pid = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_pid:
            if hasattr(self.org_pid, 'to_alipay_dict'):
                params['org_pid'] = self.org_pid.to_alipay_dict()
            else:
                params['org_pid'] = self.org_pid
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeQueryModel()
        if 'org_pid' in d:
            o.org_pid = d['org_pid']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


