#!/usr/bin/env python3

from autopkglib import Processor

APPNAME = "Mock"

__all__ = [APPNAME]

class Mock(Processor):
    """Custom processor for autopkg that is a mock"""

    description = __doc__

    input_variables = {
        "mock": {"required": False, "description": "Mock"},
    }
    output_variables = {
        "mock": {"description": "Mock"}
    }

    def main(self):
        """Do it!"""

if __name__ == "__main__":
    PROCESSOR = Mock()
    PROCESSOR.execute_shell()
