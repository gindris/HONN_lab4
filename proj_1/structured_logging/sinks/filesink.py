from structured_logging.sinks.i_sink import ISink

class FileSink(ISink):
    def sink_data(self, data: dict):
        with open("log.txt", "a") as file:
            file.write(str(data) + "\n")