# Variable Partition Allocation

In Variable Partition Allocation:
- Memory is divided into **variable-sized** blocks at runtime.
- The size of the block matches the size of the process.
- Reduces internal fragmentation but causes **external fragmentation**.

## Example:
RAM = 1000 KB initially free:
- Process A = 200 KB → allocated first 200 KB
- Process B = 300 KB → allocated next 300 KB
- Process C = 100 KB → allocated next 100 KB

## Advantages:
- Better memory utilization.
- Process size is flexible.

## Disadvantages:
- External fragmentation.
- More complex to manage than fixed partitioning.
