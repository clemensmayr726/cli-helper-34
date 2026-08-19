import time

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.cache = {}

    def process_data(self):
        results = []
        for item in self.data:
            result = self._process_item(item)
            results.append(result)
        return results

    def _process_item(self, item):
        if item in self.cache:
            return self.cache[item]
        # Simulate an expensive operation
        time.sleep(0.1)
        processed = self._expensive_operation(item)
        self.cache[item] = processed
        return processed

    def _expensive_operation(self, item):
        # Just a mockup of an expensive operation
        return item * item

# Example usage
if __name__ == '__main__':
    processor = DataProcessor(range(10))
    start_time = time.time()
    results = processor.process_data()
    end_time = time.time()
    print(results)
    print(f'Processing time: {end_time - start_time}')