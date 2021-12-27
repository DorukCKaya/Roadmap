class WebPush:
    def __init__(self, Platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type):
        self.Platform = Platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print('Push gönderildi!')


class TriggerPush(WebPush):
    def __init__(self, Platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page: str):
        super().__init__(Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, Platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 send_date: int):
        super().__init__(Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date


class SegmentPush(WebPush):
    def __init__(self, Platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name: str):
        super().__init__(Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __init__(self, Platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 price_info: int, discount_rate: float):
        super().__init__(Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(price_info, discount_rate):
        return price_info * discount_rate


class InstockPush(WebPush):
    def __init__(self, Platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info: bool):
        super().__init__(Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stockUpdate(self):
        if stock_info == true:
            stock_info = false
        else:
            stock_info = true
        return stock_info
