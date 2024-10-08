from structured_logging.sinks.i_sink import ISink

class ConsoleSink(ISink):
    def sink_data(self, data: dict):
        print(data)