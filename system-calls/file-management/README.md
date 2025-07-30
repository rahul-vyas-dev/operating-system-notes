
---

### ✅ Example: `file-management.md`

```markdown
# File Management System Calls

These system calls manage files: creation, deletion, reading, and writing.

## Examples
- `open()` – Open a file.
- `read()` – Read data from a file.
- `write()` – Write data to a file.
- `close()` – Close a file.

## Example in C
```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("test.txt", O_WRONLY | O_CREAT, 0644);
    write(fd, "Hello File!", 11);
    close(fd);
    return 0;
}
