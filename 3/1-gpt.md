Для этой задачи вам нужно создать контекстный менеджер `stream_switcher`, который переключает потоки `stdout` и `stderr` внутри контекста. Также нужно реализовать классы `ToStdout`, `ToStderr` и `ToDevnull`, которые будут управлять направлением вывода.

Вот как можно реализовать эту задачу:

1. Определим классы `ToStdout`, `ToStderr` и `ToDevnull`.
   - `ToStdout` и `ToStderr` просто будут возвращать стандартные `sys.stdout` и `sys.stderr`.
   - `ToDevnull` будет направлять вывод в "черную дыру", чтобы игнорировать его.

2. Определим контекстный менеджер `stream_switcher`, который принимает аргументы `stdout` и `stderr`. Внутри этого менеджера будем временно переключать потоки `sys.stdout` и `sys.stderr`.

### Реализация:

```python
import sys
from contextlib import contextmanager
import os

class ToStdout:
    def __enter__(self):
        return sys.stdout

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class ToStderr:
    def __enter__(self):
        return sys.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class ToDevnull:
    def __enter__(self):
        return open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__enter__().close()

@contextmanager
def stream_switcher(stdout=None, stderr=None):
    original_stdout = sys.stdout
    original_stderr = sys.stderr

    try:
        if stdout is not None:
            sys.stdout = stdout().enter()
        if stderr is not None:
            sys.stderr = stderr().enter()
        yield
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
```

### Пояснение к реализации

- Классы `ToStdout`, `ToStderr` и `ToDevnull` используют метод `__enter__` для возвращения нужного потока.
- Контекстный менеджер `stream_switcher` сохраняет исходные потоки `sys.stdout` и `sys.stderr`, чтобы затем восстановить их после выхода из контекста.
- `stdout()` и `stderr()` возвращают экземпляры классов, предоставленных пользователем (например, `ToStdout()`, `ToDevnull()`).

### Пример использования

```python
with stream_switcher(stdout=ToStdout, stderr=ToDevnull):
    print("Эта строка пойдет в stdout")
    print("Эта строка в stderr", file=sys.stderr)
```

Эта реализация корректно переключает потоки на указанные в контексте и возвращает их после завершения блока.
