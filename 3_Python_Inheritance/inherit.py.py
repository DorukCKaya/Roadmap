class WebPush:
    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type):
        self.Platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    @staticmethod
    def send_push():
        print('Push gönderildi!')


class TriggerPush(WebPush):
    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page: str):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 send_date: int):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date


class SegmentPush(WebPush):
    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name: str):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 price_info: int, discount_rate: float):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    @staticmethod
    def discount_price(price_info, discount_rate):
        return price_info * discount_rate


class InstockPush(WebPush):
    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info: bool):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stock_update(self):
        if self.stock_info:
            self.stock_info = False
        else:
            self.stock_info = True
        return self.stock_info
