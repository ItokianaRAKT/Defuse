import sys
import time
import threading

from utils import save_cursor, restore_cursor, move_to_row_col, clear_line, flush


class Timer:
    def __init__(self, total_seconds=900):
        self.total_seconds = total_seconds
        self.time_left = total_seconds
        self._running = False
        self._pause_event = threading.Event()
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self.display_row = 1

    def start(self):
        self._running = True
        self._stop_event.clear()
        self._pause_event.clear()
        self._thread.start()

    def pause(self):
        self._pause_event.clear()

    def resume(self):
        self._pause_event.set()

    def stop(self):
        self._running = False
        self._stop_event.set()
        self._pause_event.set()

    def _run(self):
        while self._running and self.time_left > 0:
            self._display()
            if self._pause_event.is_set():
                time.sleep(1)
                self.time_left -= 1
            else:
                time.sleep(0.5)
        if self.time_left <= 0:
            self._display()
            sys.stdout.write("\n\n  BOOM! Time's up!\n\n")
            sys.stdout.flush()

    def _display(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        timer_str = f"  TIME: {minutes:02d}:{seconds:02d}  "
        save_cursor()
        move_to_row_col(self.display_row, 65)
        clear_line()
        sys.stdout.write(timer_str)
        flush()
        restore_cursor()
        flush()
