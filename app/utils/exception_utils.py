# -*- coding: utf-8 -*-
import traceback
import log

class ExceptionUtils:
    @classmethod
    def exception_traceback(cls, e):
        print(f"\nException: {str(e)}\nCallstack:\n{traceback.format_exc()}\n")
        log.error(f"\nException: {str(e)}\nCallstack:\n{traceback.format_exc()}\n")
