import time


def wait_until(predicate, error_message, time_to_wait=5, step=0.1):
    start = time.time()
    while True:
        try:
            return_value = predicate()
            if return_value:
                return return_value
        except:
            time.sleep(step)
        if (time.time() - start) > time_to_wait:
            raise TimeoutError(error_message)
        time.sleep(step)