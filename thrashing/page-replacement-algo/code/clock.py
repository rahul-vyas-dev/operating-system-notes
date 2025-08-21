def clock_page_replacement(pages, capacity):
    memory = [-1] * capacity
    use_bit = [0] * capacity
    pointer = 0
    page_faults = 0

    for page in pages:
        if page in memory:
            use_bit[memory.index(page)] = 1
        else:
            while use_bit[pointer] == 1:
                use_bit[pointer] = 0
                pointer = (pointer + 1) % capacity
            memory[pointer] = page
            use_bit[pointer] = 1
            pointer = (pointer + 1) % capacity
            page_faults += 1
        print(f"Memory: {memory}")
    
    print("Total Page Faults:", page_faults)


if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4]
    clock_page_replacement(pages, 3)
