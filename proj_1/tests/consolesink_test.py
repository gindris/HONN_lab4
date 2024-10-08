from structured_logging.sinks.consolesink import ConsoleSink

def test_sink_data(capfd, dict):
    dict = {'key': 'value'}
    ConsoleSink().sink_data(dict)
    captured = capfd.readouterr()
    assert captured.out == str(dict) + '\n'
    
    