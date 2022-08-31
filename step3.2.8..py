def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result,  f"Wrong language, got {catalog_text} instead of {expected_result}"  