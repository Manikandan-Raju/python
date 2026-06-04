"""
Logging basics in Python.

Logging is used to track events that happen when software runs.
It's better than print() for production code.
"""

import logging
import sys

# ============================================================================
# 1. BASIC LOGGING SETUP (simplest approach)
# ============================================================================

# Configure logging for the entire application
logging.basicConfig(
    level=logging.DEBUG,  # Minimum level to display
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def basic_logging_example():
    """Demonstrate basic logging levels."""
    print("\n--- BASIC LOGGING EXAMPLE ---")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


# ============================================================================
# 2. LOGGING LEVELS (in order of severity)
# ============================================================================

def logging_levels():
    """
    Log levels (lowest to highest severity):
    - DEBUG (10): Detailed info for diagnosing problems
    - INFO (20): General informational messages
    - WARNING (30): Warning messages for potential issues [DEFAULT]
    - ERROR (40): Error messages for serious problems
    - CRITICAL (50): Critical messages for very serious problems
    """
    print("\n--- LOGGING LEVELS ---")
    logger.debug("DEBUG: Variable x = 42")
    logger.info("INFO: Application started")
    logger.warning("WARNING: Disk space low")
    logger.error("ERROR: Failed to connect to database")
    logger.critical("CRITICAL: System failure imminent")


# ============================================================================
# 3. CUSTOM LOGGER WITH FILE HANDLER
# ============================================================================

def setup_file_logging():
    """Create a logger that writes to both console and file."""
    print("\n--- FILE LOGGING EXAMPLE ---")
    
    # Create a new logger
    file_logger = logging.getLogger("file_logger")
    file_logger.setLevel(logging.DEBUG)
    
    # Create file handler
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.INFO)
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    # Attach formatter to handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Attach handlers to logger
    file_logger.addHandler(file_handler)
    file_logger.addHandler(console_handler)
    
    # Test logging
    file_logger.info("This appears in both console and file")
    file_logger.debug("This appears only in console (file level is INFO)")


# ============================================================================
# 4. FORMAT STRINGS (common attributes)
# ============================================================================

def logging_format_example():
    """Demonstrate different format string options."""
    print("\n--- FORMAT STRING OPTIONS ---")
    
    custom_logger = logging.getLogger("format_demo")
    custom_logger.setLevel(logging.DEBUG)
    
    # Clear existing handlers
    custom_logger.handlers.clear()
    
    # Different format styles
    formats = {
        "Simple": "%(message)s",
        "With Level": "%(levelname)s: %(message)s",
        "With Timestamp": "%(asctime)s - %(message)s",
        "Full": "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    }
    
    for style_name, fmt in formats.items():
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(fmt))
        custom_logger.addHandler(handler)
        print(f"\n{style_name}:")
        custom_logger.info("Test message")
        custom_logger.handlers.clear()


# ============================================================================
# 5. FORMAT ATTRIBUTES
# ============================================================================

def format_attributes():
    """
    Common format attributes:
    - %(name)s: Logger name
    - %(levelname)s: Log level (DEBUG, INFO, WARNING, etc.)
    - %(message)s: Log message
    - %(asctime)s: Date/time
    - %(filename)s: Source filename
    - %(funcName)s: Function name
    - %(lineno)d: Line number
    - %(process)d: Process ID
    - %(thread)d: Thread ID
    """
    pass


# ============================================================================
# 6. LOGGER HIERARCHY
# ============================================================================

def logger_hierarchy_example():
    """Demonstrate logger naming and hierarchy."""
    print("\n--- LOGGER HIERARCHY ---")
    
    # Loggers follow a hierarchy with dots
    parent_logger = logging.getLogger("myapp")
    child_logger = logging.getLogger("myapp.module")
    grandchild_logger = logging.getLogger("myapp.module.submodule")
    
    # Configure parent logger once
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(name)s - %(message)s"))
    parent_logger.addHandler(handler)
    parent_logger.setLevel(logging.DEBUG)
    
    # All children inherit parent's handlers and level
    parent_logger.info("Message from parent")
    child_logger.info("Message from child (uses parent's handler)")
    grandchild_logger.info("Message from grandchild")


# ============================================================================
# 7. EXCEPTION LOGGING
# ============================================================================

def exception_logging_example():
    """Demonstrate logging exceptions with traceback."""
    print("\n--- EXCEPTION LOGGING ---")
    
    exc_logger = logging.getLogger("exception_demo")
    exc_logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    exc_logger.addHandler(handler)
    
    try:
        result = 10 / 0
    except ZeroDivisionError:
        # exc_info=True includes the full traceback
        exc_logger.error("An error occurred", exc_info=True)
        # Alternative: logger.exception() automatically includes traceback
        # exc_logger.exception("An error occurred")


# ============================================================================
# 8. DISABLING LOGGING
# ============================================================================

def disable_logging_example():
    """Show how to disable logging."""
    print("\n--- DISABLING LOGGING ---")
    
    test_logger = logging.getLogger("test")
    test_logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(message)s"))
    test_logger.addHandler(handler)
    
    test_logger.info("This will appear")
    
    # Disable this logger
    logging.disable(logging.CRITICAL)
    test_logger.info("This will NOT appear (disabled)")
    
    # Re-enable
    logging.disable(logging.NOTSET)
    test_logger.info("This will appear again (re-enabled)")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    basic_logging_example()
    logging_levels()
    setup_file_logging()
    logger_hierarchy_example()
    exception_logging_example()
    disable_logging_example()
    
    print("\n✓ Logging examples completed")
