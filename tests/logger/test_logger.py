# -*- coding: utf-8 -*-
"""
Tests logger.py
"""
from testfixtures import log_capture


@log_capture()
def test_logger(capture):
    """
    Tests logger from Logger class .

    Parameters
    ----------
    capture: testfixtures.logcapture.LogCaptureForDecorator

    Returns
    -------
    None

    """
    # Setup
    from logger import log

    log.info("info1")
    log.warning("warning2")
    log.error("error3")

    # Test
    capture.check(
        ("root", "INFO", "info1"),
        ("root", "WARNING", "warning2"),
        ("root", "ERROR", "error3"),
    )
