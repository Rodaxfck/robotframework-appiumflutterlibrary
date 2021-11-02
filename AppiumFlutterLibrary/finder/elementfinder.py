from appium_flutter_finder import FlutterElement, FlutterFinder

class ElementFinder():
    def __init__(self):
        self._element_finder = FlutterFinder()
        self._strategies = {
            'xpath': self._find_by_xpath,
            'key': self._find_by_key
        }

    def find(self, application, locator):
        assert application is not None
        assert application is not None and len(locator) > 0

        (prefix , criteria) = self._parse_locator(locator)

        prefix= 'default' if prefix is None else prefix
        strategy = self._strategies.get(prefix)
        if strategy is None:
            raise ValueError("Element locator with prefix '" + prefix + "' is not supported")
        return strategy(application, criteria)

    def _find_by_key(self, application, element_key):
        finder_key = self._element_finder.by_value_key(element_key)
        element = FlutterElement(application, finder_key)

        return element
        
    def _find_by_xpath(self, application, xpath):
        return

    def _parse_locator(self, locator):
        prefix = None
        criteria = locator

        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0].strip().lower()
                criteria = locator_parts[2].strip()
        return (prefix, criteria)